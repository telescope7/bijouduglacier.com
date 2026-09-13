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

*Sources consulted: [IndexNow FAQ](https://www.indexnow.org/faq) ·
[AI crawler user-agent reference 2026](https://www.anagram.ai/blog/ai-crawler-user-agent-list-2026-14-bots-and-robotstxt-tokens-to-know) ·
[AI crawlers explained](https://www.anagram.ai/blog/ai-crawlers-explained-gptbot-claudebot-perplexitybot-and-how-to-let-them-in-2026)*
