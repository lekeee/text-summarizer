from fastapi import APIRouter

from app.schemas.methods import SummaryMethod
from app.services.summarizers.registry import METHODS

router = APIRouter(tags=["metode"])


@router.get("/methods", response_model=list[SummaryMethod])
def list_methods() -> list[SummaryMethod]:
    return METHODS
