from typing import Literal

from pydantic import BaseModel


class SummaryMethod(BaseModel):
    id: str
    name: str
    description: str
    kind: Literal["ekstraktivni", "apstraktivni"] | None
    available: bool
