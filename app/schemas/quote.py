from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional, List
from enum import Enum

class QuoteStatus(str, Enum):
    DRAFT = "draft"
    SUBMITTED = "submitted"
    APPROVED = "approved"
    REJECTED = "rejected"
    SENT_TO_CLIENT = "sent_to_client"
    ACCEPTED = "accepted"
    EXPIRED = "expired"

class QuoteItemBase(BaseModel):
    product_id: Optional[str] = None
    group_phase: Optional[str] = None
    quantity: float
    unit_price: float
    discount_percent: float = 0.0
    discount_amount: float = 0.0
    line_total: float
    description: Optional[str] = None

class QuoteItemCreate(QuoteItemBase):
    pass

class QuoteItem(QuoteItemBase):
    id: str
    quote_id: str
    created_date: datetime

    class Config:
        from_attributes = True

class QuoteBase(BaseModel):
    quote_number: Optional[str] = None
    opportunity_id: str
    price_list_id: Optional[str] = None
    status: QuoteStatus = QuoteStatus.DRAFT
    version: int = 1
    valid_until: Optional[date] = None
    tax_rate: float = 0.0
    notes: Optional[str] = None
    terms_conditions: Optional[str] = None

class QuoteCreate(QuoteBase):
    items: List[QuoteItemCreate] = []

class QuoteUpdate(BaseModel):
    status: Optional[QuoteStatus] = None
    valid_until: Optional[date] = None
    tax_rate: Optional[float] = None
    notes: Optional[str] = None
    terms_conditions: Optional[str] = None
    revision_comments: Optional[str] = None
    rejection_reason: Optional[str] = None

class Quote(QuoteBase):
    id: str
    created_date: datetime
    updated_date: Optional[datetime] = None
    subtotal: float = 0.0
    tax_amount: float = 0.0
    total_amount: float = 0.0
    digital_signature_url: Optional[str] = None
    revision_comments: Optional[str] = None
    approved_by: Optional[str] = None
    approved_at: Optional[datetime] = None
    rejection_reason: Optional[str] = None
    items: List[QuoteItem] = []

    class Config:
        from_attributes = True