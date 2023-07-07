from abc import ABC, abstractmethod
from typing import List

from app.src.words.domain.models.word import WordModel


class WordsRepository(ABC):
    """
    Word repository
    """

    @abstractmethod
    async def get_word_information(self, word: str) -> List[WordModel]:
        raise NotImplementedError

    @abstractmethod
    async def get_all_words(self) -> List[WordModel]:
        raise NotImplementedError

    @abstractmethod
    async def create_word(self, word: WordModel) -> None:
        raise NotImplementedError

    @abstractmethod
    async def delete_word(self, word: str) -> None:
        raise NotImplementedError
