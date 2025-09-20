from sqlalchemy import Column, String, Boolean, Integer, Float, Text, Enum
from app.models.base import BaseModel
import enum

class AccountType(str, enum.Enum):
    PROSPECT = "prospect"
    CUSTOMER = "customer"
    PARTNER = "partner"
    VENDOR = "vendor"

class Industry(str, enum.Enum):
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

class BusinessType(str, enum.Enum):
    B2B = "b2b"
    B2C = "b2c"
    B2B2C = "b2b2c"

class Region(str, enum.Enum):
    APAC = "apac"
    EMEA = "emea"
    AMERICAS = "americas"
    MEA = "mea"

class Account(BaseModel):
    __tablename__ = "accounts"

    name = Column(String, nullable=False, index=True)
    gst_number = Column(String, unique=True)
    pan_number = Column(String, unique=True)
    company_type = Column(String)
    account_type = Column(Enum(AccountType), default=AccountType.PROSPECT)
    region = Column(Enum(Region))
    business_type = Column(Enum(BusinessType))
    industry = Column(Enum(Industry))
    sub_industry = Column(String)
    billing_record_id = Column(String)
    website = Column(String)
    is_child = Column(Boolean, default=False)
    parent_company_id = Column(String)
    address = Column(Text)
    employee_count = Column(Integer, default=0)
    country_id = Column(String)
    state_id = Column(String)
    city_id = Column(String)
    annual_revenue = Column(Float)
    currency = Column(String, default="USD")
    status = Column(Boolean, default=True)
    lead_status = Column(String)
    lead_score = Column(Float)
    gc_approval_required = Column(Boolean, default=False)
    gc_approved = Column(Boolean, default=False)
    gc_approved_by = Column(String)
    gc_approved_at = Column(String)
    remarks = Column(Text)
    phone = Column(String)
    type = Column(Enum(AccountType), default=AccountType.PROSPECT)
    segment = Column(String)
    vertical = Column(String)
    billing_address = Column(Text)
    shipping_address = Column(Text)
    description = Column(Text)
    assigned_to = Column(String)