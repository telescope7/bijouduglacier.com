# Bijou du Glacier — do this next

> Commands below use `$SERVER`. Set it once per terminal session:
> `export SERVER=root@YOUR_SERVER_IP` — the real address is in
> `deploy/inventory.ini`, which is gitignored.

Everything in this folder is finished and usable. This is the ordered checklist for getting it live.

Estimated time to complete steps 1–5: **about two hours.**

**To change the words on the site, skip to Step 3c.** You never need to touch code for that.

---

## What's in here

```
bijou-du-glacier/
├── INSTRUCTIONS.md              ← you are here
├── website/                     ← everything in here is what you upload
│   ├── index.html               ← root: redirects to /en/, lists all four languages
│   ├── styles.css               ← the only stylesheet. Edit it directly.
│   ├── sitemap.xml              ← 16 URLs with hreflang alternates
│   ├── robots.txt
│   ├── _redirects               ← edge redirect / → /en/ (only used if you move to
│   │                              Cloudflare Pages or Netlify; nginx does it directly)
│   ├── en/ fr/ de/ it/          ← four languages × four pages each
│   │   ├── index.html               overview
│   │   ├── apartment/ …             the apartment, room by room
│   │   ├── saas-fee/                the resort
│   │   └── book/ …                  booking
│   ├── img/                     ← 27 photos × 2 formats × 3–4 widths,
│   │                              plus blason.png and its header/favicon sizes
│   ├── video/                   ← the hero walkthrough, 4 encodes (see Step 3b)
│   └── fonts/                   ← self-hosted woff2 + fonts.css (tools/fetch_fonts.py)
├── deploy/                      ← one command puts the site on the Linode. See Step 4.
│   ├── README.md                ← DNS records you need first, and what to do when it breaks
│   ├── inventory.ini            ← your server's IP. The only line you edit.
│   ├── deploy.yml               ← the Ansible playbook: nginx, firewall, upload, HTTPS
│   ├── templates/               ← the nginx config, rendered per-domain
│   └── analytics/               ← how many people click Book. No tracking script;
│                                  it reads the nginx log. Start at its README.
├── copy/                        ← THE WORDS. Edit these, not the code. See Step 3c.
│   ├── copy-en.md               ← ~290 numbered blocks of English text
│   ├── copy-fr|de|it.md         ← the same for the other three languages
│   └── _copy_map.json           ← don't touch; it maps the numbers back to source
├── tools/                       ← NOT needed to run the site. See "How this is built".
│   ├── extract_copy.py          ← makes the copy/*.md files
│   ├── apply_copy.py            ← puts your edited copy back in
│   ├── build_images.py          ← regenerates img/ from the source photos
│   ├── build_video.py           ← re-encodes the hero video from the .mp4 master
│   ├── fetch_fonts.py           ← downloads the self-hosted webfonts. Run once.
│   ├── build_site.py            ← regenerates the 16 pages
│   ├── content_en|fr|de|it.py   ← the copy in code form. You should never need to open these.
│   └── audit.py                 ← pre-flight checks. Run before every deploy.
├── _backup/                     ← the original one-page site, untouched
├── social-media/                ← START AT ITS README.md. All copy-paste ready.
│   ├── README.md                ← the hub: link map, what to do first, biggest wins
│   ├── profiles-and-bios.md     ← exact bio text + link field for all 5 platforms
│   ├── handles.md               ← ranked handle candidates, 5 platforms
│   ├── captions-instagram.md    ← 9 long-form IG/Facebook captions, English
│   ├── captions-german.md       ← 8 German posts. Saas-Fee's biggest market.
│   ├── pinterest-pins.md        ← 8 pins: title, description, board, link
│   ├── reels-tiktok.md          ← 6 short-video posts cut from the walkthrough
│   ├── tweets.md                ← 14 post-ready X/Twitter posts
│   ├── posting-calendar.md      ← 8 weeks, mapped to the files above
│   ├── images/                  ← 23 pre-cropped files, correct size per platform
│   └── video/                   ← 6 clips cut from the walkthrough, watermark-free, silent
└── strategy/
    └── marketing-plan.md        ← positioning, funnel, rates, reviews, 4-week calendar
```

The localised page folders are `en/apartment/`, `fr/appartement/`, `de/ferienwohnung/`,
`it/appartamento/`, and `en/book/`, `fr/reserver/`, `de/buchen/`, `it/prenotare/`.
The URL words are translated on purpose — that is worth real search traffic.

---

## Step 1 — Preview the site locally (2 minutes)

**Serve the folder.** One command, and it matches exactly how the live site is served:

```bash
cd "/Users/mthomas/sandbox/saas-fee-media/bijou-du-glacier/website"
python3 -m http.server 8080
```

Then open <http://localhost:8080>. Press `Ctrl-C` in the terminal when you're done.

> **This changed in September 2026.** The site used to be browsable by double-clicking
> `website/index.html`, because every internal link spelled out `index.html`. That was a nice
> convenience and it cost real crawl budget: each page carried fifteen links to URLs the
> canonical tag tells Google *not* to index, and nginx had to 301 every one of them.
>
> Internal links are now the canonical directory form (`../apartment/`), so they match the
> canonical tag exactly and never redirect. The trade-off is that `file://` shows a directory
> listing instead of the page, so local preview needs the one-line server above.
>
> Double-clicking `website/index.html` still opens the language picker and still reaches the
> four language homepages — that one file deliberately keeps explicit filenames. It's just
> the pages past it that need the server.

Things worth clicking through, either way:

- the **EN / FR / DE / IT** switcher in the header — it should keep you on the *same* page,
  not throw you back to the homepage
- **Book Direct** in the header bar, and again in the Reserve panel lower down
- narrow the window right down: the mosaic goes five cells → four → stacked
- scroll: sections should fade up gently as they arrive

Check it on your phone too — open the local address on your phone if it's on the same wifi.

### Before every deploy, run the audit

```bash
cd "/Users/mthomas/sandbox/saas-fee-media/bijou-du-glacier/tools"
python3 audit.py
```

> **First time after pulling the September 2026 changes, run this once:**
>
> ```bash
> cd "/Users/mthomas/sandbox/saas-fee-media/bijou-du-glacier/tools"
> python3 fetch_fonts.py
> ```
>
> The type is self-hosted now rather than loaded from Google, and the .woff2
> files are not in the repo. Until you run it, `audit.py` fails loudly and
> every page falls back to Georgia and Helvetica. It is a one-off.

It checks all 17 pages for broken links, missing alt text, canonical and hreflang errors,
duplicate titles, invalid JSON-LD and images without dimensions — and it walks the whole
site from `index.html`, resolving directory links the way a web server does, to prove there
are no broken internal links and no orphaned pages. It also fails the build if any page
links to the non-canonical `index.html` form. `0 fail` means ship it. It will also keep
reminding you about
anything that still needs your attention before you deploy.

---

## Step 2 — Booking links: all done

### The direct-booking link is live

`SITE["direct"]` in `tools/build_site.py` points at the real listing:

    https://saasfeeholidays.com/en/saasfeeholidays-du-glacier---b4

Photographs, availability calendar and a **Book Now** button through to the
SaasFeeHolidays checkout. It appears **40 times** across the site: the header bar, the
Reserve panel and the footer, on all 16 pages.

*One improvement still worth making.* Set up a redirect at
`bijouduglacier.com/book-direct` pointing at that URL, and put the redirect in
`SITE["direct"]` instead. Then the link never breaks if your manager changes systems, and
you can count the clicks, which is the only way you will ever know whether the direct
funnel is working.

### Expedia has been removed

There are now two platform listings on the site, Airbnb and Booking.com, and both are
real. If an Expedia listing appears later, add it back in `build_platforms()` and
`build_reservebox()` in `tools/build_site.py`.

### Already correct, no action needed

- Airbnb → `https://www.airbnb.com/rooms/1674533087008414341`
- Booking.com → `https://www.booking.com/hotel/ch/saasfeeholidays-du-glacier-b4.html`

---

## Step 3 — The photos (already done — read this if you want to change them)

**The images are already in place and the site renders correctly right now.** They are
re-derived from your `media files combined` folder by `tools/build_images.py`: cropped to
the exact aspect ratio of the slot each one sits in, then written out at three or four
widths in **both AVIF and JPEG**. The browser picks the smallest file that will look sharp
on that particular screen. The old single 421 KB hero is gone.

`website/img/` now holds 27 photographs, 150 files, 8.5 MB on disk — but a phone loading
the homepage downloads roughly 230 KB of it.

### The hero collage — what's in it and why

Five cells, in a CSS grid mosaic that reshapes at 1024 px and again at 640 px:

| Cell | Content | Job it does |
|---|---|---|
| Tall left | **The walkthrough video**, playing silently on a loop | Shows the whole apartment before anyone scrolls |
| Wide top right | Living room — green sofa, windows, balcony, kitchen beyond | The single shot that sells the space |
| Bottom, 1 of 3 | Open kitchen shelving, brass tap, stone | The detail that says "renovated properly" |
| Bottom, 2 of 3 | Master bedroom, oak-panelled wall | Sleeping quality |
| Bottom, 3 of 3 | A robe on the herringbone oak door (portrait) | Texture, and a hint of hotel |

Each still is cropped to the *exact* ratio of its cell, so `object-fit` has almost nothing
left to crop and the composition you see is the composition that was chosen.

---

## Step 3b — The hero video

`Saas-Fee house.mp4` was **62 MB** — unusable on a web page. `tools/build_video.py`
turns it into files a browser can stream:

| File | What | Size |
|---|---|---|
| `video/hero-720.mp4` | the whole 32-second clip, 720×1280 | **2.4 MB** |
| `video/hero-480.mp4` | the same, 480×854, served at ≤640 px | **1.1 MB** |
| `video/hero-clean-720.mp4` | 2.6 s–28.6 s, VOLLA marks removed | 2.0 MB |
| `video/hero-clean-480.mp4` | the same at 480×854 | 0.9 MB |
| `img/hero-poster-*` | the frame at 0.40 s, JPEG + AVIF | 68 KB |

It plays **muted, looped, inline and with no controls** — the only combination
browsers will autoplay. `object-fit: contain`, never `cover`, so the whole frame is
visible top to bottom: it's a walkthrough, and cropping it would cut the rooms in half.
The audio track is dropped (a muted video doesn't need one) and the two black opening
frames are trimmed so the loop doesn't blink.

The poster frame is preloaded and is the page's LCP element. The video itself is
**not** preloaded — it streams in after the text and the poster have painted.

### ⚠️ The video carries your property manager's branding

Two things in the master are VOLLA's, not yours:

- the word **VOLLA** fades over the mountain from about **0.9 s to 2.4 s**
- the **last three seconds** are a VOLLA logo animation

The site currently plays **the whole clip**, watermarks and all, because that's what
you asked for. If you'd rather not carry another company's mark at the top of your own
homepage, there is a clean cut of the same footage — 26 of the 32 seconds, both ends
removed. To switch, change one line in `tools/build_site.py`:

```python
HERO_CLIP = "hero"          # -> change to "hero-clean"
```

then re-run `python3 build_site.py`. Better still, ask VOLLA for an unbranded master —
you commissioned it.

### Reverting to the still photograph

Two ways, both easy:

- **In the file:** open any `*/index.html`, find `<figure class="cell-a cell-video">`.
  The original `<picture>` is sitting right there, commented out, with instructions.
  Delete the `<video>` and the `<img class="motion-still">`, un-comment the `<picture>`.
- **Everywhere at once:** set `HERO_VIDEO = False` in `tools/build_site.py` and re-run.

### Reduced motion

Visitors whose system is set to "reduce motion" get the poster frame instead of the
loop — the CSS swaps them, no JavaScript. That setting exists for people who get
motion sickness from autoplaying video, and a looping hero is exactly what it means.

### Photographs you don't have, and should take

I went through all 36 Airbnb stills and all 35 video keyframes. Three shots the collage
would be better for, and that don't exist anywhere in your folder:

1. **The building from outside, at dusk, windows lit.** Still the single biggest gap — it's
   action #4 in the marketing plan. Right now nothing on the site shows the guest what
   they are walking towards. Half a day with a local photographer in December.
2. **The ski locker.** The listing confirms there *is* one, in the basement of the
   building, and the site now says so — but there is no photograph of it. Every group of
   eight wants to know where the kit goes, and a picture would answer it faster than a
   sentence.
3. **The walk to the lifts.** Ninety seconds of the actual route, in snow. It is the claim
   the whole location argument rests on, and it is currently unillustrated.

There is **no wood stove** in this apartment — I checked every frame — so the site never
claims one.

Two existing images are the weakest links: the balcony shot and a few of the bathroom
frames came from 720 px Airbnb files, so they cap out lower than the rest. Fine at the size
they display; replace them if the photographer's originals surface.

### If you want to swap a photo

1. Drop the new file into `media files combined/` (or anywhere) and point at it from the
   `MANIFEST` list in `tools/build_images.py`.
2. Run `python3 build_images.py` then `python3 build_site.py`.
3. **Update the alt text and caption** for that image in all four `tools/content_*.py`
   files — they're in the `"alt"` and `"caption"` dicts at the bottom, keyed by image name.
   Alt text is what a blind visitor and a search engine both read; a stale one is worse
   than none.
4. Run `python3 audit.py`.

**Note on your source folder:** several frames in `media files combined/extract/` carry a
"VOLLA" watermark (your property manager's or videographer's branding). I avoided all of
them — do the same if you pick your own.

---

## Step 3c — Rewriting the words

**You never have to open a code file to change the text on this site.**

Every readable word lives in `copy/copy-en.md` (and `-fr`, `-de`, `-it`) as a numbered
block. You edit the words, and two small tools put them back exactly where they came from.

```
[EN-010]  Main headline
A jewel beneath the glacier in car-free Saas-Fee

[EN-011]  Sentence under the headline
Eight guests. Four king-size beds. A walnut table long enough for every one …
```

**281 blocks per language**, ordered the way you read the site: header and buttons, then
the homepage top to bottom, then each of the other three pages, then the FAQ, the
amenities list and the table, the footer, and finally the text nobody sees on the page —
Google result titles, image descriptions for blind visitors, and screen-reader labels.

### The three commands

```bash
cd "/Users/mthomas/sandbox/saas-fee-media/bijou-du-glacier/tools"

python3 extract_copy.py             # 1. produce fresh numbered files
#    …edit copy/copy-en.md in any text editor…
python3 apply_copy.py --dry-run     # 2. show exactly what would change
python3 apply_copy.py               # 3. put the edits back
python3 build_site.py && python3 audit.py
```

`--dry-run` prints a before/after for every block you touched and writes nothing. Use it
first, every time.

### The rules

| | |
|---|---|
| **Edit the words, never the numbers** | `[EN-010]` is how the text finds its way home. Change it and that block is ignored. |
| **Deleting a block means "no change"** | It is not a way to remove text from the site. Tell me if you want something gone. |
| **Keep the link tags** | `<a href="{apartment}">Take the tour</a>` — change the words inside, keep the `<a …>` and `</a>` around them. `{apartment}`, `{resort}` and `{book}` fill themselves in. |
| **`—` and `·` are deliberate** | Em dash and middle dot. Straight hyphens will look wrong in the display serif. |
| **Watch the headline length** | The homepage headline is sized to sit on exactly one line. Over ~48 characters in English it wraps and the masthead loses its shape. |

### Two safety nets

**It refuses to run from a stale map.** The tools work by exact byte offset into the
content files, which is why they never mangle anything. But if a content file changes
between extracting and applying, those offsets no longer line up. `apply_copy.py` stores a
checksum and **stops with an explanation** rather than corrupting the file. If you see
that message: re-run `extract_copy.py`, redo your edits on the fresh file, apply again.

*Practical consequence:* don't ask me for other copy changes while you have a copy file
out for editing. Layout, colour and image work are fine — those don't touch the content
files.

**It restores itself if anything goes wrong.** Every file gets a `.bak` before it is
touched, and afterwards the tool re-compiles it. If the result is malformed for any
reason, the backup goes straight back and you lose nothing.

### The other three languages

If you only edit `copy-en.md`, the French, German and Italian will drift out of step. Send
me the English file and I'll re-translate just the lines you changed — the translations
are written against what people actually search in each language, so running them through
a machine translator is a downgrade, not a shortcut.

---

## Step 4 — Deploy to bijouduglacier.com

You have a Linode running Ubuntu, so the site is deployed with one command from
the `deploy/` folder. Full detail, including the DNS records you need first, is in
**[deploy/README.md](deploy/README.md)**. The short version:

```bash
brew install ansible                       # once, ever

# A records for @ and www must already point at the Linode's IP
# put that same IP in deploy/inventory.ini

cd deploy
ansible-playbook -i inventory.ini deploy.yml
```

That installs nginx, opens the firewall, uploads the site, and gets an HTTPS
certificate from Let's Encrypt. It is safe to run repeatedly: the certificate is
only requested once, and later runs just re-upload the site in about twenty
seconds. Renewal is automatic through certbot's systemd timer, so the
certificate is not something you have to diary.

**The cycle from here on is three commands:**

```bash
cd tools && python3 build_site.py && python3 audit.py     # 0 fail before you ship
cd ../deploy && ansible-playbook -i inventory.ini deploy.yml
```

**Booking clicks are counted.** Every booking button points at a path on your
own domain (`/book-direct`, `/go/airbnb`, `/go/booking`) and nginx redirects it
out to the platform, logging the click on the way past. There is no analytics
script, no cookie and no third party anywhere on the site, so there is nothing
to put in a consent banner. To see this month, by channel and language:

```bash
ssh $SERVER "zcat -f /var/log/nginx/bijou-bookings.log* | awk -v m=\$(date +%b/%Y) '\$4 ~ m {split(\$7,p,\"/\"); ch=(p[2]==\"go\")?p[3]:\"direct\"; split(\$11,r,\"/\"); lang=(r[4]~/^(en|fr|de|it)\$/)?r[4]:\"none\"; n[ch\" \"lang]++} END{for(k in n) printf \"%5d  %s\\n\", n[k], k}' | sort -rn"
```

There is a full GoAccess report too, at `/analytics/`, behind a password you
set yourself. `deploy/analytics/README.md` covers all of it.

Two things the deploy does that a drag-and-drop host would not: it 301s
`/en/apartment/index.html` to `/en/apartment/`, which is the canonical form in
every page's `<link rel="canonical">`, and it teaches nginx that `.avif` is
`image/avif`, which Ubuntu 22.04's nginx 1.18 does not know and would otherwise
serve as a binary download.

*If you ever want to leave the Linode, the site is still just static HTML.
Cloudflare Pages, Netlify Drop and GitHub Pages will all serve the contents of
`website/` for free, and the `_redirects` file is there for the first two.*

**Then check:**

- [ ] `https://bijouduglacier.com` bounces to `/en/`
- [ ] `https://bijouduglacier.com/de/ferienwohnung/` loads (proves every folder went up)
- [ ] `http://bijouduglacier.com` and `https://www.bijouduglacier.com` both land on `https://bijouduglacier.com`
- [ ] The hero mosaic shows the video playing on the left and five photographs
      to the right, not six grey boxes
- [ ] The video loops silently and does not open fullscreen when tapped on a phone
- [ ] The language switcher keeps you on the same page across all four languages
- [ ] Every booking button goes where it should — **click all four, in one language**
- [ ] It looks right on your phone

### Then, the same afternoon

1. **Google Search Console** → add `bijouduglacier.com` → submit
   `https://bijouduglacier.com/sitemap.xml`. Then open the **International Targeting**
   report a week later; it is where hreflang mistakes show up.
2. **Rich Results Test** (<https://search.google.com/test/rich-results>) on
   `https://bijouduglacier.com/en/` — it should find *VacationRental*, *FAQPage* and
   *BreadcrumbList*.
3. **PageSpeed Insights** on the same URL, mobile tab. The two numbers that matter are LCP
   and CLS. CLS should be ~0: every image on the site has its dimensions declared, so
   nothing moves as the page loads.
4. Paste the URL into the **Facebook Sharing Debugger** and **X Card Validator** to warm the
   share-image cache before you post anything.

---

## Step 5 — Register the social handles (30 minutes, one sitting)

Full ranked candidates are in `social-media/handles.md`. The short version:

**Target string: `bijouduglacier`** — it matches your domain exactly and, at 14 characters, it fits inside X's 15-character limit.

Register in this order, because the constraint tightens as you go:

1. **X / Twitter** — <https://x.com/signup> — tightest limit, check first
2. **Instagram** — <https://instagram.com/accounts/emailsignup> — your most important channel
3. **TikTok** — <https://tiktok.com/signup>
4. **Pinterest** — <https://pinterest.com/business/create> (use a *business* account — you get analytics and rich pins)
5. **Facebook Page** — <https://facebook.com/pages/create> — page name `Bijou du Glacier — Saas-Fee`, then set the username

If your first choice is taken on one platform only, take that platform's top fallback — don't downgrade the other four to match.

Then: **add the handles to the site footer** (in `tools/build_site.py`, not the generated
HTML), and write them down somewhere you'll find them again.

### Step 5b — Set the profiles up properly, before posting anything

Open **`social-media/profiles-and-bios.md`**. It has the exact bio text, name field, category
and link for all five platforms, already written to length. Paste, don't compose.

Two things in there that are easy to miss and both free:

- Switch Instagram and TikTok to **Business** accounts — it's what unlocks the bio link on
  TikTok and Insights on both.
- **Claim your domain on Pinterest.** It puts your logo on every pin linking to you and turns
  on pin analytics. Same DNS-TXT dance as Search Console.

### Step 5c — Post something

`social-media/README.md` is the hub. The short version of what it says:

| Priority | What | Why |
|---|---|---|
| 1 | **German posts** (`captions-german.md`) | Saas-Fee is in German-speaking Wallis. You built a whole German site and nothing pointed at it. |
| 2 | **Pinterest** (`pinterest-pins.md`) | A pin works for 18 months; an IG post dies in 2 days. Images are pre-cut and ready. |
| 3 | **The walkthrough video** (`reels-tiktok.md`) | Already shot and paid for. Six clips are cut, watermark-free and silent, in `social-media/video/`. |
| 4 | Instagram (`captions-instagram.md`) | Your main channel. |
| 5 | X (`tweets.md`) | Cheap to keep up, lowest booking volume. |

Then put week 1 of `posting-calendar.md` into a scheduler.

> **Two corrections were made to the old social copy that matter.** The previous version
> claimed booking direct gets you a *lower nightly rate* — that implies breaking rate parity
> with Booking.com. Every file now uses the site's wording: the nightly rate is **identical**,
> and what you save is the platform's service fee on top. If you posted the old version
> anywhere, edit or delete it.
>
> The walkthrough video also carries the property manager's **VOLLA** watermark in its first
> and last three seconds, and a music track you probably don't hold rights to. The clips in
> `social-media/video/` are cut from the clean middle and have the audio stripped — use those,
> not the master file.

---

## Step 6 — Recommended go-live order for everything else

Once steps 1–5 are done:

1. **Week 1.** Site live, handles registered, profile photos and bios set on all five accounts. Bio on every platform: *Luxury 4-bedroom apartment · Saas-Fee, Valais · Sleeps 8 · Book direct → bijouduglacier.com*
2. **Week 1.** Post Instagram Caption 1 and Tweet 1. Don't wait until you have a full content bank — you'll never start.
3. **Week 2.** Order the in-apartment welcome book (action #3 in the marketing plan). This is the highest-return thing in the whole package and it's easy to keep deferring.
4. **Week 2.** Confirm with your property manager that a review request goes out ~24 hours after every checkout, and read the text they use.
5. **Weeks 2–4.** Run the four-week calendar in `strategy/marketing-plan.md` §5.
6. **Before November.** Book the exterior photo shoot. December light on lit windows is what you want, and photographers in Valais get booked up for the season.
7. **Each December.** Send the returning-guest first-refusal email. Put a recurring reminder in your calendar now, while you're thinking about it.

---

## Notes on how the site is built

Worth knowing before you or anyone else edits it:

- **No JavaScript anywhere.** No `<script>` tags except the JSON-LD data blocks, which are
  data and not code. No inline handlers, no external scripts. The FAQ accordions are native
  `<details>` elements.
- **No forms, no tracking, no third-party requests.** Nothing loads from another domain, so
  there is no cookie banner to worry about.
- **Every path is document-relative** (`../styles.css`, `saas-fee/index.html`), so the site
  works both when served from a domain and when opened straight off your disk. The absolute
  `https://bijouduglacier.com/...` URLs appear only where search engines need them: the
  canonical tag, the hreflang set, OpenGraph, the JSON-LD and `sitemap.xml`. Those all use
  the clean directory form (`/de/ferienwohnung/`), and Cloudflare Pages and Netlify both
  redirect the `.../index.html` form to it automatically.
- **The palette is "Stone & Champagne":** warm greige paper `#F5F3F0`, near-black
  `#211F1C` text, deep taupe bands `#35322E` for the header, the masthead, the reserve
  card and the footer, and bronze `#7A5E33` on light / champagne `#D8C29A` on taupe for
  links, rules and the primary call to action. Every text/background pair was measured,
  not eyeballed — the numbers are in the comment at the top of `styles.css`. All clear
  WCAG AA; most clear AAA.
- **Type is Cormorant Garamond over Inter**, from Google Fonts. See `fonts/README.md`.
  The serif is doing most of the work on "does this feel expensive".
- **One header bar, not two.** Brand, navigation, language switcher and a **Reserve**
  button all live in the single taupe bar. The white strip that used to sit under it is
  gone; on the interior pages its section links now sit inside the dark masthead instead.
- **The blason** sits in the header on taupe. It carries `alt=""` on purpose: the wordmark
  beside it already says "Bijou du Glacier", and giving the image alt text would make a
  screen reader announce the brand twice for one link. The same shield is the favicon and
  the iOS home-screen icon.
- **The masthead is three full-width lines** — the specification (SLEEPS 8 · 4 KING
  BEDROOMS · …), the headline, the lede — and then the mosaic. No rule between them, no
  buttons: **Reserve** already sits in the header bar and again in the availability block,
  so a third pair here only pushed the photography down the page.
- **The headline plays on the name.** *Bijou* is French for jewel, so the English reads
  "A jewel beneath the glacier"; the French is literally "Un bijou sous le glacier", which
  is the property's own name folded into the sentence.
- **The footer** carries the blason beside the address. The language row and the
  "privately owned…" line have been removed — the switcher is in the header, and the
  disclaimer was reassuring nobody.
- **No em dashes anywhere in the copy.** They are the single most reliable tell that a
  page was written by a machine, and this site sells a luxury apartment partly on the
  strength of sounding like a person wrote it. `audit.py` **fails the build** if one
  appears in the visible text of any page, in any language. If you add copy, use a full
  stop, a colon or a comma instead.
- **There is now one small script**, inline at the foot of each page: about twelve lines
  that fade sections in as you scroll. It is deliberately fail-safe — the stylesheet only
  hides anything once the script has added a `.js` class, so if it never runs (or the
  visitor has asked for reduced motion) the page renders complete and static. No CDN, no
  library, no dependency.
- **Type** is Archivo for headings and Inter for body, self-hosted. See `fonts/README.md` —
  the two files are not in the folder yet and the site falls back gracefully until they are.
- **Accessibility:** semantic landmarks, a skip link, `aria-current` on the active nav item
  and language, one `<h1>` per page with no heading-level skips, descriptive alt text on
  every image in the page's own language, and visible focus outlines.
- **The direct-booking CTA appears three times per language** and is visually dominant every
  time. The OTA buttons are deliberately quieter and secondary.

### How this is built (the `tools/` folder)

The 16 pages are generated from four content files by `tools/build_site.py`. **This is not a
build system and the site does not depend on it.** The HTML on disk is complete and
self-contained; you can hand-edit any page and it keeps working, and `styles.css` is edited
directly with no rebuild at all. The generator exists so a change to the copy doesn't have
to be made sixteen times by hand — and so the hreflang tags stay reciprocal, which is the
one thing you cannot reliably maintain manually.

- Change **wording** → `extract_copy.py`, edit `copy/copy-en.md`, `apply_copy.py`,
  `build_site.py`. See Step 3c — you should not need to open `content_*.py` by hand.
- Change **colours, spacing, type** → edit `website/styles.css` → nothing to run
- Change **photographs** → `tools/build_images.py`, then `build_site.py`
- Change **a URL or the address** → the `SITE` block in `build_site.py` → `build_site.py`
- **Always finish with** `python3 audit.py`

### Four languages

English, French, German and Italian, at `/en/`, `/fr/`, `/de/`, `/it/`. Each language has its
own URLs, `<html lang>`, canonical, titles, meta descriptions, headings, body copy, image
alt text, captions and structured data — this is not a JavaScript text-swap over one
indexable URL, which is the version that earns nothing in search.

The copy is written per language against what people in that language actually type, not
translated word for word. Germans search *Ferienwohnung*, not *Apartment*; the French
search *appartement de vacances*; nobody searches "self-catering" in any of the three.
The header switcher takes you to the *equivalent* page, never back to the homepage.

`x-default` points at `/en/`, and the bare domain redirects there.
