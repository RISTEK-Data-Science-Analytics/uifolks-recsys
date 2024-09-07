from sqlalchemy.orm import Session
from schemas.connection import Connection
from models.connection_model import ConnectionModel

class ConnectionDataService:
    def __init__(self, db: Session):
        self.db = db

    def add_connection(self, connection_data: Connection):
        """Create a new connection between two users."""
        connection = ConnectionModel(**connection_data.dict())
        self.db.add(connection)
        self.db.commit()
        return connection

    def get_user_connections(self, user_id: str):
        """Fetch user connections from the database and return as a list of (user1, user2) tuples."""
        user_connections = self.db.query(ConnectionModel).filter(
            (ConnectionModel.first_user_id == user_id) | 
            (ConnectionModel.second_user_id == user_id)
        ).all()
        
        user_edges = [(conn.first_user_id, conn.second_user_id) for conn in user_connections]

        return list(user_edges)
    
    def get_all_connections(self):
        all_connections = self.db.query(ConnectionModel).all()
        all_edges = [(conn.first_user_id, conn.second_user_id) for conn in all_connections]
        
        return list(all_edges)

    def delete_connection(self, first_username: str, second_username: str):
        """Delete a connection between two users."""
        connection = self.db.query(ConnectionModel).filter(
            (ConnectionModel.first_username == first_username) &
            (ConnectionModel.second_username == second_username)
        ).first()
        if connection:
            self.db.delete(connection)
            self.db.commit()
        return connection