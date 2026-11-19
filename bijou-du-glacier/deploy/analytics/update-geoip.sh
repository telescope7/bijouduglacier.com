#!/bin/bash
# Download the GeoIP database the traffic report uses for country/city.
#
#     sudo /usr/local/bin/update-geoip.sh
#
# Run it once to install, then monthly (deploy.yml installs a timer). If it is
# never run, goaccess-report.sh simply omits the geo section; nothing breaks.
#
# WHY DB-IP AND NOT MAXMIND
#
# MaxMind's GeoLite2 is the better-known free database and it is the wrong
# choice here. Since 2019 it has needed an account, a signed EULA and a licence
# key, and since December 2023 those keys expire every 90 days unless you
# reconfirm by email. The failure mode is silent: three months after setup the
# download starts failing and the report quietly keeps showing stale geo data.
#
# DB-IP Lite is CC-BY 4.0, downloads with a plain GET, has no key and no
# expiry. It is a little less precise at city level. For "which countries is my
# social reaching" that difference does not matter.
#
# Attribution is required by the licence and is printed into the report by
# goaccess-report.sh.

set -uo pipefail

DEST_DIR=/var/lib/GeoIP
DEST="$DEST_DIR/dbip-city-lite.mmdb"
TMP="$DEST.download"

mkdir -p "$DEST_DIR"

# DB-IP publishes monthly, with the year and month in the filename. On the
# first day or two of a month the new file may not be up yet, so try this
# month and fall back to last month.
try_months=("$(date -u +%Y-%m)" "$(date -u -d '1 month ago' +%Y-%m 2>/dev/null || date -u -v-1m +%Y-%m)")

for ym in "${try_months[@]}"; do
    url="https://download.db-ip.com/free/dbip-city-lite-${ym}.mmdb.gz"
    echo "Trying ${url}"
    if curl -fsSL --max-time 120 "$url" | gunzip > "$TMP" 2>/dev/null && [ -s "$TMP" ]; then
        # A real city database is tens of MB. Anything tiny is an error page
        # that gunzip happened not to choke on.
        size=$(stat -c%s "$TMP" 2>/dev/null || echo 0)
        if [ "$size" -lt 1000000 ]; then
            echo "  got only ${size} bytes, that is not the database" >&2
            rm -f "$TMP"; continue
        fi
        mv "$TMP" "$DEST"
        chmod 0644 "$DEST"
        echo "Installed ${DEST} ($(( size / 1024 / 1024 )) MB, ${ym} edition)"
        echo "Now run: /usr/local/bin/goaccess-report.sh"
        exit 0
    fi
    rm -f "$TMP"
done

echo "Could not download a GeoIP database. The report will carry on without" >&2
echo "geo data; nothing else is affected." >&2
exit 1
