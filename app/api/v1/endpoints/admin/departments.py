from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from app.core.database import get_async_session
from app.schemas.department import Department, DepartmentCreate, DepartmentUpdate
from app.crud import department as crud_department
from app.api.deps import get_current_admin_user

router = APIRouter()

@router.get("/", response_model=List[Department])
async def get_departments(
    skip: int = 0,
    limit: int = Query(default=100, le=1000),
    is_active: Optional[bool] = Query(None),
    parent_department_id: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_async_session),
    current_user = Depends(get_current_admin_user)
):
    """Get all departments with filtering and pagination"""
    departments = await crud_department.get_departments(
        db, 
        skip=skip, 
        limit=limit, 
        is_active=is_active,
        parent_department_id=parent_department_id
    )
    return departments

@router.get("/hierarchy")
async def get_department_hierarchy(
    db: AsyncSession = Depends(get_async_session),
    current_user = Depends(get_current_admin_user)
):
    """Get department hierarchy tree"""
    hierarchy = await crud_department.get_department_hierarchy(db)
    return hierarchy

@router.get("/{department_id}", response_model=Department)
async def get_department(
    department_id: str,
    db: AsyncSession = Depends(get_async_session),
    current_user = Depends(get_current_admin_user)
):
    """Get a specific department"""
    department = await crud_department.get_department(db, department_id=department_id)
    if not department:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Department not found"
        )
    return department

@router.post("/", response_model=Department, status_code=status.HTTP_201_CREATED)
async def create_department(
    department: DepartmentCreate,
    db: AsyncSession = Depends(get_async_session),
    current_user = Depends(get_current_admin_user)
):
    """Create a new department"""
    # Check if department name already exists
    existing_dept = await crud_department.get_department_by_name(db, name=department.name)
    if existing_dept:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Department name already exists"
        )
    
    return await crud_department.create_department(
        db=db, 
        department=department, 
        created_by=current_user.email
    )

@router.put("/{department_id}", response_model=Department)
async def update_department(
    department_id: str,
    department_update: DepartmentUpdate,
    db: AsyncSession = Depends(get_async_session),
    current_user = Depends(get_current_admin_user)
):
    """Update an existing department"""
    department = await crud_department.update_department(
        db, 
        department_id=department_id, 
        department_update=department_update
    )
    if not department:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Department not found"
        )
    return department

@router.delete("/{department_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_department(
    department_id: str,
    db: AsyncSession = Depends(get_async_session),
    current_user = Depends(get_current_admin_user)
):
    """Delete a department"""
    success = await crud_department.delete_department(db, department_id=department_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Department not found"
        )