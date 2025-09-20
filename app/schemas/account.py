from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from enum import Enum

class AccountType(str, Enum):
    PROSPECT = "prospect"
    CUSTOMER = "customer"
    PARTNER = "partner"
    VENDOR = "vendor"

class Industry(str, Enum):
    IT_ITES = "it_ites"
    BFSI = "bfsi"
    HEALTHCARE = "healthcare"
    MANUFACTURING = "manufacturing"
    ENERGY_UTILITIES = "energy_utilities"
    TELECOM = "telecom"
    RETAIL = "retail"
    EDUCATION = "education"
    GOVERNMENT = "government"
    OTHER = "other"

class AccountBase(BaseModel):
    name: str
    gst_number: Optional[str] = None
    pan_number: Optional[str] = None
    account_type: AccountType = AccountType.PROSPECT
    industry: Optional[Industry] = None
    sub_industry: Optional[str] = None
    website: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    billing_address: Optional[str] = None
    shipping_address: Optional[str] = None
    employee_count: int = 0
    annual_revenue: Optional[float] = None
    currency: str = "USD"
    assigned_to: Optional[str] = None
    description: Optional[str] = None

class AccountCreate(AccountBase):
    pass

class AccountUpdate(BaseModel):
    name: Optional[str] = None
    account_type: Optional[AccountType] = None
    industry: Optional[Industry] = None
    website: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    annual_revenue: Optional[float] = None
    assigned_to: Optional[str] = None
    description: Optional[str] = None

class Account(AccountBase):
    id: str
    created_date: datetime
    updated_date: Optional[datetime] = None
    created_by: Optional[str] = None

    class Config:
        from_attributes = True