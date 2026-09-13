# Social media — start here

Rewritten 13 September 2026, against the live four-language site.

Everything in this folder is finished and copy-paste ready. Nothing here needs editing before
you post it, except where a line is marked **[YOUR INPUT]**.

---

## What changed, and why the old files were wrong

The first version of these assets was written for the old one-page site. The site is now 16
pages in four languages, and three things had gone stale in a way that mattered:

**1. The direct-booking claim was wrong, and slightly risky.** The old copy said booking
direct "skips the platform commission entirely — which means the best rate we can offer goes
to you." That implies a *lower nightly rate* than the platforms, which is exactly what
Booking.com's rate-parity terms prohibit. Your live site already says it correctly:

> The nightly rate is identical to the platforms. Booking with us simply takes their service
> fee off your total.

All social copy now uses that framing. It's both compliant and more persuasive, because it's
specific. **If you have already posted the old version anywhere, edit or delete it.**

**2. Every link pointed at the bare domain.** There are now four real destinations in four
languages. A post about the glacier should land on the Saas-Fee page, not the homepage.

**3. Two image filenames no longer existed** (`hero-exterior.jpg`, `dining-room.jpg`), and 20
new photographs had appeared that nothing referenced — including the floor plan, which is one
of the strongest single assets you own.

---

## The link map — copy these exactly

| Post is about | Link to |
|---|---|
| General / brand / anything | `https://bijouduglacier.com` |
| The apartment, rooms, design, beds | `https://bijouduglacier.com/en/apartment/` |
| Saas-Fee, skiing, the village, summer | `https://bijouduglacier.com/en/saas-fee/` |
| Booking, rates, availability, direct | `https://bijouduglacier.com/en/book/` |

German audience — use these instead:

| | |
|---|---|
| Homepage | `https://bijouduglacier.com/de/` |
| Die Wohnung | `https://bijouduglacier.com/de/ferienwohnung/` |
| Saas-Fee | `https://bijouduglacier.com/de/saas-fee/` |
| Buchen | `https://bijouduglacier.com/de/buchen/` |

French: `/fr/`, `/fr/appartement/`, `/fr/saas-fee/`, `/fr/reserver/`
Italian: `/it/`, `/it/appartamento/`, `/it/saas-fee/`, `/it/prenotare/`

**Never link social posts to `/book-direct`, `/go/airbnb` or `/go/booking`.** Those are the
outbound redirect paths. They send the visitor straight off your site to the booking engine,
skipping everything that persuades them, and they're blocked in `robots.txt`. Always land
people on `/en/book/` and let them click through from there — that way the click still gets
counted in your nginx log, and they've seen the page first.

---

## Biggest bang for the buck — my honest ranking

### 1. German-language posting — the single biggest gap

Saas-Fee is in German-speaking Upper Valais. Its core markets are German-speaking
Switzerland, Germany and Austria. Your site already has a complete German version that took
real effort to produce, and **not one word of social copy points at it.**

`captions-german.md` fixes that. If you do nothing else on this list, do this one. You are
competing for a German-speaking audience against listings written in English by people who
have never been there.

### 2. Pinterest — the highest return per hour, and nobody in this market uses it

Pinterest is a search engine that happens to look like a social network. A pin keeps driving
traffic for 18 months or more; an Instagram post is dead in 48 hours. Travel and interiors
are its two strongest categories, and you have professional photography in both.

I've built eight ready-to-upload pins at the correct 1000×1500 size in
`images/pinterest/`, with the copy in `pinterest-pins.md`. One pin a week is ten minutes and
it compounds.

### 3. The walkthrough video you already paid for

You have a professionally shot vertical walkthrough sitting in `website/video/`, and four
encodes of it. It is currently used in exactly one place — the hero collage on your own
homepage, where only people who already found you will see it.

Cut into six clips it becomes a quarter of Reels and TikToks at zero marginal cost.
`reels-tiktok.md` has the cut list with timings and a caption for each.

### 4. Instagram — your main channel, but post portrait, not landscape

Detail in `captions-instagram.md`. One non-obvious thing worth knowing, explained below under
"About the images".

### 5. X / Twitter — keep it, but don't spend much on it

Lowest booking volume of anything here. It's cheap to maintain and the direct-booking
argument travels well in text. `tweets.md`, three posts a week, ten minutes.

---

## About the images — read this once

**Post the vertical shots to Instagram, not the landscape ones.**

Your photography tops out at 1200×800 pixels. Instagram displays at 1080 wide, so a landscape
photo cropped to portrait has to be blown up and goes soft. But the frames from your
walkthrough video are natively 1080×1920 — so a 4:5 Instagram crop from those is
**pixel-perfect and sharper than your actual photographs**, and portrait posts take up far
more of the phone screen.

I've pre-cut both. In `images/instagram/`:

- `ig-*.jpg` at 1080×1350 — portrait, native resolution, **use these by default**
- `ig-sq-*.jpg` at 1080×1080 — square, mildly upscaled from the stills, use when the subject
  only works in landscape (the kitchen, the floor plan)

`images/story-reel/` holds 1080×1920 frames for Stories and Reel covers, untouched.

### The one fix worth making at the source

Your photographs are downsampled web copies — 1200×800 is what an OTA listing exports, not
what a photographer delivers. **The originals are almost certainly 4000+ pixels wide.** One
email to SaasFeeHolidays or the photographer asking for the full-resolution files would
upgrade every image in this folder, cost nothing, and take five minutes.

Do that before the exterior shoot, not after.

---

## What's in this folder

| File | What it is |
|---|---|
| `README.md` | This. |
| `profiles-and-bios.md` | **Do this first.** Exact bio text, link fields and profile images for all five platforms. |
| `handles.md` | Ranked handle candidates. Availability still needs checking by hand. |
| `captions-instagram.md` | 9 long-form English captions for Instagram and Facebook. |
| `captions-german.md` | 8 German posts — captions and short-form. |
| `pinterest-pins.md` | 8 pins: title, description, board, target link. |
| `reels-tiktok.md` | 6 short-video cuts from the walkthrough, with captions and on-screen text. |
| `tweets.md` | 14 X posts. |
| `posting-calendar.md` | Eight weeks, mapped to the assets above. |
| `images/` | 23 pre-cropped, correctly-sized files. |

## If you have one hour, in order

1. `profiles-and-bios.md` — register and set up the accounts properly. 30 min.
2. Post Instagram caption 1 with `images/instagram/ig-village-carfree.jpg`. 5 min.
3. Upload three pins from `images/pinterest/`. 10 min.
4. Post German caption 1. 5 min.
5. Open `posting-calendar.md` and put week 1 into a scheduler. 10 min.
