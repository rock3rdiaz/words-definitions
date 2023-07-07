from pydantic import BaseModel


class WordModel(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
