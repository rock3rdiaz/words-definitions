from sqlalchemy.orm import Session
from typing import Optional, List

from app.api.main import get_db
from app.src.words.domain.models.word import WordModel
from app.src.words.infrastructure.google_translate_service import GoogleTranslateService
from app.src.words.infrastructure.words_repository import WordsRepository
from app.src.words.infrastructure.words_repository import WordsSQLAlchemyRepository

translate_repository = GoogleTranslateService()
words_repository = WordsSQLAlchemyRepository()


async def get_word(word: str) -> Optional[List[WordModel]]:
    """
    Return all word information founded.
    First check in local information, if doesn't exist, check translate service.

    @param word: Word to get
    @return Word founded or None
    """
    word_found = await words_repository.get_word_information(word.strip())
    if word_found:
        return word_found
    word_found = await translate_repository.tanslate_word(word.strip())
    # check if everything is ok
    if word_found:
        words_respository.create_word()
    return word_found


async def get_words() -> Optional[List[WordModel]]:
    """
    Return all words information.

    @param word: Word to get
    @return Word founded or None
    """
    words = await words_repository.get_all_word()
    return words


async def add_word(word: WordModel) -> None:
    """
    Save a Word into local repository.

    @param word: Word to save
    @return None
    """
    try:
        await words_repository.create_word(word)
    except Exception as ex:
        print('-- error: ', str(ex.args))
