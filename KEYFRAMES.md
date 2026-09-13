# Video Keyframe Extractor

Extract high-resolution keyframes from MP4 videos for digital marketing use.
This is the utility that produced `media files combined/extract/`, the stills
the site's hero mosaic and gallery draw on.

> **Note on this file.** The original README for this tool was at the top level
> of the repository and was overwritten when the repository README was written.
> What follows is reconstructed from the script itself, so it is accurate about
> behaviour but is not the original wording.

## Features

- **Intelligent frame selection** — compares consecutive frames by grayscale
  histogram (Bhattacharyya distance) to find genuine scene changes rather than
  sampling at fixed intervals
- **Memory efficient** — streams the video rather than loading it into memory,
  so a 62 MB source is no harder than a small one
- **High quality output** — 95% JPEG by default, suitable for web and print
- **Variable extraction** — any number of frames
- **Timestamp tracking** — reports the timecode of each frame it keeps

## Installation

Requires Python 3.6+ with OpenCV:

```bash
pip install opencv-python numpy
```

## Usage

Arguments are positional, all optional after the video path:

```bash
python3 extract_keyframes.py VIDEO [NUM_FRAMES] [OUTPUT_DIR] [QUALITY]
```

| Argument | Default | Meaning |
|----------|---------|---------|
| `VIDEO` | — | path to the input MP4 |
| `NUM_FRAMES` | `35` | how many keyframes to keep |
| `OUTPUT_DIR` | `extract` | where to write them |
| `QUALITY` | `95` | JPEG quality, 1–100 |

For example, the 35 stills in this repository came from:

```bash
python3 extract_keyframes.py "Saas-Fee house.mp4" 35 extract 95
```

Frames are written as `keyframe_001.jpg`, `keyframe_002.jpg` and so on, which
is the naming `bijou-du-glacier/tools/build_images.py` expects when it refers to
them via its `kf()` helper.
