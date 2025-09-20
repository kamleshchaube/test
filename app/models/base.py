import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base

class BaseModel(Base):
    """
    Base model class that includes common fields for all entities
    """
    __abstract__ = True
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    created_date = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_date = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    created_by = Column(String, nullable=True)  # Email of user who created record
    
    def to_dict(self):
        """Convert model instance to dictionary"""
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
        
    def __repr__(self):
        return f"<{self.__class__.__name__}(id={self.id})>"