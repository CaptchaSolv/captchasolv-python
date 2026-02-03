# CaptchaSolv Python SDK

Official Python library for [CaptchaSolv.com](https://captchasolv.com) - Fast and reliable captcha solving API.

[![PyPI version](https://badge.fury.io/py/captchasolv.svg)](https://pypi.org/project/captchasolv/)
[![Python](https://img.shields.io/pypi/pyversions/captchasolv.svg)](https://pypi.org/project/captchasolv/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Supported Captcha Types

- ReCaptcha V3
- Cloudflare Turnstile
- GeeTest V4
- Akamai Bot Manager
- Kasada
- DataDome
- AWS WAF

## Installation

```bash
pip install captchasolv
```

For async support:
```bash
pip install captchasolv[async]
```

## Quick Start

```python
from captchasolv import CaptchaSolv

solver = CaptchaSolv("YOUR_API_KEY")

result = solver.turnstile(
    website_url="https://example.com",
    website_key="0x4AAAAAAABS7vwvV6VFfMcD"
)

print(result.solution.token)
```

## Async Usage

```python
import asyncio
from captchasolv import AsyncCaptchaSolv

async def main():
    async with AsyncCaptchaSolv("YOUR_API_KEY") as solver:
        result = await solver.turnstile(
            website_url="https://example.com",
            website_key="0x4AAAAAAABS7vwvV6VFfMcD"
        )
        print(result.solution.token)

asyncio.run(main())
```

## Examples

### ReCaptcha V3

```python
result = solver.recaptcha_v3(
    website_url="https://example.com",
    website_key="6Le-wvkSAAAAAPBMRTvw0Q4Muexq1bi0DJwx_mJ-",
    page_action="login"
)
```

### Cloudflare Turnstile

```python
result = solver.turnstile(
    website_url="https://example.com",
    website_key="0x4AAAAAAABS7vwvV6VFfMcD"
)
```

### Akamai

```python
result = solver.akamai(
    website_url="https://example.com",
    akamai_script="https://example.com/path/to/akamai/script.js",  # or use website_key
    data={
        "_abck": "current_abck_cookie_value",
        "bm_sz": "current_bm_sz_cookie_value"
    }
)
print(result.solution.sensor_data)
print(result.solution.cookies)
```

### Kasada

```python
result = solver.kasada(
    website_url="https://example.com",
    pjs="https://example.com/path/to/kasada/script.js",  # or use website_key
    v="optional_version"
)
print(result.solution.headers)
```

### DataDome

```python
result = solver.datadome(
    website_url="https://example.com",
    captcha_url="https://geo.captcha-delivery.com/captcha/?..."
)
print(result.solution.cookies)
```

### AWS WAF

```python
result = solver.aws_waf(
    website_url="https://example.com",
    aws_key="AQIDAHjcYu/GjX+QlghicBg..."
)
```

### GeeTest V4

```python
result = solver.geetest_v4(
    website_url="https://example.com",
    website_key="647f5ed2ed8acb4be36784e01556bb71"
)
```

## Using Proxies

All convenience methods support an optional `proxy` parameter:

```python
# Turnstile with proxy
result = solver.turnstile(
    website_url="https://example.com",
    website_key="0x4AAAAAAABS7vwvV6VFfMcD",
    proxy="http://user:pass@proxy.example.com:8080"
)

# Akamai with proxy
result = solver.akamai(
    website_url="https://example.com",
    akamai_script="https://example.com/script.js",
    proxy="socks5://user:pass@proxy.example.com:1080"
)

# Kasada with proxy
result = solver.kasada(
    website_url="https://example.com",
    pjs="https://example.com/ips.js",
    proxy="http://proxy.example.com:8080"
)
```

### Supported Proxy Formats

```
http://host:port
http://user:pass@host:port
https://user:pass@host:port
socks4://host:port
socks5://user:pass@host:port
```

## Generic Solve Method

For advanced usage or custom task types:

```python
from captchasolv import CaptchaSolv, TaskType

solver = CaptchaSolv("YOUR_API_KEY")

result = solver.solve(
    task_type=TaskType.TURNSTILE,
    website_url="https://example.com",
    website_key="0x4AAAAAAABS7vwvV6VFfMcD",
    user_agent="Mozilla/5.0 ...",
)
```

## Async/Polling Mode

For long-running tasks, you can create a task and poll separately:

```python
task_id = solver.create_task(
    task_type=TaskType.TURNSTILE,
    website_url="https://example.com",
    website_key="0x4AAAAAAABS7vwvV6VFfMcD"
)

result = solver.wait_for_result(task_id, timeout=120)
print(result.solution.token)
```

## Check Balance

```python
balance = solver.get_balance()
print(f"Balance: ${balance}")
```

## Error Handling

```python
from captchasolv import (
    CaptchaSolv,
    CaptchaSolvError,
    InvalidKeyError,
    LimitExceededError,
    CaptchaUnsolvableError,
)

try:
    result = solver.turnstile(...)
except InvalidKeyError:
    print("Invalid API key")
except LimitExceededError:
    print("Balance exhausted or rate limit reached")
except CaptchaUnsolvableError:
    print("Failed to solve captcha, retry")
except CaptchaSolvError as e:
    print(f"Error {e.error_code}: {e.error_description}")
```

## Configuration

```python
solver = CaptchaSolv(
    api_key="YOUR_API_KEY",
    base_url="https://v1.captchasolv.com",
    timeout=130.0,
    poll_interval=3.0,
)
```

## Response Object

```python
result = solver.recaptcha_v2(...)

print(result.status)
print(result.solution.token)
print(result.solution.user_agent)
print(result.solution.cookies)
print(result.cost)
print(result.solve_count)
```

## Links

- [Website](https://captchasolv.com)
- [Documentation](https://docs.captchasolv.com)

## License

MIT