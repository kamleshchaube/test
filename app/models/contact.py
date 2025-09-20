from sqlalchemy import Column, String, Boolean, Text
from sqlalchemy.orm import relationship
from app.models.base import BaseModel

class Contact(BaseModel):
    __tablename__ = "contacts"

    account_id = Column(String, nullable=False)
    salutation = Column(String)
    first_name = Column(String, nullable=False)
    middle_name = Column(String)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    phone = Column(String)
    mobile = Column(String)
    designation = Column(String)
    department = Column(String)
    linkedin_profile = Column(String)
    is_decision_maker = Column(Boolean, default=False)
    is_spoc = Column(Boolean, default=False)
    comments = Column(Text)
    lead_source = Column(String)
    assigned_to = Column(String)