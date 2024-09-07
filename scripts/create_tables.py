import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db import engine, Base
from models.user_model import UserModel
from models.connection_model import ConnectionModel
from models.achievement_model import AchievementModel

# Create all tables defined in models
Base.metadata.create_all(bind=engine)