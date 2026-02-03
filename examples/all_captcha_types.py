from captchasolv import CaptchaSolv

API_KEY = "YOUR_API_KEY"

solver = CaptchaSolv(API_KEY)


def solve_recaptcha_v3():
    result = solver.recaptcha_v3(
        website_url="https://example.com",
        website_key="6Le-wvkSAAAAAPBMRTvw0Q4Muexq1bi0DJwx_mJ-",
        page_action="login"
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
        website_key="647f5ed2ed8acb4be36784e01556bb71"
    )
    return result.solution.token


def solve_akamai():
    result = solver.akamai(
        website_url="https://example.com",
        akamai_script="https://example.com/akam/13/script.js",
        data={
            "_abck": "current_abck_cookie_value",
            "bm_sz": "current_bm_sz_cookie_value"
        }
    )
    return result.solution.sensor_data, result.solution.cookies


def solve_kasada():
    result = solver.kasada(
        website_url="https://example.com",
        pjs="https://example.com/{uuid}/{uuid}/p.js",
        v="i-1.18.2"
    )
    return result.solution.headers


def solve_datadome():
    result = solver.datadome(
        website_url="https://example.com",
        captcha_url="https://geo.captcha-delivery.com/captcha/?..."
    )
    return result.solution.cookies


def solve_aws_waf():
    result = solver.aws_waf(
        website_url="https://example.com",
        aws_key="AQIDAHjcYu/GjX..."
    )
    return result.solution.token
