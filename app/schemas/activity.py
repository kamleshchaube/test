from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List
from enum import Enum

class ActivityType(str, Enum):
    CALL = "call"
    MEETING = "meeting"
    EMAIL = "email"
    TASK = "task"
    DEMO = "demo"
    PROPOSAL = "proposal"

class ActivityStatus(str, Enum):
    PLANNED = "planned"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class ActivityBase(BaseModel):
    subject: str
    type: ActivityType
    status: ActivityStatus = ActivityStatus.PLANNED
    priority: str = "medium"
    due_date: Optional[datetime] = None
    duration: Optional[int] = None
    description: Optional[str] = None
    related_to_type: Optional[str] = None
    related_to_id: Optional[str] = None
    assigned_to: Optional[str] = None
    outcome: Optional[str] = None

class ActivityCreate(ActivityBase):
    pass

class ActivityUpdate(BaseModel):
    subject: Optional[str] = None
    type: Optional[ActivityType] = None
    status: Optional[ActivityStatus] = None
    priority: Optional[str] = None
    due_date: Optional[datetime] = None
    duration: Optional[int] = None
    description: Optional[str] = None
    related_to_type: Optional[str] = None
    related_to_id: Optional[str] = None
    assigned_to: Optional[str] = None
    outcome: Optional[str] = None

class Activity(ActivityBase):
    id: str
    created_date: datetime
    updated_date: Optional[datetime] = None
    created_by: Optional[str] = None

    class Config:
        from_attributes = True
