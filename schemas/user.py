from pydantic import BaseModel, Field
from typing import List
from constants.interest import interest, MAX_INTEREST_ID
from typing_extensions import Annotated

class User(BaseModel):
    username: str
    fakultas: str
    jurusan: str
    angkatan: int
    name: str
    bio: str
    interest_ids: List[Annotated[int, Field(strict=True, ge=0, le=MAX_INTEREST_ID)]] # Validate the interests' elements.
    achievement_ids: List[int]  # Will be validated in achievement schema.

class UserCreate(BaseModel):
    username: str
    fakultas: str
    jurusan: str
    angkatan: int
    name: str
    bio: str