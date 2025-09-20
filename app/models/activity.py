from sqlalchemy import Column, String, Integer, DateTime, Text, Enum, JSON
from app.models.base import BaseModel
import enum

class ActivityType(str, enum.Enum):
    CALL = "call"
    MEETING = "meeting"
    EMAIL = "email"
    TASK = "task"
    DEMO = "demo"
    PROPOSAL = "proposal"
    FOLLOW_UP = "follow_up"
    PRESENTATION = "presentation"

class ActivityStatus(str, enum.Enum):
    PLANNED = "planned"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class Activity(BaseModel):
    __tablename__ = "activities"

    subject = Column(String, nullable=False)
    type = Column(Enum(ActivityType), nullable=False)
    status = Column(Enum(ActivityStatus), default=ActivityStatus.PLANNED)
    priority = Column(String, default="medium")
    due_date = Column(DateTime, nullable=False)
    duration = Column(Integer)  # in minutes
    description = Column(Text)
    related_to_type = Column(String, nullable=False)
    related_to_id = Column(String, nullable=False)
    assigned_to = Column(String)
    outcome = Column(Text)
    stage = Column(String)
    location = Column(String)
    attendees = Column(JSON)
    attachments = Column(JSON)