from sqlalchemy import Column, String, Text, DateTime, Integer
from sqlalchemy.dialects.postgresql import UUID
from app.models.base import BaseModel
from datetime import datetime

class ProjectDeliveryLog(BaseModel):
    __tablename__ = "project_delivery_logs"
    
    project_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    line_item_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    
    delivered_quantity = Column(Integer, nullable=False)
    delivery_date = Column(DateTime, nullable=False)
    delivered_by = Column(String(255), nullable=False)
    comment = Column(Text, nullable=True)
    proof_document_url = Column(String(512), nullable=True)
    
    def __repr__(self):
        return f"<ProjectDeliveryLog(project_id={self.project_id}, quantity={self.delivered_quantity})>"