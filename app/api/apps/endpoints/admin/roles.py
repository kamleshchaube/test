from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from app.core.database import get_async_session
from app.schemas.role import Role, RoleCreate, RoleUpdate, RoleWithPermissions
from app.crud import role as crud_role
from app.api.deps import get_current_admin_user

router = APIRouter()

@router.get("/", response_model=List[Role])
async def get_roles(
    skip: int = 0,
    limit: int = Query(default=100, le=1000),
    is_active: Optional[bool] = Query(None),
    db: AsyncSession = Depends(get_async_session),
    current_user = Depends(get_current_admin_user)
):
    """Get all roles with filtering and pagination"""
    roles = await crud_role.get_roles(
        db, 
        skip=skip, 
        limit=limit, 
        is_active=is_active
    )
    return roles

@router.get("/{role_id}", response_model=RoleWithPermissions)
async def get_role(
    role_id: str,
    db: AsyncSession = Depends(get_async_session),
    current_user = Depends(get_current_admin_user)
):
    """Get a specific role with permissions"""
    role = await crud_role.get_role_with_permissions(db, role_id=role_id)
    if not role:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Role not found"
        )
    return role

@router.post("/", response_model=Role, status_code=status.HTTP_201_CREATED)
async def create_role(
    role: RoleCreate,
    db: AsyncSession = Depends(get_async_session),
    current_user = Depends(get_current_admin_user)
):
    """Create a new role"""
    # Check if role name already exists
    existing_role = await crud_role.get_role_by_name(db, name=role.name)
    if existing_role:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Role name already exists"
        )
    
    return await crud_role.create_role(
        db=db, 
        role=role, 
        created_by=current_user.email
    )

@router.put("/{role_id}", response_model=Role)
async def update_role(
    role_id: str,
    role_update: RoleUpdate,
    db: AsyncSession = Depends(get_async_session),
    current_user = Depends(get_current_admin_user)
):
    """Update an existing role"""
    role = await crud_role.update_role(
        db, 
        role_id=role_id, 
        role_update=role_update
    )
    if not role:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Role not found"
        )
    return role

@router.patch("/{role_id}/permissions")
async def assign_permissions_to_role(
    role_id: str,
    permission_data: dict,
    db: AsyncSession = Depends(get_async_session),
    current_user = Depends(get_current_admin_user)
):
    """Assign permissions to a role"""
    permission_ids = permission_data.get("permission_ids", [])
    
    success = await crud_role.assign_permissions(
        db,
        role_id=role_id,
        permission_ids=permission_ids,
        assigned_by=current_user.email
    )
    
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Role not found"
        )
    
    return {"message": "Permissions assigned successfully"}

@router.delete("/{role_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_role(
    role_id: str,
    db: AsyncSession = Depends(get_async_session),
    current_user = Depends(get_current_admin_user)
):
    """Delete a role"""
    # Check if role has compliance tag (system role)
    role = await crud_role.get_role(db, role_id=role_id)
    if role and role.compliance_tag:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot delete system role"
        )
    
    success = await crud_role.delete_role(db, role_id=role_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Role not found"
        )