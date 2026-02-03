from enum import Enum


class TaskType(str, Enum):
    RECAPTCHA_V3 = "RecaptchaV3Task"
    TURNSTILE = "TurnstileTask"
    GEETEST_V4 = "GeeTestV4Task"
    AKAMAI = "AkamaiTask"
    KASADA = "KasadaTask"
    DATADOME = "DataDomeTask"
    AWS_WAF = "AwsWafTask"
    HUMAN_SECURITY = "HumanSecurityTask"


class ErrorCode(Enum):
    SUCCESS = 0
    INVALID_REQUEST = 1
    KEY_DOES_NOT_EXIST = 2
    UNSUPPORTED_CAPTCHA_TYPE = 3
    LIMIT_EXCEEDED = 10
    CAPTCHA_UNSOLVABLE = 12
    NO_SUCH_CAPTCHA_ID = 16
