from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.dialects.postgresql import UUID
from app.models.base import BaseModel
from datetime import datetime

class CustomerRateCard(BaseModel):
    __tablename__ = "customer_rate_cards"
    
    account_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    rate_card_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    
    priority = Column(Integer, default=1)  # 1 = highest priority
    assigned_by = Column(String(255), nullable=True)
    assigned_at = Column(DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f"<CustomerRateCard(account_id={self.account_id}, rate_card_id={self.rate_card_id})>"