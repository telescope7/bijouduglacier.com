#!/bin/bash
# Regenerate the traffic report. Installed to /usr/local/bin/ by deploy.yml and
# run daily by bijou-analytics.timer. Safe to run by hand at any time.
#
#     sudo /usr/local/bin/goaccess-report.sh
#
# Reads nothing but the nginx access logs. There is no tracking script on the
# site and no third party involved.
#
# This script must never take the website down with it. A missing report is an
# inconvenience; a failed deploy is not. So it exits 0 for every ordinary
# "nothing to report yet" case, and deploy.yml does not treat a failure here as
# fatal either.

set -uo pipefail

OUT=/var/www/analytics
REPORT="$OUT/index.html"

# The temporary file MUST end in .html. GoAccess picks its output format from
# the filename extension, so a name like `index.html.new` ends in `.new`, which
# it does not recognise: it then exits 0 having written nothing at all, and the
# mv that follows fails with a baffling "cannot stat" error. That is exactly
# what happened on the first deploy of this script.
TMP="$OUT/.report-in-progress.html"

LOGS=(/var/log/nginx/bijou-access.log /var/log/nginx/bijou-bookings.log)

# Addresses to leave out of the report, one per line, '#' for comments. Your
# own home and phone IPs belong here: on a site with this little traffic YOU
# are otherwise the largest single visitor, and every deploy check and link
# test lands in the numbers.
#
# Deliberately NOT in the git repo. The repo is public and a home IP address
# is personal data. Create it by hand on the server:
#
#     mkdir -p /etc/bijou-analytics
#     echo "203.0.113.45" > /etc/bijou-analytics/exclude-ips
#
# Matching is on the start of the line, so a prefix like `203.0.113.` covers a
# whole range and works for both IPv4 and IPv6.
EXCLUDE_FILE=/etc/bijou-analytics/exclude-ips

# Country and city lookup. Installed by update-geoip.sh; optional. If the file
# is absent the report is generated without the geo panels rather than failing.
GEODB=/var/lib/GeoIP/dbip-city-lite.mmdb

mkdir -p "$OUT"

# Collect the logs that actually exist. nginx creates a log file lazily, on the
# first line written to it, so bijou-bookings.log does not exist until somebody
# clicks a booking button. Passing a missing path to zcat is an error, so check
# each one. zcat -f also reads uncompressed files, which is how the live log and
# the rotated .gz ones are handled together.
shopt -s nullglob
FILES=()
for base in "${LOGS[@]}"; do
    for f in "$base" "$base".*; do
        [ -f "$f" ] && FILES+=("$f")
    done
done
shopt -u nullglob

placeholder() {
    # Only ever stand in for a report that does not exist. Never overwrite a
    # real one with "no data" because today's parse happened to come up empty.
    [ -s "$REPORT" ] && return 0
    cat > "$REPORT" <<HTML
<!doctype html>
<meta charset="utf-8">
<title>Bijou du Glacier — traffic</title>
<body style="font:16px/1.6 system-ui,sans-serif;max-width:34em;margin:4rem auto;padding:0 1rem;color:#211F1C">
<h1 style="font-weight:400">Nothing to report yet</h1>
<p>$1</p>
<p>This page is rebuilt every day by <code>bijou-analytics.timer</code> and will
fill itself in as soon as there is traffic. Nothing is broken.</p>
HTML
    chmod 0644 "$REPORT"
}

if [ ${#FILES[@]} -eq 0 ]; then
    placeholder "nginx has not written an access log yet."
    echo "No log files yet. Nothing to do."
    exit 0
fi

if [ -z "$(zcat -f -- "${FILES[@]}" 2>/dev/null | head -c 1)" ]; then
    placeholder "The access log exists but is still empty."
    echo "Logs are empty. Nothing to do."
    exit 0
fi

# Optional geo lookup, only if the database is actually there.
GEO_ARGS=()
if [ -f "$GEODB" ]; then
    GEO_ARGS=(--geoip-database="$GEODB")
else
    echo "No GeoIP database at $GEODB; continuing without country data." >&2
    echo "Run /usr/local/bin/update-geoip.sh to add it." >&2
fi

# Drop excluded addresses before goaccess ever sees them. grep -v with a file
# of patterns is simpler and faster than anything goaccess offers, and it means
# the excluded traffic never reaches the report by any route.
filter() {
    [ -s "$EXCLUDE_FILE" ] || { cat; return; }

    # Build one anchored regex from the file.
    #
    # Two things matter here and both bit during testing:
    #
    #  - Dots are escaped. Unescaped, `203.0.113.45` is a regex in which every
    #    dot matches any character.
    #  - An entry that does NOT end in `.` or `:` is treated as a complete
    #    address and must be followed by whitespace. Without that, entering
    #    `203.0.113.4` to exclude one machine silently also excludes .40 to
    #    .49, and you would never notice: the visitors just quietly stop
    #    appearing in the report.
    #
    # An entry that DOES end in `.` or `:` is a deliberate prefix and matches
    # the range, which is how `198.51.100.` covers a whole /24.
    # sed and not tr for the whitespace strip: tr works on the whole stream and
    # would delete the newlines BETWEEN patterns too, collapsing the file into
    # one nonsense line that matches nothing. sed works a line at a time.
    local pats
    pats=$(grep -vE '^[[:space:]]*(#|$)' "$EXCLUDE_FILE" \
           | sed 's/[[:space:]]//g' \
           | sed -e 's/\./\\./g' \
                 -e 's/^/^/' \
                 -e '/[.:]$/! s/$/[[:space:]]/')

    [ -n "$pats" ] || { cat; return; }
    grep -vE "$(echo "$pats" | paste -sd'|' -)" || true
}

if ! zcat -f -- "${FILES[@]}" | filter | goaccess - \
        --log-format=COMBINED \
        --html-report-title="Bijou du Glacier" \
        --tz=Europe/Zurich \
        --ignore-crawlers \
        "${GEO_ARGS[@]}" \
        --no-progress \
        --output="$TMP"
then
    rm -f "$TMP"
    echo "goaccess exited non-zero. The previous report, if any, is untouched." >&2
    exit 1
fi

# --ignore-crawlers can legitimately leave nothing behind on a new server whose
# only visitors so far have been bots.
if [ ! -s "$TMP" ]; then
    rm -f "$TMP"
    placeholder "So far the only requests have been from crawlers, which are
                 excluded from the report."
    echo "No human traffic yet. Nothing to do."
    exit 0
fi

# CC-BY 4.0 requires attribution wherever the data is shown.
if [ -f "$GEODB" ]; then
    printf '%s\n' '<p style="font:12px system-ui,sans-serif;text-align:center;color:#888;padding:1rem">IP geolocation by <a href="https://db-ip.com" style="color:#888">DB-IP</a> (CC BY 4.0)</p>' >> "$TMP"
fi

mv "$TMP" "$REPORT"
chmod 0644 "$REPORT"
echo "Report written to $REPORT"
