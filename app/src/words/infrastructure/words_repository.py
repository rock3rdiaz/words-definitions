from sqlalchemy import select, func
from sqlalchemy.orm import Session
from typing import List

from app.src.words.domain.models.word import WordModel
from app.src.words.domain.words_repository import WordsRepository
from app.src.words.infrastructure.entities.word import WordEntity


class WordsSQLAlchemyRepository(WordsRepository):

    def __init__(self, session: Session):
        self.session = session

    async def get_word_information(self, word: str, db: Session = None) -> List[WordModel]:
        query = select(WordEntity).filter(WordEntity.name.ilike(f'%{word}%'))
        response = self.session.execute(query).scalars().all()
        if response:
            return [item for item in response]
        return []

    async def get_all_words(self) -> List[WordModel]:
        query = select(WordEntity)
        response = self.session.execute(query).scalars().all()
        if response:
            return [item for item in response]
        return []

    async def create_word(self, word: WordModel) -> None:
        self.session.add(WordEntity(**word.dict()))
        self.session.commit()

    async def delete_word(self, word: str) -> None:
        query = select(WordEntity).where(func.lower(WordEntity.name) == func.lower(word))
        response = self.session.execute(query).scalar_one_or_none()
        if response:
            self.session.delete(response)
            self.session.commit()
