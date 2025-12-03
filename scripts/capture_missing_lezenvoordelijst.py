#!/usr/bin/env python3
"""Capture replacement screenshot for LezenVoorDeLijst (replace error page)."""

import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image
from io import BytesIO

# Screenshot to capture - replacing error page with a working page
SCREENSHOTS = [
    {
        # Blog post about docenten lezen in de klas - a working archived page with content
        "url": "https://web.archive.org/web/20180706115322/https://www.lezenvoordelijst.nl/blog/2012/docenten-lezen-in-de-klas/",
        "filename": "wbm_pagina_1296.png"  # Replacing the error page screenshot
    }
]

OUTPUT_DIR = "archived-sites/LezenVoorDeLijst/images"
BANNER_HEIGHT = 210  # WBM donation banner height to trim

def capture_screenshot(driver, url, output_path):
    """Capture screenshot and trim donation banner."""
    print(f"Capturing: {url}")
    driver.get(url)
    time.sleep(5)  # Wait for page to load

    # Take screenshot
    screenshot = driver.get_screenshot_as_png()
    img = Image.open(BytesIO(screenshot))

    # Trim donation banner from top
    width, height = img.size
    if height > BANNER_HEIGHT:
        img = img.crop((0, BANNER_HEIGHT, width, height))

    img.save(output_path)
    print(f"Saved: {output_path}")

def main():
    # Setup Chrome
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)

    try:
        for screenshot in SCREENSHOTS:
            output_path = os.path.join(OUTPUT_DIR, screenshot["filename"])
            capture_screenshot(driver, screenshot["url"], output_path)
            time.sleep(2)
    finally:
        driver.quit()

    print("Done!")

if __name__ == "__main__":
    main()
