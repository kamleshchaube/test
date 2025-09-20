from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime, date
from enum import Enum

class ProductCategory(str, Enum):
    SOFTWARE = "software"
    HARDWARE = "hardware"
    SERVICES = "services"
    SUPPORT = "support"
    TRAINING = "training"

class UnitOfMeasure(str, Enum):
    EACH = "each"
    LICENSE = "license"
    USER = "user"
    HOUR = "hour"
    MONTH = "month"
    YEAR = "year"

class ProductBase(BaseModel):
    sku: str = Field(..., min_length=1, max_length=50)
    name: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = None
    category: Optional[ProductCategory] = None
    unit_of_measure: UnitOfMeasure = UnitOfMeasure.EACH
    is_active: bool = True
    standard_price: Optional[float] = Field(None, ge=0)
    input_cost: Optional[float] = Field(None, ge=0)
    cost_currency: str = "USD"
    margin_percentage: Optional[float] = Field(None, ge=0, le=100)
    supplier: Optional[str] = None
    last_cost_update: Optional[date] = None

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    sku: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    category: Optional[ProductCategory] = None
    is_active: Optional[bool] = None
    standard_price: Optional[float] = None
    input_cost: Optional[float] = None
    margin_percentage: Optional[float] = None

class Product(ProductBase):
    id: str
    created_date: datetime
    updated_date: Optional[datetime] = None
    created_by: Optional[str] = None

    class Config:
        from_attributes = True