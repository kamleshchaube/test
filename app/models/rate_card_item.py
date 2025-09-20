from sqlalchemy import Column, String, Float, Integer, Boolean
from sqlalchemy.dialects.postgresql import UUID
from app.models.base import BaseModel

class RateCardItem(BaseModel):
    __tablename__ = "rate_card_items"
    
    rate_card_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    product_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    sku = Column(String(100), nullable=True)
    
    selling_price = Column(Float, nullable=False)
    minimum_quantity = Column(Integer, default=1)
    maximum_quantity = Column(Integer, nullable=True)
    is_active = Column(Boolean, default=True)
    
    def __repr__(self):
        return f"<RateCardItem(sku={self.sku}, price={self.selling_price})>"