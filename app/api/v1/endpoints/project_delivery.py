from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from app.core.database import get_async_session
from app.schemas.project_line_item import ProjectLineItem, ProjectLineItemCreate, ProjectLineItemUpdate, DeliveryUpdate
from app.crud import project_delivery as crud_delivery
from app.api.deps import get_current_user

router = APIRouter()

@router.get("/projects/{project_id}/line-items", response_model=List[ProjectLineItem])
async def get_project_line_items(
    project_id: str,
    db: AsyncSession = Depends(get_async_session),
    current_user = Depends(get_current_user)
):
    """Get all line items for a project"""
    line_items = await crud_delivery.get_project_line_items(db, project_id=project_id)
    return line_items

@router.post("/projects/{project_id}/line-items", response_model=ProjectLineItem)
async def create_project_line_item(
    project_id: str,
    line_item: ProjectLineItemCreate,
    db: AsyncSession = Depends(get_async_session),
    current_user = Depends(get_current_user)
):
    """Create a new project line item"""
    # Ensure project_id matches the URL parameter
    line_item.project_id = project_id
    
    return await crud_delivery.create_project_line_item(
        db=db, 
        line_item=line_item, 
        created_by=current_user.email
    )

@router.put("/line-items/{line_item_id}", response_model=ProjectLineItem)
async def update_project_line_item(
    line_item_id: str,
    line_item_update: ProjectLineItemUpdate,
    db: AsyncSession = Depends(get_async_session),
    current_user = Depends(get_current_user)
):
    """Update a project line item"""
    line_item = await crud_delivery.update_project_line_item(
        db, 
        line_item_id=line_item_id, 
        line_item_update=line_item_update
    )
    if not line_item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Line item not found"
        )
    return line_item

@router.patch("/line-items/{line_item_id}/delivery")
async def update_delivery_status(
    line_item_id: str,
    delivery_update: DeliveryUpdate,
    db: AsyncSession = Depends(get_async_session),
    current_user = Depends(get_current_user)
):
    """Update delivery status for a line item"""
    result = await crud_delivery.update_delivery_status(
        db,
        line_item_id=line_item_id,
        delivery_update=delivery_update,
        delivered_by=current_user.email
    )
    
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Line item not found"
        )
    
    return {"message": "Delivery status updated successfully", "line_item": result}

@router.get("/projects/{project_id}/delivery-summary")
async def get_delivery_summary(
    project_id: str,
    db: AsyncSession = Depends(get_async_session),
    current_user = Depends(get_current_user)
):
    """Get delivery summary for a project"""
    summary = await crud_delivery.get_project_delivery_summary(db, project_id=project_id)
    if summary is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found"
        )
    return summary

@router.get("/projects/{project_id}/delivery-logs")
async def get_project_delivery_logs(
    project_id: str,
    skip: int = 0,
    limit: int = Query(default=50, le=200),
    db: AsyncSession = Depends(get_async_session),
    current_user = Depends(get_current_user)
):
    """Get delivery logs for a project"""
    logs = await crud_delivery.get_project_delivery_logs(
        db, 
        project_id=project_id,
        skip=skip,
        limit=limit
    )
    return logs

@router.delete("/line-items/{line_item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_project_line_item(
    line_item_id: str,
    db: AsyncSession = Depends(get_async_session),
    current_user = Depends(get_current_user)
):
    """Delete a project line item"""
    success = await crud_delivery.delete_project_line_item(db, line_item_id=line_item_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Line item not found"
        )