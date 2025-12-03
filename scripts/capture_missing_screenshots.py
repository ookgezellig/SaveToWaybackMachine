"""
Capture missing screenshots that failed due to connection issues.
Uses https URLs instead of http.
"""
import asyncio
import os
from PIL import Image
from playwright.async_api import async_playwright

BASE_DIR = r"D:\KB-OPEN\github-repos\SaveToWaybackMachine\archived-sites"
BANNER_HEIGHT = 210

# URLs that failed - trying with https and different timestamps
MISSING_URLS = {
    "LezenVoorDeLijst": {
        "images_dir": "images",
        "urls": [
            ("homepage", "https://web.archive.org/web/20180706111728/https://www.lezenvoordelijst.nl/"),
            ("pagina_104937", "https://web.archive.org/web/20180706112454/https://www.lezenvoordelijst.nl/104937.aspx"),
            ("pagina_1296", "https://web.archive.org/web/20180706112515/https://www.lezenvoordelijst.nl/1296.aspx"),
            ("pagina_154224", "https://web.archive.org/web/20180706112606/https://www.lezenvoordelijst.nl/154224.aspx"),
            ("pagina_168938", "https://web.archive.org/web/20180706112616/https://www.lezenvoordelijst.nl/168938.aspx"),
            ("pagina_50393", "https://web.archive.org/web/20180706112839/https://www.lezenvoordelijst.nl/50393.aspx"),
        ]
    },
    "Literaireprijzen.nl": {
        "images_dir": "images",
        "urls": [
            ("homepage", "https://web.archive.org/web/20181103203225/http://www.literaireprijzen.nl/"),
        ]
    },
    "Leesplein": {
        "images_dir": "images",
        "urls": [
            ("boek_372", "https://web.archive.org/web/20180619111907/https://www.leesplein.nl/JB_plein.php?hm=3&sm=1&id=372"),
            ("boek_400", "https://web.archive.org/web/20180619111917/https://www.leesplein.nl/JB_plein.php?hm=3&sm=1&id=400"),
        ]
    },
}


def trim_banner(image_path, banner_height=BANNER_HEIGHT):
    """Trim the donation banner from the top of the image."""
    try:
        with Image.open(image_path) as img:
            width, height = img.size
            if height <= banner_height:
                print(f"    Image too small to trim: {image_path}")
                return False
            cropped = img.crop((0, banner_height, width, height))
            cropped.save(image_path)
            print(f"    Trimmed {banner_height}px banner from: {os.path.basename(image_path)}")
            return True
    except Exception as e:
        print(f"    Error trimming banner: {e}")
        return False


async def capture_screenshot(page, url, output_path, name, max_retries=3):
    """Capture a screenshot of a Wayback Machine URL."""
    for attempt in range(max_retries):
        print(f"  [{attempt + 1}/{max_retries}] Capturing {name}...")
        try:
            await page.goto(url, timeout=120000, wait_until="domcontentloaded")
            await asyncio.sleep(5)
            await page.screenshot(path=output_path, full_page=False)
            print(f"    Saved: {os.path.basename(output_path)}")
            trim_banner(output_path)
            return True
        except Exception as e:
            print(f"    Error: {str(e)[:80]}")
            if attempt < max_retries - 1:
                print(f"    Retrying in 5 seconds...")
                await asyncio.sleep(5)
    return False


async def main():
    print("=" * 60)
    print("Capturing Missing Screenshots")
    print("=" * 60)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(viewport={"width": 1400, "height": 900})
        page = await context.new_page()

        for site_name, config in MISSING_URLS.items():
            print(f"\n{'=' * 40}")
            print(f"Processing: {site_name}")
            print(f"{'=' * 40}")

            site_dir = os.path.join(BASE_DIR, site_name)
            images_dir = os.path.join(site_dir, config["images_dir"])
            os.makedirs(images_dir, exist_ok=True)

            for name, url in config["urls"]:
                output_path = os.path.join(images_dir, f"wbm_{name}.png")
                # Skip if file already exists
                if os.path.exists(output_path):
                    print(f"  Skipping {name} - already exists")
                    continue
                success = await capture_screenshot(page, url, output_path, name)
                if not success:
                    print(f"    FAILED: {name}")

        await browser.close()
        print("\nDone!")


if __name__ == "__main__":
    asyncio.run(main())
