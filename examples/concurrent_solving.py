import asyncio
from captchasolv import AsyncCaptchaSolv

API_KEY = "YOUR_API_KEY"

TASKS = [
    {"url": "https://site1.com", "key": "6Le-wvkSAAAAAPBMRTvw0Q4Muexq1bi0DJwx_mJ-"},
    {"url": "https://site2.com", "key": "6Le-wvkSAAAAAPBMRTvw0Q4Muexq1bi0DJwx_mJ-"},
    {"url": "https://site3.com", "key": "6Le-wvkSAAAAAPBMRTvw0Q4Muexq1bi0DJwx_mJ-"},
]


async def solve_one(solver: AsyncCaptchaSolv, url: str, key: str) -> str:
    result = await solver.recaptcha_v2(website_url=url, website_key=key)
    return result.solution.token


async def main():
    async with AsyncCaptchaSolv(API_KEY) as solver:
        tasks = [solve_one(solver, t["url"], t["key"]) for t in TASKS]
        tokens = await asyncio.gather(*tasks, return_exceptions=True)

        for i, token in enumerate(tokens):
            if isinstance(token, Exception):
                print(f"Task {i + 1} failed: {token}")
            else:
                print(f"Task {i + 1} solved: {token[:50]}...")


asyncio.run(main())
