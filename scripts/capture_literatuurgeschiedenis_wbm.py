#!/usr/bin/env python3
"""Capture Literatuurgeschiedenis.org screenshots from Wayback Machine with proper banners."""

import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image
from io import BytesIO

# Verified Wayback Machine URLs for Literatuurgeschiedenis.org
SCREENSHOTS = [
    {
        "url": "https://web.archive.org/web/20220325125436/https://www.literatuurgeschiedenis.org/",
        "filename": "wbm_homepage.png"
    },
    {
        "url": "https://web.archive.org/web/20220325125250/https://www.literatuurgeschiedenis.org/17e-eeuw",
        "filename": "wbm_17e_eeuw.png"
    },
    {
        "url": "https://web.archive.org/web/20220325125306/https://www.literatuurgeschiedenis.org/18e-eeuw",
        "filename": "wbm_18e_eeuw.png"
    },
    {
        "url": "https://web.archive.org/web/20220325144122/https://www.literatuurgeschiedenis.org/16e-eeuw/de-drukpers-als-wapen",
        "filename": "wbm_drukpers_als_wapen.png"
    },
    {
        "url": "https://web.archive.org/web/20220325164314/https://www.literatuurgeschiedenis.org/17e-eeuw/gouden-tijden",
        "filename": "wbm_gouden_tijden.png"
    }
]

OUTPUT_DIR = "archived-sites/Literaruurgeschiedenis.org/images"

def capture_screenshot(driver, url, output_path):
    """Capture screenshot keeping the WBM banner visible."""
    print(f"Capturing: {url}")
    driver.get(url)
    time.sleep(5)  # Wait for page to load fully

    # Take screenshot - keep full page with WBM banner
    screenshot = driver.get_screenshot_as_png()
    img = Image.open(BytesIO(screenshot))
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
