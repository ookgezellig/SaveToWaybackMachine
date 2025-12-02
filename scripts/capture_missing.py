"""Capture missing screenshots."""
import asyncio
import os
from playwright.async_api import async_playwright

BASE_DIR = r"D:\KB-OPEN\github-repos\SaveToWaybackMachine\archived-sites"

MISSING = [
    ("Leesplein", "homepage", "https://web.archive.org/web/20180607144514/https://www.leesplein.nl/"),
    ("LezenVoorDeLijst", "homepage", "https://web.archive.org/web/20180816235959/https://www.lezenvoordelijst.nl/"),
    ("Literaruurgeschiedenis.org", "homepage", "https://web.archive.org/web/20220325120947/https://www.literatuurgeschiedenis.org/"),
    ("Literaruurgeschiedenis.org", "18e_eeuw", "https://web.archive.org/web/20220326000000*/https://www.literatuurgeschiedenis.org/18e-eeuw"),
]

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={"width": 1280, "height": 800})
        page = await context.new_page()

        for site_name, name, url in MISSING:
            print(f"Capturing {site_name}/{name}...")
            images_dir = os.path.join(BASE_DIR, site_name, "images")
            os.makedirs(images_dir, exist_ok=True)
            output_path = os.path.join(images_dir, f"wbm_{name}.png")
            try:
                await page.goto(url, timeout=90000, wait_until="domcontentloaded")
                await asyncio.sleep(3)
                await page.screenshot(path=output_path, full_page=False)
                print(f"  Saved: {output_path}")
            except Exception as e:
                print(f"  Error: {e}")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
