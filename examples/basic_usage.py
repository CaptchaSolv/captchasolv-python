from captchasolv import CaptchaSolv

API_KEY = "YOUR_API_KEY"

solver = CaptchaSolv(API_KEY)

result = solver.recaptcha_v2(
    website_url="https://example.com",
    website_key="6Le-wvkSAAAAAPBMRTvw0Q4Muexq1bi0DJwx_mJ-"
)

print(f"Token: {result.solution.token}")
print(f"Cost: ${result.cost}")
