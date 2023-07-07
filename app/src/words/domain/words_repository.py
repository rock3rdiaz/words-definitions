from abc import ABC, abstractmethod
from typing import List, Optional
from app.src.words.domain.models.word import WordModel


class WordsRepository(ABC):
    """
    Word repository
    """
    @abstractmethod
    async def get_word_information(self, word: str) -> Optional[List[WordModel]]:
        raise NotImplementedError

    @abstractmethod
    async def get_all_words(self) -> Optional[List[WordModel]]:
        raise NotImplementedError

    @abstractmethod
    async def create_word(self, word: WordModel) -> None:
        raise NotImplementedError

    @abstractmethod
    async def delete_word(self, word: str) -> None:
        raise NotImplementedError

