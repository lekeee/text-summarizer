from fastapi import APIRouter, HTTPException

from app.schemas.summarize import SummarizeRequest, SummarizeResponse
from app.services.summarization import SummarizationError, summarize_text

router = APIRouter(tags=["sažimanje"])


@router.post("/summarize", response_model=SummarizeResponse)
def summarize(request: SummarizeRequest) -> SummarizeResponse:
    try:
        return summarize_text(request.text, request.method, request.ratio)
    except SummarizationError as error:
        raise HTTPException(status_code=400, detail=str(error))
