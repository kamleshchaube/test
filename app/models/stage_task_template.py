from sqlalchemy import Column, String, Boolean, Integer, Text, JSON
from sqlalchemy.orm import relationship
from app.models.base import BaseModel

class StageTaskTemplate(BaseModel):
    __tablename__ = "stage_task_templates"

    template_name = Column(String, nullable=False)
    entity_type = Column(String, nullable=False)
    stage = Column(String, nullable=False)
    task_title = Column(String, nullable=False)
    task_description = Column(Text)
    task_type = Column(String, default="checklist_item")
    is_mandatory = Column(Boolean, default=True)
    auto_assign_to = Column(String, default="opportunity_owner")
    auto_assign_role = Column(String)
    estimated_duration = Column(Integer)
    due_days_from_stage_entry = Column(Integer, default=1)
    task_order = Column(Integer, default=0)
    prerequisites = Column(JSON)
    is_active = Column(Boolean, default=True)
    checklist_items = Column(JSON)
    form_fields = Column(JSON)
    
    # Relationships
    tasks = relationship("OpportunityTask", back_populates="template")