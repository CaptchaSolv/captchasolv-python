from enum import Enum


class TaskType(str, Enum):
    RECAPTCHA_V2 = "RecaptchaV2TaskProxyless"
    RECAPTCHA_V2_PROXY = "RecaptchaV2Task"
    RECAPTCHA_V3 = "RecaptchaV3TaskProxyless"
    TURNSTILE = "TurnstileTaskProxyless"
    GEETEST_V4 = "GeeTestV4TaskProxyless"
    AKAMAI = "AkamaiTaskProxyless"
    KASADA = "KasadaTaskProxyless"
    DATADOME = "DataDomeTaskProxyless"
    AWS_WAF = "AwsWafTaskProxyless"
    HUMAN_SECURITY = "HumanSecurityTaskProxyless"


class ErrorCode(Enum):
    SUCCESS = 0
    INVALID_REQUEST = 1
    KEY_DOES_NOT_EXIST = 2
    UNSUPPORTED_CAPTCHA_TYPE = 3
    LIMIT_EXCEEDED = 10
    CAPTCHA_UNSOLVABLE = 12
    NO_SUCH_CAPTCHA_ID = 16
