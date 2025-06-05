from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime


def create_model(db):
    class Contact(db.Model):
        __tablename__ = "contacts"

        id = Column(Integer, primary_key=True)
        username = Column(String(50), unique=True, nullable=False)
        email = Column(String(120), unique=True, nullable=False)
        password_hash = Column(String(128), nullable=False)
        created_at = Column(DateTime, default=datetime.utcnow)
        updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

        def __repr__(self):
            return f"<Register {self.username}>"

    return Contact
