from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from app.models.base import BaseModel

class RolePermission(BaseModel):
    __tablename__ = "role_permissions"

    role_id = Column(String, nullable=False)
    permission_id = Column(String, nullable=False)
    granted_by = Column(String)
    granted_at = Column(String)
    conditions = Column(String)  # JSON conditions for conditional permissions
    
    # Relationships
    role = relationship("Role", foreign_keys=[role_id], back_populates="permissions")
    permission = relationship("Permission", foreign_keys=[permission_id], back_populates="roles")