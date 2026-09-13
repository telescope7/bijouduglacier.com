#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bijou du Glacier — pre-flight audit.

Checks the built site the way a picky reviewer would. Run it after any edit:

    python3 audit.py

Exit code 0 = clean, 1 = at least one FAIL.
"""

import json
import os
import re
import sys
from html.parser import HTMLParser
from urllib.parse import urlparse

HERE = os.path.dirname(os.path.abspath(__file__))
WEB = os.path.abspath(os.path.join(HERE, "..", "website"))
ORIGIN = "https://bijouduglacier.com"

# The booking buttons point at paths on our own domain that nginx 302s out to
# the platforms. They are real URLs but there is no file behind them, so the
# link checker has to know not to look for one. Imported rather than retyped,
# so build_site.py stays the single place the channels are defined.
sys.path.insert(0, HERE)
from build_site import CHANNEL_PATHS, DESTINATIONS  # noqa: E402

REDIRECT_PATHS = set(CHANNEL_PATHS.values())
NGINX_TEMPLATE = os.path.abspath(
    os.path.join(HERE, "..", "deploy", "templates", "site-body.conf.j2"))

# Known placeholders on our own domain, carried over from the original build.
# They are reported once, as a to-do, rather than as 48 broken-link failures.
# Nothing left. The direct-booking link points at the real listing on
# saasfeeholidays.com, and the Expedia stand-in has been removed from the site.
# Add an entry here if a stand-in URL is ever introduced again.
PLACEHOLDERS = {}

fails, warns = [], []
placeholder_hits = {}


def fail(where, msg):
    fails.append("%s: %s" % (where, msg))


def warn(where, msg):
    warns.append("%s: %s" % (where, msg))


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.headings = []          # (level, text)
        self.imgs = []              # dict of attrs
        self.links = []             # href
        self.canonical = None
        self.alternates = []        # (hreflang, href)
        self.title = None
        self.desc = None
        self.html_lang = None
        self.jsonld = []
        self.ids = set()
        self.anchors = []
        self._cur_h = None
        self._buf = []
        self._in_ld = False
        self._ld = []
        self._in_title = False
        self._in_video = False
        self.videos = []            # dict of <video> attrs
        self.video_sources = []     # src of each <source> inside a <video>

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get("id"):
            self.ids.add(a["id"])
        if tag == "html":
            self.html_lang = a.get("lang")
        elif tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self._cur_h = int(tag[1])
            self._buf = []
        elif tag == "video":
            self._in_video = True
            self.videos.append(a)
        elif tag == "img":
            self.imgs.append(a)
        elif tag == "source":
            # <source> means two different things: inside <picture> it needs a
            # srcset, inside <video> it needs a src. Don't conflate them.
            if self._in_video:
                self.video_sources.append(a)
            else:
                self.imgs.append(dict(a, _source=True))
        elif tag == "a" and a.get("href"):
            self.links.append(a["href"])
        elif tag == "link":
            rel = (a.get("rel") or "").lower()
            if rel == "canonical":
                self.canonical = a.get("href")
            elif rel == "alternate" and a.get("hreflang"):
                self.alternates.append((a["hreflang"], a.get("href")))
        elif tag == "meta":
            if a.get("name") == "description":
                self.desc = a.get("content")
        elif tag == "script" and a.get("type") == "application/ld+json":
            self._in_ld = True
            self._ld = []
        elif tag == "title":
            self._in_title = True
            self._buf = []

    def handle_endtag(self, tag):
        if tag == "video":
            self._in_video = False
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6") and self._cur_h:
            self.headings.append((self._cur_h, "".join(self._buf).strip()))
            self._cur_h = None
        elif tag == "script" and self._in_ld:
            self.jsonld.append("".join(self._ld))
            self._in_ld = False
        elif tag == "title":
            self.title = "".join(self._buf).strip()
            self._in_title = False

    def handle_data(self, d):
        if self._in_ld:
            self._ld.append(d)
        elif self._cur_h or self._in_title:
            self._buf.append(d)


def to_path(href, page_dir):
    """Resolve a site href to a file path, or None if external/anchor."""
    if href.startswith(("http://", "https://", "mailto:", "tel:")):
        if href.startswith(ORIGIN):
            href = href[len(ORIGIN):] or "/"
        else:
            return None
    if href.split("?")[0].rstrip("/") in REDIRECT_PATHS:
        return None          # served by nginx as a 302, not by a file
    if href.startswith("#"):
        return None
    p = urlparse(href).path
    if not p:
        return None
    if p.startswith("/"):
        base = os.path.join(WEB, p.lstrip("/"))
    else:
        base = os.path.normpath(os.path.join(page_dir, p))
    if p.endswith("/") or os.path.isdir(base):
        return os.path.join(base, "index.html")
    return base


def main():
    pages = []
    for root, _dirs, files in os.walk(WEB):
        if "_backup" in root:
            continue
        for f in files:
            if f.endswith(".html"):
                pages.append(os.path.join(root, f))
    pages.sort()

    parsed = {}
    for path in pages:
        p = Page()
        p.feed(open(path, encoding="utf-8").read())
        parsed[path] = p

    rel = lambda p: os.path.relpath(p, WEB)
    indexable = [p for p in pages if rel(p) != "index.html"]

    print("Auditing %d HTML files in %s\n" % (len(pages), WEB))

    # --- 1. exactly one H1, no heading-level skips -------------------------
    for path in pages:
        p = parsed[path]
        h1s = [h for h in p.headings if h[0] == 1]
        if len(h1s) != 1:
            fail(rel(path), "expected exactly 1 <h1>, found %d" % len(h1s))
        prev = 0
        for lvl, txt in p.headings:
            if prev and lvl > prev + 1:
                fail(rel(path), "heading jumps h%d -> h%d at %r" % (prev, lvl, txt[:40]))
            prev = lvl

    # --- 2. alt text and intrinsic dimensions on every img ----------------
    for path in pages:
        for a in parsed[path].imgs:
            if a.get("_source"):
                if not a.get("srcset"):
                    fail(rel(path), "<source> without srcset")
                continue
            # A MISSING alt attribute is a bug. An explicitly EMPTY one is the
            # correct markup for a decorative image whose meaning is already
            # carried by adjacent text — the blason next to the wordmark, for
            # instance. Screen readers skip it instead of announcing the brand
            # twice. So: absent = fail, empty = fine.
            if "alt" not in a:
                fail(rel(path), "img with no alt attribute: %s" % a.get("src"))
            elif not a["alt"].strip() and "blason" not in (a.get("src") or ""):
                warn(rel(path), "img has alt=\"\" (decorative) — confirm that is "
                                "intended: %s" % a.get("src"))
            if not (a.get("width") and a.get("height")):
                fail(rel(path), "img without width/height (CLS risk): %s" % a.get("src"))

    # --- 3. every referenced image file exists ----------------------------
    srcs = set()
    for path in pages:
        d = os.path.dirname(path)
        for a in parsed[path].imgs:
            for key in ("src", "srcset"):
                v = a.get(key)
                if not v:
                    continue
                for part in v.split(","):
                    u = part.strip().split(" ")[0]
                    if u:
                        srcs.add((rel(path), d, u))
    for where, d, u in sorted(srcs):
        f = (os.path.join(WEB, u.lstrip("/")) if u.startswith("/")
             else os.path.normpath(os.path.join(d, u)))
        if not os.path.isfile(f):
            fail(where, "missing image file %s" % u)

    # --- 3b. the hero video: files exist, poster set, autoplay is legal ----
    for path in pages:
        p = parsed[path]
        d = os.path.dirname(path)
        for v in p.videos:
            if "muted" not in v:
                fail(rel(path), "<video autoplay> without muted — browsers will "
                                "refuse to autoplay it")
            if "playsinline" not in v:
                warn(rel(path), "<video> without playsinline — iOS will open it "
                                "fullscreen instead of playing in the grid")
            if not v.get("poster"):
                warn(rel(path), "<video> without a poster frame")
            elif not os.path.isfile(os.path.normpath(os.path.join(d, v["poster"]))):
                fail(rel(path), "video poster missing: %s" % v["poster"])
            if not (v.get("width") and v.get("height")):
                fail(rel(path), "<video> without width/height (CLS risk)")
            if not (v.get("aria-label") or "").strip():
                warn(rel(path), "<video> with no aria-label")
        if p.videos and not p.video_sources:
            fail(rel(path), "<video> with no <source>")
        for srcel in p.video_sources:
            u = srcel.get("src")
            if not u:
                fail(rel(path), "<source> inside <video> with no src")
                continue
            f = os.path.normpath(os.path.join(d, u))
            if not os.path.isfile(f):
                fail(rel(path), "missing video file %s" % u)
            elif os.path.getsize(f) > 4 * 1024 * 1024:
                warn(rel(path), "%s is %.1f MB — heavy for an autoplaying hero"
                     % (u, os.path.getsize(f) / 1024 / 1024))

    # --- 4. internal links resolve ----------------------------------------
    for path in pages:
        d = os.path.dirname(path)
        for href in parsed[path].links:
            if href.startswith("#"):
                if href[1:] not in parsed[path].ids:
                    fail(rel(path), "anchor #%s has no matching id" % href[1:])
                continue
            if href in PLACEHOLDERS:
                placeholder_hits[href] = placeholder_hits.get(href, 0) + 1
                continue
            t = to_path(href, d)
            if t is None:
                continue
            frag = urlparse(href).fragment
            if not os.path.isfile(t):
                fail(rel(path), "broken internal link %s" % href)
            elif frag:
                target = parsed.get(t)
                if target and frag not in target.ids:
                    fail(rel(path), "link %s points at a missing id" % href)

    # --- 5. canonical present, absolute, self-referential ------------------
    for path in indexable:
        p = parsed[path]
        expected = ORIGIN + "/" + os.path.dirname(rel(path)).replace(os.sep, "/") + "/"
        if not p.canonical:
            fail(rel(path), "no canonical")
        elif p.canonical != expected:
            fail(rel(path), "canonical %s != expected %s" % (p.canonical, expected))

    # --- 6. reciprocal hreflang, including x-default ----------------------
    for path in indexable:
        p = parsed[path]
        langs = {h for h, _ in p.alternates}
        for need in ("en", "fr", "de", "it", "x-default"):
            if need not in langs:
                fail(rel(path), "hreflang missing %s" % need)
        for h, href in p.alternates:
            t = to_path(href, os.path.dirname(path))
            if not t or not os.path.isfile(t):
                fail(rel(path), "hreflang %s points at a missing page: %s" % (h, href))
                continue
            back = {hh: hr for hh, hr in parsed[t].alternates}
            if p.canonical not in back.values():
                fail(rel(path), "hreflang %s -> %s is not reciprocal" % (h, href))
        xd = [hr for hh, hr in p.alternates if hh == "x-default"]
        if xd and "/en/" not in xd[0]:
            warn(rel(path), "x-default is not the English page: %s" % xd[0])
        if p.html_lang and rel(path).split(os.sep)[0] != p.html_lang:
            fail(rel(path), "<html lang=%s> does not match directory" % p.html_lang)

    # --- 7. unique titles and descriptions --------------------------------
    seen_t, seen_d = {}, {}
    for path in indexable:
        p = parsed[path]
        if not p.title:
            fail(rel(path), "no <title>")
        elif p.title in seen_t:
            fail(rel(path), "duplicate title with %s" % seen_t[p.title])
        else:
            seen_t[p.title] = rel(path)
            if len(p.title) > 70:
                warn(rel(path), "title is %d chars (Google truncates near 60)" % len(p.title))
        if not p.desc:
            fail(rel(path), "no meta description")
        elif p.desc in seen_d:
            fail(rel(path), "duplicate meta description with %s" % seen_d[p.desc])
        else:
            seen_d[p.desc] = rel(path)
            if not 110 <= len(p.desc) <= 175:
                warn(rel(path), "meta description is %d chars (aim 110-165)" % len(p.desc))

    # --- 8. JSON-LD parses and carries the required nodes -----------------
    for path in indexable:
        p = parsed[path]
        if not p.jsonld:
            fail(rel(path), "no JSON-LD")
        for blob in p.jsonld:
            try:
                data = json.loads(blob)
            except Exception as e:
                fail(rel(path), "JSON-LD does not parse: %s" % e)
                continue
            types = {n.get("@type") for n in data.get("@graph", [])}
            if "BreadcrumbList" not in types:
                fail(rel(path), "JSON-LD has no BreadcrumbList")
            if rel(path).endswith(os.sep.join(["", "index.html"])) and \
               os.path.dirname(rel(path)).count(os.sep) == 0:
                if "FAQPage" not in types:
                    fail(rel(path), "homepage JSON-LD has no FAQPage")
                if "VacationRental" not in types:
                    fail(rel(path), "homepage JSON-LD has no VacationRental")
            for n in data.get("@graph", []):
                if n.get("@type") == "VacationRental":
                    for k in ("address", "geo", "amenityFeature", "name", "url"):
                        if k not in n:
                            fail(rel(path), "VacationRental missing %s" % k)
                    if "aggregateRating" in n:
                        warn(rel(path), "aggregateRating present — confirm it is a real, "
                                        "verifiable rating before shipping")

    # --- 9. sitemap ------------------------------------------------------
    sm = os.path.join(WEB, "sitemap.xml")
    if not os.path.isfile(sm):
        fail("sitemap.xml", "missing")
    else:
        body = open(sm, encoding="utf-8").read()
        locs = re.findall(r"<loc>(.*?)</loc>", body)
        if len(locs) != 16:
            fail("sitemap.xml", "expected 16 <loc> entries, found %d" % len(locs))
        for loc in locs:
            t = to_path(loc, WEB)
            if not t or not os.path.isfile(t):
                fail("sitemap.xml", "lists a URL with no file: %s" % loc)
        for loc in locs:
            if body.count('href="%s"' % loc) < 4:
                warn("sitemap.xml", "%s appears in fewer than 4 alternate sets" % loc)
        if "x-default" not in body:
            fail("sitemap.xml", "no x-default alternates")
    if not os.path.isfile(os.path.join(WEB, "robots.txt")):
        fail("robots.txt", "missing")

    # --- 10a. no root-absolute paths (they break file:// browsing) --------
    abs_pat = re.compile(r'(?:href|src|srcset|imagesrcset)="(/[^"]*)"')
    for path in pages:
        for m in abs_pat.finditer(open(path, encoding="utf-8").read()):
            fail(rel(path), "root-absolute path %s — 404s when the file is "
                            "opened directly from disk" % m.group(1))

    # --- 10b. ...but canonical and hreflang must stay absolute https ------
    for path in indexable:
        p = parsed[path]
        for h, hrefv in p.alternates:
            if not hrefv.startswith("https://"):
                fail(rel(path), "hreflang %s should be an absolute URL, got %s" % (h, hrefv))
        if p.canonical and not p.canonical.startswith("https://"):
            fail(rel(path), "canonical should be an absolute URL")

    # --- 10c. offline walk: can a browser reach all 17 pages from disk? ---
    # Simulates double-clicking website/index.html and clicking through, with
    # no server running. Follows the meta-refresh and every <a href>, and
    # checks the stylesheet resolves from every page it lands on.
    start = os.path.join(WEB, "index.html")
    seen, queue = set(), [start]
    while queue:
        cur = queue.pop()
        if cur in seen or cur not in parsed:
            continue
        seen.add(cur)
        d = os.path.dirname(cur)
        raw = open(cur, encoding="utf-8").read()
        m = re.search(r'http-equiv="refresh"[^>]*url=([^"\']+)', raw)
        if m:
            queue.append(os.path.normpath(os.path.join(d, m.group(1).strip())))
        # only the LOCAL stylesheet has to resolve on disk; the Google Fonts
        # sheet is deliberately remote.
        local = [h for h in re.findall(r'<link rel="stylesheet" href="([^"]+)"', raw)
                 if not h.startswith("http")]
        if not local:
            fail(rel(cur), "no local stylesheet link")
        for h in local:
            if not os.path.isfile(os.path.normpath(os.path.join(d, h))):
                fail(rel(cur), "stylesheet %s does not resolve from disk" % h)
        for h in parsed[cur].links:
            if h.startswith(("http", "#", "mailto:", "tel:")):
                continue
            t = os.path.normpath(os.path.join(d, urlparse(h).path))
            if os.path.isdir(t):
                fail(rel(cur), "link %s points at a directory — under file:// a "
                               "browser shows a listing, not the page" % h)
            elif not os.path.isfile(t):
                fail(rel(cur), "link %s does not resolve from disk" % h)
            else:
                queue.append(t)
    unreached = [rel(p) for p in pages if p not in seen]
    if unreached:
        fail("offline walk", "unreachable by clicking from website/index.html: %s"
             % ", ".join(unreached))
    else:
        print("  OK    offline walk reached all %d pages from website/index.html "
              "with no server\n" % len(seen))

    # --- 10d. no em dashes in the prose ----------------------------------
    # House rule. An em dash in body copy is the single most reliable tell that
    # a page was written by a machine, and this site is selling a €600-a-night
    # apartment on the strength of sounding like a person wrote it.
    for path in pages:
        body = open(path, encoding="utf-8").read()
        body = re.sub(r"(?s)<script.*?</script>", "", body)   # JSON-LD mirrors the copy
        body = re.sub(r"(?s)<!--.*?-->", "", body)            # the commented-out still
        body = re.sub(r"<[^>]+>", " ", body)
        for m in re.finditer(r"[^.!?]{0,55}\u2014[^.!?]{0,55}", body):
            fail(rel(path), "em dash in the copy: ...%s..."
                 % " ".join(m.group(0).split()))

    # --- 11. webfonts ----------------------------------------------------
    # Type now comes from Google Fonts, which is the one third-party request on
    # the site. Check it is actually asked for, and that the preconnects that
    # make it fast are there too.
    for path in indexable:
        raw = open(path, encoding="utf-8").read()
        if "fonts.googleapis.com/css2" not in raw:
            fail(rel(path), "no webfont stylesheet — headings will fall back to Georgia")
        if 'rel="preconnect" href="https://fonts.gstatic.com"' not in raw:
            warn(rel(path), "no preconnect to fonts.gstatic.com (costs ~100ms)")

    # --- 12. text contrast on the dark bands -----------------------------
    # The site has light sections and stone sections, and most text classes are
    # written for the light ones. Put such a class inside a stone band and it
    # keeps its dark colour: that is how `.lede` ended up near-black on the
    # near-black hero of the apartment, Saas-Fee and book pages, at 1.29:1.
    # Nothing catches that by eye at a glance, so measure it.
    css_raw = open(os.path.join(WEB, "styles.css"), encoding="utf-8").read()
    css_src = re.sub(r"/\*.*?\*/", "", css_raw, flags=re.S)   # comments hold colons
    varmap = dict(re.findall(r"(--[a-z0-9-]+):\s*(#[0-9A-Fa-f]{6})", css_src))

    colour_rules, sets_own_bg = [], set()
    for order, blk in enumerate(re.finditer(r"([^{}]+)\{([^{}]*)\}", css_src)):
        sel, body = blk.group(1).strip(), blk.group(2)
        cm = re.search(r"(?<!-)\bcolor:\s*(?:var\((--[a-z0-9-]+)\)|(#[0-9A-Fa-f]{6}))", body)
        has_bg = re.search(r"\bbackground(-color)?:\s*(var\(|#)", body)
        for one in (s.strip() for s in sel.split(",")):
            if ":" in one or "@" in one:
                continue
            if has_bg:
                sets_own_bg.update(re.findall(r"\.([a-z0-9-]+)", one))
            if cm:
                hexv = varmap.get(cm.group(1)) if cm.group(1) else cm.group(2)
                if hexv:
                    colour_rules.append((one, hexv, order))

    def _lum(hexv):
        ch = [int(hexv[i:i + 2], 16) / 255 for i in (1, 3, 5)]
        ch = [c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4 for c in ch]
        return 0.2126 * ch[0] + 0.7152 * ch[1] + 0.0722 * ch[2]

    def _ratio(a, b):
        la, lb = _lum(a), _lum(b)
        return (max(la, lb) + 0.05) / (min(la, lb) + 0.05)

    def _resolve(cls, container):
        """Winning colour for .cls inside .container: specificity, then source order."""
        best = None
        for sel, hexv, order in colour_rules:
            if sel == "." + cls:
                spec = (0, 1, 0)
            elif sel == ".%s .%s" % (container, cls):
                spec = (0, 2, 0)
            else:
                continue
            if best is None or (spec, order) >= (best[0], best[1]):
                best = (spec, order, hexv)
        return best[2] if best else None

    DARK_BANDS = {"hero": "#35322E", "reserve": "#35322E",
                  "site-footer": "#35322E", "site-header": "#35322E"}
    contrast_seen = set()
    for path in indexable:
        raw = open(path, encoding="utf-8").read()
        for band, bg in DARK_BANDS.items():
            pat = r'<(section|div|footer|header)[^>]*class="[^"]*\b%s\b[^"]*"' % band
            for m in re.finditer(pat, raw):
                seg = raw[m.end():m.end() + 12000]
                end = seg.find("</%s>" % m.group(1))
                seg = seg[:end] if end > 0 else seg
                for cm2 in re.finditer(r'class="([^"]+)"', seg):
                    toks = cm2.group(1).split()
                    if any(t in sets_own_bg for t in toks):
                        continue          # a button etc. paints its own ground
                    for cls in toks:
                        hexv = _resolve(cls, band)
                        if not hexv:
                            continue
                        r = _ratio(hexv, bg)
                        if r < 4.5 and (band, cls) not in contrast_seen:
                            contrast_seen.add((band, cls))
                            fail(rel(path), ".%s inside .%s is %s on %s = %.2f:1, "
                                            "unreadable (needs 4.5:1)"
                                 % (cls, band, hexv, bg, r))

    # --- 13. grid placement a generic rule quietly outranks -----------------
    # The mosaic places each cell by class (.cell-a, .cell-b ...) and resets
    # them with a rule on .collage figure. `.collage figure` scores (0,1,1);
    # a bare `.cell-a` scores (0,1,0) and LOSES to it, so the reset wins and
    # the cell never moves. That is invisible on a wide screen, where the
    # reset is not in play, and it silently broke the phone layout: two cells
    # meant to span the full width were auto-placed side by side instead,
    # leaving a hole under the shorter one.
    #
    # Nothing about that is specific to this stylesheet. Any time a rule
    # written as "container + element" sets grid placement in the same context
    # as rules written as a single class, the general rule wins and the
    # specific ones are dead code. Measure it rather than trusting the eye.

    def _spec(sel):
        sel = re.sub(r"::?[a-z-]+(\([^)]*\))?", "", sel)
        return (len(re.findall(r"#[\w-]+", sel)),
                len(re.findall(r"\.[\w-]+", sel)),
                len(re.findall(r"(?:^|[\s>+~])([a-z]+)(?![\w-])", sel)))

    PLACEMENT = ("grid-column", "grid-row", "grid-area")

    def _contexts(css):
        """(label, body) for the top level and for each @media block."""
        out, depth, start, rest = [], 0, None, []
        i = 0
        while i < len(css):
            if css.startswith("@media", i) and depth == 0:
                head_end = css.index("{", i)
                label = " ".join(css[i:head_end].split())
                depth, start, j = 1, head_end + 1, head_end + 1
                while j < len(css) and depth:
                    depth += (css[j] == "{") - (css[j] == "}")
                    j += 1
                out.append((label, css[start:j - 1]))
                i = j
                continue
            rest.append(css[i])
            i += 1
        out.append(("top level", "".join(rest)))
        return out

    for label, body in _contexts(css_src):
        placed = []
        for blk in re.finditer(r"([^{}]+)\{([^{}]*)\}", body):
            props = blk.group(2)
            if not any(re.search(r"\b%s\s*:" % p, props) for p in PLACEMENT):
                continue
            for sel in (x.strip() for x in blk.group(1).split(",")):
                if sel and "@" not in sel:
                    placed.append((sel, _spec(sel)))
        generic = [(s, sp) for s, sp in placed
                   if re.search(r"\.[\w-]+\s+[a-z]+$", s)]
        single = [(s, sp) for s, sp in placed if re.fullmatch(r"\.[\w-]+", s)]
        for gsel, gspec in generic:
            for ssel, sspec in single:
                if gspec > sspec:
                    fail("styles.css",
                         "%s: `%s` %s outranks `%s` %s on grid placement, so "
                         "`%s` never applies. Prefix it to raise its "
                         "specificity." % (label, gsel, gspec, ssel, sspec, ssel))

    # --- 14. the booking redirects ----------------------------------------
    # Every booking button points at a path on our own domain that nginx 302s
    # to a platform. Two files have to agree for that to work, and they live
    # in different languages in different folders, so check rather than hope.

    if not os.path.isfile(NGINX_TEMPLATE):
        fail("deploy", "site-body.conf.j2 is missing, so the booking "
                       "redirects have nowhere to be served from")
    else:
        ngx = open(NGINX_TEMPLATE, encoding="utf-8").read()
        for channel, path in sorted(CHANNEL_PATHS.items()):
            dest = DESTINATIONS[channel]
            block = re.search(
                r"location\s*=\s*%s\s*\{(.*?)\}" % re.escape(path), ngx, re.S)
            if not block:
                fail("site-body.conf.j2",
                     "no `location = %s` block, so that button would 404" % path)
                continue
            body = block.group(1)
            m = re.search(r"return\s+(\d{3})\s+(\S+?);", body)
            if not m:
                fail("site-body.conf.j2", "%s does not return a redirect" % path)
                continue
            code, target = m.group(1), m.group(2)
            if code != "302":
                fail("site-body.conf.j2",
                     "%s returns %s; these targets change, so it must be 302 "
                     "or browsers will cache the old destination" % (path, code))
            if target != dest:
                fail("site-body.conf.j2",
                     "%s redirects to %s but build_site.py DESTINATIONS[%r] is "
                     "%s — the two have drifted apart" % (path, target, channel, dest))
            if "access_log" not in body:
                fail("site-body.conf.j2",
                     "%s has no access_log line of its own, so the click cannot "
                     "be told apart from a page view" % path)
        # The redirects must sit ABOVE the catch-all or `location /` would
        # never reach them... (exact `=` matches actually win regardless, but
        # keeping the order readable is the point).
        if "location / {" in ngx:
            catch_all = ngx.index("location / {")
            for path in CHANNEL_PATHS.values():
                where = ngx.find("location = %s" % path)
                if where > catch_all:
                    warn("site-body.conf.j2",
                         "`location = %s` is written below the catch-all; it "
                         "still works, but read top-down it looks dead" % path)

    # No page may link straight at a platform: that click would be invisible.
    for path in pages:
        for href in parsed[path].links:
            for channel, dest in DESTINATIONS.items():
                if href.startswith(dest):
                    fail(rel(path),
                         "links directly to %s — use %s so the click is counted"
                         % (channel, CHANNEL_PATHS[channel]))

    # robots.txt must keep crawlers off them: there is no page there, and an
    # indexed thin redirect competes with the real booking page.
    robots_path = os.path.join(WEB, "robots.txt")
    robots = open(robots_path, encoding="utf-8").read() if os.path.isfile(robots_path) else ""
    for needed in ("/go/", "/book-direct"):
        if not re.search(r"^Disallow:\s*%s\s*$" % re.escape(needed), robots, re.M):
            fail("robots.txt", "does not Disallow %s" % needed)

    # ...and they must not be advertised in the sitemap.
    smap_path = os.path.join(WEB, "sitemap.xml")
    smap = open(smap_path, encoding="utf-8").read() if os.path.isfile(smap_path) else ""
    for path in CHANNEL_PATHS.values():
        if path in smap:
            fail("sitemap.xml", "lists %s, which is a redirect, not a page" % path)

    # --- 15. nginx location precedence ------------------------------------
    # nginx checks regex locations BEFORE settling on a prefix location. So a
    # prefix block that serves files off disk and leans on `index` to find
    # index.html can have that internal redirect stolen by an unrelated regex
    # location, which then resolves the file against the wrong root. The
    # symptom is a 404 that arrives *after* a successful auth prompt.
    #
    # `^~` is the fix: it tells nginx to stop once this prefix wins. Same shape
    # of bug as a CSS rule being outranked by a more specific selector, and
    # just as invisible by eye, so measure it.

    if os.path.isfile(NGINX_TEMPLATE):
        ngx_raw = open(NGINX_TEMPLATE, encoding="utf-8").read()
        ngx_src = re.sub(r"#.*", "", ngx_raw)

        regex_locs = re.findall(r"location\s+~\*?\s+(\S+)", ngx_src)
        for m in re.finditer(r"location\s+(\^~\s+)?(/\S*)\s*\{", ngx_src):
            caret, path = m.group(1), m.group(2)
            if caret or path == "/":
                continue                      # already guarded, or the catch-all
            depth, j = 1, m.end()
            while j < len(ngx_src) and depth:
                depth += (ngx_src[j] == "{") - (ngx_src[j] == "}")
                j += 1
            body = ngx_src[m.end():j - 1]
            serves = re.search(r"\b(root|alias)\b", body)
            uses_index = re.search(r"\bindex\b", body)
            if serves and uses_index and regex_locs:
                fail("site-body.conf.j2",
                     "`location %s` serves files and relies on `index`, but is "
                     "not `location ^~ %s`. The internal redirect to "
                     "%sindex.html will be captured by one of the regex "
                     "locations (%s) and resolved against the wrong root, "
                     "giving a 404 after a successful auth prompt."
                     % (path, path, path, ", ".join(sorted(set(regex_locs))[:3])))

    # --- report ----------------------------------------------------------
    if placeholder_hits:
        print("  TO DO — placeholder URLs still in the markup:")
        for u, n in sorted(placeholder_hits.items()):
            print("          %s  (%d links)\n            replace with %s"
                  % (u, n, PLACEHOLDERS[u]))
        print()
    for w in warns:
        print("  WARN  " + w)
    if warns:
        print()
    for f in fails:
        print("  FAIL  " + f)
    print("\n%d fail, %d warn." % (len(fails), len(warns)))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
