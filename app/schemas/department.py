from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class DepartmentBase(BaseModel):
    name: str
    description: Optional[str] = None
    is_active: bool = True
    head_of_department: Optional[str] = None
    budget: Optional[str] = None
    cost_center: Optional[str] = None
    parent_department_id: Optional[str] = None

class DepartmentCreate(DepartmentBase):
    pass

class DepartmentUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None
    head_of_department: Optional[str] = None
    budget: Optional[str] = None
    cost_center: Optional[str] = None
    parent_department_id: Optional[str] = None

class Department(DepartmentBase):
    id: str
    created_date: datetime
    updated_date: Optional[datetime] = None
    created_by: Optional[str] = None

    class Config:
        from_attributes = True