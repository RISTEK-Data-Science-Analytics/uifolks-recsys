from pydantic import BaseModel
from typing import List, Optional, Tuple

from schemas.user import User

class ConnectionRecommenderInput(BaseModel):
    user: User
    all_users: List[User]
    user_connections: List[Tuple[str, str]]
    all_connections: List[Tuple[str, str]]
    interaction_matrix: Optional[dict] = None
    top_n: int = 5
    
class FeedRecommenderInput(BaseModel):
    ...