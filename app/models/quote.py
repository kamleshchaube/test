from sqlalchemy import Column, String, Float, DateTime, Text, Enum, Integer
from sqlalchemy.orm import relationship
from app.models.base import BaseModel
import enum

class QuoteStatus(str, enum.Enum):
    DRAFT = "draft"
    SUBMITTED = "submitted"
    APPROVED = "approved"
    REJECTED = "rejected"
    SENT_TO_CLIENT = "sent_to_client"
    ACCEPTED = "accepted"
    EXPIRED = "expired"

class Quote(BaseModel):
    __tablename__ = "quotes"

    quote_number = Column(String, unique=True, index=True)
    opportunity_id = Column(String, nullable=False)
    price_list_id = Column(String)
    status = Column(Enum(QuoteStatus), default=QuoteStatus.DRAFT)
    version = Column(Integer, default=1)
    digital_signature_url = Column(String)
    revision_comments = Column(Text)
    valid_until = Column(DateTime)
    subtotal = Column(Float, default=0.0)
    tax_rate = Column(Float, default=0.0)
    tax_amount = Column(Float, default=0.0)
    total_amount = Column(Float, default=0.0)
    notes = Column(Text)
    terms_conditions = Column(Text)
    approved_by = Column(String)
    approved_at = Column(DateTime)
    rejection_reason = Column(Text)
    
    # Relationships
    items = relationship("QuoteItem", back_populates="quote")