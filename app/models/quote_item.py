from sqlalchemy import Column, String, Float, Text
from sqlalchemy.orm import relationship
from app.models.base import BaseModel

class QuoteItem(BaseModel):
    __tablename__ = "quote_items"

    quote_id = Column(String, nullable=False)
    product_id = Column(String)
    group_phase = Column(String)
    quantity = Column(Float, nullable=False)
    unit_price = Column(Float, nullable=False)
    discount_percent = Column(Float, default=0.0)
    discount_amount = Column(Float, default=0.0)
    line_total = Column(Float, nullable=False)
    description = Column(Text)
    
    # Relationships
    quote = relationship("Quote", back_populates="items")