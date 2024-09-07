import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy.orm import Session
from faker import Faker
from random import randint, choice, sample
from db import SessionLocal
from models.user_model import UserModel
from models.connection_model import ConnectionModel
from models.achievement_model import AchievementModel
from constants.interest import interest
from constants.achievement_type import achievement_type

# Initialize Faker to generate dummy data
fake = Faker()

# Generate random interests and achievements
MAX_INTEREST_ID = max(interest.keys())
MAX_ACHIEVEMENT_TYPE_ID = max(achievement_type.keys())

# Function to populate users, connections, and achievements
def populate_db(db: Session):
    # Generate dummy users
    users = []
    for _ in range(20):  # Create 20 dummy users
        user = UserModel(
            username=fake.user_name(),
            fakultas=fake.random_element(elements=("Engineering", "Science", "Arts", "Business")),
            jurusan=fake.random_element(elements=("Computer Science", "Electrical Engineering", "Mathematics")),
            angkatan=randint(2015, 2025),
            name=fake.name(),
            bio=fake.text(max_nb_chars=200),
            interest_ids=sample(range(0, MAX_INTEREST_ID), randint(1, 5))  # Each user gets 1-5 random interests
        )
        users.append(user)
        db.add(user)
    
    db.commit()  # Commit users to the database

    # Add achievements to users
    for user in users:
        for _ in range(randint(1, 3)):  # Each user gets 1-3 random achievements
            achievement = AchievementModel(
                title=fake.random_element(elements=list(achievement_type.values())),
                description=fake.text(max_nb_chars=100),
                issued_date=fake.date_between(start_date="-5y", end_date="today"),
                field=choice(range(0, MAX_ACHIEVEMENT_TYPE_ID)),  # Random achievement type
                issuer=fake.company()
            )
            # Append achievement to the user via the relationship
            user.achievements.append(achievement)
            db.add(achievement)

    db.commit()  # Commit achievements to the database

    # Add random connections between users
    for _ in range(30):  # Create 30 random connections
        user1, user2 = choice(users), choice(users)
        if user1 != user2:  # Prevent self-connection
            connection = ConnectionModel(
                first_user_id=user1.id,
                second_user_id=user2.id
            )
            db.add(connection)

    db.commit()  # Commit connections to the database

# Main function to populate the database
def main():
    db = SessionLocal()
    try:
        populate_db(db)
        print("Database populated with dummy data!")
    finally:
        db.close()

if __name__ == "__main__":
    main()