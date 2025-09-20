from sqlalchemy import Column, String, Text, DateTime, Boolean
from app.models.base import BaseModel
from datetime import datetime

class RateCard(BaseModel):
    __tablename__ = "rate_cards"
    
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    currency = Column(String(10), default="USD", nullable=False)
    
    effective_from = Column(DateTime, nullable=False)
    effective_to = Column(DateTime, nullable=True)
    
    is_default = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    
    created_by = Column(String(255), nullable=True)
    approved_by = Column(String(255), nullable=True)
    approved_at = Column(DateTime, nullable=True)
    
    def __repr__(self):
        return f"<RateCard(name={self.name}, currency={self.currency})>"