from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship
from app.models.base import BaseModel

class State(BaseModel):
    __tablename__ = "states"

    name = Column(String, nullable=False)
    code = Column(String)
    country_id = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    region = Column(String)
    
    # Relationships
    country = relationship("Country", foreign_keys=[country_id], back_populates="states")
    cities = relationship("City", back_populates="state")