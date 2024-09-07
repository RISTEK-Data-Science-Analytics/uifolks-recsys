from sqlalchemy import Table, Column, Integer, ForeignKey
from db import Base

# Association table to link users and achievements
user_achievement_association = Table(
    'user_achievement', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('achievement_id', Integer, ForeignKey('achievements.id'))
)