"""
Capture screenshots from verified Wayback Machine URLs at deeper levels.
Trims off the donation banner from the top of screenshots.
"""
import asyncio
import os
from PIL import Image
from playwright.async_api import async_playwright

BASE_DIR = r"D:\KB-OPEN\github-repos\SaveToWaybackMachine\archived-sites"

# Height of the donation banner to trim (in pixels)
BANNER_HEIGHT = 210

# Verified working WBM URLs from the archive output files - DEEPER LEVEL PAGES
VERIFIED_URLS = {
    "Literatuurplein": {
        "images_dir": "images",
        "urls": [
            ("homepage", "https://web.archive.org/web/20191129171059/https://www.literatuurplein.nl/"),
            ("thea_beckman", "https://web.archive.org/web/20191129171059/https://www.literatuurplein.nl/detail/persoon/thea-beckman/8"),
            ("canon_overzicht", "https://web.archive.org/web/20191128080343/https://www.literatuurplein.nl/canonoverzicht"),
            ("litprijzen", "https://web.archive.org/web/20191129220242/https://www.literatuurplein.nl/litprijzen"),
            ("recensies", "https://web.archive.org/web/20191130191607/https://www.literatuurplein.nl/recensies"),
            ("nieuwsarchief", "https://web.archive.org/web/20191129220520/https://www.literatuurplein.nl/nieuwsarchief"),
        ]
    },
    "Leesplein": {
        "images_dir": "images",
        "urls": [
            ("homepage", "http://web.archive.org/web/20180614121639/https://www.leesplein.nl/"),
            ("juryrapport_2015", "http://web.archive.org/web/20180614122003/https://www.leesplein.nl/assets/juryrapporten/2015-strop.pdf"),
            ("academica_2006", "http://web.archive.org/web/20180614122014/https://www.leesplein.nl/assets/juryrapporten/academica-2006.html"),
            ("boek_2374", "http://web.archive.org/web/20180614143958/https://www.leesplein.nl/JB_plein.php?hm=3&sm=1&id=2374"),
            ("boek_2421", "http://web.archive.org/web/20180614144210/https://www.leesplein.nl/JB_plein.php?hm=3&sm=1&id=2421"),
            ("boek_246", "http://web.archive.org/web/20180614144220/https://www.leesplein.nl/JB_plein.php?hm=3&sm=1&id=246"),
        ]
    },
    "LezenVoorDeLijst": {
        "images_dir": "images",
        "urls": [
            ("homepage", "http://web.archive.org/web/20180706111728/https://www.lezenvoordelijst.nl/"),
            ("page_104937", "http://web.archive.org/web/20180706112454/https://www.lezenvoordelijst.nl/104937.aspx"),
            ("page_1296", "http://web.archive.org/web/20180706112515/https://www.lezenvoordelijst.nl/1296.aspx"),
            ("page_154224", "http://web.archive.org/web/20180706112606/https://www.lezenvoordelijst.nl/154224.aspx"),
            ("page_168938", "http://web.archive.org/web/20180706112616/https://www.lezenvoordelijst.nl/168938.aspx"),
            ("page_50393", "http://web.archive.org/web/20180706112839/https://www.lezenvoordelijst.nl/50393.aspx"),
        ]
    },
    "GidsVoorNederland": {
        "images_dir": "images",
        "urls": [
            ("homepage", "https://web.archive.org/web/20201021125839/https://www.gidsvoornederland.nl/"),
            ("bibliotheken", "https://web.archive.org/web/20181111165714/https://www.gidsvoornederland.nl/gids/Bibliotheken"),
            ("contact", "https://web.archive.org/web/20181111165823/https://www.gidsvoornederland.nl/contact"),
        ]
    },
    "Literaireprijzen.nl": {
        "images_dir": "images",
        "urls": [
            ("homepage", "http://web.archive.org/web/20181103203225/http://www.literaireprijzen.nl/"),
            ("roland_holst", "http://web.archive.org/web/20181103203225/http://www.literaireprijzen.nl/Literaire-Prijzen/AwardID/284/Mode/ViewAwardYears?AwardName=A.%20Roland%20Holst%20Penning-Stipendium"),
            ("ako_prijs", "http://web.archive.org/web/20181103203409/http://www.literaireprijzen.nl/Literaire-Prijzen/AwardID/144/Mode/ViewAwardYears?AwardName=AKO%20Literatuur%20Prijs"),
            ("anna_bijns", "http://web.archive.org/web/20181103205013/http://www.literaireprijzen.nl/Literaire-Prijzen/AwardID/166/Mode/ViewAwardYears?AwardName=Anna%20Bijns%20Prijs"),
            ("anne_frank", "http://web.archive.org/web/20181103205027/http://www.literaireprijzen.nl/Literaire-Prijzen/AwardID/12/Mode/ViewAwardYears?AwardName=Anne%20Frank-prijs"),
            ("archeon", "http://web.archive.org/web/20181103205134/http://www.literaireprijzen.nl/Literaire-Prijzen/AwardID/561/Mode/ViewAwardYears?AwardName=Archeon%20Jeugdboekenprijs"),
        ]
    },
    "Literaruurgeschiedenis.org": {
        "images_dir": "images",
        "urls": [
            ("homepage", "https://web.archive.org/web/20220325125436/https://www.literatuurgeschiedenis.org/"),
            ("16e_eeuw", "https://web.archive.org/web/20220325125518/https://www.literatuurgeschiedenis.org/16e-eeuw"),
            ("17e_eeuw", "https://web.archive.org/web/20220325125250/https://www.literatuurgeschiedenis.org/17e-eeuw"),
            ("18e_eeuw", "https://web.archive.org/web/20220325125306/https://www.literatuurgeschiedenis.org/18e-eeuw"),
            ("drukpers", "https://web.archive.org/web/20220325144122/https://www.literatuurgeschiedenis.org/16e-eeuw/de-drukpers-als-wapen"),
            ("gouden_tijden", "https://web.archive.org/web/20220325164314/https://www.literatuurgeschiedenis.org/17e-eeuw/gouden-tijden"),
        ]
    },
}


def trim_banner(image_path, banner_height=BANNER_HEIGHT):
    """Trim the donation banner from the top of the image."""
    try:
        with Image.open(image_path) as img:
            width, height = img.size
            # Crop from below the banner to the bottom
            cropped = img.crop((0, banner_height, width, height))
            cropped.save(image_path)
            print(f"    Trimmed banner from: {image_path}")
            return True
    except Exception as e:
        print(f"    Error trimming banner: {e}")
        return False


async def capture_screenshot(page, url, output_path, name, max_retries=3):
    """Capture a screenshot of a Wayback Machine URL."""
    for attempt in range(max_retries):
        print(f"  Capturing {name} (attempt {attempt + 1})...")
        try:
            await page.goto(url, timeout=90000, wait_until="domcontentloaded")
            await asyncio.sleep(4)  # Wait for WBM banner to load
            await page.screenshot(path=output_path, full_page=False)
            print(f"    Saved: {output_path}")
            # Trim the donation banner
            trim_banner(output_path)
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
