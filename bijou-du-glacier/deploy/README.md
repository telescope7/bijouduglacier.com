# Deploying to the Linode

> Commands below use `$SERVER`. Set it once per terminal session:
> `export SERVER=root@YOUR_SERVER_IP` — the real address is in
> `deploy/inventory.ini`, which is gitignored.

One command puts the site on your server with HTTPS. This folder has four
files and you only ever edit one line of one of them.

```
deploy/
  inventory.ini                 <- your server's IP address goes here
  deploy.yml                    <- the playbook; domain + email at the top
  templates/site.conf.j2        <- the nginx server blocks
  templates/site-body.conf.j2   <- the parts shared by HTTP and HTTPS,
                                   including the three booking redirects
  analytics/                    <- traffic reporting from the nginx log.
    README.md                      No tracking script. Start there.
    goaccess-report.sh
    bijou-analytics.{service,timer}
```

---

## Before the first run

**1. Install Ansible on your Mac** (once, ever):

```bash
brew install ansible
```

**2. Point the DNS at the Linode.** At whoever holds `bijouduglacier.com`,
create two A records pointing at your Linode's public IPv4 address:

| Type | Name  | Value             |
|------|-------|-------------------|
| A    | `@`   | your Linode's IP  |
| A    | `www` | your Linode's IP  |

This has to be done **before** you deploy. Let's Encrypt proves you own the
domain by fetching a file from it over HTTP, so if the DNS is not pointing here
yet, there is nothing to fetch. The playbook checks this first and stops with a
clear message rather than burning a request against Let's Encrypt's rate limit.

DNS changes can take anywhere from a minute to a few hours. Check with:

```bash
dig +short bijouduglacier.com
```

**3. Confirm you can SSH in** as root with a key, without being asked for a
password:

```bash
ssh root@YOUR_LINODE_IP
```

If that asks for a password, add your key first with `ssh-copy-id root@IP`.

**4. Put your IP in `inventory.ini`.**

```bash
cd deploy
cp inventory.ini.example inventory.ini   # then edit the address
cp vars.yml.example vars.yml             # then edit the email
```

Both are gitignored, so neither ends up in the public repository.

---

## Deploying

```bash
cd deploy
ansible-playbook -i inventory.ini deploy.yml
```

First run takes two or three minutes: it installs nginx and certbot, opens the
firewall, uploads the site, and gets the certificate. Later runs take about
twenty seconds, because all they do is re-upload the site and reload nginx.

**Run it as often as you like.** It is safe to repeat. The certificate is only
requested if one does not already exist.

### The usual cycle

```bash
cd tools
python3 build_site.py        # rebuild the pages after a copy change
python3 audit.py             # must say 0 fail before you ship
cd ../deploy
ansible-playbook -i inventory.ini deploy.yml
```

---

## What it actually does

| Step | What happens |
|------|--------------|
| Pre-flight | Checks the site has been built, and that the domain does not point at some *other* server. A name it cannot resolve at all is only a warning. |
| Packages | Installs `nginx`, `certbot`, `rsync`, `ufw`. |
| Firewall | Allows SSH and ports 80/443, blocks the rest, enables `ufw`. |
| Upload | Tars `website/` locally, unpacks into a staging directory on the server, then `rsync --delete`s it into place. The live site is never empty mid-deploy, and files you deleted from the build also disappear from the server. |
| nginx | Writes the server config, removes the default welcome page, runs `nginx -t` before reloading. |
| HTTPS | `certbot certonly --webroot` for `bijouduglacier.com` and `www`, then re-renders the config with the TLS blocks. |
| Booking clicks | Three 302s (`/book-direct`, `/go/airbnb`, `/go/booking`) to the platforms, each logging to its own file so clicks are separable from page views. |
| Reporting | Installs GoAccess and a daily timer that rebuilds an HTML report at `/analytics/`, behind basic auth. See `analytics/README.md`. |
| Renewal | Installs a deploy hook that reloads nginx after a renewal, and confirms `certbot.timer` is enabled. Twice-daily checks, no cron to write. |

### What the server ends up serving

- `https://bijouduglacier.com/` is the canonical home. Plain HTTP and `www`
  both 301 to it.
- `/` redirects to `/en/` with a **302**, not a 301. English is the hreflang
  x-default, but which language a visitor should land on is not a permanent
  decision, and a 301 would be cached in their browser forever.
- `/en/apartment/index.html` 301s to `/en/apartment/`, which is the canonical
  form in every `<link rel="canonical">` on the site. The internal links spell
  out `index.html` so the folder also opens by double-clicking from disk; this
  redirect reconciles the two.
- Every booking button goes to a path on **your** domain, which nginx 302s out
  to SaasFeeHolidays, Airbnb or Booking.com. That is the only way to count
  clicks without putting a tracking script in front of a guest. 302 rather than
  301, because those listing URLs change and a 301 would be cached in a
  visitor's browser indefinitely. `robots.txt` disallows all three and they are
  absent from `sitemap.xml`, so they never get indexed as thin redirect pages.
- AVIF gets a MIME type added to `/etc/nginx/mime.types`. nginx only learned
  about `image/avif` in 1.21.4, and Ubuntu 22.04 ships 1.18, which would
  otherwise serve every AVIF as a binary download.

---

## Things worth knowing

**HSTS is on, with a one-year lifetime.** Once a browser has visited the HTTPS
site it will refuse to talk to this domain over plain HTTP for a year, even if
you take the certificate away. That is the point of it, but it does mean you
cannot casually move `bijouduglacier.com` to a host without TLS. If that ever
worries you, lower `max-age` in `templates/site.conf.j2` and deploy before you
make the move.

**Images are cached for thirty days.** The filenames are not content-hashed, so
if you replace a photo and keep the same filename, a returning visitor may see
the old one for up to a month. Either give the new file a new name, or lower
`expires 30d` in `templates/site-body.conf.j2`.

**You never renew the certificate by hand.** It is not a cron job. Ubuntu's
certbot package ships a systemd timer, `certbot.timer`, which checks twice a
day and renews once the certificate is within a third of its lifetime of
expiring. Certificates are currently 90 days, so that happens around day 60.
The playbook only makes sure that timer is enabled; it does not write any
schedule of its own.

(The package also drops `/etc/cron.d/certbot`, but that line is guarded with
`-a \! -d /run/systemd/system`, so it only runs on systems without systemd.
On this server it never fires, and the two never double up.)

Two moving parts make that work, and the second one is easy to forget:

1. `certbot.timer` renews the certificate files.
2. `/etc/letsencrypt/renewal-hooks/deploy/reload-nginx.sh`, written by the
   playbook, reloads nginx afterwards.

The second matters because `certbot certonly` writes new files but does not
touch nginx, and nginx reads certificates once at startup and never re-reads
them. Without that hook the renewal would succeed, a valid certificate would
sit on disk, and nginx would keep serving the expired one.

Let's Encrypt is shortening lifetimes. On **10 February 2027** the default
profile, which is the one this playbook uses, drops to **64-day** certificates,
and renewal will start happening around day 43 instead. Nothing here needs
changing: the timer simply fires more often. This does mean manual renewal
stops being a realistic fallback, so it is worth confirming once that the
automation works:

```bash
ssh $SERVER 'certbot renew --dry-run'
```

That runs a full renewal against Let's Encrypt's staging server without
touching the real certificate. The only realistic way renewal breaks later is
port 80 becoming unreachable, since the challenge is fetched over plain HTTP.
That is why the nginx config keeps `/.well-known/acme-challenge/` served on
port 80 even after everything else there redirects to HTTPS.

**The traffic report needs a password before it will be served at all.** The
playbook deliberately does not create one. Until `/etc/nginx/analytics.htpasswd`
exists, the `/analytics/` location is not written into the nginx config, so the
URL 404s rather than exposing your traffic stats. Create it once:

```bash
ssh $SERVER 'htpasswd -c /etc/nginx/analytics.htpasswd matt'
```

then deploy again. Full detail in `analytics/README.md`.

**Do not hand-edit the config on the server.** Everything under
`/etc/nginx/sites-available/` and `/etc/nginx/snippets/` is overwritten on the
next deploy. Change the templates here instead.

---

## When something goes wrong

**"resolves to ..., but this playbook is pointed at ..."** — the name is live
but aimed at a different server. Either the A record or `inventory.ini` is
wrong. Nothing was changed on the server.

**"Could not resolve ... from this machine"** — a note, not an error, and the
deploy carries on. Your machine failing to resolve a name does not mean the
rest of the internet cannot. macOS in particular caches negative DNS answers,
so a domain that did not exist when you last looked can keep failing locally
for a while after it starts working. If you want to clear that:

```bash
sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder
```

The check asks `dig`, then `host`, then Python's resolver, and keeps whatever
any of them finds. It only stops the deploy if the name resolves somewhere that
is not this server, which is a genuine problem worth stopping for. To skip it
entirely:

```bash
ansible-playbook -i inventory.ini deploy.yml --skip-tags dns
```

**"Let's Encrypt did not issue a certificate"** — the site is up and working on
plain HTTP; only the certificate failed. The reason is at the end of
`/var/log/letsencrypt/letsencrypt.log` on the server. The two usual causes are
DNS that has not finished propagating, and port 80 being blocked upstream at
the Linode Cloud Firewall, which is separate from `ufw`.

**Rate limits.** Let's Encrypt allows five failed attempts per account per
hour. If you have been retrying, wait an hour rather than fighting it.

**Check the booking redirects are working:**

```bash
curl -sI https://bijouduglacier.com/book-direct | head -2
ssh $SERVER 'tail -3 /var/log/nginx/bijou-bookings.log'
```

The first should print `HTTP/2 302` and a `location:` header pointing at the
SaasFeeHolidays listing. The second shows the click, in a file that contains
nothing but booking clicks.

**See what the server thinks:**

```bash
ssh root@YOUR_IP 'nginx -t && systemctl status nginx --no-pager'
ssh root@YOUR_IP 'certbot certificates'
ssh root@YOUR_IP 'ufw status'
```

**Test a renewal without actually renewing:**

```bash
ssh root@YOUR_IP 'certbot renew --dry-run'
ssh root@YOUR_IP 'systemctl list-timers certbot.timer'
ssh root@YOUR_IP 'ls -l /etc/letsencrypt/renewal-hooks/deploy/'
```

The first runs a full renewal against Let's Encrypt's staging server. The
second shows when the timer next fires. The third confirms the nginx reload
hook is in place, which is the part that would fail silently.

Worth doing once, a few days after launch. If it passes, renewal is genuinely
automatic and you never have to think about the certificate again.
