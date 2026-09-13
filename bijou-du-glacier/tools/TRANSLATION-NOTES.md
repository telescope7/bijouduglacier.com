# Translation and keyword notes

Give this page to whoever proofreads the French, German or Italian. It lists the
deliberate choices and the handful of lines I'm not fully certain about.

---

## The one that matters most

**Saas-Fee is in the German-speaking Upper Valais**, despite the French property name.
German is very likely your highest-volume search language for this property, not English —
which is the opposite of the assumption the original site was built on. If you only ever
get one of these three proofread by a native speaker, make it the German.

Swiss orthography is used throughout: **`ss`, never `ß`**. Verified: there is not a single
`ß` in the built site.

---

## Keywords, per language

These are written against what people actually type, not translated from the English.

| Language | Targeted | Deliberately **not** used |
|---|---|---|
| EN | *Saas-Fee apartment*, *4-bedroom apartment Saas-Fee*, *sleeps 8*, *car-free*, *self-catering* | — |
| DE | ***Ferienwohnung** Saas-Fee*, *Ferienwohnung Saas-Fee 8 Personen*, *4 Schlafzimmer*, *autofrei*, *Skiferien* | *Apartment* (low volume in DE), *Selbstverpflegung* (not a search term — replaced with *eigene Küche*) |
| FR | *appartement Saas-Fee*, ***appartement de vacances***, *location*, *8 personnes*, *village sans voitures* | a literal *auto-restauration*; nobody searches it |
| IT | *appartamento Saas-Fee*, ***casa vacanze***, *8 persone*, *villaggio senza auto* | *self-catering* |

`Ferienwohnung` vs `Apartment` is the single biggest gain here. A literal translation of the
English page would have missed it.

### Slugs are translated on purpose

`/de/ferienwohnung/`, `/fr/appartement/`, `/it/appartamento/`, `/fr/reserver/`,
`/de/buchen/`, `/it/prenotare/`. Keyword-bearing URLs are worth having, and it signals to
the reader before they click that the page really is in their language.

---

## Swiss regional usage, chosen on purpose

| Term | Instead of | Why |
|---|---|---|
| DE *Postauto* | *Bus* / *Reisebus* | It is the actual name of the service |
| DE *parkieren* | *parken* | Swiss standard German |
| DE *Kurtaxe* | *Übernachtungssteuer* | What the Gemeinde actually calls it |
| DE *Tablar* | *Regalbrett* | Swiss |
| FR *car postal* | *bus postal* | Swiss Romand standard |
| FR *relâches de février* | *vacances de février* | Swiss Romand term for the February school break |
| FR *taxe de séjour* | — | Correct and standard in Valais |
| IT *autopostale* | *pullman postale* | Swiss Italian standard |
| IT *tassa di soggiorno* | — | Correct |

---

## Lines I'm not fully certain about — please check these

1. **FR — `parquer`.** I used *parquer* once in the FAQ ("Où peut-on parquer ?") because it
   is authentic Romand. If your French audience skews French-from-France rather than Valaisan,
   change it to *se garer*. Both are correct; only one sounds local.
2. **FR — `relâches`.** Standard in Suisse romande for the February school break. A French
   reader from Paris may find it unfamiliar. *Vacances de février* is the safe alternative.
3. **DE — `Kingsize-Bett`.** Used untranslated because it is what Swiss listings say. I do
   **not** state a size in centimetres anywhere, because I do not know it. If the beds are
   180 × 200, saying so in the German would be worth more than the English word — German
   guests check bed dimensions. Ask your manager and add it.
4. **DE — `Vierzimmerwohnung`** appears once in the footer fine-print and once in the living
   section. In Swiss usage room-counting includes the living room, so a flat with four
   *bedrooms* is more like a 5- or 5.5-Zimmer-Wohnung. Everywhere it matters I wrote
   *vier Schlafzimmer* (unambiguous). If a Swiss reader proofreads, ask them whether the
   two loose uses of *Vierzimmerwohnung* should become *5.5-Zimmer-Wohnung*.
5. **IT — `doccia walk-in`.** Common in Swiss/Italian property listings, but
   *doccia a filo pavimento* is the more properly Italian term. Either works.
6. **IT — register.** I used the plural-you (*voi*) rather than formal *Lei*, which reads
   warmer and suits a holiday rental addressed to a group of eight. If you'd rather it were
   formal, it's a consistent find-and-replace.
7. **All languages — "the Pearl of the Alps".** Rendered as *Perle der Alpen* /
   *Perle des Alpes* / *Perla delle Alpi*. These are the forms Saas-Fee itself uses.

---

## Claims I deliberately did not make

- **Not ski-in / ski-out.** The apartment is in the village, minutes from the lifts. Instead
  of dodging the term, each language has an FAQ that answers *"Is it ski-in, ski-out?"*
  honestly. That captures the search query and reduces the risk of a disappointed guest
  writing about it in a review — which is the expensive version of this mistake.
- **No star rating or review score anywhere**, and no `aggregateRating` in the structured
  data. There are no real ratings in the source material. Invented ones are a Google
  structured-data violation as well as a lie. Add them, with real numbers, once you have
  them: `lodging_node()` in `build_site.py` has a comment marking the spot.
- **No wood stove.** There isn't one in any photograph.
- **Washing machine: now confirmed** by the official listing, and added to the amenities
  in all four languages.
- **Verified from the listing on 8 August 2026** and now stated on the site: 8 guests,
  4 bedrooms, 4 beds, **3 bathrooms**, Hypnos beds and mattresses, super-fast wi-fi,
  a ski locker in the basement, a supermarket 20 m away, a **four-minute walk to the
  slopes**, check-in from 3pm with flexible check-out, no pets, and the payment and
  cancellation terms on the booking page.
- **Minimum stays: removed entirely**, in all four languages. They were never confirmed by
  the manager, only recommended in the marketing plan, and stating an unconfirmed policy as
  fact is exactly the kind of thing that produces an argument at the booking stage. If
  SaasFeeHolidays confirm real minimums, they can go back in.
- **Balcony seating count: no longer claimed.** The apartment page said the
  balcony had "comfortable seating for the whole party". The two photographs
  supplied on 9 August show roughly four or five places: one armchair, a
  two-seat sofa, a second armchair and a pair of nested low tables. The
  apartment sleeps eight. All four languages now describe deep woven lounge
  chairs and low tables without a count, which is true whatever else is out
  there. If there is more seating beyond the frame, the count can go back in.
- **"Covered" is now confirmed**, not merely asserted. The dark timber soffit is
  clearly visible in the wider of the two photographs, which is why the crop was
  set to keep it in frame rather than trimming to the furniture.
- **The photographs are summer.** Both show green larch and no snow, while the
  balcony copy talks about sitting out in falling snow. That is not a conflict,
  but the site now has no winter photograph of the balcony furniture, and the
  older balcony-view shot is the only snow-covered one.
- **Summer skiing: reviewed and deliberately left as written**, on the owner's
  instruction. For the record, the underlying facts do not fully support it. The
  Saas-Fee summer ski area opens from **mid-July**, runs mornings only, offers
  about 20 km of glacier piste against the full winter area, and has no beginner
  runs. The copy says the glacier "skis in July as readily as in January" in
  three places per language (the resort page lede and h2, the home resort
  section, and the summer FAQ). If a guest ever books late June or early July to
  ski, this is the paragraph that caused it.
- **Payment terms and the returning-guest promise: removed.** The book page
  stated a 50 percent deposit, the balance at 70 days, a 15 percent
  pre-authorisation and non-refundable prepayments as fact, and separately
  promised returning guests first refusal on their dates. Neither was confirmed
  by SaasFeeHolidays. The payment paragraph is now a neutral line saying the
  schedule is set out at confirmation; the returning-guest block is gone. Put
  either back once the manager confirms the real terms.
- **Coordinates are now the building**, 46.107439 / 7.926044, supplied by the
  owner. They were previously the centre of the village.
- **floorSize in the structured data is 154.31 m2, gross**, on the owner's
  instruction. That is the Bruttogeschossflaeche printed on the architect's
  plan: it includes walls and the 25.23 m2 balcony. The net internal area, the
  sum of the rooms without the balcony, is 111.20 m2. Both numbers are recorded
  here so the choice is not accidentally reversed later. No floor area appears
  in the visible copy at all.
- **Street address confirmed and corrected: Blomattenstrasse 2, 3906 Saas-Fee.**
  The site previously used "Residence du Glacier" as the street address, which
  is the building name, not a street. Blomattenstrasse 2 is now the
  streetAddress in the structured data, and the building name is kept in front
  of it in the facts table and the footer. Independently corroborated: the
  Migros is registered at Blomattenstrasse 2 as well, which is the twenty
  metres the copy claims. Note the spelling is Blomattenstrasse, one "a" in
  strasse.
- **Untere Dorfstrasse confirmed** as SaasFeeHolidays' address in the village.
- **"An entire floor" was wrong, and is corrected.** All four languages said the
  apartment occupied a whole floor of Residence du Glacier. The developer's own
  second-floor plan shows four apartments on that level, of which B4 is the east
  end one. The copy now says it occupies the east end of the second floor. This
  was caught by the floor plan, not by the listing, which never contradicted it.
- **Floor plan added.** Apartment B4, lifted from the developer's second-floor
  drawing. The neighbouring unit is painted out and the sale pricing
  (CHF 1,880,000 / CHF 2,030,000) is cropped away, since the site quotes no
  prices of any kind. The room labels in the drawing are German and cannot be
  localised without redrawing it, so the FR, IT and EN captions carry a short
  glossary instead, and the alt text describes the layout in full in each
  language. Room areas quoted in the new Layout section come from the same
  source: Wohnzimmer 39.88, Zimmer 10.83 to 14.16, Balkon 25.23 square metres.
- **A lift, a dishwasher and a microwave are now claimed**, on your instruction. All three
  were previously listed here as unverified and left out. They now appear in the amenity
  list, in the kitchen FAQ, in the apartment-page kitchen paragraph and in the caption under
  the dining photograph, in all four languages. If any of them is wrong, those are the four
  places to correct.
- **The building, not just the floor, is described as fully renovated**, on your
  instruction. The earlier copy said "an entire newly renovated floor"; it now says the
  building was renovated from the ground up.
- **No table on the balcony.** The balcony copy previously claimed a table long enough to
  eat at, on both the home and apartment pages. That claim is gone in all four languages.
  Balcony seating is still claimed, and is in the photographs.

---

## House rule: no em dashes

There is not a single em dash in the visible copy of any of the four languages, and
`audit.py` fails the build if one appears. The rule exists because an em dash in body copy
is the clearest signal that a page was generated rather than written, and this site is
asking a guest to spend four figures on the basis that real people look after the place.

Where a dash was doing real work the sentence was rebuilt, not merely repunctuated. German
keeps its Gedankenstrich habit in ordinary writing, so the German file needed the most
restructuring; French and Italian mostly took a colon or a full stop.
- **Prices.** None quoted anywhere. The rate strategy in `strategy/marketing-plan.md` §3 is
  deliberately not published, and the site says only that the direct nightly rate matches
  the platforms — which is both true and parity-compliant.
