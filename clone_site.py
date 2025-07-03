import os
import asyncio
from playwright.async_api import async_playwright
from urllib.parse import urlparse

url = "https://offer.buytacticalwindshieldtool.com/offer/1/index-v1-dtcv3.php?C1=1527&uid=14287&oid=1527&affid=1267&AFFID=1267&utm_campaign=CPA_1267&utm_source=1267"

async def clone_page():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()

        # Track finished requests
        resources = set()

        page.on("requestfinished", lambda request: collect_resource(request, resources))

        await page.goto(url, wait_until='networkidle')

        # Save full HTML after JS renders
        content = await page.content()
        os.makedirs("cloned_site", exist_ok=True)
        with open("cloned_site/index.html", "w", encoding='utf-8') as f:
            f.write(content)

        # Save screenshot
        await page.screenshot(path="cloned_site/screenshot.png", full_page=True)

        # Save all static resources
        for res_url in resources:
            parsed = urlparse(res_url)
            save_path = os.path.join("cloned_site", parsed.path.lstrip("/"))
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            try:
                buffer = await page.evaluate(f"fetch('{res_url}').then(r => r.arrayBuffer())")
                with open(save_path, "wb") as f:
                    f.write(bytes(buffer))
            except Exception as e:
                print(f"Failed to fetch {res_url}: {e}")

        await browser.close()

def collect_resource(request, resource_set):
    url = request.url
    parsed = urlparse(url)
    if parsed.path.endswith(('.css', '.js', '.jpg', '.jpeg', '.png', '.webp', '.gif', '.woff2', '.svg')):
        resource_set.add(url)

asyncio.run(clone_page())
