from sqlalchemy import Column, String, Float, DateTime
from sqlalchemy.dialects.postgresql import UUID
from app.models.base import BaseModel
from datetime import datetime

class PurchaseCost(BaseModel):
    __tablename__ = "purchase_costs"
    
    product_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    sku = Column(String(100), nullable=True)
    
    cost_per_unit = Column(Float, nullable=False)
    currency = Column(String(10), default="USD", nullable=False)
    vendor_name = Column(String(255), nullable=True)
    effective_date = Column(DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f"<PurchaseCost(sku={self.sku}, cost={self.cost_per_unit} {self.currency})>"