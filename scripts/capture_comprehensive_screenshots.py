"""
Capture comprehensive screenshots from verified Wayback Machine URLs.
Takes deep-level pages (not just homepages) and trims the donation banner.
"""
import asyncio
import os
from PIL import Image
from playwright.async_api import async_playwright

BASE_DIR = r"D:\KB-OPEN\github-repos\SaveToWaybackMachine\archived-sites"

# Height of the donation banner to trim (in pixels)
BANNER_HEIGHT = 210

# Verified working WBM URLs from the archive output files - DEEP LEVEL PAGES
# Each site has 6 diverse screenshots showing different content types
VERIFIED_URLS = {
    "Literatuurplein": {
        "images_dir": "images",
        "urls": [
            # Homepage
            ("homepage", "https://web.archive.org/web/20191129171059/https://www.literatuurplein.nl/"),
            # Author page - Thea Beckman
            ("auteur_thea_beckman", "https://web.archive.org/web/20191129171059/https://www.literatuurplein.nl/detail/persoon/thea-beckman/8"),
            # Literary prize page
            ("prijzen_overzicht", "https://web.archive.org/web/20191129220242/https://www.literatuurplein.nl/litprijzen"),
            # Canon overview
            ("canon_overzicht", "https://web.archive.org/web/20191128080343/https://www.literatuurplein.nl/canonoverzicht"),
            # News archive
            ("nieuws_archief", "https://web.archive.org/web/20191129220520/https://www.literatuurplein.nl/nieuwsarchief"),
            # Reviews page
            ("recensies", "https://web.archive.org/web/20191130191607/https://www.literatuurplein.nl/recensies"),
        ]
    },
    "Leesplein": {
        "images_dir": "images",
        "urls": [
            # Homepage
            ("homepage", "http://web.archive.org/web/20180614121639/https://www.leesplein.nl/"),
            # Book page - id 277
            ("boek_277", "http://web.archive.org/web/20180619110156/https://www.leesplein.nl/JB_plein.php?hm=3&sm=1&id=277"),
            # Book page - id 287
            ("boek_287", "http://web.archive.org/web/20180619110204/https://www.leesplein.nl/JB_plein.php?hm=3&sm=1&id=287"),
            # Book page - id 342
            ("boek_342", "http://web.archive.org/web/20180619110501/https://www.leesplein.nl/JB_plein.php?hm=3&sm=1&id=342"),
            # Book page - id 372
            ("boek_372", "http://web.archive.org/web/20180619111907/https://www.leesplein.nl/JB_plein.php?hm=3&sm=1&id=372"),
            # Book page - id 400
            ("boek_400", "http://web.archive.org/web/20180619111917/https://www.leesplein.nl/JB_plein.php?hm=3&sm=1&id=400"),
        ]
    },
    "LezenVoorDeLijst": {
        "images_dir": "images",
        "urls": [
            # Homepage
            ("homepage", "http://web.archive.org/web/20180706111728/https://www.lezenvoordelijst.nl/"),
            # Content page 104937
            ("pagina_104937", "http://web.archive.org/web/20180706112454/https://www.lezenvoordelijst.nl/104937.aspx"),
            # Content page 1296
            ("pagina_1296", "http://web.archive.org/web/20180706112515/https://www.lezenvoordelijst.nl/1296.aspx"),
            # Content page 154224
            ("pagina_154224", "http://web.archive.org/web/20180706112606/https://www.lezenvoordelijst.nl/154224.aspx"),
            # Content page 168938
            ("pagina_168938", "http://web.archive.org/web/20180706112616/https://www.lezenvoordelijst.nl/168938.aspx"),
            # Content page 50393
            ("pagina_50393", "http://web.archive.org/web/20180706112839/https://www.lezenvoordelijst.nl/50393.aspx"),
        ]
    },
    "GidsVoorNederland": {
        "images_dir": "images",
        "urls": [
            # Homepage
            ("homepage", "https://web.archive.org/web/20181111165649/https://www.gidsvoornederland.nl/"),
            # Libraries page
            ("bibliotheken", "https://web.archive.org/web/20181111165714/https://www.gidsvoornederland.nl/gids/Bibliotheken"),
            # Contact page
            ("contact", "https://web.archive.org/web/20181111165823/https://www.gidsvoornederland.nl/contact"),
            # About page
            ("over_ons", "https://web.archive.org/web/20181111165735/https://www.gidsvoornederland.nl/over"),
            # Help page
            ("help", "https://web.archive.org/web/20181111165757/https://www.gidsvoornederland.nl/help"),
            # Search page
            ("zoeken", "https://web.archive.org/web/20181111165649/https://www.gidsvoornederland.nl/"),
        ]
    },
    "Literaireprijzen.nl": {
        "images_dir": "images",
        "urls": [
            # Homepage
            ("homepage", "http://web.archive.org/web/20181103203225/http://www.literaireprijzen.nl/"),
            # Roland Holst Prize
            ("roland_holst_prijs", "http://web.archive.org/web/20181103203225/http://www.literaireprijzen.nl/Literaire-Prijzen/AwardID/284/Mode/ViewAwardYears?AwardName=A.%20Roland%20Holst%20Penning-Stipendium"),
            # AKO Literatuur Prize
            ("ako_literatuur_prijs", "http://web.archive.org/web/20181103203409/http://www.literaireprijzen.nl/Literaire-Prijzen/AwardID/144/Mode/ViewAwardYears?AwardName=AKO%20Literatuur%20Prijs"),
            # Anna Bijns Prize
            ("anna_bijns_prijs", "http://web.archive.org/web/20181103205013/http://www.literaireprijzen.nl/Literaire-Prijzen/AwardID/166/Mode/ViewAwardYears?AwardName=Anna%20Bijns%20Prijs"),
            # Anne Frank Prize
            ("anne_frank_prijs", "http://web.archive.org/web/20181103205027/http://www.literaireprijzen.nl/Literaire-Prijzen/AwardID/12/Mode/ViewAwardYears?AwardName=Anne%20Frank-prijs"),
            # Archeon Youth Book Prize
            ("archeon_jeugdboekenprijs", "http://web.archive.org/web/20181103205134/http://www.literaireprijzen.nl/Literaire-Prijzen/AwardID/561/Mode/ViewAwardYears?AwardName=Archeon%20Jeugdboekenprijs"),
        ]
    },
    "Literaruurgeschiedenis.org": {
        "images_dir": "images",
        "urls": [
            # Homepage
            ("homepage", "https://web.archive.org/web/20220325125436/https://www.literatuurgeschiedenis.org/"),
            # 16th century
            ("16e_eeuw", "https://web.archive.org/web/20220325125518/https://www.literatuurgeschiedenis.org/16e-eeuw"),
            # 17th century
            ("17e_eeuw", "https://web.archive.org/web/20220325125250/https://www.literatuurgeschiedenis.org/17e-eeuw"),
            # 18th century
            ("18e_eeuw", "https://web.archive.org/web/20220325125306/https://www.literatuurgeschiedenis.org/18e-eeuw"),
            # Deep page - The Printing Press as Weapon
            ("drukpers_als_wapen", "https://web.archive.org/web/20220325144122/https://www.literatuurgeschiedenis.org/16e-eeuw/de-drukpers-als-wapen"),
            # Deep page - Golden Times
            ("gouden_tijden", "https://web.archive.org/web/20220325164314/https://www.literatuurgeschiedenis.org/17e-eeuw/gouden-tijden"),
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
            # Crop from below the banner to the bottom
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
            await asyncio.sleep(5)  # Wait for WBM banner and content to fully load
            await page.screenshot(path=output_path, full_page=False)
            print(f"    Saved: {os.path.basename(output_path)}")
            # Trim the donation banner
            trim_banner(output_path)
            return True
        except Exception as e:
            print(f"    Error: {str(e)[:80]}")
            if attempt < max_retries - 1:
                print(f"    Retrying in 3 seconds...")
                await asyncio.sleep(3)
    return False


async def main():
    print("=" * 60)
    print("Comprehensive Wayback Machine Screenshot Capture")
    print("=" * 60)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(viewport={"width": 1400, "height": 900})
        page = await context.new_page()

        total_success = 0
        total_failed = 0

        for site_name, config in VERIFIED_URLS.items():
            print(f"\n{'=' * 40}")
            print(f"Processing: {site_name}")
            print(f"{'=' * 40}")

            site_dir = os.path.join(BASE_DIR, site_name)
            images_dir = os.path.join(site_dir, config["images_dir"])
            os.makedirs(images_dir, exist_ok=True)

            site_success = 0
            site_failed = 0

            for name, url in config["urls"]:
                output_path = os.path.join(images_dir, f"wbm_{name}.png")
                success = await capture_screenshot(page, url, output_path, name)
                if success:
                    site_success += 1
                    total_success += 1
                else:
                    site_failed += 1
                    total_failed += 1
                    print(f"    FAILED: {name}")

            print(f"\n  {site_name} Summary: {site_success} success, {site_failed} failed")

        await browser.close()

        print("\n" + "=" * 60)
        print(f"TOTAL: {total_success} screenshots captured, {total_failed} failed")
        print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())
