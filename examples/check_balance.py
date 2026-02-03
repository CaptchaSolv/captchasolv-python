from captchasolv import CaptchaSolv

API_KEY = "YOUR_API_KEY"

solver = CaptchaSolv(API_KEY)

balance = solver.get_balance()
print(f"Current balance: ${balance:.2f}")
