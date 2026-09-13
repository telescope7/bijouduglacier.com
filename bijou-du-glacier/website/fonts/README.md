# Fonts

**Nothing to do here.** The site now loads its type from **Google Fonts**, which is the
one third-party request on the whole site. Every page head carries:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:…&family=Inter:…&display=swap">
```

| Role | Face | Why |
|---|---|---|
| Headlines, ledes, the wordmark | **Cormorant Garamond** 300/400 | A high-contrast old-style serif — the face luxury hotels have used for twenty years. It is the single biggest reason the page now reads expensive rather than merely large. |
| Body, navigation, buttons, labels | **Inter** 400/500/600 | Neutral, extremely legible at small sizes, and it stays out of the serif's way. |

Both are open-source (SIL Open Font License) and free for commercial use.
`display=swap` means text is never invisible while they load, and `styles.css` falls back
to Georgia and system-ui if Google Fonts is unreachable.

## If you'd rather self-host

Reasonable if you want zero third-party requests (it also removes a GDPR question some
Swiss and EU businesses prefer not to have):

1. Download both families from <https://gwfh.mranftl.com/fonts> — charset **latin**,
   Cormorant Garamond 300 + 400, Inter 400 + 500 + 600.
2. Drop the woff2 files in this folder.
3. In `tools/build_site.py`, delete the three `fonts.googleapis.com` / `preconnect` lines
   from the page template and add `@font-face` rules at the top of `styles.css` pointing at
   `fonts/…woff2`. Re-run `build_site.py`.

The audit will tell you if you break it: it fails any page that has no webfont stylesheet.
