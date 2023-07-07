from typing import Optional, List

from fastapi import Depends, FastAPI, HTTPException

from pydantic import BaseModel

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey, Column, Integer, String

from app.src.core.database import Base


class WordEntity(Base):
    __tablename__ = "words"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
