from captchasolv import (
    CaptchaSolv,
    CaptchaSolvError,
    InvalidKeyError,
    LimitExceededError,
    CaptchaUnsolvableError,
    TaskNotFoundError,
)

API_KEY = "YOUR_API_KEY"

solver = CaptchaSolv(API_KEY)

try:
    result = solver.recaptcha_v2(
        website_url="https://example.com",
        website_key="6Le-wvkSAAAAAPBMRTvw0Q4Muexq1bi0DJwx_mJ-"
    )
    print(f"Token: {result.solution.token}")

except InvalidKeyError:
    print("Invalid API key - check your credentials")

except LimitExceededError:
    print("Balance exhausted or rate limit reached")

except CaptchaUnsolvableError:
    print("Failed to solve captcha - consider retrying")

except TaskNotFoundError:
    print("Task not found - ID may be invalid or expired")

except CaptchaSolvError as e:
    print(f"API Error [{e.error_code}]: {e.error_description}")

except Exception as e:
    print(f"Unexpected error: {e}")
