from sqlalchemy import Column, String, Boolean, Integer, JSON, Text
from sqlalchemy.orm import relationship
from app.models.base import BaseModel

class ApprovalWorkflow(BaseModel):
    __tablename__ = "approval_workflows"

    workflow_name = Column(String, nullable=False)
    entity_type = Column(String, nullable=False)
    stage = Column(String)
    trigger_conditions = Column(JSON)
    approval_required = Column(Boolean, default=False)
    approver_roles = Column(JSON)
    approver_users = Column(JSON)
    minimum_approvals = Column(Integer, default=1)
    auto_approve_conditions = Column(JSON)
    escalation_rules = Column(JSON)
    notification_settings = Column(JSON)
    is_active = Column(Boolean, default=True)
    workflow_order = Column(Integer, default=0)
    timeout_hours = Column(Integer, default=72)
    
    # Relationships
    requests = relationship("ApprovalRequest", back_populates="workflow")