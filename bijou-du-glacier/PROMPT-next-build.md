# Next build — audit findings and the prompt

Two parts: **Part A** is what I found and why it matters (read this yourself).
**Part B** is the prompt to paste into your coding agent. Part B is self-contained — it
repeats what the agent needs, so you don't have to send Part A.

Audited 11 September 2026 against the live site and the repo at
`/Users/mthomas/sandbox/saas-fee-media/bijou-du-glacier/`.

---

# PART A — What I found

## What's already right, and shouldn't be touched

The technical build is better than almost anything in this market. Specifically: `hreflang`
across four languages with `x-default`, canonicals on every page, translated URL slugs
(`/de/ferienwohnung/`), `VacationRental` + `FAQPage` + `BreadcrumbList` JSON-LD, AVIF with
JPEG fallback at 3–4 widths, `fetchpriority="high"` preload on the LCP image, immutable
asset caching with no-cache HTML, and an audit script that passes 0-fail across 17 pages.
The copy is excellent — the "no, we are not ski-in ski-out, and we'd rather say so plainly"
answer in the FAQ is worth more than any amount of marketing language.

None of what follows is a criticism of the build. The site is a well-made object that
currently cannot tell you whether it works, and gives a visitor who isn't ready to book
right now nothing to do.

## The gaps, ranked by what they cost you

### 1. There is no analytics of any kind

Zero. No tag, no script, no log analysis. You cannot answer: how many people visit, which
language, which page, and — the only question that actually matters — **how many clicked
through to book.**

Everything else on this list is a guess until this is fixed. It is also the cheapest fix
here, and there is a version of it that needs no JavaScript, no cookies, no consent banner
and no third party at all. See §2.

### 2. Every outbound booking click is invisible

`Book Direct` appears 40 times across the site and every instance points straight at
`saasfeeholidays.com`. The moment someone clicks, they leave your measurable universe.

`INSTRUCTIONS.md` already flags the fix and it still hasn't been done. It is more valuable
than it looks, because of how it combines with the point above:

> Route all three booking links through redirects on your own domain — `/book-direct`,
> `/go/airbnb`, `/go/booking` — and every click lands in your nginx access log before it
> leaves. Run GoAccess over those logs and you have the entire funnel: sessions, pages,
> languages, and channel-by-channel click-through. No JavaScript, no cookies, no GDPR
> exposure, no consent banner, nothing to slow the page down.

That is the right answer for this site specifically, because it already has a server you
control and a no-JavaScript philosophy worth protecting. A client-side analytics tag would
be the conventional choice and a worse one here.

It also makes the link resilient: when your manager changes systems, you edit one nginx
line instead of rebuilding 17 pages.

### 3. A visitor who isn't ready to book has nothing to do

This is the biggest commercial gap on the site, and it's structural rather than technical.

There is exactly one conversion action — an outbound link. No enquiry form, no email
address, no WhatsApp, no phone number, no availability calendar, no "ask about a week".
There is not a single `<form>` or `mailto:` anywhere in 17 pages.

For a four-bedroom property at this price point, the booking window is six to twelve months
and the decision involves six to eight people. **Most of your qualified traffic is
researching, not buying.** Right now every one of those people leaves without a trace and
without any way for you to reach them again. You have no list, which also means the
returning-guest December email in the marketing plan — the highest-return thing in it — has
nobody to send to.

### 4. Your reviews don't appear on your own site

You have review equity on Airbnb and Booking.com and none of it is visible on
bijouduglacier.com. This is the core trust asymmetry of direct booking: Airbnb offers a
stranger buyer protection and a wall of reviews; your site currently offers neither. Three
or four pulled quotes with attribution would close most of that gap.

### 5. No price and no rating in the structured data

The `VacationRental` block has no `offers`, no `priceRange`, and no `aggregateRating`. Those
are the fields that make a lodging result eligible for price and star display in search,
which is the single largest CTR lever available in a SERP. You're leaving it on the table.

Separately, there is no price signal anywhere in the visible copy either. For a luxury
property that's a qualification problem as much as an SEO one — you want the wrong visitor
to self-select out early, and the right one to feel the number confirms the quality.

### 6. Internal links point at non-canonical URLs

Every page canonicalises to `https://bijouduglacier.com/en/` but every internal link points
at `/en/index.html` — 15 per page, 17 pages. Google will consolidate these, but you're
spending crawl budget on it, splitting signals, and showing users an uglier URL than the one
you told search engines to index. The nginx config already serves clean directory URLs, so
this is a build-time string change, not an infrastructure one.

### 7. The repo and production have drifted

The live site serves the hero walkthrough video (`video/hero-480.mp4`). The local
`en/index.html` has that video commented out and shows the `piste-dawn` stills instead, with
a note saying "un-comment this". So the deployed site is not what's in the repo, and there
is nothing on either side that tells you which is newer.

Related: `website/video/` is 6.4 MB in four encodes, and the local build references none of
them. Either the video is wanted — in which case turn `HERO_VIDEO` back on and get it under
version control properly — or it isn't, and it shouldn't be deploying.

### 8. Google Fonts is the only third party, and it's the wrong kind

Cormorant Garamond and Inter load from `fonts.googleapis.com`. Two consequences: a
render-blocking stylesheet on a critical path you otherwise control completely, and the
visitor's IP going to Google on every page load — which German courts have already ruled
against under GDPR and which is a live question under the Swiss revised FADP. Self-hosting
two font families is an afternoon, makes the page faster, and removes the last reason
anyone could ask you for a cookie banner.

### 9. Four pages per language is a low SEO ceiling

You will rank for "Bijou du Glacier" and you might rank for long-tail apartment queries. You
will not rank for the research-phase questions that bring people into the funnel a year
early — "Saas-Fee or Zermatt", "Saas-Fee with young children", "is Saas-Fee good for
non-skiers", "getting to Saas-Fee from Geneva". Those are exactly the people you want,
because they're deciding on the *resort* before they decide on the *apartment*, and nobody
in the village is competing for them properly.

This one is a genuine project, not a fix. It's listed last deliberately — do nothing about
it until §1–§3 are done and you can measure whether it works.

## What I'd actually do, in order

| | Work | Why first |
|---|---|---|
| 1 | Redirects + GoAccess (§1, §2) | Everything else is unmeasurable without it. Half a day. |
| 2 | Enquiry capture (§3) | Largest revenue gap. Start with mailto + WhatsApp; a real form later. |
| 3 | Reviews + price + ratings (§4, §5) | Trust and SERP CTR. Needs your real numbers and review text. |
| 4 | Canonical links, drift, fonts (§6, §7, §8) | Hygiene. Cheap, and stops the site rotting. |
| 5 | Content layer (§9) | Only once 1–2 prove what converts. |

Items 1, 3, 4 are in the prompt below. Item 2 is in there as far as it can go without
decisions only you can make — read the "Needs your input" block at the end of the prompt
before you send it.

---

# PART B — The prompt

Copy everything between the lines into your coding agent, from the repo root.

Two things to do first:

- Fill in the four bracketed values in the "Facts I'm supplying" block. If you don't have
  one yet, delete that whole line and the agent will skip that work item rather than invent
  a number.
- Decide the §3 question (enquiry email address / WhatsApp number). Without it, work
  item 3 gets skipped.

---

```
You are working in the Bijou du Glacier repo: a static, four-language marketing site for a
luxury 4-bedroom holiday apartment in Saas-Fee, Switzerland, generated by Python and
deployed to a Linode running nginx via Ansible.

Read these before changing anything:
  INSTRUCTIONS.md            how the whole thing fits together
  tools/build_site.py        the generator; SITE dict at the top holds all global config
  tools/audit.py             pre-flight checks; must pass 0-fail before you finish
  deploy/templates/site-body.conf.j2    the nginx config
  copy/copy-en.md            the words (also fr/de/it)

HOW THIS REPO WORKS — respect this or you will lose work:
- website/ is BUILD OUTPUT. Never hand-edit files in website/. Change tools/ and rebuild.
- The site is generated in four languages: en, fr, de, it. Any user-visible string you add
  must exist in all four. Translate properly — the French, German and Italian are for real
  Swiss and European guests, not machine output. If you are not confident in a translation,
  say so in your summary rather than shipping something clumsy.
- Hard constraint: NO client-side JavaScript, no frameworks, no third-party tags, no
  cookies, no consent banner. This is deliberate and I want it preserved. If you think you
  need JS for something, stop and explain why instead of adding it.
- Run `python3 tools/audit.py` before you declare done. 0 fail is the bar.

FACTS I'M SUPPLYING (delete any line you don't have a value for, and skip that work item):
- Nightly rate, low season: CHF [LOW]
- Nightly rate, high season: CHF [HIGH]
- Review rating and count to cite: [e.g. 4.9 from 27 reviews on Airbnb]
- Enquiry email address: [EMAIL]
- WhatsApp number in international format: [+41...]

Do the work items below in order. After each one, tell me what changed and what you
couldn't do. Do not batch them into one giant commit.

────────────────────────────────────────────────────────────────────────
WORK ITEM 1 — Make the funnel measurable, with no JavaScript
────────────────────────────────────────────────────────────────────────
Right now every booking link points straight at saasfeeholidays.com, airbnb.com or
booking.com, so I have no idea how many people click. Fix it server-side.

1a. In deploy/templates/site-body.conf.j2 add three 302 redirects, placed above the
    generic `location /` block:
        /book-direct  -> https://saasfeeholidays.com/en/saasfeeholidays-du-glacier---b4
        /go/airbnb    -> https://www.airbnb.com/rooms/1674533087008414341
        /go/booking   -> https://www.booking.com/hotel/ch/saasfeeholidays-du-glacier-b4.html
    Use 302, not 301 — these targets will change and I don't want them cached forever.
    Give each one its own access_log line so they're trivially greppable.

1b. In tools/build_site.py change SITE["direct"], SITE["airbnb"] and SITE["booking"] to the
    new first-party paths (https://bijouduglacier.com/book-direct etc.) and rebuild, so all
    40-odd booking links across the 17 pages route through my own domain.
    Keep the real destination URLs in the file as clearly-named constants next to the SITE
    dict, since the nginx template needs them and I'll want to see them in one place.
    Add rel="noopener" and leave the links as ordinary anchors — no JS click handlers.

1c. Make sure robots.txt disallows /go/ and /book-direct so these never get indexed as
    thin redirect pages, and confirm they're absent from sitemap.xml.

1d. Add deploy/analytics/ with:
    - a short README explaining that traffic reporting comes from the nginx access log via
      GoAccess, so there is no client-side tracking of any kind
    - the exact GoAccess invocation to produce a rolling HTML report, including the log
      format matching my nginx config
    - an Ansible task (wired into deploy.yml) that installs GoAccess, and a systemd timer
      that regenerates the report daily to a path served over HTTP but protected by HTTP
      basic auth — I do not want my traffic stats public
    - a one-line command I can run by hand to see this month's booking clicks broken down
      by channel and language

Acceptance: after deploy, hitting /book-direct in a browser lands on the SaasFeeHolidays
listing, and that hit is visible in the access log tagged distinctly from page views.

────────────────────────────────────────────────────────────────────────
WORK ITEM 2 — Internal links should point at canonical URLs
────────────────────────────────────────────────────────────────────────
Every page canonicalises to e.g. https://bijouduglacier.com/en/ but every internal link
points at /en/index.html — 15 per page across 17 pages. nginx already serves clean
directory URLs (try_files $uri $uri/), so this is a generator-side change only.

Update tools/build_site.py so internal links emit directory URLs (../apartment/, ../../fr/,
./ for self) instead of paths ending in index.html. This covers the main nav, the language
switcher, the footer columns, the breadcrumb JSON-LD and every inline body link.

Two things to be careful of, and audit.py must keep passing on both:
- website/index.html is the root language-picker and must still work when opened directly
  off the filesystem with no server (that's an existing audit check — don't break it).
- The language switcher must keep you on the equivalent page, using the translated slugs in
  SLUGS, not send you to the homepage.

If the offline-filesystem requirement genuinely conflicts with clean URLs for the root
picker specifically, keep index.html paths for that one file only, and tell me.

────────────────────────────────────────────────────────────────────────
WORK ITEM 3 — Give people who aren't ready to book something to do
────────────────────────────────────────────────────────────────────────
[SKIP THIS ITEM ENTIRELY if I didn't supply an enquiry email above.]

The only conversion action on the entire site is an outbound link to a booking engine. There
is no form, no mailto:, no phone, no WhatsApp anywhere in 17 pages. Most of my traffic is
researching a trip six to twelve months out and leaves no trace. Fix the cheap end of this
now; we'll do a real form later.

Add an "Ask us about your dates" block, in all four languages:
- On the book page, directly below the existing Reserve panel — secondary to Book Direct,
  not competing with it. The direct CTA stays the visually dominant action.
- On the homepage, as a single quiet line at the end of the FAQ section.

It should contain a mailto: link with a useful pre-filled subject and body (dates, party
size, which language they're writing in), and a wa.me WhatsApp link if I supplied a number.
Both as plain anchors. No form, no JavaScript.

Copy should be warm and low-pressure, in the voice of the existing site — the point is
"talk to a person who knows the apartment", not "GET A QUOTE". Write the English, then
translate to fr/de/it, and put all four in copy/*.md the normal way so I can edit them.

Also add the email address to the footer of every page, and to the Organization/
VacationRental JSON-LD as a contactPoint.

────────────────────────────────────────────────────────────────────────
WORK ITEM 4 — Price and rating in the structured data
────────────────────────────────────────────────────────────────────────
[SKIP the price half if I didn't supply rates; SKIP the rating half if I didn't supply a
rating. Do not invent either — a wrong number here is a manual action from Google.]

The VacationRental JSON-LD currently has no offers, no priceRange and no aggregateRating,
so the site can't be eligible for price or star display in search results.

4a. Add priceRange and an offers block using the rates I supplied, with
    priceCurrency: "CHF" and a clear priceSpecification covering low and high season.
4b. Add aggregateRating using the figure I supplied. Cite the source platform honestly in
    the surrounding visible copy — schema.org aggregateRating must correspond to something
    a user can actually see on the page, or it's a policy violation. So this only ships
    together with 4c.
4c. Add a short, honest reviews block to the book page and the homepage: three or four
    pulled guest quotes with first name, month, and which platform they came from. Put the
    quote text in copy/*.md so I can swap it. Leave clearly-marked placeholder quotes I can
    replace, and list in your summary exactly which lines I need to fill in with real
    review text before this goes live.

Validate the final JSON-LD against Google's Rich Results Test requirements for lodging and
tell me if anything is still missing for eligibility.

────────────────────────────────────────────────────────────────────────
WORK ITEM 5 — Self-host the fonts
────────────────────────────────────────────────────────────────────────
Cormorant Garamond and Inter currently load from fonts.googleapis.com. That's the only
third-party request on the site: it's render-blocking, and it sends every visitor's IP to
Google, which is a live GDPR/Swiss FADP problem for a site whose whole audience is European.

Self-host both. Subset to latin + latin-ext, woff2 only, only the weights actually used
(check styles.css — don't ship weights nothing references). Put them in website/fonts/,
serve with the existing immutable cache rule, preload the two faces used above the fold,
and use font-display: swap. Remove both preconnects and the Google stylesheet link.

Update website/fonts/README.md, which currently says the opposite.

Confirm in your summary that the rendered page makes zero third-party requests.

────────────────────────────────────────────────────────────────────────
WORK ITEM 6 — Stop the repo and production drifting
────────────────────────────────────────────────────────────────────────
The live site serves video/hero-480.mp4 in the hero. The local en/index.html has that video
commented out and renders piste-dawn stills instead. So production is not what's in this
repo and nothing tells me which is newer. Also website/video/ is 6.4 MB in four encodes that
the current build doesn't reference at all.

6a. Tell me which is actually live before changing anything — check the deployed HTML.
6b. Make HERO_VIDEO in tools/build_site.py the single switch, with no commented-out HTML
    left in the generated output either way, and set it to whatever production currently
    does so the repo matches reality. Tell me which you set and why.
6c. If HERO_VIDEO ends up False, exclude website/video/ from the deploy rsync rather than
    shipping 6.4 MB of unused files.
6d. Have the build write a build manifest (git SHA if available, timestamp, HERO_VIDEO
    state, page count) to website/build.json, have deploy.yml upload it, and add an audit
    check that compares local build.json against https://bijouduglacier.com/build.json and
    warns when production is behind. That's the drift detector.

────────────────────────────────────────────────────────────────────────
FINISHING UP
────────────────────────────────────────────────────────────────────────
- python3 tools/audit.py must report 0 fail. If you added checks, say which.
- Confirm the four languages are still in parity: same sections, same links, same structured
  data shape, no English leaking into fr/de/it.
- Confirm no JavaScript, no cookies, no third-party requests were introduced anywhere.
- Give me a single summary listing: what changed, what I still need to supply (real review
  quotes, rates, anything you flagged), and any translation you weren't fully confident in.
- Do not deploy. I'll run the deploy myself once I've read the diff.
```

---

## Needs your input before you send it

Four values, and one decision.

**The four values** are in the "Facts I'm supplying" block. Any you leave blank, the agent
skips rather than invents — that's deliberate, because a made-up price or an invented star
rating in structured data is the kind of thing Google issues manual actions for.

**The decision is work item 3.** It needs an email address you're happy to publish, and
ideally a WhatsApp number. If you'd rather not put a personal number on a public site, a
free Google Voice or Swiss prepaid number works and you can drop it later. If you want no
enquiry channel at all, delete work item 3 — but understand that it's the largest revenue
gap on the list, and that without some way to collect addresses the returning-guest email in
`strategy/marketing-plan.md` has nobody to go to.

## What this prompt deliberately leaves out

- **The content layer (§9).** Worth real money, but it's a writing project, not a build
  task, and doing it before you can measure anything means you'd never know if it worked.
- **A real enquiry form with a server endpoint.** Right call eventually; overkill before you
  know your enquiry volume. Mailto and WhatsApp will tell you whether anyone wants to talk
  to you at all, which is the thing worth learning first.
- **An availability calendar on your own domain.** The highest-value thing you could add to
  the site, and entirely dependent on whether SaasFeeHolidays exposes an iCal feed. Ask your
  manager; if the answer is yes, that becomes the next project.
