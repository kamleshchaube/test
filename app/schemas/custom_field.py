from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional, List, Union

class CustomFieldDefinitionBase(BaseModel):
    entity_type: str
    field_name: str
    field_label: str
    data_type: str
    picklist_options: Optional[List[str]] = None
    is_required: bool = False
    is_active: bool = True
    help_text: Optional[str] = None
    default_value: Optional[str] = None
    validation_rules: Optional[dict] = None
    display_order: str = "0"
    section: str = "general"

class CustomFieldDefinitionCreate(CustomFieldDefinitionBase):
    pass

class CustomFieldDefinitionUpdate(BaseModel):
    field_label: Optional[str] = None
    picklist_options: Optional[List[str]] = None
    is_required: Optional[bool] = None
    is_active: Optional[bool] = None
    help_text: Optional[str] = None
    default_value: Optional[str] = None
    validation_rules: Optional[dict] = None
    display_order: Optional[str] = None
    section: Optional[str] = None

class CustomFieldDefinition(CustomFieldDefinitionBase):
    id: str
    created_date: datetime
    created_by: Optional[str] = None
    is_system_field: bool = False

    class Config:
        from_attributes = True

class CustomFieldValueBase(BaseModel):
    definition_id: str
    entity_id: str
    value_text: Optional[str] = None
    value_number: Optional[float] = None
    value_date: Optional[date] = None
    value_boolean: Optional[bool] = None
    value_json: Optional[str] = None

class CustomFieldValueCreate(CustomFieldValueBase):
    pass

class CustomFieldValueUpdate(BaseModel):
    value_text: Optional[str] = None
    value_number: Optional[float] = None
    value_date: Optional[date] = None
    value_boolean: Optional[bool] = None
    value_json: Optional[str] = None

class CustomFieldValue(CustomFieldValueBase):
    id: str
    created_date: datetime

    class Config:
        from_attributes = True