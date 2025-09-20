from sqlalchemy import Column, String, Boolean, Text, JSON
from sqlalchemy.orm import relationship
from app.models.base import BaseModel

class CustomFieldDefinition(BaseModel):
    __tablename__ = "custom_field_definitions"

    entity_type = Column(String, nullable=False)
    field_name = Column(String, nullable=False)
    field_label = Column(String, nullable=False)
    data_type = Column(String, nullable=False)  # text, number, date, boolean, picklist, multi_picklist
    picklist_options = Column(JSON)
    is_required = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    is_system_field = Column(Boolean, default=False)
    help_text = Column(Text)
    default_value = Column(String)
    validation_rules = Column(JSON)
    display_order = Column(String, default="0")
    section = Column(String, default="general")
    
    # Relationships
    values = relationship("CustomFieldValue", back_populates="definition")