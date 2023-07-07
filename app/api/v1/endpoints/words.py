from fastapi import APIRouter, Depends, HTTPException, Response
from starlette import status
from typing import List, Union, Type

from app.api.v1.endpoints.schemas.words import WordResponseSchema
from app.src.words.application.services.words import get_word, add_word
from app.src.words.domain.models.word import WordModel

router = APIRouter()


@router.get(
    "/{word}",
    status_code=status.HTTP_200_OK,
    summary="| Get a word's information"
)
async def get_word(
        word: str
) -> WordResponseSchema:
    word = await get_word(word)
    return WordResponseSchema(word=word)


@router.get(
    status_code=status.HTTP_200_OK,
    summary="| Get all words information"
)
async def get_words(
        word: str
) -> WordResponseSchema:
    words = await get_words(word)
    return WordResponseSchema(words=words)


@router.post(
    status_code=status.HTTP_201_CREATED,
    summary="| Save a word's information"
)
async def create_word(
        word: WordModel
) -> WordResponseSchema:
    word = await add_word(word)
    return WordResponseSchema(word=word)
