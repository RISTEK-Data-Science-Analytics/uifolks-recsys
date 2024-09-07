import os

class Settings:
    SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./local_dev.db")
    
    # PostgreSQL connection string for production (example)
    # SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/dbname")
    
    ALGORITHMS = ['graph', 'content_based']
    MAX_CONNECTION_RECOMMENDATIONS = 10

settings = Settings()