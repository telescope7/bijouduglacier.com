#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bijou du Glacier — pull every editable piece of text out into a numbered file.

    python3 extract_copy.py

Writes ../copy/copy-en.md (and -fr, -de, -it) plus ../copy/_copy_map.json.

Edit the .md, keep the [EN-001] markers exactly as they are, then run
apply_copy.py to put the changes back.

HOW IT FINDS THE TEXT
  It parses the content_*.py files with Python's own `ast` module, so it knows
  the exact character offset of every string literal rather than guessing with
  search-and-replace. Text inside the page bodies (which are HTML) is located a
  second time by regex within the body blob, and the offsets are added together.
  apply_copy.py then splices by offset, working backwards through the file so
  earlier edits cannot shift later ones.

WHAT IT SKIPS
  Anything that does not appear in the built site. Several strings are left over
  from earlier versions (the "Continue" cards, the old footer disclaimer); they
  are checked against website/**/*.html and dropped if unused, so the file you
  edit only contains text a visitor can actually read.
"""

import ast
import glob
import hashlib
import html as htmllib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
WEB = os.path.abspath(os.path.join(HERE, "..", "website"))
OUT = os.path.abspath(os.path.join(HERE, "..", "copy"))

LANGS = [("en", "English"), ("fr", "Français"), ("de", "Deutsch"), ("it", "Italiano")]

PAGE_TITLES = {
    "home": "Homepage",
    "apartment": "Page: the apartment",
    "resort": "Page: Saas-Fee",
    "book": "Page: booking",
}

# Friendly names for the keys, so the file reads like a document rather than code.
UI_LABELS = {
    "brand_sub": "Strapline under the logo, top left",
    "book_cta": "Long booking button",
    "book_cta_short": "Short booking button (header bar)",
    "note": "Sentence inside the dark Reserve panel",
    "book_block_title": "Heading inside the dark Reserve panel",
    "gallery_note": "(unused)",
    "next_label": "(unused)",
    "skip": "Hidden 'skip to content' link (keyboard users)",
    "home_label": "Breadcrumb: name for the homepage",
    "lang_label": "Screen-reader label for the language switcher",
    "jump_label": "Screen-reader label for the section links",
    "nav_label": "Screen-reader label for the main navigation",
    "crumb_label": "Screen-reader label for the breadcrumb",
}
A11Y = {"skip", "lang_label", "jump_label", "nav_label", "crumb_label"}

BLOCK_RE = re.compile(
    r"<(h2|h3|p|caption|th|td|summary)\b[^>]*>(.*?)</\1>", re.S)


def literal_spans(path):
    """{('a','b',0): (start, end, quote)} for every string literal in the file.

    All offsets are BYTE offsets into the UTF-8 source, and that is not a
    detail: ast reports col_offset in bytes, not characters. On any line with an
    em dash or a middle dot in it, a character-based index silently slides right
    and you capture the closing quote along with the text. Line index, slicing
    and the offsets written to the map all stay in bytes.
    """
    raw = open(path, "rb").read()
    starts, n = [0], 0
    for line in raw.splitlines(keepends=True):
        n += len(line)
        starts.append(n)

    def abs_off(lineno, col):
        return starts[lineno - 1] + col

    tree = ast.parse(raw.decode("utf-8"))
    out = {}

    def walk(node, path_):
        if isinstance(node, ast.Dict):
            for k, v in zip(node.keys, node.values):
                key = k.value if isinstance(k, ast.Constant) else "?"
                walk(v, path_ + (key,))
        elif isinstance(node, (ast.List, ast.Tuple)):
            for i, el in enumerate(node.elts):
                walk(el, path_ + (i,))
        elif isinstance(node, ast.Constant) and isinstance(node.value, str):
            s = abs_off(node.lineno, node.col_offset)
            e = abs_off(node.end_lineno, node.end_col_offset)
            lit = raw[s:e]
            for q in (b'"""', b"'''", b'"', b"'"):
                if lit.startswith(q):
                    out[path_] = (s + len(q), e - len(q), q.decode())
                    break
    for stmt in tree.body:
        if isinstance(stmt, ast.Assign):
            walk(stmt.value, ())
    return raw, out


def used_in_site(text):
    """Is this string actually rendered anywhere in the built site?"""
    needle = htmllib.escape(text.strip(), quote=True)[:70]
    if not needle:
        return False
    return any(needle in blob for blob in used_in_site.blobs)


used_in_site.blobs = []


def main():
    os.makedirs(OUT, exist_ok=True)
    used_in_site.blobs = [open(p, encoding="utf-8").read()
                          for p in glob.glob(os.path.join(WEB, "**", "*.html"),
                                             recursive=True)]
    themap = {"files": {}, "items": {}}

    for code, name in LANGS:
        f = os.path.join(HERE, "content_%s.py" % code)
        raw, spans = literal_spans(f)
        themap["files"][code] = {
            "path": os.path.relpath(f, os.path.dirname(OUT)),
            "sha256": hashlib.sha256(raw).hexdigest(),
        }
        prefix = code.upper()
        n = [0]
        lines = []
        items = []

        def emit(label, key, start, end, quote, note=""):
            text = raw[start:end].decode("utf-8")
            if not text.strip():
                return
            n[0] += 1
            ident = "%s-%03d" % (prefix, n[0])
            items.append((ident, start, end, quote))
            lines.append("[%s]  %s%s\n%s\n" % (ident, label, note, text.strip()))

        def add(pathkey, label, note=""):
            if pathkey in spans:
                s, e, q = spans[pathkey]
                emit(label, pathkey, s, e, q, note)

        def heading(t):
            lines.append("\n\n" + "=" * 74 + "\n%s\n" % t + "=" * 74 + "\n")

        # ---- chrome ---------------------------------------------------
        heading("HEADER, BUTTONS AND SHARED LABELS")
        add(("ui", "brand_sub"), UI_LABELS["brand_sub"])
        for k in ("home", "apartment", "resort", "book"):
            add(("nav", k), "Navigation link")
        for k in ("book_cta_short", "book_cta", "book_block_title", "note"):
            if UI_LABELS.get(k, "").startswith("(unused"):
                continue
            add(("ui", k), UI_LABELS[k])

        # ---- pages ----------------------------------------------------
        for page in ("home", "apartment", "resort", "book"):
            heading(PAGE_TITLES[page].upper())
            add(("pages", page, "h1"), "Main headline")
            add(("pages", page, "lede"), "Sentence under the headline")
            if page == "home":
                for i in range(8):
                    add(("pages", page, "facts", i), "Specification line, item %d" % (i + 1))
            for i in range(10):
                add(("pages", page, "jump", i, 1), "Section link")
            # body: every block element, in the order it appears on the page
            bk = ("pages", page, "body")
            if bk in spans:
                bs, be, bq = spans[bk]
                body = raw[bs:be].decode("utf-8")

                def bo(off, _body=body, _bs=bs):
                    """regex offsets are in characters — convert back to bytes"""
                    return _bs + len(_body[:off].encode("utf-8"))

                for m in BLOCK_RE.finditer(body):
                    tag, inner = m.group(1), m.group(2)
                    if "{{" in inner or not inner.strip():
                        continue
                    label = {"h2": "Section heading", "h3": "Sub-heading",
                             "p": "Paragraph", "caption": "Table caption",
                             "th": "Table row label", "td": "Table row value",
                             "summary": "Question"}[tag]
                    emit(label, bk, bo(m.start(2)), bo(m.end(2)), bq)

        # ---- shared blocks --------------------------------------------
        heading("QUESTIONS AND ANSWERS  (shown on the homepage)")
        for i in range(12):
            add(("faq", i, 0), "Question")
            add(("faq", i, 1), "Answer")

        heading("WHAT'S INCLUDED  (list on the apartment page)")
        for i in range(30):
            add(("amenities", i), "Item %d" % (i + 1))

        heading("THE PARTICULARS  (table on the apartment page)")
        add(("facts_table", "caption"), "Caption above the table")
        for i in range(15):
            add(("facts_table", "rows", i, 0), "Row label")
            add(("facts_table", "rows", i, 1), "Row value")

        heading("FOOTER")
        for k, lab in (("address", "Address line"), ("explore", "Column heading"),
                       ("book", "Column heading")):
            add(("footer", k), lab)

        heading("SEARCH-ENGINE TEXT  (never shown on the page itself)")
        for page in ("home", "apartment", "resort", "book"):
            add(("pages", page, "title"), "%s — browser tab and Google result title"
                % PAGE_TITLES[page])
            add(("pages", page, "desc"), "%s — Google result description"
                % PAGE_TITLES[page])

        heading("IMAGE DESCRIPTIONS  (read aloud by screen readers, and by Google)")
        for k in sorted(set(p[1] for p in spans if p and p[0] == "alt")):
            add(("alt", k), "Photograph: %s" % k)
        heading("PHOTO CAPTIONS  (printed under the gallery images)")
        for k in sorted(set(p[1] for p in spans if p and p[0] == "caption")):
            add(("caption", k), "Caption: %s" % k)

        heading("ACCESSIBILITY LABELS  (invisible; only screen readers hear them)")
        for k in sorted(A11Y):
            add(("ui", k), UI_LABELS[k])

        for ident, s, e, q in items:
            themap["items"][ident] = {"lang": code, "start": s, "end": e, "quote": q}

        header = """# Bijou du Glacier — %s copy

Every piece of text on the site, numbered. **Edit the words, not the numbers.**

HOW TO USE THIS FILE
  1. Change any line of text you like, underneath its `[%s-001]` marker.
  2. Leave the markers exactly as they are — they are how the text finds its
     way back into the right place.
  3. Delete nothing. If you want a line gone, say so separately; removing it
     here just means "no change".
  4. Send the file back and it gets spliced in, then the site is rebuilt and
     re-checked.

A FEW THINGS TO KNOW
  * `<a href="{apartment}">…</a>` is a link. Keep the tags around the words you
    want to be clickable; change the words freely.
  * `—` is an em dash. `·` is a middle dot. Both are deliberate.
  * The last four sections are text nobody sees on the page — Google results,
    image descriptions for blind visitors, and screen-reader labels. They still
    matter, but change them last.

%d editable pieces of text.

""" % (name, prefix, n[0])

        p = os.path.join(OUT, "copy-%s.md" % code)
        open(p, "w", encoding="utf-8").write(header + "\n".join(lines) + "\n")
        print("  %-28s %3d pieces of text" % (os.path.relpath(p, os.path.dirname(OUT)), n[0]))

    with open(os.path.join(OUT, "_copy_map.json"), "w", encoding="utf-8") as fh:
        json.dump(themap, fh, indent=1)
    print("\n  copy/_copy_map.json written — do not edit or delete it,\n"
          "  apply_copy.py needs it to know where each number belongs.")


if __name__ == "__main__":
    sys.exit(main())
