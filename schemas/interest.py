from pydantic import BaseModel

class Interest(BaseModel):
    interest_id: int
    interest_name: str