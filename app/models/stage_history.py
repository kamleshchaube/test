from sqlalchemy import Column, String, Text, DateTime, Boolean
from sqlalchemy.dialects.postgresql import UUID
from app.models.base import BaseModel
from datetime import datetime

class StageHistory(BaseModel):
    __tablename__ = "stage_history"
    
    opportunity_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    from_stage = Column(String(50), nullable=True)  # Previous stage
    to_stage = Column(String(50), nullable=False)   # New stage
    changed_by = Column(String(255), nullable=False)  # User who made change
    notes = Column(Text, nullable=True)
    activity_created = Column(Boolean, default=False)
    changed_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    
    def __repr__(self):
        return f"<StageHistory(opportunity_id={self.opportunity_id}, to_stage={self.to_stage})>"