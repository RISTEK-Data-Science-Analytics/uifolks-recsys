from pydantic import BaseModel
from datetime import datetime

class Connection(BaseModel):
    first_username: str
    second_username: str
    timestamp: datetime