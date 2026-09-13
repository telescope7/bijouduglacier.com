#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bijou du Glacier — put edited copy back into the site.

    python3 apply_copy.py                 # apply every copy/copy-*.md
    python3 apply_copy.py ../copy/copy-en.md
    python3 apply_copy.py --dry-run       # show what would change, touch nothing

Reads the numbered .md files, compares each block against what is currently in
content_*.py, and splices in only the ones you actually changed. Then run:

    python3 build_site.py && python3 audit.py

SAFETY
  * It refuses to run if a content_*.py file has been edited by hand since
    extract_copy.py produced the map — the byte offsets would no longer line up
    and it would corrupt the file. Re-run extract_copy.py and start again.
  * It writes a .bak of every file it touches.
  * Edits are applied back-to-front so an earlier splice cannot shift a later
    offset.
  * A missing or unchanged block means "leave it alone". Deleting a block from
    the .md is not a way to delete text from the site.
"""

import hashlib
import json
import os
import re
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
COPY = os.path.abspath(os.path.join(HERE, "..", "copy"))
MAP = os.path.join(COPY, "_copy_map.json")

MARKER = re.compile(r"^\[([A-Z]{2}-\d{3})\]\s*(.*)$")


def read_blocks(path):
    """{'EN-001': 'the text'} from an edited copy file."""
    blocks, ident, buf = {}, None, []
    for line in open(path, encoding="utf-8").read().splitlines():
        m = MARKER.match(line.strip())
        if m:
            if ident:
                blocks[ident] = "\n".join(buf).strip()
            ident, buf = m.group(1), []
        elif ident is not None:
            if line.startswith("=====") or line.strip().isupper() and len(line.strip()) > 20:
                blocks[ident] = "\n".join(buf).strip()
                ident, buf = None, []
            else:
                buf.append(line)
    if ident:
        blocks[ident] = "\n".join(buf).strip()
    return {k: v for k, v in blocks.items() if v}


def escape_for(quote, text):
    """Make `text` safe inside a Python literal delimited by `quote`."""
    text = text.replace("\\", "\\\\")
    if quote == '"':
        return text.replace('"', '\\"')
    if quote == "'":
        return text.replace("'", "\\'")
    if quote == '"""':
        # inside a triple-quoted blob only a literal """ or a trailing \ hurts
        return text.replace('"""', '\\"\\"\\"')
    return text.replace("'''", "\\'\\'\\'")


def main(argv):
    dry = "--dry-run" in argv
    files = [a for a in argv if a.endswith(".md")]
    if not files:
        files = sorted(f for f in
                       (os.path.join(COPY, x) for x in os.listdir(COPY))
                       if f.endswith(".md"))
    if not os.path.isfile(MAP):
        sys.exit("copy/_copy_map.json is missing — run extract_copy.py first.")
    m = json.load(open(MAP, encoding="utf-8"))

    # ---- refuse to work from a stale map --------------------------------
    sources = {}
    for lang, info in m["files"].items():
        p = os.path.abspath(os.path.join(COPY, "..", info["path"]))
        raw = open(p, "rb").read()
        if hashlib.sha256(raw).hexdigest() != info["sha256"]:
            sys.exit(
                "%s has changed since the copy file was produced.\n"
                "The character offsets no longer line up, so applying edits now\n"
                "would corrupt it. Re-run extract_copy.py, re-do your edits on\n"
                "the fresh file, then run this again." % os.path.basename(p))
        sources[lang] = (p, raw)

    edits = {}                      # lang -> [(start, end, quote, new, ident)]
    unchanged = skipped = 0
    for f in files:
        for ident, new in read_blocks(f).items():
            item = m["items"].get(ident)
            if not item:
                print("  ?  %s is not a known marker — ignored" % ident)
                skipped += 1
                continue
            lang = item["lang"]
            _p, raw = sources[lang]
            old = raw[item["start"]:item["end"]].decode("utf-8")
            if new == old.strip():
                unchanged += 1
                continue
            edits.setdefault(lang, []).append(
                (item["start"], item["end"], item["quote"], new, ident, old.strip()))

    if not edits:
        print("No changes found. (%d blocks read, all identical.)" % unchanged)
        return 0

    total = 0
    for lang, items in sorted(edits.items()):
        p, raw = sources[lang]
        print("\n%s — %d change%s" % (os.path.basename(p), len(items),
                                      "" if len(items) == 1 else "s"))
        for _s, _e, _q, new, ident, old in sorted(items):
            print("  %s" % ident)
            print("    was: %s" % (old[:96] + ("…" if len(old) > 96 else "")))
            print("    now: %s" % (new[:96] + ("…" if len(new) > 96 else "")))
        if dry:
            total += len(items)
            continue
        shutil.copy2(p, p + ".bak")
        out = raw
        for start, end, quote, new, _ident, _old in sorted(items, reverse=True):
            out = out[:start] + escape_for(quote, new).encode("utf-8") + out[end:]
        open(p, "wb").write(out)
        # prove we did not break the file
        try:
            compile(out.decode("utf-8"), p, "exec")
        except SyntaxError as e:
            shutil.copy2(p + ".bak", p)
            sys.exit("Applying to %s produced invalid Python (%s).\n"
                     "The file has been restored from its .bak — nothing lost."
                     % (os.path.basename(p), e))
        total += len(items)

    print("\n%d change%s %s, %d unchanged%s."
          % (total, "" if total == 1 else "s",
             "would be applied" if dry else "applied",
             unchanged, ", %d unrecognised" % skipped if skipped else ""))
    if not dry:
        print("\nNow run:  python3 build_site.py && python3 audit.py")
        print("Then re-run extract_copy.py to refresh the numbered files.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
