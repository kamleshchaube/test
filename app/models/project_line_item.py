from sqlalchemy import Column, String, Text, DateTime, Float, Integer, Enum
from sqlalchemy.dialects.postgresql import UUID
from app.models.base import BaseModel
from datetime import datetime
import enum

class DeliveryStatus(enum.Enum):
    pending = "pending"
    partial = "partial"
    delivered = "delivered"

class ProjectLineItem(BaseModel):
    __tablename__ = "project_line_items"
    
    project_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    quote_item_id = Column(UUID(as_uuid=True), nullable=True)
    product_id = Column(UUID(as_uuid=True), nullable=True)
    
    sku = Column(String(100), nullable=True)
    description = Column(Text, nullable=False)
    
    ordered_quantity = Column(Integer, nullable=False)
    delivered_quantity = Column(Integer, default=0)
    unit_price = Column(Float, nullable=False)
    line_total = Column(Float, nullable=False)
    
    delivery_status = Column(Enum(DeliveryStatus), default=DeliveryStatus.pending)
    delivery_date = Column(DateTime, nullable=True)
    delivery_comment = Column(Text, nullable=True)
    delivered_by = Column(String(255), nullable=True)
    delivery_proof_url = Column(String(512), nullable=True)
    
    def __repr__(self):
        return f"<ProjectLineItem(project_id={self.project_id}, description={self.description})>"