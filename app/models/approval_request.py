from sqlalchemy import Column, String, DateTime, Text, Boolean, Integer
from sqlalchemy.orm import relationship
from app.models.base import BaseModel

class ApprovalRequest(BaseModel):
    __tablename__ = "approval_requests"

    workflow_id = Column(String, nullable=False)
    entity_type = Column(String, nullable=False)
    entity_id = Column(String, nullable=False)
    stage = Column(String)
    requested_by = Column(String, nullable=False)
    requested_at = Column(DateTime)
    status = Column(String, default="pending")  # pending, approved, rejected, cancelled, expired
    approver_id = Column(String)
    approved_at = Column(DateTime)
    rejection_reason = Column(Text)
    approval_notes = Column(Text)
    priority = Column(String, default="medium")
    due_date = Column(DateTime)
    escalated = Column(Boolean, default=False)
    escalated_to = Column(String)
    escalated_at = Column(DateTime)
    approval_level = Column(Integer, default=1)
    total_approvals_needed = Column(Integer, default=1)
    current_approvals = Column(Integer, default=0)
    
    # Relationships
    workflow = relationship("ApprovalWorkflow", foreign_keys=[workflow_id], back_populates="requests")