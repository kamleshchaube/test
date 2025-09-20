from sqlalchemy import Column, String, Text, DateTime
from sqlalchemy.dialects.postgresql import UUID
from app.models.base import BaseModel
from datetime import datetime

class ProjectHistory(BaseModel):
    __tablename__ = "project_history"
    
    project_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    from_status = Column(String(50), nullable=True)  # Previous status
    to_status = Column(String(50), nullable=False)   # New status
    changed_by = Column(String(255), nullable=False)  # User who made change
    reason = Column(String(500), nullable=True)      # Reason for change
    comment = Column(Text, nullable=True)            # Additional comments
    changed_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    
    def __repr__(self):
        return f"<ProjectHistory(project_id={self.project_id}, to_status={self.to_status})>"