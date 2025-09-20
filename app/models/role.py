from sqlalchemy import Column, String, Boolean, Text
from sqlalchemy.orm import relationship
from app.models.base import BaseModel

class Role(BaseModel):
    __tablename__ = "roles"

    name = Column(String, nullable=False, unique=True)
    description = Column(Text)
    is_active = Column(Boolean, default=True)
    compliance_tag = Column(Boolean, default=False)
    level = Column(String, default="user")  # user, manager, admin, super_admin
    
    # Relationships
    users = relationship("User", foreign_keys="User.role_id", back_populates="role")
    permissions = relationship("RolePermission", back_populates="role")