import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID

def create_model(db):
    class Register(db.Model):
        __tablename__ = "registers"

        id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
        username = Column(String(255), unique=True, nullable=False)
        email = Column(String(255), unique=True, nullable=False)
        password_hash = Column(String(255), nullable=False)
        created_at = Column(DateTime, default=datetime.utcnow)
        updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

        def __repr__(self):
            return f"<Register {self.username}>"

    return Register