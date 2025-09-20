from sqlalchemy import Column, String, Float, Boolean, DateTime, Text
from sqlalchemy.orm import relationship
from app.models.base import BaseModel

class CustomFieldValue(BaseModel):
    __tablename__ = "custom_field_values"

    definition_id = Column(String, nullable=False)
    entity_id = Column(String, nullable=False)
    value_text = Column(Text)
    value_number = Column(Float)
    value_date = Column(DateTime)
    value_boolean = Column(Boolean)
    value_json = Column(String)  # For complex data types
    
    # Relationships
    definition = relationship("CustomFieldDefinition", foreign_keys=[definition_id], back_populates="values")