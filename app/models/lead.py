from sqlalchemy import Column, String, Float, Boolean, Text, Enum, JSON
from sqlalchemy.orm import relationship
from app.models.base import BaseModel
import enum

class TenderType(str, enum.Enum):
    TENDER = "tender"
    PRE_TENDER = "pre_tender"
    POST_TENDER = "post_tender"
    NON_TENDER = "non_tender"

class LeadStatus(str, enum.Enum):
    NEW = "new"
    CONTACTED = "contacted"
    QUALIFIED = "qualified"
    NURTURING = "nurturing"
    UNQUALIFIED = "unqualified"
    PENDING_APPROVAL = "pending_approval"
    APPROVED = "approved"
    REJECTED = "rejected"
    CONVERTED = "converted"

class LeadSource(str, enum.Enum):
    WEBSITE = "website"
    REFERRAL = "referral"
    COLD_CALL = "cold_call"
    EMAIL_CAMPAIGN = "email_campaign"
    SOCIAL_MEDIA = "social_media"
    TRADE_SHOW = "trade_show"
    EVENT = "event"
    OTHER = "other"

class Lead(BaseModel):
    __tablename__ = "leads"

    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    phone = Column(String)
    company = Column(String, nullable=False)
    account_id = Column(String, nullable=False)
    title = Column(String)
    status = Column(Enum(LeadStatus), default=LeadStatus.NEW)
    source = Column(Enum(LeadSource))
    lead_score = Column(Float, default=0.0)
    notes = Column(Text)
    assigned_to = Column(String)
    tender_type = Column(Enum(TenderType), default=TenderType.NON_TENDER)
    project_title = Column(String)
    state = Column(String)
    partner_id = Column(String)
    lead_subtype = Column(String, default="direct")
    product_id = Column(String)
    is_enquiry = Column(Boolean, default=False)
    billing_type = Column(String)
    expected_orc = Column(Float)
    approval_status = Column(String, default="not_submitted")
    proof_urls = Column(JSON)
    converted_opportunity_id = Column(String)
    converted_at = Column(String)
    converted_by = Column(String)