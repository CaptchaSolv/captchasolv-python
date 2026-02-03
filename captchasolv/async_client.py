from __future__ import annotations

import asyncio
import time
from typing import TYPE_CHECKING, Union

import aiohttp

from .exceptions import raise_for_error
from .models import TaskResult
from .types import TaskType

if TYPE_CHECKING:
    from typing import Any, Optional


class AsyncCaptchaSolv:
    DEFAULT_BASE_URL = "https://v1.captchasolv.com"
    DEFAULT_POLL_INTERVAL = 3.0
    DEFAULT_TIMEOUT = 130.0

    def __init__(
        self,
        api_key: str,
        base_url: str = DEFAULT_BASE_URL,
        timeout: float = DEFAULT_TIMEOUT,
        poll_interval: float = DEFAULT_POLL_INTERVAL,
    ):
        self._api_key = api_key
        self._base_url = base_url.rstrip("/")
        self._timeout = aiohttp.ClientTimeout(total=timeout)
        self._poll_interval = poll_interval
        self._session: Optional[aiohttp.ClientSession] = None

    async def _get_session(self) -> aiohttp.ClientSession:
        if self._session is None or self._session.closed:
            self._session = aiohttp.ClientSession(timeout=self._timeout)
        return self._session

    async def close(self) -> None:
        if self._session is not None and not self._session.closed:
            await self._session.close()
            self._session = None

    async def __aenter__(self) -> AsyncCaptchaSolv:
        return self

    async def __aexit__(self, *args: Any) -> None:
        await self.close()

    async def _post(self, endpoint: str, payload: dict[str, Any]) -> dict[str, Any]:
        session = await self._get_session()
        async with session.post(f"{self._base_url}{endpoint}", json=payload) as response:
            return await response.json()

    def _build_task(
        self,
        task_type: Union[TaskType, str],
        website_url: str,
        website_key: Optional[str] = None,
        proxy: Optional[str] = None,
        user_agent: Optional[str] = None,
        **extra: Any,
    ) -> dict[str, Any]:
        task: dict[str, Any] = {
            "type": task_type.value if isinstance(task_type, TaskType) else task_type,
            "websiteURL": website_url,
        }
        if website_key is not None:
            task["websiteKey"] = website_key
        if proxy is not None:
            task["proxy"] = proxy
        if user_agent is not None:
            task["userAgent"] = user_agent
        task.update(extra)
        return task

    async def create_task(
        self,
        task_type: Union[TaskType, str],
        website_url: str,
        website_key: Optional[str] = None,
        proxy: Optional[str] = None,
        user_agent: Optional[str] = None,
        **extra: Any,
    ) -> str:
        task = self._build_task(task_type, website_url, website_key, proxy, user_agent, **extra)
        response = await self._post("/createTask", {"clientKey": self._api_key, "task": task})
        raise_for_error(response)
        return response["taskId"]

    async def get_task_result(self, task_id: str) -> TaskResult:
        response = await self._post("/getTaskResult", {"clientKey": self._api_key, "taskId": task_id})
        raise_for_error(response)
        return TaskResult.from_dict(response)

    async def wait_for_result(self, task_id: str, timeout: Optional[float] = None) -> TaskResult:
        timeout_val = timeout or self._timeout.total
        start = time.monotonic()
        while True:
            result = await self.get_task_result(task_id)
            if result.is_ready:
                return result
            if time.monotonic() - start > timeout_val:
                raise TimeoutError(f"Task {task_id} did not complete within {timeout_val}s")
            await asyncio.sleep(self._poll_interval)

    async def solve(
        self,
        task_type: Union[TaskType, str],
        website_url: str,
        website_key: Optional[str] = None,
        proxy: Optional[str] = None,
        user_agent: Optional[str] = None,
        **extra: Any,
    ) -> TaskResult:
        task = self._build_task(task_type, website_url, website_key, proxy, user_agent, **extra)
        response = await self._post("/solve", {"clientKey": self._api_key, "task": task})
        raise_for_error(response)
        return TaskResult.from_dict(response)

    async def get_balance(self) -> float:
        response = await self._post("/getBalance", {"clientKey": self._api_key})
        raise_for_error(response)
        return response["balance"]

    async def recaptcha_v3(
        self,
        website_url: str,
        website_key: str,
        page_action: Optional[str] = None,
        proxy: Optional[str] = None,
        user_agent: Optional[str] = None,
    ) -> TaskResult:
        extra: dict[str, Any] = {}
        if page_action is not None:
            extra["pageAction"] = page_action
        return await self.solve(TaskType.RECAPTCHA_V3, website_url, website_key, proxy=proxy, user_agent=user_agent, **extra)

    async def turnstile(
        self,
        website_url: str,
        website_key: str,
        proxy: Optional[str] = None,
        user_agent: Optional[str] = None,
    ) -> TaskResult:
        return await self.solve(TaskType.TURNSTILE, website_url, website_key, proxy=proxy, user_agent=user_agent)

    async def geetest_v4(
        self,
        website_url: str,
        website_key: str,
        proxy: Optional[str] = None,
        user_agent: Optional[str] = None,
    ) -> TaskResult:
        return await self.solve(TaskType.GEETEST_V4, website_url, website_key, proxy=proxy, user_agent=user_agent)

    async def akamai(
        self,
        website_url: str,
        akamai_script: Optional[str] = None,
        website_key: Optional[str] = None,
        data: Optional[dict[str, str]] = None,
        proxy: Optional[str] = None,
        user_agent: Optional[str] = None,
    ) -> TaskResult:
        script = akamai_script or website_key
        if script is None:
            raise ValueError("akamai_script or website_key is required")
        extra: dict[str, Any] = {}
        if data is not None:
            extra["data"] = data
        return await self.solve(TaskType.AKAMAI, website_url, proxy=proxy, user_agent=user_agent, akamaiScript=script, **extra)

    async def kasada(
        self,
        website_url: str,
        pjs: Optional[str] = None,
        website_key: Optional[str] = None,
        v: Optional[str] = None,
        proxy: Optional[str] = None,
        user_agent: Optional[str] = None,
    ) -> TaskResult:
        script = pjs or website_key
        if script is None:
            raise ValueError("pjs or website_key is required")
        extra: dict[str, Any] = {}
        if v is not None:
            extra["v"] = v
        return await self.solve(TaskType.KASADA, website_url, proxy=proxy, user_agent=user_agent, pjs=script, **extra)

    async def datadome(
        self,
        website_url: str,
        website_key: Optional[str] = None,
        proxy: Optional[str] = None,
        user_agent: Optional[str] = None,
    ) -> TaskResult:
        return await self.solve(TaskType.DATADOME, website_url, website_key, proxy=proxy, user_agent=user_agent)

    async def aws_waf(
        self,
        website_url: str,
        aws_key: Optional[str] = None,
        proxy: Optional[str] = None,
        user_agent: Optional[str] = None,
    ) -> TaskResult:
        extra: dict[str, Any] = {}
        if aws_key is not None:
            extra["awsKey"] = aws_key
        return await self.solve(TaskType.AWS_WAF, website_url, proxy=proxy, user_agent=user_agent, **extra)
