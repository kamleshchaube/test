from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List
from enum import Enum

class ContactBase(BaseModel):
    first_name: str
    last_name: str
    salutation: Optional[str] = None
    email: EmailStr
    phone: Optional[str] = None
    mobile: Optional[str] = None
    account_id: str
    designation: Optional[str] = None
    department: Optional[str] = None
    is_decision_maker: bool = False
    is_spoc: bool = False
    notes: Optional[str] = None
    lead_id: Optional[str] = None

class ContactCreate(ContactBase):
    pass

class ContactUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    salutation: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    mobile: Optional[str] = None
    designation: Optional[str] = None
    department: Optional[str] = None
    is_decision_maker: Optional[bool] = None
    is_spoc: Optional[bool] = None
    notes: Optional[str] = None

class Contact(ContactBase):
    id: str
    created_date: datetime
    updated_date: Optional[datetime] = None
    created_by: Optional[str] = None

    class Config:
        from_attributes = True
