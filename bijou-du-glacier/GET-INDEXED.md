# Getting bijouduglacier.com crawled and indexed

Written 13 September 2026, after checking the live site.

**Current status: the site is invisible.** I searched for "Bijou du Glacier Saas-Fee
apartment" and your domain does not appear anywhere in the results. What comes back instead
is a *different* Saas-Fee property ("Apartment Bijou" by Interhome), the Residence du Glacier
developer site, and — this one matters — **your own apartment listed on a third-party agency
site at `luxurychaletco.com/properties/du-glacier-b4`.**

That is not a problem with the site. I checked the live pages and everything a search engine
needs is already correct:

| Check | Result |
|---|---|
| HTTPS serving | ✅ |
| `noindex` anywhere crawlable | ✅ none |
| Canonical URL | ✅ `https://bijouduglacier.com/en/` |
| hreflang, 4 languages + `x-default` | ✅ complete |
| `robots.txt` | ✅ 200, allows all, declares the sitemap |
| `sitemap.xml` | ✅ 200, correct MIME type, 16 URLs with hreflang and lastmod |
| Structured data | ✅ WebSite, WebPage, VacationRental, BreadcrumbList, FAQPage |
| Body text on homepage | ✅ ~4,600 characters — not thin |

The site is ready. It has simply never been submitted anywhere, and nothing on the internet
links to it. Those are the only two problems, and steps 1–4 below fix the first one this
afternoon.

**Set your expectations now:** Google will index a brand-new domain with no inbound links
slowly — typically one to three weeks for the first pages, six to twelve weeks before you
rank for anything but your own brand name. Bing is usually faster. Nothing below speeds that
up beyond what's physically possible; it just makes sure the clock actually starts.

---

## What I already changed in the repo

Three things, all built and audited at 0-fail. Review the diff before you deploy.

1. **`tools/build_site.py` — robots.txt now names 16 crawlers explicitly** (OpenAI,
   Anthropic, Perplexity, Google-Extended, Applebot, Common Crawl, Amazon, Meta, Bingbot,
   DuckDuckGo), each with `Allow: /`.

   Honestly: this changes nothing functionally today, because `User-agent: *` + `Allow: /`
   already permitted all of them. It matters for one specific reason — **a crawler that finds
   a group matching its own name obeys only that group and ignores the wildcard completely.**
   So if you or your agent ever adds a `Disallow:` to the `*` group, these stay open. It also
   puts the decision on the record instead of leaving it to a default.

   Note this runs against the common 2026 advice, which is to allow search bots and block
   training bots. I allowed everything on purpose: there is no intellectual property here
   worth protecting — it's marketing copy about one apartment — and being quotable in an AI
   travel answer is a booking channel, not a cost. The reasoning is written into the file so
   you can revisit it.

2. **An IndexNow key file** is now generated at
   `website/c13d276a206e5cd14dbf8988027af48b.txt`. It's public by design and proves only
   that whoever submits URLs controls the domain. Not a secret.

3. **`deploy/indexing/indexnow-submit.sh`** — reads your sitemap, verifies the key file is
   actually live, and notifies Bing, Yandex, Seznam and Naver in one request.

**Deploy these before doing anything below**, or step 4 will fail:

```bash
cd "/Users/mthomas/sandbox/saas-fee-media/bijou-du-glacier/tools"
python3 build_site.py && python3 audit.py
cd ../deploy && ansible-playbook -i inventory.ini deploy.yml
```

---

## Step 1 — Google Search Console (20 minutes, do this first)

Google will find you eventually on its own. Search Console is how you stop guessing about
when, and it's the only way to see what Google actually thinks of the site.

1. Go to <https://search.google.com/search-console> and sign in.
2. Choose **Domain** property (the left-hand box), not URL prefix. Enter `bijouduglacier.com`.

   Domain properties cover every subdomain and both protocols in one place, which is what you
   want. They require DNS verification, which you can do because you control the domain.
3. Google gives you a TXT record. Add it at your registrar's DNS panel — the same place you
   set the A record pointing at the Linode. Then click Verify.

   DNS changes can take up to an hour. If it fails, wait and press Verify again; don't start
   over.
4. Once verified, go to **Sitemaps** in the left sidebar and submit: `sitemap.xml`
5. Go to **URL Inspection** at the top, paste `https://bijouduglacier.com/en/`, and click
   **Request Indexing**. Repeat for these three:
   - `https://bijouduglacier.com/en/apartment/`
   - `https://bijouduglacier.com/en/saas-fee/`
   - `https://bijouduglacier.com/en/book/`

   There's a daily quota of around ten, so do the four English pages now and the French,
   German and Italian homepages tomorrow. Don't bother requesting all sixteen — the sitemap
   handles the rest and manual requests don't confer any ranking benefit.

**Do not** set anything under international targeting — it's deprecated, and your hreflang
tags already tell Google everything it needs.

### What to look at afterwards, and when

Nothing will be there for about 48 hours. After that:

- **Pages** report → how many of your 16 URLs are indexed, and the reason for any that aren't
- **Performance** → impressions and clicks, once you start appearing at all
- **Enhancements / Rich results** → whether the VacationRental and FAQ markup is eligible

If a page shows "Discovered – currently not indexed", that's normal for a new site and means
Google knows about it but hasn't prioritised crawling it. It resolves as the domain builds
authority. Don't keep re-requesting.

---

## Step 2 — Bing Webmaster Tools (10 minutes)

Worth more than its market share suggests, because Bing's index also feeds **Copilot,
DuckDuckGo, and ChatGPT's web results**. Getting into Bing is getting into several AI answer
engines at once.

1. Go to <https://www.bing.com/webmasters> and sign in.
2. Choose **Import from Google Search Console**. It carries over the property and the
   verification in about thirty seconds — do this rather than verifying again by hand.
3. Confirm the sitemap came across under **Sitemaps**. If not, submit `sitemap.xml` manually.
4. Use **URL Submission** to push the four English URLs. Bing's quota is far more generous
   than Google's — you can submit all 16 without worrying.

---

## Step 3 — Deploy, then verify the robots and sitemap are actually live

Before pinging anything, confirm the new files are up:

```bash
curl -s https://bijouduglacier.com/robots.txt | head -20
curl -s https://bijouduglacier.com/c13d276a206e5cd14dbf8988027af48b.txt
curl -sI https://bijouduglacier.com/sitemap.xml | head -3
```

You want: robots showing the named crawler groups, the key file returning the bare key, and
the sitemap returning `200` with an XML content type.

---

## Step 4 — IndexNow (2 minutes, instant)

One request tells Bing, Yandex, Seznam and Naver that all 16 pages exist.

```bash
cd "/Users/mthomas/sandbox/saas-fee-media/bijou-du-glacier"
./deploy/indexing/indexnow-submit.sh
```

`HTTP 202` is success — it means queued. It is not a promise to index, only confirmation
that the engines were told.

**Google does not participate in IndexNow.** Google finds changes through Search Console and
its own crawl, which is what step 1 is for.

Run this script after every deploy that changes page content. It's the cheapest thing on this
list and takes two seconds. Worth having your coding agent wire it into the end of
`deploy.yml` so it happens automatically.

---

## Step 5 — The AI answer engines

There is no submission form for any of these. You cannot ask ChatGPT or Claude or Perplexity
to index you. They find sites by crawling, and what determines whether you show up is:

1. **Being crawlable** — done, and now explicit in robots.txt.
2. **Being in Bing's index** — step 2. This is the big one for ChatGPT specifically.
3. **Having structured data** — you already have `VacationRental` and `FAQPage`, which is
   exactly the shape these systems ingest well. Your FAQ answers are unusually good for this
   because they're direct and factual. The "we are not ski-in ski-out, and we'd rather say so"
   answer is precisely the kind of specific, checkable claim an answer engine will quote.
4. **Being mentioned somewhere else** — step 6.

Once you're indexed, test it by asking ChatGPT, Claude and Perplexity something like *"Where
can I stay in Saas-Fee with 8 people in a 4-bedroom apartment?"* and see whether you come up.
Expect nothing for the first month or two.

One thing you can do now: **Common Crawl** (`CCBot`, now explicitly allowed) runs monthly and
feeds a large number of downstream datasets and AI systems. Being open to it is a slow but
free distribution channel.

---

## Step 6 — Inbound links, which is the actual bottleneck

This is the part that determines whether indexing turns into traffic, and it's the part no
amount of technical work substitutes for. A new domain with zero inbound links gets crawled
slowly and ranks nowhere, no matter how good the markup is.

You need a handful of real links. In rough order of value:

**Saas-Fee tourism office (`saas-fee.ch`).** A listing or accommodation-directory entry on the
official resort site is the single most valuable link available to you — topically perfect, a
`.ch` domain, and genuinely authoritative. Email them and ask what's required for a privately
owned apartment. This is worth more than everything else in this section combined.

**Your social profiles.** Register the handles in `social-media/handles.md` and put
`bijouduglacier.com` in each bio. These are low-value links individually but they're
instant, free, and they're how a new domain first gets discovered. Instagram, X, Pinterest,
Facebook, TikTok — five links in an afternoon.

**`luxurychaletco.com/properties/du-glacier-b4`.** They're already listing your apartment and
already ranking for it. Ask them to link the listing to your site. Worst case they say no.

**Swiss directories.** `local.ch` and `search.ch` both take business listings and both carry
weight in Swiss search results.

**Your property manager.** SaasFeeHolidays has a site that links out to listings. Ask whether
they'll link to bijouduglacier.com from the B4 listing page. You're sending them bookings;
it's a reasonable ask.

### One thing you must not do

**Do not put your website URL in your Airbnb or Booking.com listing** — not in the
description, not in photo captions, not in house rules, not in platform messages. It violates
both platforms' terms and risks delisting, which would cost you far more than the links are
worth. This is the same warning as in `strategy/marketing-plan.md` §2 and it still applies.

---

## Step 7 — Watch for crawlers in your own logs

You already built the tooling for this. Googlebot and Bingbot hitting the site show up in
nginx's access log, so you'll see crawling begin before Search Console reports it:

```bash
ssh $SERVER "grep -icE 'googlebot|bingbot' /var/log/nginx/bijou-access.log"
ssh $SERVER "grep -oiE 'googlebot|bingbot|gptbot|claudebot|perplexitybot|applebot|ccbot' \
  /var/log/nginx/bijou-access.log | sort | uniq -c | sort -rn"
```

The second command gives you a live picture of which crawlers have found you. Run it a week
after step 1 — first Googlebot hits usually appear within a few days of submitting the
sitemap, and seeing them is the earliest confirmation that any of this worked.

---

## Timeline, honestly

| When | What should have happened |
|---|---|
| Today | Steps 1–4 done. Sitemap submitted to Google and Bing, IndexNow pinged. |
| 2–4 days | First Googlebot and Bingbot hits in your access log. Bing may show early pages. |
| 1–2 weeks | `site:bijouduglacier.com` in Google returns something. Search Console Pages report populates. |
| 3–6 weeks | Ranking for "Bijou du Glacier" and close variants. Bing largely complete. |
| 2–4 months | Beginning to appear for unbranded long-tail queries — *if* step 6 got done. |
| 3–6 months | AI answer engines may start citing you. |

If you're still not indexed after three weeks, the cause is almost always one of: DNS
verification never actually completed, the sitemap was submitted with a typo, or nothing
links to the site. Check in that order.

## The one thing to do if you only do one thing

**Step 1.** Fifteen minutes, and everything else becomes measurable instead of hopeful.

---

---
---

# Part 2 — Live site review, 19 September 2026

Re-audited against the deployed site, six days after the first pass.

## What's working

| Check | Result |
|---|---|
| HTTPS, HSTS (`max-age=31536000; includeSubDomains`) | ✅ |
| `www` → apex, and `http` → `https` | ✅ 301 |
| `X-Content-Type-Options`, `X-Frame-Options`, `Referrer-Policy` | ✅ all set |
| gzip on HTML/CSS | ✅ |
| 404 returns a real 404 | ✅ |
| Booking links route through first-party `/book-direct`, `/go/airbnb`, `/go/booking` | ✅ |
| VacationRental markup: `identifier`, `containsPlace`, `occupancy.value: 8`, 11 images | ✅ live |
| Homepage HTML | 36 KB, one `<h1>`, 20 images, 14 lazy-loaded |
| hreflang + canonical, all four languages | ✅ |

The structured-data fix is confirmed live. Google last crawled on 13 September and you
deployed on 18 September, so Search Console will keep showing the old errors until it
re-crawls. Use **URL Inspection → Test Live URL** to see the truth now.

## What still needs dealing with

### 1. You are still not indexed — and your GitHub repo is

A `site:bijouduglacier.com` search returns **nothing from your domain**. The only thing
ranking for your brand is `github.com/telescope7/bijouduglacier.com` — the public repo.

Two consequences. Your repo currently outranks your website for your own name. And the repo
is public, so your marketing plan, rate strategy notes and this file are readable by anyone
who finds it. No credentials are exposed — `.gitignore` correctly excludes `inventory.ini`
and `vars.yml` — so this is a judgement call, not an emergency. Making it private costs
nothing and removes both problems.

### 2. Internal links still point at non-canonical URLs — FIXED 19 Sep 2026

Every page carried **15 internal links ending in `/index.html`** while the canonical tag said
the directory form. Zero clean directory links. Google was being asked to spend crawl budget
on URLs the site itself declared non-canonical, on a new domain where that budget is scarce,
and nginx had to 301 every internal click.

**Now fixed in `tools/build_site.py`.** `href()` emits the canonical directory form
(`../apartment/`, `./` for self). Verified over HTTP: 21 pages crawled, 0 broken links, and
the only remaining `index.html` links are the four on `website/index.html` — the root
language picker, which is `noindex`, which nginx 302s past, and which keeps explicit
filenames so the build still opens from disk.

`audit.py` now enforces this: it resolves directory links the way a web server does, and
**fails the build if any page other than the root picker links to an `index.html` URL**, so
this cannot silently come back.

One consequence, documented in `INSTRUCTIONS.md`: local preview now needs
`python3 -m http.server 8080` rather than double-clicking, because `file://` shows a
directory listing instead of the page.

### 3. Google Fonts is still the only third-party request

`fonts.googleapis.com` and `fonts.gstatic.com` on every page load. Render-blocking on the
critical path, and every visitor's IP goes to Google — a live question under GDPR and the
revised Swiss FADP. Work item 5 in `PROMPT-next-build.md`, still open. Self-hosting two
families is an afternoon and makes the page faster.

### 4. There is now JavaScript on the site

A small inline script adds a `.js` class so the stylesheet can run the scroll-reveal
animation. It's well-built progressive enhancement — no cookies, no third party, no
tracking, and the page renders complete without it.

Flagging it because the "no JavaScript at all" rule is no longer literally true. That's not
a problem in itself, but it changes the Google Ads conversation below: adding a conversion
tag would no longer be breaking a clean principle, only a question of degree.

### 5. Minor

- `<img class="motion-still">` has no `width`/`height` — the one image on the page without
  dimensions, and a small CLS risk.
- No `Content-Security-Policy` or `Permissions-Policy` header. Cheap hardening; neither
  affects search.

---

# Part 3 — Getting more traffic, in priority order

Ranked by return per hour, given that you run this as a passive owner with operations
outsourced.

### 1. The Saas-Fee tourism office listing — still the single best link available

`saas-fee.ch` is the official resort site: topically perfect, authoritative, and a `.ch`
domain. One email asking what's required to list a privately owned apartment. Nothing else
on this list comes close for effort-to-value, and it directly addresses the real bottleneck,
which is that **almost nothing on the internet links to you**.

### 2. Ask `luxurychaletco.com` to link to you

They already list your apartment at `/properties/du-glacier-b4` and they already rank for it.
A link from that listing to your site costs them nothing. Worst case they say no.

### 3. Post the social content that's already written

Nine English captions, eight German, eight Pinterest pins, six video cuts — all finished, in
`social-media/`, none of it posted. Social profiles are also the fastest way for a new domain
to acquire its first few links.

Start with German. Saas-Fee is in German-speaking Wallis and your `/de/` pages have no
traffic source pointed at them at all.

### 4. Content pages for research-phase searches

Your four pages per language will rank for your brand and for narrow long-tail queries. They
will never rank for the questions that bring people into the funnel a year early:

- Saas-Fee or Zermatt — which to choose
- Saas-Fee with young children
- Getting to Saas-Fee from Geneva or Zurich
- Is Saas-Fee good for non-skiers
- Where to eat in Saas-Fee

These are exactly your buyers, deciding on the *resort* before the *apartment*, and nobody
in the village competes for them properly. This is a writing project, not a build task —
which is why it sits below the three items above.

### 5. Brand-defence Google Ads

See Part 4. Cheap insurance, not a growth channel.

### 6. Get the full-resolution photo originals

Free, one email. Everything you have is a 1200 px web export; the photographer's originals
will be 4000 px+. Upgrades the website, the social assets and any future ad creative at once.

---

# Part 4 — Google Ads for Book Direct

## Read this first: you cannot currently measure a conversion

The booking completes on `saasfeeholidays.com`, which you don't control, so you cannot place
a tag on the confirmation page. **There is no way for you to report a real booking back to
Google Ads.** Everything below is shaped around that fact.

Three consequences, all non-negotiable:

1. **You cannot use Smart Bidding.** Maximize Conversions, Target CPA and Target ROAS all
   need conversion data. Use **Manual CPC** (or Maximize Clicks with a bid cap) and nothing
   else. If someone tells you to "let Google optimise it", they're assuming data you don't
   have.
2. **Your best available signal is a click on Book Direct**, which you already log
   server-side. Treat that as the proxy conversion.
3. **Don't let Google's onboarding talk you into a Performance Max campaign.** PMax is
   almost entirely automated and needs conversion data to function. Without it you're handing
   over budget with no steering. Search campaigns only.

## The URL to use

**Final URL — English:**
```
https://bijouduglacier.com/en/book/
```
**German:**
```
https://bijouduglacier.com/de/buchen/
```
French: `https://bijouduglacier.com/fr/reserver/` · Italian: `https://bijouduglacier.com/it/prenotare/`

**Do not use `https://bijouduglacier.com/book-direct` as a Final URL.** It's a 302 redirect
to a third-party domain and it's `Disallow`ed in robots.txt. Google Ads requires the final
URL to resolve to a crawlable page on your display domain; that one would be disapproved for
a destination mismatch. Send people to your booking page and let them click through from
there — which also means the click still lands in your log.

Use one ad group per language with the matching Final URL. Don't rely on the root redirect
to sort out language; it always lands on English.

**Display path:** `bijouduglacier.com/book` (or `/buchen`).

## Measuring it without a tag

Put this in **Settings → Account settings → Final URL suffix**:

```
utm_source=google&utm_medium=cpc&utm_campaign={campaignid}&utm_term={keyword}&utm_content={creative}
```

Those parameters land in the nginx request line, so your existing log-based reporting can
count them. No JavaScript, no cookie, no consent banner, nothing new on the page.

```bash
# ad clicks that landed on the site this month
ssh $SERVER "grep -c 'utm_source=google' /var/log/nginx/bijou-access.log"

# how many of them went on to click Book Direct
ssh $SERVER "wc -l /var/log/nginx/bijou-*click*.log"

# which keyword sent them
ssh $SERVER "grep -o 'utm_term=[^& ]*' /var/log/nginx/bijou-access.log | sort | uniq -c | sort -rn"
```

That gives you cost per Book Direct click, which is the number to manage against.

## Campaign A — Brand defence. Run this one.

**Purpose:** when someone hears about the apartment and searches its name, you appear first
— not `luxurychaletco.com`, not Booking.com, not the developer's property-sales site.

- **Type:** Search. Manual CPC.
- **Budget:** CHF 3–5/day.
- **Bids:** CHF 0.30–0.80. Brand terms are cheap because nobody else wants them.
- **Match:** exact and phrase.
- **Locations:** Switzerland, Germany, Austria, UK, France, Netherlands, Belgium, Italy.
- **Keywords:**
  ```
  [bijou du glacier]
  [bijouduglacier]
  "bijou du glacier saas fee"
  "bijou du glacier apartment"
  [du glacier b4]
  "residence du glacier saas fee apartment"
  ```

**Negative keywords — important.** "Residence du Glacier" is also a property *for sale*
development, and those searches are worthless to you:
```
-kaufen -verkauf -immobilien -eigentum -zu verkaufen -for sale -buy -purchase
-property for sale -investment -makler -estate agent -preisliste
-jobs -stellen -career -wikipedia
```

## Campaign B — High-intent long-tail. Test only, hard limits.

German first — that's the market.

- **Budget:** CHF 10/day, hard cap. **Kill criterion: six weeks.** If it hasn't produced
  Book Direct clicks at a cost you'd accept, switch it off and put the money into the
  photographer.
- **Match:** exact only. Not broad. Broad match without conversion data burns budget on
  irrelevant traffic faster than anything else in Ads.
- **Keywords (DE):**
  ```
  [ferienwohnung saas fee 8 personen]
  [ferienwohnung saas fee 4 schlafzimmer]
  [saas fee wohnung für gruppen]
  [gruppenunterkunft saas fee]
  ```
- **Keywords (EN):**
  ```
  [saas fee apartment 8 people]
  [saas fee 4 bedroom apartment]
  [large apartment saas fee]
  [saas fee group accommodation]
  ```

## Campaign C — Do not run

Generic terms: `saas fee apartment`, `ski chalet switzerland`, `valais holiday rental`.

You'd be bidding against Booking.com, Airbnb and Interhome — who have unlimited budgets,
instant booking, live availability, prices and thousands of reviews — while sending traffic
to a site that shows **no price, no availability and no reviews**. The clicks cost CHF
1.50–4.00 in this market and they will not convert. Revisit once you have reviews on the
site.

## Ad copy — responsive search ads

Paste these in. Headlines are ≤30 characters, descriptions ≤90, as Google requires.

**English headlines:**
```
Bijou du Glacier, Saas-Fee
4-Bedroom Apartment, Saas-Fee
Sleeps 8 · 4 King Bedrooms
Book Direct, No Platform Fee
Car-Free Saas-Fee Apartment
4 Minutes From The Slopes
Three Bathrooms, Four Beds
Official Site, Book Direct
Same Rate, No Service Fee
Luxury Apartment, Valais
Newly Renovated, Sleeps 8
No Small Room. Four Kings.
Glacier Views From Balcony
Group Ski Trips, Saas-Fee
See The Floor Plan
```

**English descriptions:**
```
Four real bedrooms, four king beds, three bathrooms. Nobody takes the small room.
Book direct: same nightly rate as the platforms, without their service fee on top.
Four minutes' walk to the slopes, in a village with no cars. Sleeps eight.
Newly renovated apartment in the heart of Saas-Fee. See the floor plan and photos.
```

**German headlines:**
```
Bijou du Glacier, Saas-Fee
Ferienwohnung für 8 Personen
4 Schlafzimmer, 3 Bäder
Direkt buchen, ohne Gebühr
Autofreies Saas-Fee
4 Gehminuten zur Piste
Offizielle Website
Kein kleines Zimmer
Neu renoviert, Wallis
Gruppenreise Saas-Fee
Platz für acht Gäste
Blick auf 13 Viertausender
Zum Grundriss
```

**German descriptions:**
```
Vier echte Schlafzimmer, vier Kingsize-Betten, drei Bäder. Niemand schläft auf dem Sofa.
Direkt buchen: gleicher Übernachtungspreis, ohne die Servicegebühr der Portale.
Vier Gehminuten zur Piste, mitten im autofreien Dorf. Platz für acht Gäste.
Neu renovierte Ferienwohnung im Herzen von Saas-Fee. Grundriss und Fotos ansehen.
```

**Sitelinks** (all four languages have equivalents):

| Text | URL |
|---|---|
| The apartment | `/en/apartment/` |
| Floor plan | `/en/apartment/` |
| Saas-Fee | `/en/saas-fee/` |
| Book direct | `/en/book/` |

**Callouts:** `Sleeps 8` · `4 King Bedrooms` · `3 Bathrooms` · `4 Min To Slopes` ·
`Car-Free Village` · `Newly Renovated` · `No Platform Fee`

## What to do before spending anything

1. **Fix the internal `/index.html` links** (Part 2 item 2). Landing page experience is a
   Quality Score input, and redirect chains on the landing page don't help.
2. **Set the Final URL suffix** and confirm a test click shows up in your log. If you can't
   see the click, don't buy clicks.
3. **Start brand-only, at CHF 3/day, for two weeks.** Learn the interface on cheap traffic
   before risking money on anything competitive.

Expect roughly CHF 90–150/month for brand defence alone. That is the whole recommendation
until there are reviews on the site — at which point Campaign B becomes worth a real test.


---

*Sources consulted: [IndexNow FAQ](https://www.indexnow.org/faq) ·
[AI crawler user-agent reference 2026](https://www.anagram.ai/blog/ai-crawler-user-agent-list-2026-14-bots-and-robotstxt-tokens-to-know) ·
[AI crawlers explained](https://www.anagram.ai/blog/ai-crawlers-explained-gptbot-claudebot-perplexitybot-and-how-to-let-them-in-2026)*
