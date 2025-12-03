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
        # De leesniveaus page - main section page with proper WBM banner
        "url": "https://web.archive.org/web/20180706125126/https://www.lezenvoordelijst.nl/de-leesniveaus",
        "filename": "wbm_pagina_1296.png"  # Replacing the error page screenshot
    }
]

OUTPUT_DIR = "archived-sites/LezenVoorDeLijst/images"

def capture_screenshot(driver, url, output_path):
    """Capture screenshot keeping the WBM banner visible."""
    print(f"Capturing: {url}")
    driver.get(url)
    time.sleep(5)  # Wait for page to load

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
