from pydantic import BaseModel, Field
from typing import List
from constants.interest import interest, MAX_INTEREST_ID
from typing_extensions import Annotated

class User(BaseModel):
    user_id: str
    username: str
    fakultas: str
    jurusan: str
    angkatan: int
    name: str
    bio: str
    interest_ids: List[Annotated[int, Field(strict=True, ge=0, le=MAX_INTEREST_ID)]]  # Validate the interests' elements
    achievement_ids: List[str]  # Will be validated in the achievement schema

class UserCreate(BaseModel):
    username: str
    fakultas: str
    jurusan: str
    angkatan: int
    name: str
    bio: str