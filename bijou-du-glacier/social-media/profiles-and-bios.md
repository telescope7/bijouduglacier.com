# Profiles and bios — set these up first

Everything below is copy-paste. Nothing needs rewording.

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
4 king beds · 3 baths · 4 min to the slopes.
Book direct ↓
```

**Link:**

```
https://bijouduglacier.com
```

**Category:** Vacation Home Rental
**Contact:** add the email once you've decided on it — see `PROMPT-next-build.md` item 3.

> Switch to a **Professional account → Business**. It's free, it unlocks Insights, and it lets
> you add the contact button. Do it before you post.

---

## Facebook Page

**Page name:**

```
Bijou du Glacier — Saas-Fee
```

**Username:** `@bijouduglacier` (see `handles.md` for fallbacks)

**Category:** Vacation Home Rental

**Short description** (255 characters):

```
A newly renovated four-bedroom apartment for eight in car-free Saas-Fee, Valais. Four king-size bedrooms, three bathrooms, a walnut table that seats everyone, and a covered balcony facing thirteen four-thousand-metre peaks. Four minutes from the slopes.
```

**Website:**

```
https://bijouduglacier.com
```

**About / long description:**

```
Bijou du Glacier occupies the east end of the second floor of Residence du Glacier, in the heart of Saas-Fee.

Four bedrooms, each with its own king-size bed, its own window and its own morning light. Three bathrooms in pale stone and dark slate — two with deep baths, the third with a walk-in shower. One long open room holding the kitchen, the sitting area and a live-edge walnut table that seats all eight at once.

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
Four-bedroom apartment for eight in car-free Saas-Fee, Valais. 4 king beds, 3 baths, 4 minutes to the slopes. Book direct — same nightly rate, no platform fee.
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

---

## One thing not to do

**Don't put your website URL in your Airbnb or Booking.com listing** — not in the
description, not in photo captions, not in house rules, not in guest messages. It breaches
both platforms' terms and risks delisting, which would cost far more than the referral is
worth.

Linking *from* your own social profiles *to* your site is entirely fine. It's the direction
into the OTAs that's restricted.
