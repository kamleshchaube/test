from sqlalchemy import Column, String, Float, DateTime, Boolean, Text, Enum, JSON
from app.models.base import BaseModel
import enum

class OpportunityStage(str, enum.Enum):
    PROSPECTING = "prospecting"
    QUALIFICATION = "qualification"
    PROPOSAL = "proposal"
    TECHNICAL_QUALIFICATION = "technical_qualification"
    COMMERCIAL_NEGOTIATION = "commercial_negotiation"
    WON = "won"
    LOST = "lost"
    DROPPED = "dropped"

class Opportunity(BaseModel):
    __tablename__ = "opportunities"

    name = Column(String, nullable=False)
    account_id = Column(String, nullable=False)
    contact_id = Column(String)
    amount = Column(Float, nullable=False)
    currency = Column(String, default="USD")
    stage = Column(Enum(OpportunityStage), default=OpportunityStage.PROSPECTING)
    status = Column(String)
    probability = Column(Float, default=10.0)
    close_date = Column(DateTime, nullable=False)
    next_step = Column(String)
    lead_source = Column(String)
    description = Column(Text)
    assigned_to = Column(String)
    type = Column(String)
    region = Column(String)
    product_interest = Column(String)
    qualification_notes = Column(Text)
    go_no_go_checklist = Column(JSON)
    proposal_document_url = Column(String)
    proposal_submission_date = Column(DateTime)
    stakeholders = Column(JSON)
    approval_status = Column(String, default="not_requested")
    cpc = Column(Float)
    overhead = Column(Float)
    terms_and_conditions = Column(Text)
    po_number = Column(String)
    final_value = Column(Float)
    handover_status = Column(String)
    lost_reason = Column(String)
    competitor_name = Column(String)
    internal_learnings = Column(Text)
    drop_reason = Column(String)
    delivered_to_sd = Column(Boolean, default=False)