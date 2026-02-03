from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Any


class CaptchaSolvError(Exception):
    def __init__(self, error_id: int, error_code: str, error_description: str):
        self.error_id = error_id
        self.error_code = error_code
        self.error_description = error_description
        super().__init__(f"{error_code}: {error_description}")


class InvalidKeyError(CaptchaSolvError):
    pass


class UnsupportedTypeError(CaptchaSolvError):
    pass


class LimitExceededError(CaptchaSolvError):
    pass


class CaptchaUnsolvableError(CaptchaSolvError):
    pass


class TaskNotFoundError(CaptchaSolvError):
    pass


ERROR_MAP: dict[int, type[CaptchaSolvError]] = {
    2: InvalidKeyError,
    3: UnsupportedTypeError,
    10: LimitExceededError,
    12: CaptchaUnsolvableError,
    16: TaskNotFoundError,
}


def raise_for_error(response: dict[str, Any]) -> None:
    error_id = response.get("errorId", 0)
    if error_id == 0:
        return
    error_code = response.get("errorCode", "ERROR_UNKNOWN")
    error_description = response.get("errorDescription", "Unknown error")
    exc_class = ERROR_MAP.get(error_id, CaptchaSolvError)
    raise exc_class(error_id, error_code, error_description)
