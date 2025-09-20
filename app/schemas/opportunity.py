from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Dict, Any, List
from enum import Enum

class OpportunityStage(str, Enum):
    PROSPECTING = "prospecting"
    QUALIFICATION = "qualification"
    PROPOSAL = "proposal"
    TECHNICAL_QUALIFICATION = "technical_qualification"
    COMMERCIAL_NEGOTIATION = "commercial_negotiation"
    WON = "won"
    LOST = "lost"
    DROPPED = "dropped"

class OpportunityBase(BaseModel):
    name: str
    account_id: str
    contact_id: Optional[str] = None
    amount: float
    currency: str = "USD"
    stage: OpportunityStage = OpportunityStage.PROSPECTING
    probability: float = 10.0
    close_date: datetime
    next_step: Optional[str] = None
    description: Optional[str] = None
    assigned_to: Optional[str] = None
    region: Optional[str] = None
    product_interest: Optional[str] = None
    go_no_go_checklist: Optional[Dict[str, Any]] = {}
    stakeholders: Optional[List[str]] = []
    competitor_name: Optional[str] = None
    lost_reason: Optional[str] = None
    drop_reason: Optional[str] = None
    final_value: Optional[float] = None

class OpportunityCreate(OpportunityBase):
    pass

class OpportunityUpdate(BaseModel):
    name: Optional[str] = None
    amount: Optional[float] = None
    stage: Optional[OpportunityStage] = None
    probability: Optional[float] = None
    close_date: Optional[datetime] = None
    next_step: Optional[str] = None
    description: Optional[str] = None
    final_value: Optional[float] = None

class Opportunity(OpportunityBase):
    id: str
    created_date: datetime
    updated_date: Optional[datetime] = None
    created_by: Optional[str] = None

    class Config:
        from_attributes = True