from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List
from enum import Enum

class CampaignStatus(str, Enum):
    PLANNED = "planned"
    ACTIVE = "active"
    COMPLETED = "completed"
    PAUSED = "paused"
    CANCELLED = "cancelled"

class CampaignBase(BaseModel):
    name: str
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    status: CampaignStatus = CampaignStatus.PLANNED
    budget: Optional[float] = None
    actual_cost: Optional[float] = None
    expected_revenue: Optional[float] = None
    leads_generated: Optional[int] = 0
    opportunities_created: Optional[int] = 0
    description: Optional[str] = None
    assigned_to: Optional[str] = None

class CampaignCreate(CampaignBase):
    pass

class CampaignUpdate(BaseModel):
    name: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    status: Optional[CampaignStatus] = None
    budget: Optional[float] = None
    actual_cost: Optional[float] = None
    expected_revenue: Optional[float] = None
    leads_generated: Optional[int] = None
    opportunities_created: Optional[int] = None
    description: Optional[str] = None
    assigned_to: Optional[str] = None

class Campaign(CampaignBase):
    id: str
    created_date: datetime
    updated_date: Optional[datetime] = None
    created_by: Optional[str] = None

    class Config:
        from_attributes = True
