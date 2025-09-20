from sqlalchemy import Column, String, Boolean, Text
from sqlalchemy.orm import relationship
from app.models.base import BaseModel

class Department(BaseModel):
    __tablename__ = "departments"

    name = Column(String, nullable=False, unique=True)
    description = Column(Text)
    is_active = Column(Boolean, default=True)
    head_of_department = Column(String)  # User ID
    budget = Column(String)
    cost_center = Column(String)
    parent_department_id = Column(String)
    
    # Relationships
    users = relationship("User", foreign_keys="User.department_id", back_populates="department")
    parent_department = relationship("Department", remote_side=[id])