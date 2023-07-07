from typing import Optional, List
from app.src.words.domain.models.word import WordModel
from pydantic import BaseModel


class WordResponseSchema(BaseModel):
    message: Optional[str]
    words: Optional[List[WordModel]]
