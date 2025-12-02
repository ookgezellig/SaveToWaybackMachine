"""
Capture screenshots from the Wayback Machine for archived sites.
"""
import asyncio
import os
from playwright.async_api import async_playwright

BASE_DIR = r"D:\KB-OPEN\github-repos\SaveToWaybackMachine\archived-sites"

# Define sites and their Wayback Machine URLs to capture
SITES = {
    "Literatuurplein": {
        "images_dir": "images",
        "urls": [
            ("homepage", "https://web.archive.org/web/20191206120000*/https://www.literatuurplein.nl/"),
            ("personen", "https://web.archive.org/web/20191206/https://www.literatuurplein.nl/personen.php"),
            ("boeken", "https://web.archive.org/web/20191206/https://www.literatuurplein.nl/boeken.php"),
            ("prijzen", "https://web.archive.org/web/20191206/https://www.literatuurplein.nl/prijzen.php"),
            ("recensies", "https://web.archive.org/web/20191206/https://www.literatuurplein.nl/recensies.php"),
            ("nieuws", "https://web.archive.org/web/20191206/https://www.literatuurplein.nl/nieuws.php"),
        ]
    },
    "Leesplein": {
        "images_dir": "images",
        "urls": [
            ("homepage", "https://web.archive.org/web/20180614/https://www.leesplein.nl/"),
            ("boeken", "https://web.archive.org/web/20180614/https://www.leesplein.nl/LL_boeken.php"),
            ("schrijvers", "https://web.archive.org/web/20180614/https://www.leesplein.nl/LL_schrijvers.php"),
            ("recensies", "https://web.archive.org/web/20180614/https://www.leesplein.nl/LL_recensies.php"),
            ("tips", "https://web.archive.org/web/20180614/https://www.leesplein.nl/LL_tips.php"),
            ("themas", "https://web.archive.org/web/20180614/https://www.leesplein.nl/LL_themas.php"),
        ]
    },
    "LezenVoorDeLijst": {
        "images_dir": "images",
        "urls": [
            ("homepage", "https://web.archive.org/web/20180817/https://www.lezenvoordelijst.nl/"),
            ("boeken", "https://web.archive.org/web/20180817/https://www.lezenvoordelijst.nl/boeken"),
            ("schrijvers", "https://web.archive.org/web/20180817/https://www.lezenvoordelijst.nl/schrijvers"),
            ("recensies", "https://web.archive.org/web/20180817/https://www.lezenvoordelijst.nl/recensies"),
            ("lijsten", "https://web.archive.org/web/20180817/https://www.lezenvoordelijst.nl/lijsten"),
            ("tips", "https://web.archive.org/web/20180817/https://www.lezenvoordelijst.nl/tips"),
        ]
    },
    "GidsVoorNederland": {
        "images_dir": "images",
        "urls": [
            ("homepage", "https://web.archive.org/web/20181101/https://www.gidsvoornederland.nl/"),
            ("bibliotheken", "https://web.archive.org/web/20181101/https://www.gidsvoornederland.nl/bibliotheken"),
            ("zoeken", "https://web.archive.org/web/20181101/https://www.gidsvoornederland.nl/zoeken"),
            ("contact", "https://web.archive.org/web/20181101/https://www.gidsvoornederland.nl/contact"),
            ("over", "https://web.archive.org/web/20181101/https://www.gidsvoornederland.nl/over"),
            ("help", "https://web.archive.org/web/20181101/https://www.gidsvoornederland.nl/help"),
        ]
    },
    "Literaireprijzen.nl": {
        "images_dir": "images",
        "urls": [
            ("homepage", "https://web.archive.org/web/20181031/https://www.literaireprijzen.nl/"),
            ("prijzen", "https://web.archive.org/web/20181031/https://www.literaireprijzen.nl/prijzen"),
            ("winnaars", "https://web.archive.org/web/20181031/https://www.literaireprijzen.nl/winnaars"),
            ("auteurs", "https://web.archive.org/web/20181031/https://www.literaireprijzen.nl/auteurs"),
            ("boeken", "https://web.archive.org/web/20181031/https://www.literaireprijzen.nl/boeken"),
            ("nieuws", "https://web.archive.org/web/20181031/https://www.literaireprijzen.nl/nieuws"),
        ]
    },
    "Literaruurgeschiedenis.org": {
        "images_dir": "images",
        "urls": [
            ("homepage", "https://web.archive.org/web/20220325/https://www.literatuurgeschiedenis.org/"),
            ("18e_eeuw", "https://web.archive.org/web/20220325/https://www.literatuurgeschiedenis.org/18e-eeuw"),
            ("19e_eeuw", "https://web.archive.org/web/20220325/https://www.literatuurgeschiedenis.org/19e-eeuw"),
            ("20e_eeuw", "https://web.archive.org/web/20220325/https://www.literatuurgeschiedenis.org/20e-eeuw"),
            ("middeleeuwen", "https://web.archive.org/web/20220325/https://www.literatuurgeschiedenis.org/middeleeuwen"),
            ("auteurs", "https://web.archive.org/web/20220325/https://www.literatuurgeschiedenis.org/auteurs"),
        ]
    },
}


async def capture_screenshot(page, url, output_path, name):
    """Capture a screenshot of a Wayback Machine URL."""
    print(f"  Capturing {name}...")
    try:
        await page.goto(url, timeout=60000, wait_until="networkidle")
        await asyncio.sleep(2)  # Wait for page to fully render
        await page.screenshot(path=output_path, full_page=False)
        print(f"    Saved: {output_path}")
        return True
    except Exception as e:
        print(f"    Error capturing {name}: {e}")
        return False


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={"width": 1280, "height": 800})
        page = await context.new_page()

        for site_name, config in SITES.items():
            print(f"\nProcessing {site_name}...")
            site_dir = os.path.join(BASE_DIR, site_name)
            images_dir = os.path.join(site_dir, config["images_dir"])
            os.makedirs(images_dir, exist_ok=True)

            for name, url in config["urls"]:
                output_path = os.path.join(images_dir, f"wbm_{name}.png")
                await capture_screenshot(page, url, output_path, name)

        await browser.close()
        print("\nDone!")


if __name__ == "__main__":
    asyncio.run(main())
