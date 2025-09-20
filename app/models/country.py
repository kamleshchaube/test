from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship
from app.models.base import BaseModel

class Country(BaseModel):
    __tablename__ = "countries"

    name = Column(String, nullable=False, unique=True)
    code = Column(String, unique=True, nullable=False)
    iso_code = Column(String)
    phone_code = Column(String)
    currency = Column(String)
    timezone = Column(String)
    is_active = Column(Boolean, default=True)
    
    # Relationships
    states = relationship("State", back_populates="country")