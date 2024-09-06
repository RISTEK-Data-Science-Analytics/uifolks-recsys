from pydantic import BaseModel, Field
from typing import List
from datetime import datetime
from constants.achievement_type import MAX_ACHIEVEMENT_TYPE_ID
from typing_extensions import Annotated

class Achievement(BaseModel):
    achievement_id: int
    title: str
    description: str
    issued_date: datetime
    field: List[Annotated[int, Field(strict=True, ge=0, le=MAX_ACHIEVEMENT_TYPE_ID)]] # Validate the achievements' elements
    issuer: str