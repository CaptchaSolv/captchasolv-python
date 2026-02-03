from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Any, Optional


@dataclass
class Solution:
    token: str
    user_agent: Optional[str] = None
    cookies: Optional[dict[str, str]] = None
    headers: Optional[dict[str, str]] = None
    raw: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Solution:
        return cls(
            token=data.get("token", ""),
            user_agent=data.get("userAgent"),
            cookies=data.get("cookies"),
            headers=data.get("headers"),
            raw=data
        )


@dataclass
class TaskResult:
    status: str
    solution: Optional[Solution] = None
    cost: Optional[str] = None
    create_time: Optional[int] = None
    end_time: Optional[int] = None
    solve_count: Optional[int] = None

    @property
    def is_ready(self) -> bool:
        return self.status == "ready"

    @property
    def is_processing(self) -> bool:
        return self.status == "processing"

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> TaskResult:
        solution = None
        if "solution" in data:
            solution = Solution.from_dict(data["solution"])
        return cls(
            status=data.get("status", ""),
            solution=solution,
            cost=data.get("cost"),
            create_time=data.get("createTime"),
            end_time=data.get("endTime"),
            solve_count=data.get("solveCount")
        )
