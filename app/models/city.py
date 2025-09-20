from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship
from app.models.base import BaseModel

class City(BaseModel):
    __tablename__ = "cities"

    name = Column(String, nullable=False)
    state_id = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    postal_code = Column(String)
    latitude = Column(String)
    longitude = Column(String)
    
    # Relationships
    state = relationship("State", foreign_keys=[state_id], back_populates="cities")