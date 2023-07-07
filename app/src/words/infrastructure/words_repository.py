from app.src.shared.infrastructure.db_connections import get_db
from fastapi import Depends
from sqlalchemy import func, select, update, case
from typing import List, Optional

from app.api.main import get_db
from app.src.core.database import SessionLocal
from app.src.words.domain.models.word import WordModel
from app.src.words.domain.words_repository import WordsRepository
from app.src.words.infrastructure.entities.word import WordEntity


class WordsSQLAlchemyRepository(WordsRepository):

    def __init__(self, session: SessionLocal = Depends(get_db)):
        self.session = session

    async def get_word_information(self, word: str) -> Optional[WordModel]:
        query = select(WordEntity).where(WordEntity.name == word)
        response = await self.session.execute(query)
        return WordModel.from_orm(response.scalar_one_or_none())

    async def get_all_word(self) -> Optional[List[WordModel]]:
        query = select(WordEntity).all()
        response = await self.session.execute(query)
        return WordModel.from_orm(response)

    async def create_word(self, word: WordModel) -> None:
        self.session.add(word)
        self.session.commit()

    async def delete_word(self, word: str) -> None:
        query = select(Word).where(Word.name == name)
        response = await self.session.execute(query)
        word_to_delete = response.scalar_one_or_none()
        if word_to_delete:
            self.session.delete(response.scalar_one_or_none())
            self.session.commit()
