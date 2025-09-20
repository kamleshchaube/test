from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional, List
from enum import Enum

class ProjectStatus(str, Enum):
    PLANNING = "planning"
    IN_DELIVERY = "in_delivery"
    PARTIALLY_DELIVERED = "partially_delivered"
    DELIVERED_AWAITING_SIGNOFF = "delivered_awaiting_signoff"
    AWAITING_HOD_APPROVAL = "awaiting_hod_approval"
    CLOSED = "closed"
    REJECTED = "rejected"
    CANCELLED = "cancelled"

class ProjectBase(BaseModel):
    name: str
    opportunity_id: str

    account_id: str
    contact_id: Optional[str] = None
    quote_id: Optional[str] = None
    status: ProjectStatus = ProjectStatus.PLANNING
    project_manager: Optional[str] = None
    coordinator: Optional[str] = None
    sd_owner: str
    total_value: Optional[float] = None
    start_date: Optional[date] = None
    planned_end_date: Optional[date] = None
    description: Optional[str] = None
    notes: Optional[str] = None

class ProjectCreate(ProjectBase):
    pass

class ProjectUpdate(BaseModel):
    name: Optional[str] = None
    status: Optional[ProjectStatus] = None
    project_manager: Optional[str] = None
    coordinator: Optional[str] = None
    total_value: Optional[float] = None
    start_date: Optional[date] = None
    planned_end_date: Optional[date] = None
    actual_end_date: Optional[date] = None
    description: Optional[str] = None
    notes: Optional[str] = None
    rejection_reason: Optional[str] = None
    cancellation_reason: Optional[str] = None

class ProjectStatusUpdate(BaseModel):
    status: ProjectStatus
    reason: Optional[str] = None
    comment: Optional[str] = None

class Project(ProjectBase):
    id: str
    created_date: datetime
    updated_date: Optional[datetime] = None
    created_by: Optional[str] = None
    actual_end_date: Optional[date] = None
    client_signoff_file_url: Optional[str] = None
    client_signoff_uploaded_at: Optional[datetime] = None
    client_signoff_uploaded_by: Optional[str] = None
    closed_at: Optional[datetime] = None
    closed_by: Optional[str] = None
    rejection_reason: Optional[str] = None
    cancellation_reason: Optional[str] = None

    class Config:
        from_attributes = True