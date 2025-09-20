from sqlalchemy import Column, String, Text, DateTime, Float, Boolean, Enum
from sqlalchemy.dialects.postgresql import UUID
from app.models.base import BaseModel
from datetime import datetime
import enum

class ProjectStatus(enum.Enum):
    planning = "planning"
    in_delivery = "in_delivery"
    partially_delivered = "partially_delivered"
    delivered_awaiting_signoff = "delivered_awaiting_signoff"
    awaiting_hod_approval = "awaiting_hod_approval"
    closed = "closed"
    rejected = "rejected"
    cancelled = "cancelled"

class Project(BaseModel):
    __tablename__ = "projects"
    
    name = Column(String(255), nullable=False)
    opportunity_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    account_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    contact_id = Column(UUID(as_uuid=True), nullable=True)
    quote_id = Column(UUID(as_uuid=True), nullable=True)
    
    status = Column(Enum(ProjectStatus), default=ProjectStatus.planning)
    project_manager = Column(String(255), nullable=True)
    coordinator = Column(String(255), nullable=True)
    sd_owner = Column(String(255), nullable=False)
    
    total_value = Column(Float, nullable=True)
    start_date = Column(DateTime, nullable=True)
    planned_end_date = Column(DateTime, nullable=True)
    actual_end_date = Column(DateTime, nullable=True)
    
    client_signoff_file_url = Column(String(512), nullable=True)
    client_signoff_uploaded_at = Column(DateTime, nullable=True)
    client_signoff_uploaded_by = Column(String(255), nullable=True)
    
    closed_at = Column(DateTime, nullable=True)
    closed_by = Column(String(255), nullable=True)
    rejection_reason = Column(Text, nullable=True)
    cancellation_reason = Column(Text, nullable=True)
    
    description = Column(Text, nullable=True)
    notes = Column(Text, nullable=True)
    
    def __repr__(self):
        return f"<Project(name={self.name}, status={self.status})>"