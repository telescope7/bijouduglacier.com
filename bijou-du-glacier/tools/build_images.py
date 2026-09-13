#!/usr/bin/env python3
"""
Bijou du Glacier — image build.

Reads originals from ../../media files combined/ and writes optimised,
multi-width AVIF + JPEG derivatives into ../website/images/.

This is NOT a build system for the site. The site is plain static HTML+CSS and
needs nothing to serve it. This script exists only so the image set can be
regenerated if a source photo is replaced.

    python3 build_images.py

Requires Pillow >= 10 with AVIF support.
"""

import os
import sys
from PIL import Image, ImageOps

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.abspath(os.path.join(HERE, "..", "..", "media files combined"))
OUT = os.path.abspath(os.path.join(HERE, "..", "website", "img"))

AB = os.path.join(SRC, "airbnb")
KF = os.path.join(SRC, "extract")


def ab(stub):
    """Resolve an abbreviated airbnb uuid to its full path."""
    for f in os.listdir(AB):
        if f.startswith(stub):
            return os.path.join(AB, f)
    raise FileNotFoundError(stub)


def kf(n):
    return os.path.join(KF, "keyframe_%03d.jpg" % n)


def src(name):
    return os.path.join(SRC, name)


# Per-image encoder overrides. The defaults (JPEG 80 / AVIF 58) are tuned for
# photographs. The floor plan is line art: thin dark strokes on a flat ground,
# which is exactly what those settings ring and smear. It gets a higher quality
# and is still small, because flat areas compress almost for free.
QUALITY = {"floorplan": (93, 74)}


# name, source, target aspect (w/h), vertical focus 0=top 1=bottom, widths
MANIFEST = [
    # ---- hero collage ------------------------------------------------
    ("piste-dawn",      kf(2),            8 / 9,   0.46, [560, 840, 1080]),
    ("massif",          ab("68dde24d"),   8 / 3,   0.52, [600, 900, 1200]),
    # Cell A of the mosaic is the hero video; the four stills beside it are cut
    # to the exact ratio of their cell, so object-fit has almost nothing to do.
    ("living-room",     ab("1417450a"),  23 / 10,  0.46, [500, 800, 1200]),   # cell B
    ("kitchen-shelves", ab("234bb200"),  17 / 20,  0.50, [300, 460, 680]),    # cell C
    ("master-bedroom",  ab("557ab4a1"),  17 / 20,  0.50, [300, 460, 680]),    # cell D
    ("robe-door",       kf(26),           5 / 9,   0.50, [220, 400, 600]),    # cell E
    ("balcony-view",    ab("456335db"),   3 / 2,   0.50, [360, 540, 720]),
    ("dining-band",     ab("6a6c369f"),   7 / 2,   0.55, [600, 900, 1200]),

    # ---- balcony -----------------------------------------------------
    # Both sources are 940x1672 portrait. At 2/3 the crop only trims height, and
    # the focus is set high on the frame so the timber soffit stays in shot: it
    # is what proves the balcony is covered. patio-hero is 5/9, which is within
    # 0.007 of the source ratio, so it loses eleven pixels of width and nothing
    # else, and drops straight into cell E of the hero mosaic.
    ("patio-seating", src("patio_all.png"),   2 / 3,   0.35, [420, 640, 900]),
    ("patio-chair",   src("patio_large.png"), 2 / 3,   0.35, [420, 640, 900]),
    ("patio-hero",    src("patio_large.png"), 5 / 9,   0.50, [220, 400, 600]),

    # ---- floor plan --------------------------------------------------
    # Apartment B4 of Residence du Glacier, lifted from the developer's own
    # second-floor plan. The neighbouring unit is painted out and the sale
    # pricing is cropped away; what is left is this apartment and the stair
    # that reaches its door. Aspect is the master's own, so crop_to is a no-op
    # and no part of the drawing is ever trimmed.
    ("floorplan", src("floorplan-b4.png"), 900 / 863, 0.50, [440, 660, 900]),

    # ---- gallery: living ---------------------------------------------
    ("living-wide",     ab("781e9178"),   3 / 2,   0.50, [480, 800, 1200]),
    ("coffee-table",    ab("dcdf24d2"),   3 / 2,   0.50, [480, 800, 1200]),
    ("living-corner",   ab("f1f96fdb"),   3 / 2,   0.50, [480, 720]),

    # ---- gallery: eating ---------------------------------------------
    ("dining-table",    ab("6a6c369f"),   3 / 2,   0.50, [480, 800, 1200]),
    ("dining-walnut",   ab("e3f23727"),   3 / 2,   0.50, [480, 800, 1200]),
    ("kitchen",         ab("1691966f"),   3 / 2,   0.50, [480, 800, 1200]),
    ("kitchen-oven",    ab("50cfcea7"),   3 / 2,   0.50, [480, 800, 1200]),
    ("kitchen-tap",     ab("376618b3"),   3 / 2,   0.50, [480, 720]),

    # ---- gallery: sleeping -------------------------------------------
    ("bedroom-2",       ab("99fcfafa"),   3 / 2,   0.50, [480, 800, 1200]),
    ("bedroom-3",       ab("efceccd2"),   3 / 2,   0.50, [480, 800, 1200]),
    ("bedroom-4",       ab("3a2151c2"),   3 / 2,   0.50, [480, 720]),
    ("wardrobe",        ab("e49582cb"),   3 / 2,   0.50, [480, 720]),
    ("blanket",         kf(17),           3 / 2,   0.50, [480, 720, 1080]),

    # ---- gallery: bathrooms ------------------------------------------
    ("bathroom",        ab("fa81d026"),   3 / 2,   0.50, [480, 800, 1200]),
    ("bathroom-shower", ab("0b0a5abb"),   3 / 2,   0.50, [480, 800, 1200]),
    ("bathroom-bath",   ab("5da2d6d4"),   3 / 2,   0.50, [480, 720]),

    # ---- gallery: outside --------------------------------------------
    ("village",         kf(4),            3 / 2,   0.62, [480, 800, 1080]),
    ("glacier-view",    ab("64643eb7"),   3 / 2,   0.50, [480, 720]),

    # ---- social share image (1200x630) -------------------------------
    ("share",           ab("68dde24d"),   1200 / 630, 0.50, [1200]),
]


def crop_to(im, aspect, focus):
    w, h = im.size
    cur = w / h
    if abs(cur - aspect) < 0.005:
        return im
    if cur > aspect:                       # too wide -> trim sides (centred)
        nw = int(round(h * aspect))
        x = (w - nw) // 2
        return im.crop((x, 0, x + nw, h))
    nh = int(round(w / aspect))            # too tall -> trim using focus point
    y = int(round((h - nh) * focus))
    y = max(0, min(y, h - nh))
    return im.crop((0, y, w, y + nh))


def build_blason():
    """Derive the header logo and the favicons from website/img/blason.png.

    The source is a 1024x1024 RGBA shield with transparent surrounds. We trim to
    the shield, then emit the three header sizes (1x/2x/3x of a 56px lock-up)
    plus a favicon and an iOS home-screen icon. blason.png itself is never
    loaded by the site — it is the master.
    """
    src = os.path.join(OUT, "blason.png")
    if not os.path.isfile(src):
        print("blason.png not found — skipping logo build")
        return
    import numpy as np
    im = Image.open(src).convert("RGBA")
    a = np.array(im.getchannel("A"))
    ys, xs = np.where(a > 8)
    pad = 4
    sh = im.crop((max(0, xs.min() - pad), max(0, ys.min() - pad),
                  min(im.width, xs.max() + 1 + pad),
                  min(im.height, ys.max() + 1 + pad)))
    for h in (56, 112, 168):
        w = round(sh.width * h / sh.height)
        r = sh.resize((w, h), Image.LANCZOS)
        r.save(os.path.join(OUT, "blason-%d.png" % h))
        r.save(os.path.join(OUT, "blason-%d.avif" % h), quality=72)
    for size, name, bg in ((32, "favicon-32.png", None),
                           (180, "apple-touch-icon.png", (34, 55, 43, 255))):
        c = Image.new("RGBA", (size, size), (0, 0, 0, 0))
        s = sh.copy()
        s.thumbnail((size, size), Image.LANCZOS)
        c.paste(s, ((size - s.width) // 2, (size - s.height) // 2), s)
        if bg:                      # iOS discards alpha — give it loden green
            plate = Image.new("RGBA", (size, size), bg)
            plate.alpha_composite(c)
            c = plate
        c.save(os.path.join(OUT, name))
    print("blason: trimmed to %dx%d, wrote 3 header sizes + 2 icons\n" % sh.size)


def main():
    os.makedirs(OUT, exist_ok=True)
    if not sys.argv[1:]:
        build_blason()

    # `python3 build_images.py floorplan` rebuilds just that one, instead of
    # regenerating all 195 files to change a single image.
    only = set(sys.argv[1:])
    total = 0
    rows = []
    for name, source, aspect, focus, widths in MANIFEST:
        if only and name not in only:
            continue
        im = Image.open(source)
        im = ImageOps.exif_transpose(im).convert("RGB")
        im = crop_to(im, aspect, focus)
        native = im.size[0]
        widths = sorted({min(w, native) for w in widths})
        for w in widths:
            h = int(round(w / aspect))
            r = im.resize((w, h), Image.LANCZOS)
            jp = os.path.join(OUT, f"{name}-{w}.jpg")
            av = os.path.join(OUT, f"{name}-{w}.avif")
            jq, aq = QUALITY.get(name, (80, 58))
            r.save(jp, "JPEG", quality=jq, optimize=True, progressive=True)
            r.save(av, "AVIF", quality=aq, speed=6)
            total += os.path.getsize(jp) + os.path.getsize(av)
        big = widths[-1]
        rows.append((name, aspect, big, int(round(big / aspect)), widths, native))

    print(f"{'name':18s} {'aspect':>7s} {'largest':>11s} {'widths':<24s} source")
    for name, aspect, w, h, widths, native in rows:
        note = "  (source-limited)" if w < max(
            dict((m[0], m[4]) for m in MANIFEST)[name]) else ""
        print(f"{name:18s} {aspect:7.3f} {str(w)+'x'+str(h):>11s} "
              f"{','.join(map(str, widths)):<24s} {native}px{note}")
    print(f"\n{len(rows)} images, {sum(len(r[4]) for r in rows)*2} files, "
          f"{total/1024/1024:.2f} MB total")


if __name__ == "__main__":
    sys.exit(main())
