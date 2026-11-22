from pydantic import BaseModel


class ExtractResponse(BaseModel):
    file_name: str
    text: str
    words: int
    sentences: int
    pages: int
