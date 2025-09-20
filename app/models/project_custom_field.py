from sqlalchemy import Column, String, Float, DateTime, Boolean, Text
from sqlalchemy.orm import relationship
from app.models.base import BaseModel

class ProjectCustomField(BaseModel):
    __tablename__ = "project_custom_fields"
    
    project_id = Column(String, nullable=False)
    field_name = Column(String, nullable=False)
    field_value = Column(Text)
    field_type = Column(String, default="text")  # text, number, date, boolean
    field_label = Column(String)
    
    # For different data types
    value_text = Column(Text)
    value_number = Column(Float)
    value_date = Column(DateTime)
    value_boolean = Column(Boolean)
    
    # Relationships
    project = relationship("Project", back_populates="custom_fields")