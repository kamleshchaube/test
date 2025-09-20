from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from app.core.database import get_async_session
from app.schemas.user import User, UserCreate, UserUpdate, UserPasswordUpdate
from app.crud import user as crud_user
from app.api.deps import get_current_user, get_current_admin_user

router = APIRouter()

@router.get("/", response_model=List[User])
async def get_users(
    skip: int = 0,
    limit: int = Query(default=100, le=1000),
    status: Optional[str] = Query(None),
    department_id: Optional[str] = Query(None),
    role_id: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_async_session),
    current_user = Depends(get_current_admin_user)
):
    """Get all users with filtering and pagination (Admin only)"""
    users = await crud_user.get_users(
        db, 
        skip=skip, 
        limit=limit, 
        status=status,
        department_id=department_id,
        role_id=role_id
    )
    return users

@router.get("/me", response_model=User)
async def get_current_user_profile(
    current_user = Depends(get_current_user)
):
    """Get current user's profile"""
    return current_user

@router.get("/{user_id}", response_model=User)
async def get_user(
    user_id: str,
    db: AsyncSession = Depends(get_async_session),
    current_user = Depends(get_current_admin_user)
):
    """Get a specific user by ID (Admin only)"""
    user = await crud_user.get_user(db, user_id=user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(
    user: UserCreate,
    db: AsyncSession = Depends(get_async_session),
    current_user = Depends(get_current_admin_user)
):
    """Create a new user (Admin only)"""
    # Check if email already exists
    existing_user = await crud_user.get_user_by_email(db, email=user.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    return await crud_user.create_user(
        db=db, 
        user=user, 
        created_by=current_user.email
    )

@router.put("/me", response_model=User)
async def update_current_user_profile(
    user_update: UserUpdate,
    db: AsyncSession = Depends(get_async_session),
    current_user = Depends(get_current_user)
):
    """Update current user's profile"""
    user = await crud_user.update_user(
        db, 
        user_id=current_user.id, 
        user_update=user_update
    )
    return user

@router.put("/{user_id}", response_model=User)
async def update_user(
    user_id: str,
    user_update: UserUpdate,
    db: AsyncSession = Depends(get_async_session),
    current_user = Depends(get_current_admin_user)
):
    """Update a user (Admin only)"""
    user = await crud_user.update_user(
        db, 
        user_id=user_id, 
        user_update=user_update
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user

@router.patch("/{user_id}/status")
async def update_user_status(
    user_id: str,
    status_data: dict,
    db: AsyncSession = Depends(get_async_session),
    current_user = Depends(get_current_admin_user)
):
    """Update user status (Admin only)"""
    user = await crud_user.update_user_status(
        db,
        user_id=user_id,
        new_status=status_data.get("status"),
        updated_by=current_user.email
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return {"message": "User status updated successfully", "user": user}

@router.patch("/me/password")
async def change_password(
    password_update: UserPasswordUpdate,
    db: AsyncSession = Depends(get_async_session),
    current_user = Depends(get_current_user)
):
    """Change current user's password"""
    success = await crud_user.change_password(
        db,
        user_id=current_user.id,
        current_password=password_update.current_password,
        new_password=password_update.new_password
    )
    
    if not success:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Current password is incorrect"
        )
    
    return {"message": "Password changed successfully"}

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    user_id: str,
    db: AsyncSession = Depends(get_async_session),
    current_user = Depends(get_current_admin_user)
):
    """Soft delete a user (Admin only)"""
    # Prevent deleting yourself
    if user_id == current_user.id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot delete your own account"
        )
    
    success = await crud_user.delete_user(db, user_id=user_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )