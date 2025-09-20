from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional
from enum import Enum

class DeliveryStatus(str, Enum):
    PENDING = "pending"
    PARTIAL = "partial"
    DELIVERED = "delivered"

class ProjectLineItemBase(BaseModel):
    project_id: str
    product_id: Optional[str] = None
    sku: Optional[str] = None
    description: str
    ordered_quantity: float
    unit_price: float
    line_total: float
    quote_item_id: Optional[str] = None

class ProjectLineItemCreate(ProjectLineItemBase):
    pass

class ProjectLineItemUpdate(BaseModel):
    description: Optional[str] = None
    ordered_quantity: Optional[float] = None
    delivered_quantity: Optional[float] = None
    unit_price: Optional[float] = None
    line_total: Optional[float] = None
    delivery_status: Optional[DeliveryStatus] = None
    delivery_comment: Optional[str] = None

class DeliveryUpdate(BaseModel):
    delivered_quantity: float
    delivery_date: date
    delivery_comment: Optional[str] = None
    delivery_proof_url: Optional[str] = None

class ProjectLineItem(ProjectLineItemBase):
    id: str
    created_date: datetime
    updated_date: Optional[datetime] = None
    delivered_quantity: float = 0
    delivery_status: DeliveryStatus = DeliveryStatus.PENDING
    delivery_date: Optional[date] = None
    delivery_comment: Optional[str] = None
    delivered_by: Optional[str] = None
    delivery_proof_url: Optional[str] = None

    class Config:
        from_attributes = True