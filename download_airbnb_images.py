#!/usr/bin/env python3
"""
Airbnb Image Downloader
Downloads highest-resolution images from Airbnb listings.
"""

import os
import sys
import json
import re
from pathlib import Path
from urllib.parse import urlparse, parse_qs
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Try to import Playwright for JavaScript rendering
try:
    import asyncio
    from playwright.async_api import async_playwright
    HAS_PLAYWRIGHT = True
except ImportError:
    HAS_PLAYWRIGHT = False
    print("Note: Playwright not installed. Using fallback method.")


def create_session():
    """Create a requests session with retries."""
    session = requests.Session()
    retry = Retry(
        total=3,
        backoff_factor=0.5,
        status_forcelist=(500, 502, 504)
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
    })
    return session


def extract_images_from_html(html_content):
    """Extract image URLs from HTML content using regex."""
    images = set()

    # Look for image URLs in the HTML
    # Airbnb uses data: attributes and src attributes
    patterns = [
        r'"url":"([^"]*?\.(?:jpg|jpeg|png|webp)[^"]*?)"',
        r"'url':'([^']*?\.(?:jpg|jpeg|png|webp)[^']*?)'",
        r'src=["\']([^"\']*?\.(?:jpg|jpeg|png|webp)[^"\']*?)["\']',
        r'data-src=["\']([^"\']*?\.(?:jpg|jpeg|png|webp)[^"\']*?)["\']',
        r'background-image:\s*url\(["\']?([^"\']*?\.(?:jpg|jpeg|png|webp)[^"\']*?)["\']?\)',
    ]

    for pattern in patterns:
        matches = re.findall(pattern, html_content, re.IGNORECASE)
        images.update(matches)

    # Also look for JSON data embedded in the page
    json_pattern = r'<script[^>]*type="application/json"[^>]*>(.*?)</script>'
    json_matches = re.findall(json_pattern, html_content, re.DOTALL)

    for json_str in json_matches:
        try:
            data = json.loads(json_str)
            # Recursively search for image URLs in JSON
            images.update(extract_images_from_json(data))
        except:
            pass

    return images


def extract_images_from_json(obj):
    """Recursively extract image URLs from JSON objects."""
    images = set()

    if isinstance(obj, dict):
        for key, value in obj.items():
            if key in ['url', 'src', 'pictureUrl', 'photoUrl', 'image']:
                if isinstance(value, str) and any(ext in value.lower() for ext in ['.jpg', '.jpeg', '.png', '.webp']):
                    images.add(value)
            else:
                images.update(extract_images_from_json(value))
    elif isinstance(obj, list):
        for item in obj:
            images.update(extract_images_from_json(item))

    return images


def get_highest_resolution_url(url):
    """
    Convert Airbnb image URL to highest resolution.
    Airbnb uses URL parameters for different sizes.
    """
    if not url:
        return url

    # Airbnb image URLs often have 'w=XXX' or 'h=XXX' parameters
    # We want the largest available

    # Remove or set width/height to large values
    url = re.sub(r'[?&]w=\d+', '', url)
    url = re.sub(r'[?&]h=\d+', '', url)
    url = re.sub(r'[?&]s=\d+', '', url)

    # Add max size parameters
    separator = '&' if '?' in url else '?'
    url = f"{url}{separator}w=1080&h=1440"

    return url


async def download_with_playwright(url, output_dir):
    """Download images using Playwright to render JavaScript."""
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        print(f"Loading page: {url}")
        await page.goto(url, wait_until='networkidle')

        # Get page content
        content = await page.content()

        # Extract images
        images = extract_images_from_html(content)

        # Also try to get images from the page's image elements
        image_elements = await page.query_selector_all('img')
        for img in image_elements:
            src = await img.get_attribute('src')
            if src:
                images.add(src)

        await browser.close()

        return download_images(images, output_dir)


def download_with_requests(url, output_dir):
    """Download images using requests (fallback method)."""
    session = create_session()

    print(f"Fetching page: {url}")
    try:
        response = session.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching page: {e}")
        return []

    # Extract images from HTML
    images = extract_images_from_html(response.text)

    return download_images(images, output_dir, session)


def download_images(image_urls, output_dir, session=None):
    """Download images from URLs."""
    if session is None:
        session = create_session()

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # Filter and convert URLs to highest resolution
    images = set()
    for img_url in image_urls:
        if img_url and ('http' in img_url or img_url.startswith('/')):
            # Skip very small images or icons
            if any(x in img_url.lower() for x in ['icon', 'avatar', 'logo', '_xs', '_sm']):
                continue

            # Convert to absolute URL if needed
            if img_url.startswith('/'):
                img_url = 'https://a0.muscache.com' + img_url
            elif not img_url.startswith('http'):
                img_url = 'https://' + img_url

            # Get highest resolution version
            img_url = get_highest_resolution_url(img_url)
            images.add(img_url)

    print(f"Found {len(images)} unique images")

    downloaded = []
    for idx, img_url in enumerate(images, 1):
        try:
            print(f"  [{idx}/{len(images)}] Downloading: {img_url[:80]}...")

            response = session.get(img_url, timeout=10)
            response.raise_for_status()

            # Get filename from URL
            parsed = urlparse(img_url)
            filename = os.path.basename(parsed.path)
            if not filename or '.' not in filename:
                # Use index if no proper filename
                filename = f"image_{idx:03d}.jpg"

            filepath = output_path / filename

            with open(filepath, 'wb') as f:
                f.write(response.content)

            downloaded.append(str(filepath))
            print(f"      ✓ Saved: {filename} ({len(response.content) / 1024 / 1024:.2f} MB)")

        except requests.RequestException as e:
            print(f"      ✗ Error downloading: {e}")
        except Exception as e:
            print(f"      ✗ Error saving: {e}")

    return downloaded


def main():
    """Main function."""
    if len(sys.argv) < 2:
        print("Usage: python download_airbnb_images.py <airbnb_url> [output_dir]")
        print("\nExample:")
        print("  python download_airbnb_images.py 'https://www.airbnb.com/rooms/1234567890' Airbnb")
        sys.exit(1)

    url = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "Airbnb"

    # Validate URL
    if 'airbnb.com' not in url:
        print("Error: Please provide a valid Airbnb URL")
        sys.exit(1)

    print(f"Downloading images from: {url}")
    print(f"Output directory: {output_dir}")
    print()

    try:
        # Try Playwright first (better for JavaScript-heavy pages)
        if HAS_PLAYWRIGHT:
            print("Using Playwright for JavaScript rendering...")
            downloaded = asyncio.run(download_with_playwright(url, output_dir))
        else:
            print("Using requests fallback method...")
            downloaded = download_with_requests(url, output_dir)

        print(f"\n✓ Successfully downloaded {len(downloaded)} images")
        print(f"  Location: {Path(output_dir).absolute()}")

    except KeyboardInterrupt:
        print("\nDownload cancelled by user")
        sys.exit(0)
    except Exception as e:
        print(f"\nError: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
