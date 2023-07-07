from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status
from typing import List, Union, Type

from app.api.v1.endpoints.schemas.words import WordResponseSchema
from app.src.words.application.services.words import WordsServices
from app.src.words.domain.models.word import WordModel

router = APIRouter()


@router.get(
    '/{word}',
    status_code=status.HTTP_200_OK,
    summary="| Get a word's information"
)
async def search_word(
        word: str,
        words_services: WordsServices = Depends(WordsServices)
) -> WordResponseSchema:
    word = await words_services.get_word(word)
    return WordResponseSchema(words=word)


@router.get(
    '/',
    status_code=status.HTTP_200_OK,
    summary="| Get all words information"
)
async def get_all_words(
        words_services: WordsServices = Depends(WordsServices)
) -> WordResponseSchema:
    words = await words_services.get_words()
    return WordResponseSchema(words=words)


@router.post(
    '/',
    status_code=status.HTTP_201_CREATED,
    summary="| Save a word's information"
)
async def create_word(
        word: WordModel,
        words_services: WordsServices = Depends(WordsServices)
) -> WordResponseSchema:
    word = await words_services.add_word(word)
    return WordResponseSchema(words=word)


@router.delete(
    '/{word}',
    status_code=status.HTTP_200_OK,
    summary="| Remove a word's information"
)
async def delete_word(
        word: str,
        words_services: WordsServices = Depends(WordsServices)
) -> WordResponseSchema:
    word = await words_services.remove_word(word)
    return WordResponseSchema(words=word)
