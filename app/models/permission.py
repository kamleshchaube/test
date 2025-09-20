from sqlalchemy import Column, String, Text
from sqlalchemy.orm import relationship
from app.models.base import BaseModel

class Permission(BaseModel):
    __tablename__ = "permissions"

    name = Column(String, nullable=False, unique=True)
    description = Column(Text)
    entity = Column(String, nullable=False)
    action = Column(String, nullable=False)
    resource = Column(String)  # Specific resource if needed
    conditions = Column(Text)  # JSON conditions
    category = Column(String, default="general")
    
    # Relationships
    roles = relationship("RolePermission", back_populates="permission")