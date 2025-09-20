from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PermissionBase(BaseModel):
    name: str
    description: Optional[str] = None
    entity: str
    action: str
    resource: Optional[str] = None
    conditions: Optional[str] = None
    category: str = "general"

class PermissionCreate(PermissionBase):
    pass

class PermissionUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    conditions: Optional[str] = None
    category: Optional[str] = None

class Permission(PermissionBase):
    id: str
    created_date: datetime

    class Config:
        from_attributes = True