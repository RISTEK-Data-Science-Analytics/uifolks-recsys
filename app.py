from typing import List
from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import JSONResponse
from schemas.user import UserCreate, User
from services.connection_recommender_service import ConnectionRecommenderService
from services.user_service import UserService
from services.achievement_service import AchievementService
from sqlalchemy.orm import Session
from config import settings
from db import get_db
import json

app = FastAPI()

@app.post("/users/")
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    user_service = UserService(db)
    return user_service.create_user(user_data)

@app.get("/users/{username}")
def get_user(username: str, db: Session = Depends(get_db)):
    user_service = UserService(db)
    user = user_service.get_user(username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# New route to fetch all users
@app.get("/users/", response_model=List[User])
def get_all_users(db: Session = Depends(get_db)):
    user_service = UserService(db)
    users = user_service.get_all_users()
    return users

@app.get("/users/{user_id}/recommendations")
def recommend_connections(user_id: str, top_n: int = 5, db: Session = Depends(get_db)):
    # Fetch the full details of the current user using user_id
    user_service = UserService(db)
    current_user = user_service.get_user_by_id(user_id)
    
    if not current_user:
        raise HTTPException(status_code=404, detail="User not found")

    # Generate recommendations using user_id
    recommender_service = ConnectionRecommenderService(db)
    recommendations_user_ids = recommender_service.recommend_connections(user_id, algorithms=settings.ALGORITHMS)

    # Fetch the full details of the recommended users
    recommended_users = []
    for rec_user_id in recommendations_user_ids:
        recommended_user = user_service.get_user_by_id(rec_user_id)
        if recommended_user:
            recommended_users.append(recommended_user)
    
    # Return full details of current user and their recommendations
    return {
        "current_user": current_user,
        "recommended_users": recommended_users
    }