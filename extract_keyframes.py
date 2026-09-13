#!/usr/bin/env python3
"""
Video Keyframe Extractor (Memory-Efficient)
Extracts key frames from MP4 videos intelligently based on scene changes.
Suitable for high-resolution digital marketing use.
"""

import cv2
import numpy as np
import os
import sys
from pathlib import Path


def calculate_frame_difference(frame1, frame2):
    """Calculate the difference between two frames using histogram comparison."""
    # Convert to grayscale
    gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    # Calculate histograms
    hist1 = cv2.calcHist([gray1], [0], None, [256], [0, 256])
    hist2 = cv2.calcHist([gray2], [0], None, [256], [0, 256])

    # Normalize histograms
    hist1 = cv2.normalize(hist1, hist1).flatten()
    hist2 = cv2.normalize(hist2, hist2).flatten()

    # Compare histograms using Bhattacharyya distance
    return cv2.compareHist(hist1, hist2, cv2.HISTCMP_BHATTACHARYYA)


def extract_keyframes(video_path, num_frames=35, output_dir="extract", quality=95):
    """
    Extract keyframes from a video file (memory-efficient streaming version).

    Args:
        video_path: Path to input MP4 video
        num_frames: Number of keyframes to extract (default: 35)
        output_dir: Directory to save extracted frames
        quality: JPEG quality (1-100, default: 95 for high quality)

    Returns:
        List of saved frame paths
    """

    # Validate input
    if not os.path.exists(video_path):
        print(f"Error: Video file not found: {video_path}")
        return []

    # Create output directory
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    print(f"Opening video: {video_path}")
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video file")
        return []

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    print(f"Video info: {total_frames} frames, {fps:.2f} fps, {width}x{height}")
    print(f"Duration: {total_frames/fps:.2f} seconds")
    print(f"Extracting {num_frames} keyframes...")

    # First pass: analyze frame differences and identify keyframes
    frame_diffs = []
    frame_metadata = []  # Store (frame_index, difference) for selection
    frame_count = 0

    ret, prev_frame = cap.read()
    if not ret:
        print("Error: Could not read first frame")
        cap.release()
        return []

    frame_diffs.append(0)  # First frame has no previous frame
    frame_metadata.append((0, 0))
    frame_count = 1

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Calculate difference from previous frame
        diff = calculate_frame_difference(prev_frame, frame)
        frame_diffs.append(diff)
        frame_metadata.append((frame_count, diff))
        prev_frame = frame
        frame_count += 1

        # Print progress
        if frame_count % 100 == 0:
            print(f"  Analyzed {frame_count}/{total_frames} frames...", end='\r')

    print(f"\nAnalyzed {frame_count} frames")

    # Select keyframes based on differences
    if len(frame_metadata) <= num_frames:
        # If fewer frames than requested, use all
        keyframe_indices = [idx for idx, _ in frame_metadata]
        print(f"Video has fewer frames than requested. Using all {len(keyframe_indices)} frames.")
    else:
        # Use a combination of strategies:
        # 1. Always include first and last frame
        # 2. Include frames with highest differences (scene changes)
        # 3. Fill remaining slots with evenly distributed frames

        keyframe_indices = set()
        keyframe_indices.add(0)  # First frame
        keyframe_indices.add(len(frame_metadata) - 1)  # Last frame

        # Find frames with largest differences
        sorted_by_diff = sorted(
            frame_metadata,
            key=lambda x: x[1],
            reverse=True
        )

        # Add top difference frames
        for frame_idx, _ in sorted_by_diff:
            keyframe_indices.add(frame_idx)
            if len(keyframe_indices) >= num_frames:
                break

        # If still not enough, add evenly spaced frames
        if len(keyframe_indices) < num_frames:
            spacing = len(frame_metadata) // (num_frames - len(keyframe_indices) + 1)
            for i in range(spacing, len(frame_metadata), spacing):
                keyframe_indices.add(i)
                if len(keyframe_indices) >= num_frames:
                    break

        keyframe_indices = sorted(list(keyframe_indices))[:num_frames]

    cap.release()

    # Second pass: Extract and save selected frames
    print(f"\nExtracting {len(keyframe_indices)} keyframes...")
    cap = cv2.VideoCapture(video_path)

    saved_paths = []
    keyframe_set = set(keyframe_indices)
    current_frame_idx = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if current_frame_idx in keyframe_set:
            # Create filename with sequence number
            sequence_num = keyframe_indices.index(current_frame_idx) + 1
            filename = f"keyframe_{sequence_num:03d}.jpg"
            filepath = output_path / filename

            # Save with high quality
            success = cv2.imwrite(
                str(filepath),
                frame,
                [cv2.IMWRITE_JPEG_QUALITY, quality]
            )

            if success:
                saved_paths.append(str(filepath))
                time_code = current_frame_idx / fps
                minutes = int(time_code // 60)
                seconds = time_code % 60
                diff = frame_diffs[current_frame_idx] if current_frame_idx < len(frame_diffs) else 0
                print(f"  {sequence_num:2d}. {filename} (frame {current_frame_idx}, {minutes}:{seconds:05.2f}, diff: {diff:.3f})")
            else:
                print(f"  Error saving {filename}")

        current_frame_idx += 1

    cap.release()

    print(f"\n✓ Successfully extracted {len(saved_paths)} keyframes")
    print(f"  Location: {output_path.absolute()}")
    print(f"  Resolution: {width}x{height}")
    print(f"  Quality: {quality}%")

    return saved_paths


def main():
    """Command-line interface for keyframe extraction."""

    # Default values
    video_path = "Saas-Fee house.mp4"  # Will look for this in current directory
    num_frames = 35
    output_dir = "extract"
    quality = 95

    # Parse command-line arguments
    if len(sys.argv) > 1:
        video_path = sys.argv[1]
    if len(sys.argv) > 2:
        try:
            num_frames = int(sys.argv[2])
        except ValueError:
            print(f"Invalid number of frames: {sys.argv[2]}")
            sys.exit(1)
    if len(sys.argv) > 3:
        output_dir = sys.argv[3]
    if len(sys.argv) > 4:
        try:
            quality = int(sys.argv[4])
            quality = max(1, min(100, quality))  # Clamp to 1-100
        except ValueError:
            print(f"Invalid quality: {sys.argv[4]}")
            sys.exit(1)

    # Check if video exists, search in common locations
    if not os.path.exists(video_path):
        # Try current directory and parent
        possible_paths = [
            video_path,
            os.path.join(".", video_path),
            os.path.join("..", video_path),
        ]
        found = False
        for path in possible_paths:
            if os.path.exists(path):
                video_path = path
                found = True
                break
        if not found:
            print(f"Usage: python extract_keyframes.py [video_path] [num_frames] [output_dir] [quality]")
            print(f"\nExample:")
            print(f"  python extract_keyframes.py video.mp4 40 extracted_frames 95")
            print(f"\nDefault: python extract_keyframes.py")
            print(f"  Uses: '{video_path}' -> {num_frames} frames -> '{output_dir}/' (quality: {quality}%)")
            print(f"\nArguments:")
            print(f"  video_path  - Path to MP4 video file")
            print(f"  num_frames  - Number of keyframes to extract (1-1000, default 35)")
            print(f"  output_dir  - Output directory name (default 'extract')")
            print(f"  quality     - JPEG quality 1-100 (default 95 for high quality)")
            sys.exit(1)

    # Extract keyframes
    extract_keyframes(video_path, num_frames, output_dir, quality)


if __name__ == "__main__":
    main()
