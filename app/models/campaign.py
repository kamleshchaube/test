from sqlalchemy import Column, String, Text, DateTime, Float, Integer, Boolean, JSON, Enum
from sqlalchemy.dialects.postgresql import UUID
from app.models.base import BaseModel
from datetime import datetime
import enum

class CampaignStatus(enum.Enum):
    draft = "draft"
    scheduled = "scheduled"
    active = "active"
    paused = "paused"
    completed = "completed"
    cancelled = "cancelled"

class CampaignType(enum.Enum):
    email = "email"
    event = "event"
    social_media = "social_media"
    sms = "sms"
    direct_mail = "direct_mail"
    webinar = "webinar"
    content_marketing = "content_marketing"
    ppc = "ppc"

class Campaign(BaseModel):
    __tablename__ = "campaigns"
    
    campaign_id = Column(String(50), nullable=True, unique=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    
    type = Column(Enum(CampaignType), nullable=False)
    status = Column(Enum(CampaignStatus), default=CampaignStatus.draft)
    
    # Budget information - FIXED: Import Float from sqlalchemy
    budget = Column(Float, nullable=True)  # FIXED: Float is now properly imported
    budget_currency = Column(String(10), default="USD")
    spent_budget = Column(Float, default=0.0)
    
    # Performance
    roi = Column(Float, nullable=True)
    revenue_generated = Column(Float, default=0.0)
    
    def __repr__(self):
        return f"<Campaign(name={self.name}, status={self.status})>"