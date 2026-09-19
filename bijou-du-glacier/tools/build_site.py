#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bijou du Glacier — page generator.

Writes 16 localized pages (4 pages x 4 languages) plus the root redirect,
sitemap.xml, robots.txt and _redirects into ../website/.

WHAT THIS IS NOT: a build system. The HTML it emits is complete, self-contained
static markup with no dependencies. You can hand-edit any page afterwards and it
will keep working, and you can edit styles.css directly without running anything.
The script exists so that a change to the copy or the structure does not have to
be repeated sixteen times by hand.

    python3 build_site.py
"""

import html
import json
import os
import posixpath
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from content_en import EN
from content_fr import FR
from content_de import DE
from content_it import IT

HERE = os.path.dirname(os.path.abspath(__file__))
WEB = os.path.abspath(os.path.join(HERE, "..", "website"))
IMG = os.path.join(WEB, "img")

# ---------------------------------------------------------------------------
# Site-wide facts.
#
# lat/lon are the pin on Residence du Glacier itself, supplied by the owner
# from Google Maps on 9 August 2026. Six decimal places is roughly 0.1 m, which
# is well past the precision anything here needs.
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# Where the booking buttons ACTUALLY go.
#
# Nothing on the site links to these directly any more. Every booking button
# points at a path on our own domain, and nginx answers with a 302 to the URL
# below. That is the only way to find out how many people click, without
# putting a single line of tracking script in front of a guest.
#
# These constants are the one place the real URLs live. deploy/templates/
# site-body.conf.j2 has to carry the same three, so if you change one here,
# change it there too: build_site.py cannot reach into the nginx template, and
# audit.py checks the two agree.
#
# 302, never 301: the platforms reissue listing URLs, and a 301 would be
# cached in a guest's browser long after the target moved.
# ---------------------------------------------------------------------------

DESTINATIONS = {
    # Verified against the listing on 2026-08-08: 8 guests, 4 bedrooms,
    # 4 beds, 3 bathrooms.
    "direct":  "https://saasfeeholidays.com/en/saasfeeholidays-du-glacier---b4",
    "airbnb":  "https://www.airbnb.com/rooms/1674533087008414341",
    "booking": "https://www.booking.com/hotel/ch/saasfeeholidays-du-glacier-b4.html",
}

# The first-party path each destination is reached through.
CHANNEL_PATHS = {
    "direct":  "/book-direct",
    "airbnb":  "/go/airbnb",
    "booking": "/go/booking",
}

SITE = {
    "origin": "https://bijouduglacier.com",
    "name": "Bijou du Glacier",
    "street": "Blomattenstrasse 2",
    "building": "Residence du Glacier",
    "locality": "Saas-Fee",
    "region": "Valais",
    "postal": "3906",
    "country": "CH",
    "lat": 46.107439,
    "lon": 7.926044,
    # What the BUTTONS link to. Absolute, on our own origin, so the link is
    # identical whether the page is opened from the server or from disk.
    # nginx 302s each of these to the matching DESTINATIONS entry.
    "direct": "https://bijouduglacier.com/book-direct",
    "airbnb": "https://bijouduglacier.com/go/airbnb",
    "booking": "https://bijouduglacier.com/go/booking",
    "handle": "Managed locally by SaasFeeHolidays.com",
    "share_img": "/img/share-1200.jpg",
    "share_w": 1200,
    "share_h": 630,
}

LANGS = {"en": EN, "fr": FR, "de": DE, "it": IT}
LANG_ORDER = ["en", "fr", "de", "it"]
X_DEFAULT = "en"

PAGE_ORDER = ["home", "apartment", "resort", "book"]

SLUGS = {
    "home":      {"en": "",          "fr": "",             "de": "",               "it": ""},
    "apartment": {"en": "apartment", "fr": "appartement",  "de": "ferienwohnung",  "it": "appartamento"},
    "resort":    {"en": "saas-fee",  "fr": "saas-fee",     "de": "saas-fee",       "it": "saas-fee"},
    "book":      {"en": "book",      "fr": "reserver",     "de": "buchen",         "it": "prenotare"},
}

SITEMAP_PRIORITY = {"home": "1.0", "apartment": "0.9", "resort": "0.8", "book": "0.9"}


def url(page, lang, absolute=False):
    """The CANONICAL, clean URL. Used for canonical/hreflang/OG/JSON-LD/sitemap."""
    slug = SLUGS[page][lang]
    path = "/%s/" % lang if not slug else "/%s/%s/" % (lang, slug)
    return (SITE["origin"] + path) if absolute else path


# ---------------------------------------------------------------------------
# Relative paths.
#
# Every href, src and stylesheet link is DOCUMENT-RELATIVE, so the built tree
# can be moved or served from anywhere.
#
# Page links point at the DIRECTORY form (`../apartment/`), matching the
# canonical exactly. They used to spell out `index.html` so the site could be
# browsed by double-clicking website/index.html with no server; that was a nice
# convenience and it cost real crawl budget. Every page carried fifteen links
# to URLs the canonical tag tells Google not to index, and on a new domain
# where Google is rationing crawl, that is budget spent on 301s instead of
# content. nginx redirects the index.html form, so the old links also meant an
# extra round trip on every internal click.
#
# The one exception is website/index.html, the root language picker. It keeps
# explicit filenames: it is noindex, nginx 302s `/` to `/en/` so it is almost
# never served, and it is the entry point for opening the build off the disk.
#
# Consequence: to preview locally, serve the folder rather than double-clicking
# it. `python3 -m http.server 8080` in website/ is what INSTRUCTIONS.md says,
# and it matches how the site is actually served.
# ---------------------------------------------------------------------------

_CUR = "."          # directory of the page being written, relative to website/


def set_depth(page=None, lang=None):
    """'.' for website/index.html, 'en' for en/index.html, 'en/book' for that page."""
    global _CUR
    _CUR = "." if page is None else url(page, lang).strip("/") or "."


def _rel(target):
    """Document-relative path from the current page's directory to `target`."""
    return posixpath.relpath(target, _CUR)


def asset(path):
    """Relative path to something at the site root, e.g. 'styles.css'.

    A trailing slash is preserved, so asset("img/") can be used as a prefix.
    """
    p = path.lstrip("/")
    out = _rel(p)
    return out + "/" if p.endswith("/") and not out.endswith("/") else out


def font_preloads():
    """The two above-the-fold faces, read from the manifest fetch_fonts.py writes.

    Not hardcoded, because the filenames depend on whether Google serves a
    variable font (one file per subset) or static instances (one per weight),
    and that is not ours to decide. If the manifest is missing, the build still
    succeeds without preloads and audit.py reports it.
    """
    mf = os.path.join(WEB, "fonts", "manifest.json")
    if not os.path.isfile(mf):
        return None, None
    with open(mf, encoding="utf-8") as fh:
        m = json.load(fh)
    return m.get("serif"), m.get("sans")


def _font_preload_tags():
    serif, sans = font_preloads()
    tags = []
    for f in (serif, sans):
        if f:
            tags.append('<link rel="preload" href="%s" as="font" '
                        'type="font/woff2" crossorigin>' % asset("fonts/" + f))
    return "\n".join(tags)


def href(page, lang):
    """Relative link to another page, in the canonical directory form.

    `../apartment/`, not `../apartment/index.html`, so every internal link
    matches the canonical tag and nginx never has to redirect one.

    website/index.html is the exception — see the note above. It is identified
    by _CUR being the site root, which only build_root() sets.
    """
    target = url(page, lang).strip("/")
    if _CUR == ".":                       # the root language picker
        return _rel(target + "/index.html")
    rel_path = _rel(target)
    return "./" if rel_path == "." else rel_path.rstrip("/") + "/"


def esc(s):
    return html.escape(s, quote=True)


# ---------------------------------------------------------------------------
# Images
# ---------------------------------------------------------------------------

_variants = {}


def scan_images():
    """Map base name -> sorted [(width, height)] from what is actually on disk."""
    pat = re.compile(r"^(.*)-(\d+)\.jpg$")
    for f in sorted(os.listdir(IMG)):
        m = pat.match(f)
        if not m:
            continue
        name, w = m.group(1), int(m.group(2))
        _variants.setdefault(name, []).append(w)
    for name in _variants:
        _variants[name] = sorted(set(_variants[name]))
    if not _variants:
        raise SystemExit("No images found in %s — run build_images.py first." % IMG)


_dims_cache = {}


def dims(name, w):
    """Real pixel dimensions of a variant, read once from the file itself."""
    key = (name, w)
    if key not in _dims_cache:
        from PIL import Image
        with Image.open(os.path.join(IMG, "%s-%d.jpg" % (name, w))) as im:
            _dims_cache[key] = im.size
    return _dims_cache[key]


def picture(name, alt, sizes, loading="lazy", priority=False, cls=""):
    ws = _variants[name]
    big = ws[-1]
    w, h = dims(name, big)
    base = asset("img/")
    avif = ", ".join("%s%s-%d.avif %dw" % (base, name, x, x) for x in ws)
    jpg = ", ".join("%s%s-%d.jpg %dw" % (base, name, x, x) for x in ws)
    attrs = [
        'src="%s%s-%d.jpg"' % (base, name, big),
        'srcset="%s"' % jpg,
        'sizes="%s"' % sizes,
        'width="%d"' % w,
        'height="%d"' % h,
        'alt="%s"' % esc(alt),
        'loading="%s"' % loading,
        'decoding="async"',
    ]
    if priority:
        attrs.append('fetchpriority="high"')
    if cls:
        attrs.append('class="%s"' % cls)
    return (
        '<picture>'
        '<source type="image/avif" srcset="%s" sizes="%s">'
        '<img %s>'
        '</picture>' % (avif, sizes, " ".join(attrs))
    )


# ---------------------------------------------------------------------------
# Components
# ---------------------------------------------------------------------------

COLLAGE = [
    # css class, image, loading, priority, sizes
    # A = the hero video (4 of 12 cols). B = the living room, the shot that
    # shows the green sofa AND the windows, which is what sells the room.
    # C and D are near-square, E is a portrait detail. Each still is cut to the
    # exact ratio of its cell.
    ("cell-a", "piste-dawn",      "eager", True,
     "(min-width: 640px) min(410px, 33vw), 96vw"),
    ("cell-b", "living-room",     "eager", False,
     "(min-width: 640px) min(810px, 64vw), 96vw"),
    ("cell-c", "kitchen-shelves", "lazy",  False,
     "(min-width: 640px) min(300px, 24vw), 48vw"),
    ("cell-d", "master-bedroom",  "lazy",  False,
     "(min-width: 640px) min(300px, 24vw), 48vw"),
    # Cell E was "robe-door", a wardrobe detail. The balcony chair in afternoon
    # sun does more work in the hero for the same 5/9 slot. robe-door is still
    # built and still used in the apartment gallery, so this is a one-line
    # revert if you prefer it back.
    ("cell-e", "patio-hero",      "lazy",  False,
     "(min-width: 1024px) min(200px, 16vw), 0px"),
]


# ---------------------------------------------------------------------------
# The hero video occupies cell A. To go back to the still photograph, set
# HERO_VIDEO = False and re-run — the <picture> is emitted commented-out in the
# markup either way, so it can also be restored by hand in a text editor.
#
# HERO_CLIP: "hero" is the whole 32-second master. "hero-clean" is the same
# footage from 2.6s to 28.6s, with your property manager's VOLLA wordmark and
# their closing logo animation cut off. Swap the string, re-run, done.
# ---------------------------------------------------------------------------

HERO_VIDEO = True
HERO_CLIP = "hero"          # or "hero-clean"


def build_video(L):
    v = asset("video/")
    i = asset("img/")
    alt = L["alt"]["hero-video"]
    return """<video class="hero-video" autoplay muted loop playsinline
         preload="metadata" poster="%(i)shero-poster-720.jpg"
         width="720" height="1280" aria-label="%(alt)s">
    <source src="%(v)s%(clip)s-480.mp4" type="video/mp4" media="(max-width: 640px)">
    <source src="%(v)s%(clip)s-720.mp4" type="video/mp4">
    <img src="%(i)shero-poster-720.jpg" width="720" height="1280" alt="%(alt)s">
  </video>
  <img class="motion-still" src="%(i)shero-poster-720.jpg"
       srcset="%(i)shero-poster-480.jpg 480w, %(i)shero-poster-720.jpg 720w"
       sizes="(min-width: 1024px) 33vw, (min-width: 640px) 33vw, 96vw"
       width="720" height="1280" alt="%(alt)s" decoding="async">""" % {
        "v": v, "i": i, "clip": HERO_CLIP, "alt": esc(alt)}


def build_collage(L):
    out = ['<div class="collage">']
    for cls, name, loading, prio, sizes in COLLAGE:
        if cls == "cell-a" and HERO_VIDEO:
            # The still is kept, commented out, so the change is one deletion
            # away from being reverted without re-running anything.
            still = picture(name, L["alt"][name], sizes, loading, prio)
            out.append(
                '<figure class="%s cell-video">\n'
                '  <!-- TO REVERT TO THE STILL PHOTOGRAPH: delete the <video> and\n'
                '       <img class="motion-still"> below, then un-comment this.\n'
                '       (Or set HERO_VIDEO = False in tools/build_site.py.)\n'
                '  %s\n'
                '  -->\n'
                '  %s\n'
                '</figure>' % (cls, still.replace("--", "&#45;&#45;"), build_video(L)))
        else:
            out.append('<figure class="%s">%s</figure>'
                       % (cls, picture(name, L["alt"][name], sizes, loading, prio)))
    out.append("</div>")
    return "\n".join(out)


def build_header(L, lang, page):
    home = href("home", lang)
    nav = []
    for p in PAGE_ORDER:
        cur = ' aria-current="page"' if p == page else ""
        nav.append('<a href="%s"%s>%s</a>' % (href(p, lang), cur, esc(L["nav"][p])))

    langs = []
    for other in LANG_ORDER:
        o = LANGS[other]
        cur = ' aria-current="true"' if other == lang else ""
        langs.append(
            '<li><a href="%s" hreflang="%s" lang="%s"%s>%s</a></li>'
            % (href(page, other), other, other, cur, esc(o["dir_label"]))
        )

    # The blason carries alt="" on purpose: the wordmark beside it already says
    # "Bijou du Glacier", so giving the image alt text would make a screen reader
    # announce the brand twice for one link.
    b = asset("img/")
    mark = ('<img class="brand-mark" src="%sblason-56.png" '
            'srcset="%sblason-56.png 1x, %sblason-112.png 2x, %sblason-168.png 3x" '
            'width="49" height="56" alt="" decoding="async">' % (b, b, b, b))

    return """<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="%s">%s<span class="brand-text">%s<span>%s</span></span></a>
    <nav class="site-nav" aria-label="%s">%s</nav>
    <ul class="langs" aria-label="%s">%s</ul>
    <a class="header-cta" href="%s" rel="noopener">%s</a>
  </div>
</header>""" % (
        home, mark, esc(SITE["name"]), esc(L["ui"]["brand_sub"]),
        esc(L["ui"]["nav_label"]), "".join(nav),
        esc(L["ui"]["lang_label"]), "".join(langs),
        SITE["direct"], esc(L["ui"]["book_cta_short"]),
    )


def build_jump(L, jump):
    """Section links. They live INSIDE the dark masthead on the interior pages
    and are omitted from the homepage, where the main navigation already covers
    the same ground — the separate white strip under the header was doing no
    work and breaking the run of the brand colour."""
    items = "".join('<li><a href="#%s">%s</a></li>' % (i, esc(t)) for i, t in jump)
    return '<nav class="jump" aria-label="%s"><ul>%s</ul></nav>' % (
        esc(L["ui"]["jump_label"]), items)


def build_crumbs(L, lang, page):
    if page == "home":
        return ""
    items = [
        '<li><a href="%s">%s</a></li>' % (href("home", lang), esc(L["ui"]["home_label"])),
        '<li><span aria-current="page">%s</span></li>' % esc(L["nav"][page]),
    ]
    return ('<nav class="crumbs wrap" aria-label="%s"><ol>%s</ol></nav>'
            % (esc(L["ui"]["crumb_label"]), "".join(items)))


def build_faq(L):
    out = ['<div class="faq">']
    for q, a in L["faq"]:
        out.append("<details><summary>%s</summary><div class=\"answer\"><p>%s</p></div></details>"
                   % (esc(q), a))
    out.append("</div>")
    return "\n".join(out)


def build_amenities(L):
    return ('<ul class="amenities">%s</ul>'
            % "".join("<li>%s</li>" % esc(a) for a in L["amenities"]))


def build_facts(L):
    t = L["facts_table"]
    rows = "".join("<tr><th scope=\"row\">%s</th><td>%s</td></tr>" % (esc(k), esc(v))
                   for k, v in t["rows"])
    return ('<table class="facts"><caption>%s</caption><tbody>%s</tbody></table>'
            % (esc(t["caption"]), rows))


def build_bookblock(L):
    return """<div class="reserve reveal">
  <h3>%s</h3>
  <p>%s</p>
  <p class="cta-row"><a class="btn btn-primary" href="%s" rel="noopener">%s</a></p>
  <p class="cta-note">%s</p>
</div>""" % (
        esc(L["ui"]["book_block_title"]),
        esc(L["ui"]["note"]),
        SITE["direct"],
        esc(L["ui"]["book_cta"]),
        esc(SITE["handle"]),
    )


def build_reservebox(L):
    """The homepage panel. The direct call to action and the two platform
    listings now live in the same box: a visitor deciding between them should
    not have to scan three separate blocks to do it."""
    plat = "".join(
        '<li><a class="btn btn-primary" href="%s" rel="noopener">%s</a></li>'
        % (u, n) for n, u in [("Airbnb", SITE["airbnb"]),
                              ("Booking.com", SITE["booking"])])
    return """<div class="reserve reveal">
  <h3>%s</h3>
  <p>%s</p>
  <p class="cta-row"><a class="btn btn-primary" href="%s" rel="noopener">%s</a></p>
  <p class="cta-note">%s</p>
  <div class="reserve-alt">
    <p class="reserve-alt-label">%s</p>
    <ul class="platforms">%s</ul>
  </div>
</div>""" % (
        esc(L["ui"]["book_block_title"]), esc(L["ui"]["note"]),
        SITE["direct"], esc(L["ui"]["book_cta"]), esc(SITE["handle"]),
        esc(L["ui"]["or_label"]), plat)


def build_platforms(L):
    links = [("Airbnb", SITE["airbnb"]),
             ("Booking.com", SITE["booking"])]
    return ('<ul class="platforms">%s</ul>'
            % "".join('<li><a class="btn btn-primary" href="%s" rel="noopener">%s</a></li>'
                      % (u, n) for n, u in links))


def build_next(L, lang, page):
    others = [p for p in PAGE_ORDER if p != page]
    cards = []
    for p in others:
        title, blurb = L["next"][p]
        cards.append('<li><a href="%s"><strong>%s</strong><span>%s</span></a></li>'
                     % (href(p, lang), esc(title), esc(blurb)))
    return """<section class="section" aria-labelledby="next-h">
  <div class="wrap">
    <h2 id="next-h" class="eyebrow">%s</h2>
    <ul class="next-links">%s</ul>
  </div>
</section>""" % (esc(L["ui"]["next_label"]), "".join(cards))


def build_footer(L, lang):
    f = L["footer"]
    explore = "".join('<li><a href="%s">%s</a></li>' % (href(p, lang), esc(L["nav"][p]))
                      for p in PAGE_ORDER)
    booking = "".join(
        '<li><a href="%s" rel="noopener">%s</a></li>' % (u, n)
        for n, u in [(L["ui"]["book_cta_short"], SITE["direct"]),
                     ("Airbnb", SITE["airbnb"]),
                     ("Booking.com", SITE["booking"])])
    b = asset("img/")
    mark = ('<img class="footer-mark" src="%sblason-112.png" '
            'srcset="%sblason-112.png 1x, %sblason-168.png 2x" '
            'width="98" height="112" alt="" decoding="async" loading="lazy">'
            % (b, b, b))

    return """<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div class="footer-identity">
        %s
        <div>
          <p class="footer-brand">%s</p>
          <p>%s</p>
          <p><a href="%s">bijouduglacier.com</a></p>
        </div>
      </div>
      <div>
        <h2>%s</h2>
        <ul>%s</ul>
      </div>
      <div>
        <h2>%s</h2>
        <ul>%s</ul>
      </div>
    </div>
  </div>
</footer>""" % (
        mark, esc(SITE["name"]), esc(f["address"]), SITE["origin"],
        esc(f["explore"]), explore,
        esc(f["book"]), booking,
    )


# ---------------------------------------------------------------------------
# Structured data
# ---------------------------------------------------------------------------

# Google's VacationRental amenityFeature vocabulary is a CONTROLLED list, and
# the values must be these exact English tokens even on the fr/de/it pages.
# Free text here is simply ignored. Every entry below is claimed in the site's
# own copy (see L["amenities"]); nothing is assumed.
#   wifi        <- "High-speed internet throughout"
#   tv          <- "Television in the living room"
#   washerDryer <- "Washing machine and tumble dryer"
#   heating     <- "Oak floors, underfloor-warm and quiet"
#   elevator    <- "Lift access to the apartment"
#   childFriendly <- "Games for the children", and the FAQ answer
# Deliberately absent: ac, pool, hotTub, fireplace, parkingType, airportShuttle,
# wheelchairAccessible, selfCheckinCheckout — none of them are claimed anywhere,
# and an amenity a guest arrives to find missing is worse than no markup.
GOOGLE_AMENITIES = [
    ("balcony", True), ("childFriendly", True), ("elevator", True),
    ("heating", True), ("kitchen", True), ("microwave", True),
    ("ovenStove", True), ("tv", True), ("washerDryer", True),
    ("wifi", True),
]

# Stable, content-independent, and identical across all four languages, exactly
# as Google requires: it must not change when the listing name or the room count
# does. "b4" is the apartment's designation in Residence du Glacier.
PROPERTY_ID = "bijouduglacier-b4"


def lodging_node(L, lang):
    """VacationRental is a subtype of LodgingBusiness, so this satisfies both.

    Shaped to Google's VacationRental spec: the unit's physical details live in
    containsPlace (an Accommodation), not on the VacationRental itself, and
    occupancy.value is required there. See
    https://developers.google.com/search/docs/appearance/structured-data/vacation-rental

    aggregateRating and review are deliberately absent: the listing is new and
    has no ratings yet. Inventing them is both a Google structured-data
    violation and a lie. Add them here once real figures exist.

    Note that the rich result itself is gated behind Google's vacation-rental
    Early Adopters Program, which needs Hotel Center access. This markup is
    correct and useful regardless — it is what general search and the AI answer
    engines read — but do not expect a carousel from it.
    """
    # Google requires at least 8 images, including at least one each of a
    # bedroom, a bathroom and a common area. All three are covered below.
    images = ["%s/img/%s-%d.jpg" % (SITE["origin"], n, _variants[n][-1])
              for n in ("piste-dawn", "living-room", "living-wide",
                        "dining-table", "kitchen", "master-bedroom",
                        "bedroom-2", "bedroom-3", "bathroom",
                        "balcony-view", "village")]
    return {
        "@type": "VacationRental",
        "@id": url("home", lang, True) + "#lodging",
        "name": SITE["name"],
        "url": url("home", lang, True),
        "description": L["pages"]["home"]["desc"],
        "inLanguage": lang,
        "image": images,
        "address": {
            "@type": "PostalAddress",
            "streetAddress": SITE["street"],
            "addressLocality": SITE["locality"],
            "addressRegion": SITE["region"],
            "postalCode": SITE["postal"],
            "addressCountry": SITE["country"],
        },
        "geo": {
            "@type": "GeoCoordinates",
            "latitude": SITE["lat"],
            "longitude": SITE["lon"],
        },
        "containedInPlace": {
            "@type": "Place",
            "name": "Saas-Fee",
            "address": {
                "@type": "PostalAddress",
                "addressLocality": "Saas-Fee",
                "addressRegion": "Valais",
                "postalCode": "3906",
                "addressCountry": "CH",
            },
            "geo": {"@type": "GeoCoordinates", "latitude": 46.1085, "longitude": 7.9291},
        },
        # REQUIRED by Google, and the thing Search Console was complaining
        # about. The unit's physical detail belongs here, on an Accommodation,
        # not on the VacationRental above. occupancy.value is required and must
        # be a plain integer — maxValue is not accepted in its place.
        "containsPlace": {
            "@type": "Accommodation",
            "additionalType": "EntirePlace",
            "occupancy": {"@type": "QuantitativeValue", "value": 8},
            "numberOfBedrooms": 4,
            "numberOfBathroomsTotal": 3,
            "bed": [{"@type": "BedDetails", "numberOfBeds": 4, "typeOfBed": "King"}],
            "floorSize": {
                # 154.31 m2 is the Bruttogeschossflaeche printed on the
                # architect's plan: gross area including walls and the 25.23 m2
                # balcony. Quoted on the owner's instruction. The net internal
                # area, being the sum of the rooms without the balcony, is
                # 111.20 m2.
                "@type": "QuantitativeValue",
                "value": 154.31,
                "unitCode": "MTK",
            },
            "petsAllowed": False,
            "smokingAllowed": False,
            "amenityFeature": [
                {"@type": "LocationFeatureSpecification", "name": n, "value": v}
                for n, v in GOOGLE_AMENITIES
            ] + [
                {"@type": "LocationFeatureSpecification",
                 "name": "internetType", "value": "Free"},
            ],
        },
        # numberOfRooms is deliberately omitted. It previously read 4, which
        # merely duplicated the bedroom count; the honest figure depends on
        # whether the living room counts, and the field is optional.
        "numberOfBedrooms": 4,
        "numberOfBathroomsTotal": 3,
        "occupancy": {"@type": "QuantitativeValue", "maxValue": 8, "unitText": "guests"},
        "petsAllowed": False,
        "smokingAllowed": False,
        # Apartment is one of Google's suggested additionalType values for a
        # vacation rental. Chalet would be a stretch: this is a flat in a
        # building, and saying otherwise sets the wrong expectation.
        "additionalType": "Apartment",
        "identifier": PROPERTY_ID,
        # sameAs and the ReserveAction below deliberately use the REAL
        # destinations, not our redirect paths. sameAs exists to tell a search
        # engine "this listing and that listing are the same property"; aiming
        # it at our own 302 would break exactly the association it is there to
        # make, and /go/ is disallowed in robots.txt besides.
        "sameAs": list(DESTINATIONS.values()),
        # floorSize now lives on containsPlace, which is where Google reads it.
        "checkinTime": "15:00",
        "isAccessibleForFree": False,
        "potentialAction": {
            "@type": "ReserveAction",
            "target": {
                "@type": "EntryPoint",
                "urlTemplate": DESTINATIONS["direct"],
                "actionPlatform": [
                    "http://schema.org/DesktopWebPlatform",
                    "http://schema.org/MobileWebPlatform",
                ],
            },
        },
    }


def jsonld(L, lang, page, meta):
    graph = []

    website = {
        "@type": "WebSite",
        "@id": SITE["origin"] + "/#website",
        "url": SITE["origin"] + "/",
        "name": SITE["name"],
        "inLanguage": lang,
    }
    graph.append(website)

    webpage = {
        "@type": "WebPage",
        "@id": url(page, lang, True) + "#webpage",
        "url": url(page, lang, True),
        "name": meta["title"],
        "description": meta["desc"],
        "inLanguage": lang,
        "isPartOf": {"@id": SITE["origin"] + "/#website"},
        "about": {"@id": url("home", lang, True) + "#lodging"},
        "primaryImageOfPage": "%s/img/piste-dawn-%d.jpg" % (SITE["origin"], _variants["piste-dawn"][-1]),
    }
    graph.append(webpage)

    if page in ("home", "apartment", "book"):
        graph.append(lodging_node(L, lang))

    if page != "home":
        graph.append({
            "@type": "BreadcrumbList",
            "@id": url(page, lang, True) + "#breadcrumb",
            "itemListElement": [
                {"@type": "ListItem", "position": 1,
                 "name": L["ui"]["home_label"], "item": url("home", lang, True)},
                {"@type": "ListItem", "position": 2,
                 "name": L["nav"][page], "item": url(page, lang, True)},
            ],
        })
    else:
        graph.append({
            "@type": "BreadcrumbList",
            "@id": url(page, lang, True) + "#breadcrumb",
            "itemListElement": [
                {"@type": "ListItem", "position": 1,
                 "name": L["ui"]["home_label"], "item": url("home", lang, True)},
            ],
        })
        graph.append({
            "@type": "FAQPage",
            "@id": url("home", lang, True) + "#faq",
            "inLanguage": lang,
            "mainEntity": [
                {"@type": "Question", "name": q,
                 "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}}
                for q, a in L["faq"]
            ],
        })

    return json.dumps({"@context": "https://schema.org", "@graph": graph},
                      ensure_ascii=False, indent=1)


# ---------------------------------------------------------------------------
# Page assembly
# ---------------------------------------------------------------------------

TOKEN = re.compile(r"\{\{(fig|pic)\|([a-z0-9-]+)\|([a-z0-9\- ]*)\|([^}]*)\}\}")
SIMPLE = re.compile(r"\{\{(faq|amenities|facts|bookblock|reservebox|platforms|collage)\}\}")


def expand(body, L, lang):
    for token, target in (("{apartment}", href("apartment", lang)),
                          ("{resort}", href("resort", lang)),
                          ("{book}", href("book", lang)),
                          ("{home}", href("home", lang))):
        body = body.replace(token, target)

    def fig(m):
        kind, name, cls, sizes = m.groups()
        pic = picture(name, L["alt"][name], sizes.strip())
        if kind == "pic":
            return pic
        cap = L["caption"].get(name)
        capel = "<figcaption>%s</figcaption>" % esc(cap) if cap else ""
        c = (' class="%s"' % cls.strip()) if cls.strip() else ""
        return "<figure%s>%s%s</figure>" % (c, pic, capel)

    def simple(m):
        return {
            "faq": build_faq,
            "amenities": build_amenities,
            "facts": build_facts,
            "bookblock": build_bookblock,
            "reservebox": build_reservebox,
            "platforms": build_platforms,
        }[m.group(1)](L)

    body = TOKEN.sub(fig, body)
    body = SIMPLE.sub(simple, body)
    return body


def build_page(lang, page):
    set_depth(page, lang)
    L = LANGS[lang]
    P = L["pages"][page]
    canonical = url(page, lang, True)

    alts = "\n".join(
        '<link rel="alternate" hreflang="%s" href="%s">' % (o, url(page, o, True))
        for o in LANG_ORDER)
    alts += '\n<link rel="alternate" hreflang="x-default" href="%s">' % url(page, X_DEFAULT, True)

    og_alt = "\n".join('<meta property="og:locale:alternate" content="%s">' % LANGS[o]["locale"]
                       for o in LANG_ORDER if o != lang)

    preload_hero = ""
    if page == "home":
        # The LCP element is the hero video's poster frame, so that is what
        # gets preloaded. (The video itself is deliberately NOT preloaded —
        # it should never compete with the poster or the text for bandwidth.)
        base = asset("img/")
        name = "hero-poster" if HERO_VIDEO else "piste-dawn"
        ws = _variants[name]
        srcset = ", ".join("%s%s-%d.avif %dw" % (base, name, w, w) for w in ws)
        preload_hero = (
            '<link rel="preload" as="image" type="image/avif" '
            'href="%s%s-%d.avif" imagesrcset="%s" '
            'imagesizes="(min-width: 640px) min(400px, 33vw), 96vw" '
            'fetchpriority="high">' % (base, name, ws[-1], srcset))

    hero = ""
    if page == "home":
        facts = "".join("<li>%s</li>" % esc(f) for f in P["facts"])
        # Headline, facts and the booking CTA come first; the mosaic is the
        # payoff underneath, not the thing you have to scroll past.
        # Full-bleed masthead: the facts read as a kicker, the headline spans
        # the whole measure, then a rule with the lede on the left and the
        # booking CTA hard right. Nothing is column-locked, so there is no
        # dead space above the headline waiting for a taller neighbour.
        # Facts, headline and lede each run the full measure, one under the
        # other. No rule, no buttons — the Reserve button lives in the header
        # bar and again in the availability block, so putting a third pair here
        # only pushed the photography down the page.
        hero = """<section class="hero" aria-labelledby="page-title">
  <div class="wrap">
    <ul class="hero-facts">%s</ul>
    <h1 id="page-title">%s</h1>
    <p class="hero-lede">%s</p>
    %s
  </div>
</section>""" % (facts, esc(P["h1"]), esc(P["lede"]), build_collage(L))
    else:
        # Interior pages get the same loden masthead band, minus the collage,
        # so the brand reads as one block from the header down.
        # Interior pages get the same loden masthead band, minus the collage,
        # with the breadcrumb sitting inside it rather than stranded on the
        # linen above.
        hero = """<section class="hero hero-simple" aria-labelledby="page-title">
  <div class="wrap">
    %s
    <h1 id="page-title">%s</h1>
    <p class="lede">%s</p>
    %s
  </div>
</section>""" % (build_crumbs(LANGS[lang], lang, page).replace(' class="crumbs wrap"',
                                                              ' class="crumbs"'),
                 esc(P["h1"]), esc(P["lede"]), build_jump(LANGS[lang], P["jump"]))

    body = expand(P["body"], L, lang)

    return """<!DOCTYPE html>
<html lang="%(lang)s">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s</title>
<meta name="description" content="%(desc)s">
<link rel="canonical" href="%(canonical)s">
%(alts)s
%(font_preload)s
<link rel="stylesheet" href="%(fontcss)s">
<link rel="stylesheet" href="%(css)s">
%(preload_hero)s
<link rel="icon" type="image/png" sizes="32x32" href="%(fav)s">
<link rel="apple-touch-icon" href="%(touch)s">
<meta name="theme-color" content="#35322E">
<meta property="og:type" content="website">
<meta property="og:site_name" content="%(site)s">
<meta property="og:title" content="%(title)s">
<meta property="og:description" content="%(desc)s">
<meta property="og:url" content="%(canonical)s">
<meta property="og:locale" content="%(locale)s">
%(og_alt)s
<meta property="og:image" content="%(origin)s%(share)s">
<meta property="og:image:width" content="%(share_w)d">
<meta property="og:image:height" content="%(share_h)d">
<meta property="og:image:alt" content="%(share_alt)s">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="%(title)s">
<meta name="twitter:description" content="%(desc)s">
<meta name="twitter:image" content="%(origin)s%(share)s">
<meta name="twitter:image:alt" content="%(share_alt)s">
<script type="application/ld+json">
%(jsonld)s
</script>
</head>
<body>
<a class="skip-link" href="#main">%(skip)s</a>
%(header)s
<main id="main">
%(hero)s
%(body)s
</main>
%(footer)s
</body>
</html>
""" % {
        "lang": lang,
        "css": asset("styles.css"),
        "fontcss": asset("fonts/fonts.css"),
        "font_preload": _font_preload_tags(),
        "fav": asset("img/favicon-32.png"),
        "touch": asset("img/apple-touch-icon.png"),
        "title": esc(P["title"]),
        "desc": esc(P["desc"]),
        "canonical": canonical,
        "alts": alts,
        "preload_hero": preload_hero,
        "site": esc(SITE["name"]),
        "locale": LANGS[lang]["locale"],
        "og_alt": og_alt,
        "origin": SITE["origin"],
        "share": SITE["share_img"],
        "share_w": SITE["share_w"],
        "share_h": SITE["share_h"],
        "share_alt": esc(LANGS[lang]["alt"]["share"]),
        "jsonld": jsonld(LANGS[lang], lang, page, P),
        "skip": esc(LANGS[lang]["ui"]["skip"]),
        "header": build_header(LANGS[lang], lang, page),
        "hero": hero,
        "body": body,
        "footer": build_footer(LANGS[lang], lang),
    }


# ---------------------------------------------------------------------------
# Root, sitemap, robots
# ---------------------------------------------------------------------------

def build_root():
    alts = "\n".join('<link rel="alternate" hreflang="%s" href="%s">' % (o, url("home", o, True))
                     for o in LANG_ORDER)
    alts += '\n<link rel="alternate" hreflang="x-default" href="%s">' % url("home", X_DEFAULT, True)
    set_depth()
    links = "".join('<li><a class="btn btn-secondary" href="%s" hreflang="%s" lang="%s">%s</a></li>'
                    % (href("home", o), o, o, LANGS[o]["name"]) for o in LANG_ORDER)
    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, follow">
<title>Bijou du Glacier, Saas-Fee</title>
<meta http-equiv="refresh" content="0; url=en/index.html">
%s
<link rel="stylesheet" href="fonts/fonts.css">
<link rel="stylesheet" href="styles.css">
<link rel="icon" type="image/png" sizes="32x32" href="img/favicon-32.png">
<meta name="theme-color" content="#22372B">
</head>
<body>
<main id="main" class="wrap page-head">
<img src="img/blason-168.png" width="148" height="168" alt="Bijou du Glacier" style="margin-bottom:1.5rem">
<h1>Bijou du Glacier</h1>
<p class="lede">A four-bedroom apartment in Saas-Fee, Valais. Choose a language:</p>
<ul class="platforms" style="margin-top:2rem">%s</ul>
</main>
</body>
</html>
""" % (alts, links)


BUILD_DATE = __import__("datetime").date.today().isoformat()


def build_sitemap():
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
           'xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for page in PAGE_ORDER:
        for lang in LANG_ORDER:
            out.append("  <url>")
            out.append("    <loc>%s</loc>" % url(page, lang, True))
            for o in LANG_ORDER:
                out.append('    <xhtml:link rel="alternate" hreflang="%s" href="%s"/>'
                           % (o, url(page, o, True)))
            out.append('    <xhtml:link rel="alternate" hreflang="x-default" href="%s"/>'
                       % url(page, X_DEFAULT, True))
            out.append("    <lastmod>%s</lastmod>" % BUILD_DATE)
            out.append("    <changefreq>monthly</changefreq>")
            out.append("    <priority>%s</priority>" % SITEMAP_PRIORITY[page])
            out.append("  </url>")
    out.append("</urlset>")
    return "\n".join(out) + "\n"


# IndexNow key. Public by design — it is hosted in the clear at the site root
# and proves only that whoever submits URLs also controls the domain. Not a
# secret; do not treat it as one. Changing it means re-hosting the new key file.
INDEXNOW_KEY = "c13d276a206e5cd14dbf8988027af48b"

# Every crawler we care about, named explicitly.
#
# Why name them when "User-agent: *" already allows everything: a crawler that
# finds a group matching its own token obeys ONLY that group and ignores the
# wildcard entirely. So the day someone adds a Disallow to the * group, these
# stay allowed. It also puts the decision on the record instead of leaving it
# to a default.
#
# The usual 2026 advice is to allow the search/retrieval bots and block the
# training ones. We allow all of them, deliberately. There is no IP here worth
# protecting — it is marketing copy about one apartment — and being quotable in
# an AI travel answer is a booking channel, not a cost. Revisit only if that
# stops being true.
AI_CRAWLERS = [
    ("OAI-SearchBot",    "OpenAI — ChatGPT search index"),
    ("ChatGPT-User",     "OpenAI — fetches a page when a user asks for it"),
    ("GPTBot",           "OpenAI — training"),
    ("Claude-SearchBot", "Anthropic — Claude search index"),
    ("Claude-User",      "Anthropic — user-initiated fetch"),
    ("ClaudeBot",        "Anthropic — training"),
    ("PerplexityBot",    "Perplexity — index for cited answers"),
    ("Perplexity-User",  "Perplexity — user-initiated fetch"),
    ("Google-Extended",  "Google — AI Overviews and Gemini grounding"),
    ("Applebot",         "Apple — Siri and Spotlight"),
    ("Applebot-Extended","Apple — Apple Intelligence"),
    ("CCBot",            "Common Crawl — feeds many downstream datasets"),
    ("Amazonbot",        "Amazon — Alexa and search"),
    ("meta-externalagent", "Meta — AI products"),
    ("Bingbot",          "Microsoft — Bing and Copilot"),
    ("DuckDuckBot",      "DuckDuckGo"),
]

_AI_BLOCK = "\n\n".join(
    "# %s\nUser-agent: %s\nAllow: /\nDisallow: /_backup/\nDisallow: /go/\nDisallow: /book-direct"
    % (why, tok) for tok, why in AI_CRAWLERS
)

ROBOTS = """# Bijou du Glacier — Saas-Fee
#
# Everything here is open to everyone. The only closed paths are the backup of
# the old site and the booking redirects.

User-agent: *
Allow: /
Disallow: /_backup/

# The booking buttons point at these paths and nginx 302s them straight out to
# SaasFeeHolidays, Airbnb and Booking.com. There is no page behind them. Left
# crawlable they would be indexed as thin redirects competing with the real
# booking page, so keep them out.
Disallow: /go/
Disallow: /book-direct

%s

Sitemap: %s/sitemap.xml
""" % (_AI_BLOCK, SITE["origin"])

REDIRECTS = """# Edge redirect for Cloudflare Pages / Netlify.
# Sends the bare domain to the English homepage, which is the hreflang x-default.
/    /en/    302
"""


# ---------------------------------------------------------------------------

def main():
    scan_images()
    written = []
    for lang in LANG_ORDER:
        for page in PAGE_ORDER:
            path = url(page, lang).strip("/")
            d = os.path.join(WEB, path)
            os.makedirs(d, exist_ok=True)
            f = os.path.join(d, "index.html")
            with open(f, "w", encoding="utf-8") as fh:
                fh.write(build_page(lang, page))
            written.append(os.path.relpath(f, WEB))

    for rel, content in (("index.html", build_root()),
                         ("sitemap.xml", build_sitemap()),
                         ("robots.txt", ROBOTS),
                         # IndexNow verification. Must be reachable at the site
                         # root and contain the key and nothing else.
                         ("%s.txt" % INDEXNOW_KEY, INDEXNOW_KEY + "\n"),
                         ("_redirects", REDIRECTS)):
        with open(os.path.join(WEB, rel), "w", encoding="utf-8") as fh:
            fh.write(content)
        written.append(rel)

    for w in written:
        print("  wrote", w)
    print("\n%d files." % len(written))


if __name__ == "__main__":
    sys.exit(main())
