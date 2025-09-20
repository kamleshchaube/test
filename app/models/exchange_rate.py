from sqlalchemy import Column, String, Float, DateTime
from app.models.base import BaseModel
from datetime import datetime

class ExchangeRate(BaseModel):
    __tablename__ = "exchange_rates"
    
    from_currency = Column(String(10), nullable=False)
    to_currency = Column(String(10), nullable=False)
    rate = Column(Float, nullable=False)
    effective_date = Column(DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f"<ExchangeRate({self.from_currency} -> {self.to_currency}: {self.rate})>"