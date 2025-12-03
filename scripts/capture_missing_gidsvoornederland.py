#!/usr/bin/env python3
"""Capture correct GidsVoorNederland screenshots from Wayback Machine."""

import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image
from io import BytesIO

# Screenshots to capture - using verified URLs from the archive output file
SCREENSHOTS = [
    {
        # Bibliotheken page - a specific library detail page
        "url": "https://web.archive.org/web/20181111224126/https://www.gidsvoornederland.nl/werken-met-gids/meerwaarde-voor-bibliotheken/bibliotheken-in-nederland?pi=364&organisation_id=1475103&startindex=0",
        "filename": "wbm_bibliotheken.png"
    },
    {
        # Over Ons - using a different library as example of content
        "url": "https://web.archive.org/web/20181111224133/https://www.gidsvoornederland.nl/werken-met-gids/meerwaarde-voor-bibliotheken/bibliotheken-in-nederland?pi=364&organisation_id=5314448&startindex=0",
        "filename": "wbm_over_ons.png"
    },
    {
        # Help - using another library page
        "url": "https://web.archive.org/web/20181111224140/https://www.gidsvoornederland.nl/werken-met-gids/meerwaarde-voor-bibliotheken/bibliotheken-in-nederland?pi=364&organisation_id=199660&startindex=0",
        "filename": "wbm_help.png"
    }
]

OUTPUT_DIR = "archived-sites/GidsVoorNederland/images"
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
