# Traffic reporting

> Commands below use `$SERVER`. Set it once per terminal session:
> `export SERVER=root@YOUR_SERVER_IP` — the real address is in
> `deploy/inventory.ini`, which is gitignored.

**There is no tracking on this site.** No analytics script, no cookie, no
pixel, no third party, nothing loaded from another domain, no consent banner
needed. A guest's browser talks to your server and to nobody else.

Everything below is built from the log nginx already writes for every request
it serves. The report is generated on your own machine, from your own files,
and served only to you behind a password.

---

## How a booking click becomes a number

Every booking button on all 17 pages points at a path on your own domain:

| Button | Path | nginx 302s it to |
|--------|------|------------------|
| Book direct | `/book-direct` | saasfeeholidays.com listing |
| Airbnb | `/go/airbnb` | the Airbnb room |
| Booking.com | `/go/booking` | the Booking.com hotel page |

The guest clicks, nginx writes one line and redirects, and they land on the
platform. From their side it is indistinguishable from a normal link, and
nothing is stored in their browser.

The three redirect paths write to **`/var/log/nginx/bijou-bookings.log`**,
separate from page views in `bijou-access.log`, so a click can never be
confused with someone reading a page. Both use nginx's stock `combined`
format, which is what makes the GoAccess command below a one-liner:

```
$remote_addr - $remote_user [$time_local] "$request" $status
    $body_bytes_sent "$http_referer" "$http_user_agent"
```

The referer is the page the guest clicked *from*, which is where the language
breakdown comes from: a click from `/de/buchen/` is a German booking click.

The real destination URLs live in two places and must agree:
`DESTINATIONS` in `tools/build_site.py`, and the three `location` blocks in
`deploy/templates/site-body.conf.j2`. `audit.py` fails the build if they drift
apart.

---

## This month's booking clicks, by channel and language

```bash
ssh $SERVER "zcat -f /var/log/nginx/bijou-bookings.log* | awk -v m=\$(date +%b/%Y) '\$4 ~ m {split(\$7,p,\"/\"); ch=(p[2]==\"go\")?p[3]:\"direct\"; split(\$11,r,\"/\"); lang=(r[4]~/^(en|fr|de|it)\$/)?r[4]:\"none\"; n[ch\" \"lang]++} END{for(k in n) printf \"%5d  %s\n\", n[k], k}' | sort -rn"
```

Output looks like this:

```
    2  direct en
    2  airbnb de
    1  direct none
    1  booking fr
```

`none` means the click had no referer, which usually means a bookmark, a
pasted link, or a privacy-conscious browser.

Run it directly on the server and it is much easier to read:

```bash
zcat -f /var/log/nginx/bijou-bookings.log* | awk -v m=$(date +%b/%Y) '$4 ~ m {split($7,p,"/"); ch=(p[2]=="go")?p[3]:"direct"; split($11,r,"/"); lang=(r[4]~/^(en|fr|de|it)$/)?r[4]:"none"; n[ch" "lang]++} END{for(k in n) printf "%5d  %s\n", n[k], k}' | sort -rn
```

Change `$(date +%b/%Y)` to any month you like, e.g. `Aug/2026`. Drop the
`-v m` filter and the `$4 ~ m` test to count everything the logs still hold.

---

## The full report

GoAccess renders a single self-contained HTML page: visitors, pages, referrers,
countries, browsers, status codes. It is rebuilt every day by
`bijou-analytics.timer` and written to `/var/www/analytics/index.html`.

The exact invocation, from `goaccess-report.sh`:

```bash
zcat -f /var/log/nginx/bijou-access.log* /var/log/nginx/bijou-bookings.log* \
  | goaccess - \
      --log-format=COMBINED \
      --html-report-title="Bijou du Glacier" \
      --tz=Europe/Zurich \
      --ignore-crawlers \
      --no-progress \
      --output=/var/www/analytics/.report-in-progress.html
```

then the finished file is moved over `index.html`, so nobody ever loads a
half-written report.

`--log-format=COMBINED` is GoAccess's built-in name for exactly the nginx
format quoted above, so there is no format string to keep in sync.

**The temporary filename has to end in `.html`.** GoAccess chooses its output
format from the extension, so an obvious name like `index.html.new` ends in
`.new`, which it does not recognise: it exits 0 having written nothing, and the
move that follows fails with `mv: cannot stat`. That is a real bug this script
shipped with once.

**The report covers whatever logrotate still has**, which on Ubuntu is 14 daily
rotations of `/var/log/nginx/*.log`. To keep a longer history, raise `rotate`
in `/etc/logrotate.d/nginx`.

I deliberately did *not* use GoAccess's `--persist` / `--restore` database.
Restoring a database and then re-parsing the same log double-counts every line
in it, and a confidently wrong number is worse than an honestly short one.

To rebuild on demand:

```bash
ssh $SERVER 'systemctl start bijou-analytics.service'
ssh $SERVER 'systemctl list-timers bijou-analytics.timer'
```

---

## Getting at the report

It is served at **https://bijouduglacier.com/analytics/**, behind HTTP basic
auth, with `X-Robots-Tag: noindex` and its own access logging switched off.

**You have to create the password yourself. The playbook will not do it**, and
I never see it. One command on the server:

```bash
ssh $SERVER 'htpasswd -c /etc/nginx/analytics.htpasswd matt'
```

### What that command actually does

`htpasswd` comes from `apache2-utils`, which the playbook installs. It creates
and maintains the little password file that both Apache and nginx understand.

| Part | Meaning |
|------|---------|
| `htpasswd` | the tool |
| `-c` | **c**reate the file. Only on the very first run: `-c` truncates an existing file, so using it again would wipe out every user already in there. |
| `/etc/nginx/analytics.htpasswd` | where to write. Must match `auth_basic_user_file` in the nginx config, which is set in `deploy/templates/site-body.conf.j2`. |
| `matt` | the username you will type in the browser prompt. Any name; it is not a Linux account and grants nothing else on the server. |

It then prompts you twice for a password and writes a single line: the
username, a colon, and a **bcrypt hash** of what you typed. The password itself
is never stored, and nothing in this repository ever contains it.

```
matt:$2y$05$Ea6Y.e0OWzUuQ8kFq...
```

When you next open `https://bijouduglacier.com/analytics/`, the browser shows
its own username-and-password box, sends what you type, and nginx compares it
against that hash. Nothing else on the server or the site is protected by it,
and losing it costs you nothing but the report.

Because `-c` is destructive, **use it once and never again**. To change the
password later, or add a second person, leave it off:

```bash
htpasswd /etc/nginx/analytics.htpasswd matt     # change matt's password
htpasswd /etc/nginx/analytics.htpasswd anna     # add another user
```

No redeploy is needed after either: nginx reads the file on each request.

### After the first time, deploy again

Until `/etc/nginx/analytics.htpasswd` exists, the `/analytics/` location is
**not written into the nginx config at all**, so the URL is a plain 404 rather
than a traffic report sitting open on the public internet. The playbook checks
for the file each run and only then adds the block. So: create the password,
run the playbook once more, and the report appears.

That is the failure direction worth having. Forgetting the password step leaves
you with no report; it can never leave you with a public one.

Basic auth over HTTPS is fine for this. It is one page of visitor counts, the
connection is encrypted, and the alternative is a login system to maintain.

---

## Why not Google Analytics or Plausible

Because the log is already there. GA would add a third-party request to every
page, put you inside the scope of a cookie banner, and hand a guest's browsing
to an advertising company — on a site whose whole argument is that booking
direct means dealing with people rather than platforms. Plausible is far better
behaved but is still a paid third party and still a script.

What you lose by using logs: no scroll depth, no click heatmaps, no
session recording, and bot traffic inflates raw hits (hence `--ignore-crawlers`).
For an eight-page brochure site whose single conversion is "did they click a
booking button", the log answers the only question that matters.
