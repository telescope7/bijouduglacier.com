#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bijou du Glacier — hero video build.

Turns the 62 MB camera master into web-deliverable files and extracts the
poster frame.

    python3 build_video.py

Source : ../../Saas-Fee house.mp4   1080x1920, 25fps, 32.06s, 15.8 Mbit/s + AAC
Output : ../website/video/*.mp4     and the poster in ../website/img/

WHAT IT MAKES

  hero-720.mp4        the whole clip, 720x1280      — used on desktop/tablet
  hero-480.mp4        the whole clip, 480x854       — used at <=640px
  hero-clean-720.mp4  2.60s-28.60s, 720x1280        — the same footage with the
  hero-clean-480.mp4  2.60s-28.60s, 480x854           VOLLA marks cut off
  img/hero-poster-*   the frame at 0.40s, 9:16, JPEG + AVIF

WHY THERE IS A "CLEAN" CUT
  The master carries your property manager's branding: the word VOLLA is
  superimposed from roughly 0.9s to 2.4s, and the last three seconds are a
  VOLLA logo animation. That is their mark, not yours, sitting at the top of
  your own homepage. The clean cut drops both ends and keeps 26 of the 32
  seconds. See INSTRUCTIONS.md for the one-line swap.

NO AUDIO
  A hero video has to be muted to autoplay at all, so the audio track is
  dropped rather than shipped and silenced. That alone saves about 1.2 MB.

BLACK FIRST FRAME
  The master opens on two black frames. Because the hero loops, that would
  blink once every 32 seconds, so encoding starts at 0.12s.
"""

import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.abspath(os.path.join(HERE, "..", "..", "Saas-Fee house.mp4"))
VID = os.path.abspath(os.path.join(HERE, "..", "website", "video"))
IMG = os.path.abspath(os.path.join(HERE, "..", "website", "img"))

START = 0.12          # skip the black first frames
CLEAN_IN = 2.60       # after the VOLLA wordmark fades
CLEAN_OUT = 28.60     # before the VOLLA outro begins
POSTER_AT = 0.40      # mountain, no watermark, no black

RENDITIONS = [(720, 1280, 30), (480, 854, 31)]


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        sys.exit("ffmpeg failed:\n" + r.stderr[-2000:])


def encode(w, h, crf, out, start, duration=None):
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-ss", str(start), "-i", SRC]
    if duration:
        cmd += ["-t", str(duration)]
    cmd += [
        "-vf", "scale=%d:%d:flags=lanczos" % (w, h),
        "-an",
        "-c:v", "libx264", "-profile:v", "high", "-level", "4.0",
        "-preset", "slow", "-crf", str(crf), "-pix_fmt", "yuv420p",
        "-g", "50", "-movflags", "+faststart", out,
    ]
    run(cmd)
    return os.path.getsize(out)


def main():
    if not os.path.isfile(SRC):
        sys.exit("Source not found: %s" % SRC)
    os.makedirs(VID, exist_ok=True)
    os.makedirs(IMG, exist_ok=True)

    print("source: %.1f MB\n" % (os.path.getsize(SRC) / 1024 / 1024))
    total = 0
    for w, h, crf in RENDITIONS:
        f = os.path.join(VID, "hero-%d.mp4" % w)
        n = encode(w, h, crf, f, START)
        total += n
        print("  hero-%-3d.mp4        %dx%-5d  %6.2f MB   whole clip" % (w, w, h, n / 1024 / 1024))
    for w, h, crf in RENDITIONS:
        f = os.path.join(VID, "hero-clean-%d.mp4" % w)
        n = encode(w, h, crf, f, CLEAN_IN, CLEAN_OUT - CLEAN_IN)
        print("  hero-clean-%-3d.mp4  %dx%-5d  %6.2f MB   VOLLA marks removed"
              % (w, w, h, n / 1024 / 1024))

    # ---- poster ----------------------------------------------------------
    tmp = os.path.join(VID, "_poster_full.png")
    run(["ffmpeg", "-y", "-loglevel", "error", "-ss", str(POSTER_AT),
         "-i", SRC, "-frames:v", "1", tmp])
    from PIL import Image
    im = Image.open(tmp).convert("RGB")
    for w in (480, 720):
        h = int(round(w * 16 / 9))
        r = im.resize((w, h), Image.LANCZOS)
        r.save(os.path.join(IMG, "hero-poster-%d.jpg" % w),
               "JPEG", quality=80, optimize=True, progressive=True)
        r.save(os.path.join(IMG, "hero-poster-%d.avif" % w), "AVIF", quality=58, speed=6)
    os.remove(tmp)
    print("\n  img/hero-poster-480|720.{jpg,avif}   frame at %.2fs" % POSTER_AT)
    print("\nthe two files the page actually loads total %.2f MB "
          "(down from %.1f MB)" % (total / 1024 / 1024, os.path.getsize(SRC) / 1024 / 1024))


if __name__ == "__main__":
    sys.exit(main())
