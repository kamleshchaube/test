from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class RoleBase(BaseModel):
    name: str
    description: Optional[str] = None
    is_active: bool = True
    compliance_tag: bool = False
    level: str = "user"

class RoleCreate(RoleBase):
    pass

class RoleUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None
    level: Optional[str] = None

class Role(RoleBase):
    id: str
    created_date: datetime
    updated_date: Optional[datetime] = None
    created_by: Optional[str] = None

    class Config:
        from_attributes = True

class RoleWithPermissions(Role):
    permissions: List[str] = []