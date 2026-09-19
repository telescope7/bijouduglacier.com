# Fonts

**The type is self-hosted.** The site makes no third-party requests at all.

## One command

The `.woff2` files and `fonts.css` in this folder are generated. If they're
missing, or `audit.py` complains that a font is "not a real font", run:

```bash
cd ../../tools && python3 fetch_fonts.py
```

It downloads from Google Fonts once, writes the files here, and is safe to
re-run — it always overwrites, so a half-finished download can't leave you
stuck.

## What's here and why

| Face | Weights | Role |
|---|---|---|
| **Cormorant Garamond** | 300, 400 | Headlines, ledes, the wordmark. A high-contrast old-style serif — the face luxury hotels have used for twenty years, and the single biggest reason the page reads expensive rather than merely large. |
| **Inter** | 300, 400, 500, 600, 700 | Body, navigation, buttons, labels. Neutral, extremely legible small, stays out of the serif's way. |

Each comes in `latin` and `latin-ext` subsets. The site is EN/FR/DE/IT and
`latin` covers all four; `latin-ext` is a few KB and catches the stray Central
European character. Cyrillic, Greek and Vietnamese are not downloaded. Neither
is italic — the stylesheet never sets `font-style: italic` and no page contains
an `<em>`.

## Why this changed

It used to load from `fonts.googleapis.com`. Three reasons that was worth
fixing:

1. **Two round trips before any text could paint.** A render-blocking
   stylesheet on somebody else's server, which then tells the browser which
   `.woff2` files to go and fetch from a *second* origin.
2. **Every visitor's IP went to Google.** A German court has already ruled that
   unlawful under GDPR (LG München I, 3 O 17493/20), and it's a live question
   under the revised Swiss FADP. This site's audience is almost entirely
   European.
3. **It was the last third-party request on the site.** Removing it means there
   is now no argument that a cookie banner is needed.

Self-hosted files are same-origin, so they pick up the immutable cache header
the rest of the static assets get, and the two faces used above the fold are
preloaded in every page head.

## It also fixed two rendering bugs

The old Google Fonts URL loaded **Inter at 400/500/600 only**, but `styles.css`
uses `font-weight: 300` and `font-weight: 700` as well. Both were being
synthesised by the browser — faux-light and faux-bold, which look visibly wrong
at display sizes. Those weights are now real.

It also stopped loading Cormorant italic, which nothing on the site uses.

## If you change the type

Edit `WANTED` at the top of `tools/fetch_fonts.py`, re-run it, then
`build_site.py` and `audit.py`. If you change which weight is used above the
fold, update the two `preload` lines in `build_site.py` and the matching check
in `audit.py` — both name the files explicitly, and the audit will tell you if
they drift.
