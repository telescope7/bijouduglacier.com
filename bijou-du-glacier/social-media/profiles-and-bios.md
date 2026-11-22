# Profiles and bios — set these up first

Everything below is copy-paste. Nothing needs rewording.

> **Decisions made 21 November 2026:**
> - **Doing now:** Instagram, Facebook, Pinterest. X and TikTok deferred, though the
>   handle is still checked on X first, because its 15-character limit is what
>   constrains the choice everywhere else.
> - **Public contact address: `hello@bijouduglacier.com`**, forwarding to Matt's
>   personal inbox. The domain's MX records already point at Porkbun's forwarders,
>   so this is an alias to create, not a mail system to set up. The personal
>   address stays off all public profiles.
> - **Handle: one string everywhere.** Target `bijouduglacier`; if X has it, take
>   the same fallback on all three rather than a different name per platform.
> - **The site will link to these** from the footer in all four languages, plus
>   `sameAs` in the structured data, once the accounts have some content on them.

Do this before you post anything. A post that lands on an empty profile with no bio and no
link converts nobody, and you only get one first impression per visitor.

---

## Profile and cover images

| Use | File | Notes |
|---|---|---|
| **Profile picture**, every platform | `../website/img/blason.png` | Your crest. Square-ish, reads at small sizes, and it's the same mark as the website header — that continuity is worth more than a photo. |
| Facebook cover | `images/instagram/ig-sq-village.jpg` or `../website/img/massif-1200.jpg` | The massif shot is 1200×450, close to Facebook's cover ratio. |
| X header | `../website/img/massif-1200.jpg` | 1200×450 is almost exactly X's 3:1 header. |
| Pinterest cover | `images/pinterest/pin-village-carfree.jpg` | |

If the crest looks cramped as a circular avatar, use `../website/img/blason-112.png` and let
the platform scale it.

---

## Instagram

**Name field** (this is searchable — it is not the handle, and most people waste it):

```
Bijou du Glacier | Saas-Fee Apartment
```

**Bio** (150 character limit — this is 109):

```
Four-bedroom apartment for 8 in car-free Saas-Fee.
4 double bedrooms · 3 baths · 4 min to the slopes.
Book direct ↓
```

**Link:**

```
https://bijouduglacier.com
```

**Category:** Vacation Home Rental

**Contact email:**

```
hello@bijouduglacier.com
```

> Switch to a **Professional account → Business**. It's free, it unlocks Insights, and it lets
> you add the contact button. Do it before you post.

---

## Facebook Page

**Page name:**

```
Bijou du Glacier - Saas-Fee
```

> **Plain hyphen, not an em dash.** Facebook rejects `—` in Page names outright:
> *"The name 'Bijou du Glacier — Saas-Fee' is invalid. We suggest 'Bijou du
> Glacier - Saas-Fee'."* Found the hard way on 21 November 2026. The hyphen form
> is what the live Page uses.

**Username:** `@bijouduglacier` (see `handles.md` for fallbacks)

**Category:** Vacation Home Rental

**Short description** (255 characters):

```
A newly renovated four-bedroom apartment for eight in car-free Saas-Fee, Valais. Four doubles made up as kings or twins, three bathrooms, a walnut table that seats everyone, and a covered balcony facing thirteen four-thousand-metre peaks.
```

**Website:**

```
https://bijouduglacier.com
```

**Contact email:**

```
hello@bijouduglacier.com
```

**About / long description:**

```
Bijou du Glacier occupies the east end of the second floor of Residence du Glacier, in the heart of Saas-Fee.

Four double bedrooms, each with its own window and its own morning light. Two have king-size beds; the other two are zip-and-link, made up as a king or as twins, whichever suits the party. Three bathrooms in pale stone and dark slate — two with deep baths, the third with a walk-in shower. One long open room holding the kitchen, the sitting area and a live-edge walnut table that seats all eight at once.

The balcony runs the full width of the apartment, covered, facing the Mischabel massif.

Saas-Fee has been closed to traffic for decades. You leave the car at the entrance to the village and walk from there — four minutes to the slopes, twenty metres to the supermarket.

Booking direct: the nightly rate is identical to the platforms, and booking with us simply takes their service fee off your total.
```

---

## Pinterest

Create a **Business** account, not personal — it's free and it's the only way to get analytics
and rich pins.

**Display name** (Pinterest indexes this heavily — keywords earn their place here in a way
they don't on Instagram):

```
Bijou du Glacier | Luxury Apartment, Saas-Fee
```

**About:**

```
A four-bedroom luxury apartment for eight in car-free Saas-Fee, Valais, Switzerland. Modern alpine interiors, glacier views, four minutes from the slopes.
```

**Website:** `https://bijouduglacier.com` — then **claim the domain** under Settings. Claiming
gets your logo on every pin that links to you and unlocks analytics on them. It's a DNS TXT
record or an HTML file upload; you've done this for Search Console already, so it's familiar.

**Boards to create** — exactly these five, in this order:

| Board name | Description |
|---|---|
| Saas-Fee, Switzerland | The car-free Pearl of the Alps: glacier skiing, summer hiking, and a village with no traffic. |
| Modern Alpine Interiors | Oak, pale stone and brushed brass. Chalet style without the carved-pine cliché. |
| Luxury Ski Apartments | Four-bedroom apartments and chalets for groups in the Swiss Alps. |
| Skiing the Allalin Glacier | Year-round glacier skiing above Saas-Fee at 3,500 m. |
| Group Ski Trips | Where to stay when there are eight of you and nobody wants the small room. |

---

## X / Twitter

**Name:**

```
Bijou du Glacier
```

**Bio** (160 characters — this is 159):

```
Four-bedroom apartment for eight in car-free Saas-Fee, Valais. Kings or twins, 3 baths, 4 min to the slopes. Book direct: same rate, no platform fee.
```

**Location:** `Saas-Fee, Valais, Switzerland`
**Website:** `https://bijouduglacier.com`

> ⚠️ **`@du_glacier` on X already exists** and belongs to Residence du Glacier — the building,
> not your apartment. Don't mistake it for yours, and don't impersonate it. Worth following,
> and worth knowing about if someone tags the wrong account.

---

## TikTok

**Name:**

```
Bijou du Glacier · Saas-Fee
```

**Bio** (80 character limit — this is 79):

```
4-bed apartment for 8 · car-free Saas-Fee 🇨🇭
Glacier skiing, 4 min to the lifts
```

**Link:** `https://bijouduglacier.com` — note TikTok only allows a bio link on Business
accounts, so switch to one.

---

## The link field, and why it's just the homepage

Every platform above points at `https://bijouduglacier.com`, not a link-in-bio service.

Three reasons. It's a domain you own, so nothing breaks when a third-party service changes
its pricing. It costs no extra hop, which matters on mobile. And your traffic measurement
reads the nginx log — a click that lands on your own server is a click you can count, and one
that lands on Linktree is one you can't.

The homepage bounces to `/en/` and shows the language switcher, so a German visitor is one
tap from German.

---

## Before you post anything — the five-minute check

- [ ] Profile picture set on all five, and it's the same image everywhere
- [ ] Bio filled in, with the specifics (8 guests / 4 bedrooms / 4 minutes) not adjectives
- [ ] Link field filled in and **clicked once to confirm it works**
- [ ] Instagram and TikTok switched to Business accounts
- [ ] Pinterest domain claimed
- [ ] All handles recorded in `handles.md` so you don't have to remember them
- [ ] `hello@bijouduglacier.com` created in Porkbun and **tested by sending it a mail**

---

## One thing not to do

**Don't put your website URL in your Airbnb or Booking.com listing** — not in the
description, not in photo captions, not in house rules, not in guest messages. It breaches
both platforms' terms and risks delisting, which would cost far more than the referral is
worth.

Linking *from* your own social profiles *to* your site is entirely fine. It's the direction
into the OTAs that's restricted.


---

## Status — 21 November 2026

### Facebook: Page created and configured

**https://www.facebook.com/profile.php?id=61596559180995**

| Field | Value |
|---|---|
| Page name | `Bijou du Glacier - Saas-Fee` (hyphen, see above) |
| Category | Vacation Home Rental |
| Profile picture | `website/img/blason.png` |
| Cover photo | `website/img/massif-1200.jpg` |
| Website | `https://bijouduglacier.com` |
| Contact email | `hello@bijouduglacier.com` |
| Bio | the 255-character short description, 236 used |

**Deliberately left undone, and why:**

- **Username `@bijouduglacier` is NOT set, and Facebook does not currently offer
  the field.** `bijouduglacier` was confirmed free and registered on X, Instagram
  and Facebook on 21 November, so the string is settled. But on this Page the
  username control could not be found in Page setup, in "How people find and
  contact you", in Page details, or in the About editor. Facebook commonly
  withholds a custom username on a brand-new Page until it has some age or
  activity. Check again after the first few posts, or set it from Meta Business
  Suite. Until then the Page URL stays the numeric `profile.php?id=` form.
- **Street address left blank.** This file never specified one for Facebook, and
  publishing the exact address on the Page is the owner's call, not a default.
  It is already public in the site footer and the structured data.
- **Hours left unset**, which shows no hours rather than implying a staffed reception.
- **WhatsApp not connected** — it sends a verification code to a phone.
- **Friends not invited** — that sends messages on the owner's behalf.
- **Meta marketing emails turned OFF.** They default to on.

### X: profile configured — 21 November 2026

**https://x.com/bijouduglacier**

| Field | Value |
|---|---|
| Handle | `@bijouduglacier` (registered by Matt) |
| Display name | `Bijou du Glacier` — **was "Matthew Thomas"**, the registration default |
| Bio | the 160-character bio from this file, 149 used |
| Location | `Saas-Fee, Valais, Switzerland` |
| Website | `https://bijouduglacier.com` |
| Avatar | the crest, already uploaded by Matt |
| Header | `website/img/massif-1200.jpg` |

X rewrites the website field as a `t.co` short link in the profile display. That
is normal and the click still lands on the site, so it still shows up in the
nginx log.

### Still to do

1. **Pinterest — not started.** Nothing exists yet: no account, no boards, no
   domain claim. This is the platform the README ranks highest for return per
   hour, so it is the biggest remaining gap. Needs a Business account, the five
   boards in the order listed above, and the domain claimed via a DNS TXT record
   at Porkbun.
2. **Instagram** — account registered, profile picture awaiting validation.
   Threads comes free with it and is worth claiming at the same time.
3. **Facebook Page username** — see above; Facebook is not currently offering the
   field on a Page this new. Retry after the first few posts.
4. **Website footer links and `sameAs`.** The site still links to no social
   account and the structured data lists only the three booking channels. Worth
   doing once Instagram is live and the Facebook Page has a real username, so
   the footer does not have to carry a `profile.php?id=` URL.
5. **Nothing has been posted yet.** `posting-calendar.md` is an eight-week plan
   that has not started.

### Done

- `hello@bijouduglacier.com` created and tested, 21 November 2026.
- `bijouduglacier` registered on X, Instagram and Facebook — one string
  everywhere, as planned.
- X profile fully configured. Facebook Page created and configured apart from
  the username.


---

## Status — 22 November 2026: all four accounts live and posted

| Platform | Profile | First post |
|---|---|---|
| X | `@bijouduglacier` — name, bio, location, website, header, crest | tweets.md post 1, with image |
| Facebook | Page configured; bio, website, `hello@` contact, crest, cover | captions-instagram.md caption 1, adapted, with image |
| Pinterest | `pinterest.com/bijouduglacier` — crest, About, **domain verified** | pinterest-pins.md pin 1, to the "Saas-Fee, Switzerland" board |
| Instagram | `@bijouduglacier` — crest and bio | caption 1, single image |

### Things found the hard way

- **Pinterest ignores programmatically set field values.** Setting them leaves
  the text visible but the Save button disabled, because its React state never
  updates. Everything has to be typed as real keystrokes. Budget for that.
- **The Pinterest username saved as `bijouduglacir`** at one point, missing an
  "e", and had to be retyped. Worth re-reading any Pinterest field after saving.
- **The Pinterest display name in this file is impossible.** Pinterest splits
  Name into first/last at the first space and caps each at 30 characters, so
  `Bijou du Glacier | Luxury Apartment, Saas-Fee` is rejected: the "last name"
  part is 39. The live name is `Bijou du Glacier, Saas-Fee`. The keywords live
  in the About field instead, which Pinterest also indexes.
- **Facebook rejects em dashes in Page names.** The Page is
  `Bijou du Glacier - Saas-Fee`, with a hyphen.

### Outstanding

1. **Instagram: name, category, contact email and Business account are not set.**
   Instagram's *web* profile editor only exposes Bio and Website, and the
   Website field is disabled with the notice "Editing your links is only
   available on mobile". **The display name still reads "Matthew Thomas"** and
   there is no link in the bio, which matters because the posted caption says
   "Link in bio". All of this needs the phone app, about five minutes.
2. ~~Four Pinterest boards still to create~~ — **done 22 November 2026.** All
   five now exist and are public:

   | Board | Pins |
   |---|---|
   | Saas-Fee, Switzerland | 1 (pin 1) |
   | Modern Alpine Interiors | 0 |
   | Luxury Ski Apartments | 0 |
   | Skiing the Allalin Glacier | 0 |
   | Group Ski Trips | 0 |

   **Board descriptions are not set.** Pinterest's create-board dialog offers
   only a name and a private toggle, so the descriptions listed earlier in this
   file have to be added by editing each board afterwards. Worth doing, since
   Pinterest indexes them, but it is four separate edits.

   Pins 2-8 in `pinterest-pins.md` can now go up; each names its board.
3. **Facebook Page username** still not offered by Facebook on a Page this new.
4. ~~Website footer links and `sameAs`~~ — **done 22 November 2026.** All four
   accounts are linked from the footer of all 16 content pages in their own
   language (Follow / Folgen / Suivre / Seguici), and all four are listed in
   `sameAs` alongside the three booking channels. The root `index.html` is a
   noindex redirect stub with no footer, so it is correctly excluded.
   The Facebook link is the numeric `profile.php?id=` form because Facebook
   withholds a Page username until 25 likes; it will keep redirecting once the
   username exists, so update `SOCIAL` in `build_site.py` at leisure.
   **Not yet deployed** — run the playbook to put it live.
5. **Nothing from week 1 of `posting-calendar.md` beyond these first posts.**
