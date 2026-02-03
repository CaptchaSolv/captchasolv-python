from captchasolv import CaptchaSolv

API_KEY = "YOUR_API_KEY"

MY_USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

solver = CaptchaSolv(API_KEY)

result = solver.recaptcha_v2(
    website_url="https://example.com",
    website_key="6Le-wvkSAAAAAPBMRTvw0Q4Muexq1bi0DJwx_mJ-",
    user_agent=MY_USER_AGENT
)

print(f"Token: {result.solution.token}")
print(f"Solved with UA: {result.solution.user_agent}")
