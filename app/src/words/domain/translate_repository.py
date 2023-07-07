from abc import ABC, abstractmethod
from typing import List, Optional

from app.src.words.domain.models.word import WordModel


class TranslateRepository(ABC):
    """
    Translate repository
    """
    @abstractmethod
    async def translate_word(self, word: str) -> Optional[List[WordModel]]:
        raise NotImplementedError
