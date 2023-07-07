from fastapi import Depends
from sqlalchemy.orm import Session
from typing import Optional, List

from app.src.core.database import SessionLocal, get_db
from app.src.words.domain.models.word import WordModel
from app.src.words.infrastructure.google_translate_service import GoogleTranslateService
from app.src.words.infrastructure.words_repository import WordsSQLAlchemyRepository


class WordsServices:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db
        self.translate_repository = GoogleTranslateService()
        self.words_repository = WordsSQLAlchemyRepository(self.db)

    async def get_word(self, word: str) -> Optional[List[WordModel]]:
        """
        Return all word information founded.
        First check in local information, if doesn't exist, check translate service.

        @param word: Word to get
        @return Word founded or None
        """
        word_found = await self.words_repository.get_word_information(word.strip())
        if word_found:
            return word_found
        word_found = await self.translate_repository.translate_word(word.strip())
        # check if everything is ok
        if word_found:
            words_respository.create_word()
        return word_found

    async def get_words(self) -> Optional[List[WordModel]]:
        """
        Return all words information.

        @param word: Word to get
        @return Word founded or None
        """
        words = await self.words_repository.get_all_words()
        return words

    async def add_word(self, word: WordModel) -> None:
        """
        Save a Word into local repository.

        @param word: Word to save
        @return None
        """
        try:
            await self.words_repository.create_word(word)
        except Exception as ex:
            print('-- error: ', str(ex.args))

    async def remove_word(self, word: str) -> None:
        """
        Remove a Word into local repository.

        @param word: Word to delete
        @return None
        """
        try:
            await self.words_repository.delete_word(word)
        except Exception as ex:
            print('-- error: ', str(ex.args))
