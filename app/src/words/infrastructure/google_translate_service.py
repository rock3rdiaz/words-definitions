import aiohttp
from bs4 import BeautifulSoup
from typing import Optional, List

from app.src.words.domain.models.word import WordModel
from app.src.words.domain.translate_repository import TranslateRepository


class GoogleTranslateService(TranslateRepository):
    """
    Translation service from google API.
    """

    def __init__(self):
        self.URL = 'https://translate.google.com/details'

    async def translate_word(self, word: str) -> Optional[List[WordModel]]:
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{self.URL}?sl=es&tl=es&text={word}&op=translate') as response:
                print("Status:", response.status)
                print("Content-type:", response.headers['content-type'])

                html = await response.text()
                print("Body:", await self.__unwrapper(html[:100]))

    async def __unwrapper(self, html_content: str) -> None:
        soup = BeautifulSoup(html_content, 'html.parser')
        definitions = soup.find_all('div', class_='Dwvecf')
