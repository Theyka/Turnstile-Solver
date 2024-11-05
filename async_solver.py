# Made the script async, faster, less ressource intensive, solve time ≈ 5 seconds can be faster depending on your internet and if you remove the logging, added page.html directly in the script

import asyncio
from undetected_playwright.async_api import async_playwright
from logmagix import Logger, Loader
import time


async def get_turnstile_token(headless=False, url=None, sitekey=None):
    loader = Loader(desc="Solving captcha...", timeout=0.05)
    loader.start()
    log = Logger()
    Debug = True
    
    async with async_playwright() as playwright:
        args = [
            "--disable-blink-features=AutomationControlled",
            "--no-sandbox",
            "--disable-dev-shm-usage",
            "--disable-background-networking",
            "--disable-background-timer-throttling",
            "--disable-backgrounding-occluded-windows",
            "--disable-renderer-backgrounding",
            "--window-position=2000,2000",
        ]
        
        start_time = time.time()
       

        browser = await playwright.chromium.launch(headless=headless, args=args)
        url_with_slash = url + "/" if not url.endswith("/") else url

        if Debug:
            log.debug(f"Navigating to URL: {url_with_slash}")

        context = await browser.new_context()
        page = await context.new_page()

        page_data = """
        <!DOCTYPE html>
        <html lang="en">
          <head>
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <title>Turnstile Solver</title>
            <script
              src="https://challenges.cloudflare.com/turnstile/v0/api.js?onload=onloadTurnstileCallback"
              async=""
              defer=""
            ></script>
          </head>
          <body>
            <!-- cf turnstile -->
          </body>
        </html>
        """
        turnstile_div = f"<div class=\"cf-turnstile\" data-sitekey=\"{sitekey}\"></div>"
        page_data = page_data.replace("<!-- cf turnstile -->", turnstile_div)

        if Debug:
            log.debug("Setting up page data and route.")

        await page.route(url_with_slash, lambda route: route.fulfill(body=page_data, status=200))
        await page.goto(url_with_slash)

        if Debug:
            log.debug("Getting window dimensions.")

        page.window_width = await page.evaluate("window.innerWidth")
        page.window_height = await page.evaluate("window.innerHeight")

        turnstile_value = None
        attempts = 0
        max_attempts = 10 

        if Debug:
            log.debug("Starting Turnstile response retrieval loop.")

        while attempts < max_attempts:
            turnstile_check = await page.eval_on_selector("[name=cf-turnstile-response]", "el => el.value")

            if turnstile_check == "":
                if Debug:
                    log.debug(f"Attempt {attempts + 1}: No Turnstile response yet. Clicking Turnstile div.")
                
                await page.evaluate("document.querySelector('.cf-turnstile').style.width = '70px'")
                await page.click(".cf-turnstile")
                await asyncio.sleep(0.5)
                attempts += 1
            else:
                turnstile_value = await page.query_selector("[name=cf-turnstile-response]")
                if turnstile_value:
                    turnstile_value = await turnstile_value.get_attribute("value")
                if Debug:
                    log.debug(f"Turnstile response received: {turnstile_value}")
                break
        
        end_time = time.time()
        elapsed_time = round(end_time - start_time, 3)
        loader.stop()

        if not turnstile_value:
            log.failure("Failed to retrieve Turnstile value.")
            result = {
                "turnstile_value": None,
                "elapsed_time_seconds": elapsed_time,
                "status": "failure",
                "reason": "Max attempts reached without token retrieval"
            }
        else:
            log.message("Cloudflare", f"Successfully solved captcha: {turnstile_value[:45] + '...'}", start=start_time, end=end_time)
            result = {
                "turnstile_value": turnstile_value,
                "elapsed_time_seconds": elapsed_time,
                "status": "success"
            }
            if Debug:
                log.debug(f"Elapsed time: {elapsed_time} seconds")

        await context.close()
        await browser.close()

        if Debug:
            log.debug("Browser closed. Returning result.")
        return result

if __name__ == "__main__":
    async def main():
        result = await get_turnstile_token(headless=False, url="https://bypass.city/", sitekey="0x4AAAAAAAGzw6rXeQWJ_y2P")
        print(result)

    asyncio.run(main())


# Credits for the changes: github.com/sexfrance
# Credit for the original script: github.com/Theyka
