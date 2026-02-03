import asyncio
from captchasolv import AsyncCaptchaSolv

API_KEY = "YOUR_API_KEY"


async def main():
    async with AsyncCaptchaSolv(API_KEY) as solver:
        result = await solver.recaptcha_v2(
            website_url="https://example.com",
            website_key="6Le-wvkSAAAAAPBMRTvw0Q4Muexq1bi0DJwx_mJ-"
        )
        print(f"Token: {result.solution.token}")


asyncio.run(main())
