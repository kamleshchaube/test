from sqlalchemy import Column, String, DateTime, Text, JSON, Boolean
from sqlalchemy.orm import relationship
from app.models.base import BaseModel

class OpportunityTask(BaseModel):
    __tablename__ = "opportunity_tasks"

    template_id = Column(String)
    opportunity_id = Column(String, nullable=False)
    stage = Column(String, nullable=False)
    task_title = Column(String, nullable=False)
    task_description = Column(Text)
    task_type = Column(String, default="checklist_item")
    assigned_to = Column(String, nullable=False)
    status = Column(String, default="not_started")
    priority = Column(String, default="medium")
    due_date = Column(DateTime)
    started_at = Column(DateTime)
    completed_at = Column(DateTime)
    completion_notes = Column(Text)
    uploaded_files = Column(JSON)
    checklist_data = Column(JSON)
    form_data = Column(JSON)
    is_mandatory = Column(Boolean, default=True)
    blocked_reason = Column(Text)
    
    # Relationships
    template = relationship("StageTaskTemplate", foreign_keys=[template_id], back_populates="tasks")