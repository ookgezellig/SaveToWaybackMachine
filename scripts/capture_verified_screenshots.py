"""
Capture screenshots from verified Wayback Machine URLs.
These URLs are known to have actual archived content.
"""
import asyncio
import os
from playwright.async_api import async_playwright

BASE_DIR = r"D:\KB-OPEN\github-repos\SaveToWaybackMachine\archived-sites"

# Verified working WBM URLs from the archive output files
VERIFIED_URLS = {
    "Literatuurplein": {
        "images_dir": "images",
        "urls": [
            ("homepage", "https://web.archive.org/web/20191129171059/https://www.literatuurplein.nl/"),
            ("personen", "https://web.archive.org/web/20191129171059/https://www.literatuurplein.nl/detail/persoon/thea-beckman/8"),
            ("boeken", "https://web.archive.org/web/20191128080343/https://www.literatuurplein.nl/canonoverzicht"),
            ("prijzen", "https://web.archive.org/web/20191129220242/https://www.literatuurplein.nl/litprijzen"),
            ("recensies", "https://web.archive.org/web/20191130191607/https://www.literatuurplein.nl/recensies"),
            ("nieuws", "https://web.archive.org/web/20191129220520/https://www.literatuurplein.nl/nieuwsarchief"),
        ]
    },
    "Leesplein": {
        "images_dir": "images",
        "urls": [
            ("boeken", "https://web.archive.org/web/20180607144514/https://www.leesplein.nl/LL_home.php"),
            ("schrijvers", "https://web.archive.org/web/20180607144514/https://www.leesplein.nl/LL_home.php"),
            ("recensies", "https://web.archive.org/web/20180607144514/https://www.leesplein.nl/LL_home.php"),
            ("tips", "https://web.archive.org/web/20180607144514/https://www.leesplein.nl/LL_home.php"),
            ("themas", "https://web.archive.org/web/20180607144514/https://www.leesplein.nl/LL_home.php"),
        ]
    },
    "LezenVoorDeLijst": {
        "images_dir": "images",
        "urls": [
            ("boeken", "https://web.archive.org/web/20180706092046/https://www.lezenvoordelijst.nl/"),
            ("schrijvers", "https://web.archive.org/web/20180706092046/https://www.lezenvoordelijst.nl/"),
            ("recensies", "https://web.archive.org/web/20180706092046/https://www.lezenvoordelijst.nl/"),
            ("lijsten", "https://web.archive.org/web/20180706092046/https://www.lezenvoordelijst.nl/"),
            ("tips", "https://web.archive.org/web/20180706092046/https://www.lezenvoordelijst.nl/"),
        ]
    },
    "GidsVoorNederland": {
        "images_dir": "images",
        "urls": [
            ("zoeken", "https://web.archive.org/web/20201021125839/https://www.gidsvoornederland.nl/"),
            ("over", "https://web.archive.org/web/20201021125839/https://www.gidsvoornederland.nl/"),
            ("help", "https://web.archive.org/web/20201021125839/https://www.gidsvoornederland.nl/"),
        ]
    },
    "Literaireprijzen.nl": {
        "images_dir": "images",
        "urls": [
            ("prijzen", "https://web.archive.org/web/20181031000000*/https://www.literaireprijzen.nl/"),
            ("winnaars", "https://web.archive.org/web/20181031000000*/https://www.literaireprijzen.nl/"),
            ("auteurs", "https://web.archive.org/web/20181031000000*/https://www.literaireprijzen.nl/"),
            ("boeken", "https://web.archive.org/web/20181031000000*/https://www.literaireprijzen.nl/"),
            ("nieuws", "https://web.archive.org/web/20181031000000*/https://www.literaireprijzen.nl/"),
        ]
    },
    "Literaruurgeschiedenis.org": {
        "images_dir": "images",
        "urls": [
            ("18e_eeuw", "https://web.archive.org/web/20220325120947/https://www.literatuurgeschiedenis.org/18e-eeuw"),
            ("auteurs", "https://web.archive.org/web/20220325120947/https://www.literatuurgeschiedenis.org/schrijvers"),
        ]
    },
}


async def capture_screenshot(page, url, output_path, name, max_retries=3):
    """Capture a screenshot of a Wayback Machine URL."""
    for attempt in range(max_retries):
        print(f"  Capturing {name} (attempt {attempt + 1})...")
        try:
            await page.goto(url, timeout=90000, wait_until="domcontentloaded")
            await asyncio.sleep(4)  # Wait for WBM banner to load
            await page.screenshot(path=output_path, full_page=False)
            print(f"    Saved: {output_path}")
            return True
        except Exception as e:
            print(f"    Error (attempt {attempt + 1}): {e}")
            if attempt < max_retries - 1:
                await asyncio.sleep(2)
    return False


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # headless=False to see what's happening
        context = await browser.new_context(viewport={"width": 1400, "height": 900})
        page = await context.new_page()

        for site_name, config in VERIFIED_URLS.items():
            print(f"\nProcessing {site_name}...")
            site_dir = os.path.join(BASE_DIR, site_name)
            images_dir = os.path.join(site_dir, config["images_dir"])
            os.makedirs(images_dir, exist_ok=True)

            for name, url in config["urls"]:
                output_path = os.path.join(images_dir, f"wbm_{name}.png")
                success = await capture_screenshot(page, url, output_path, name)
                if not success:
                    print(f"    FAILED to capture {name} after all retries")

        await browser.close()
        print("\nDone!")


if __name__ == "__main__":
    asyncio.run(main())
