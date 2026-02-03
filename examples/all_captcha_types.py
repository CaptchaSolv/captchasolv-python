from captchasolv import CaptchaSolv

API_KEY = "YOUR_API_KEY"

solver = CaptchaSolv(API_KEY)


def solve_recaptcha_v2():
    result = solver.recaptcha_v2(
        website_url="https://example.com",
        website_key="6Le-wvkSAAAAAPBMRTvw0Q4Muexq1bi0DJwx_mJ-"
    )
    return result.solution.token


def solve_recaptcha_v3():
    result = solver.recaptcha_v3(
        website_url="https://example.com",
        website_key="6Le-wvkSAAAAAPBMRTvw0Q4Muexq1bi0DJwx_mJ-",
        page_action="login",
        min_score=0.7
    )
    return result.solution.token


def solve_turnstile():
    result = solver.turnstile(
        website_url="https://example.com",
        website_key="0x4AAAAAAABS7vwvV6VFfMcD"
    )
    return result.solution.token


def solve_geetest_v4():
    result = solver.geetest_v4(
        website_url="https://example.com",
        captcha_id="647f5ed2ed8acb4be36784e01556bb71"
    )
    return result.solution.token


def solve_akamai():
    result = solver.akamai(website_url="https://example.com")
    return result.solution.cookies


def solve_kasada():
    result = solver.kasada(website_url="https://example.com")
    return result.solution.headers


def solve_datadome():
    result = solver.datadome(
        website_url="https://example.com",
        captcha_url="https://geo.captcha-delivery.com/captcha/?..."
    )
    return result.solution.cookies


def solve_aws_waf():
    result = solver.aws_waf(website_url="https://example.com")
    return result.solution.token


def solve_human_security():
    result = solver.human_security(website_url="https://example.com")
    return result.solution.cookies
