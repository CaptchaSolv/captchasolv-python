__version__ = "1.0.0"
__author__ = "CaptchaSolv.com"
__license__ = "MIT"

from .types import TaskType, ErrorCode
from .models import Solution, TaskResult
from .exceptions import (
    CaptchaSolvError,
    InvalidKeyError,
    UnsupportedTypeError,
    LimitExceededError,
    CaptchaUnsolvableError,
    TaskNotFoundError,
)
from .client import CaptchaSolv
from .async_client import AsyncCaptchaSolv

__all__ = [
    "__version__",
    "__author__",
    "__license__",
    "TaskType",
    "ErrorCode",
    "Solution",
    "TaskResult",
    "CaptchaSolvError",
    "InvalidKeyError",
    "UnsupportedTypeError",
    "LimitExceededError",
    "CaptchaUnsolvableError",
    "TaskNotFoundError",
    "CaptchaSolv",
    "AsyncCaptchaSolv",
]
