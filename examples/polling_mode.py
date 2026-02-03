from captchasolv import CaptchaSolv, TaskType

API_KEY = "YOUR_API_KEY"

solver = CaptchaSolv(API_KEY)

task_id = solver.create_task(
    task_type=TaskType.RECAPTCHA_V2,
    website_url="https://example.com",
    website_key="6Le-wvkSAAAAAPBMRTvw0Q4Muexq1bi0DJwx_mJ-"
)

print(f"Task created: {task_id}")

result = solver.wait_for_result(task_id, timeout=120)

print(f"Status: {result.status}")
print(f"Token: {result.solution.token}")
print(f"Solve time: {result.end_time - result.create_time}s")
