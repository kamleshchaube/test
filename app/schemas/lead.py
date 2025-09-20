from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime
from enum import Enum

class TenderType(str, Enum):
    TENDER = "tender"
    PRE_TENDER = "pre_tender"
    POST_TENDER = "post_tender"
    NON_TENDER = "non_tender"

class LeadStatus(str, Enum):
    NEW = "new"
    CONTACTED = "contacted"
    QUALIFIED = "qualified"
    NURTURING = "nurturing"
    UNQUALIFIED = "unqualified"
    PENDING_APPROVAL = "pending_approval"
    APPROVED = "approved"
    REJECTED = "rejected"
    CONVERTED = "converted"

class LeadSource(str, Enum):
    WEBSITE = "website"
    REFERRAL = "referral"
    COLD_CALL = "cold_call"
    EMAIL_CAMPAIGN = "email_campaign"
    SOCIAL_MEDIA = "social_media"
    TRADE_SHOW = "trade_show"
    EVENT = "event"
    OTHER = "other"

class LeadBase(BaseModel):
    first_name: str = Field(..., min_length=1, max_length=100)
    last_name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    phone: Optional[str] = None
    company: str = Field(..., min_length=1, max_length=255)
    account_id: str
    title: Optional[str] = None
    status: LeadStatus = LeadStatus.NEW
    source: Optional[LeadSource] = None
    lead_score: float = Field(default=0.0, ge=0, le=100)
    notes: Optional[str] = None
    assigned_to: Optional[str] = None
    tender_type: TenderType = TenderType.NON_TENDER
    project_title: Optional[str] = None
    state: Optional[str] = None
    partner_id: Optional[str] = None
    lead_subtype: str = "direct"
    product_id: Optional[str] = None
    is_enquiry: bool = False
    billing_type: Optional[str] = None
    expected_orc: Optional[float] = None
    approval_status: str = "not_submitted"
    proof_urls: List[str] = Field(default_factory=list)

class LeadCreate(LeadBase):
    pass

class LeadUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    company: Optional[str] = None
    account_id: Optional[str] = None
    status: Optional[LeadStatus] = None
    notes: Optional[str] = None
    tender_type: Optional[TenderType] = None
    billing_type: Optional[str] = None
    expected_orc: Optional[float] = None

class Lead(LeadBase):
    id: str
    created_date: datetime
    updated_date: Optional[datetime] = None
    created_by: Optional[str] = None

    class Config:
        from_attributes = True