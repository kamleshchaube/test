from sqlalchemy import Column, String, Text, JSON
from sqlalchemy.orm import relationship
from app.models.base import BaseModel

class AuditLog(BaseModel):
    __tablename__ = "audit_logs"

    entity_type = Column(String, nullable=False)
    entity_id = Column(String)
    action = Column(String, nullable=False)
    user_id = Column(String)
    user_email = Column(String)
    ip_address = Column(String)
    user_agent = Column(String)
    session_id = Column(String)
    details = Column(JSON)
    old_values = Column(JSON)
    new_values = Column(JSON)
    request_id = Column(String)
    severity = Column(String, default="info")  # info, warning, error, critical
    
    # Relationships
    user = relationship("User", foreign_keys=[user_id], back_populates="audit_logs")