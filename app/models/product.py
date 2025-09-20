from sqlalchemy import Column, String, Float, Boolean, DateTime, Text
from app.models.base import BaseModel
import enum

class ProductCategory(str, enum.Enum):
    SOFTWARE = "software"
    HARDWARE = "hardware"
    SERVICES = "services"
    SUPPORT = "support"
    TRAINING = "training"

class UnitOfMeasure(str, enum.Enum):
    EACH = "each"
    LICENSE = "license"
    USER = "user"
    HOUR = "hour"
    MONTH = "month"
    YEAR = "year"

class Currency(str, enum.Enum):
    USD = "USD"
    EUR = "EUR"
    GBP = "GBP"
    INR = "INR"

class Product(BaseModel):
    __tablename__ = "products"
    
    sku = Column(String, unique=True, nullable=False, index=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    category = Column(String)
    unit_of_measure = Column(String, default="each")
    is_active = Column(Boolean, default=True)
    standard_price = Column(Float)
    input_cost = Column(Float)
    cost_currency = Column(String, default="USD")
    margin_percentage = Column(Float)
    supplier = Column(String)
    last_cost_update = Column(DateTime)