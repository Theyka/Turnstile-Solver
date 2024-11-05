# Not tested might not work

import asyncio
from async_solver import get_turnstile_token as async_get_token
from sync_solver import get_turnstile_token as sync_get_token

async def main():
    mode = input("Mode (sync/async): ").strip().lower()
    url = input("URL: ").strip()
    sitekey = input("Sitekey: ").strip()
    headless = input("Headless? (y/n): ").strip().lower() == "y"

    if mode == "async":
        result = await async_get_token(headless=headless, url=url, sitekey=sitekey)
    elif mode == "sync":
        result = sync_get_token(headless=headless, url=url, sitekey=sitekey)
    else:
        print("Invalid mode.")
        return

    print("Result:", result)

if __name__ == "__main__":
    asyncio.run(main())
