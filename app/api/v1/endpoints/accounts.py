from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from app.core.database import get_async_session
from app.schemas.account import Account, AccountCreate, AccountUpdate
from app.crud import account as crud_account
from app.api.deps import get_current_user

router = APIRouter()

@router.get("/", response_model=List[Account])
async def get_accounts(
    skip: int = 0,
    limit: int = Query(default=100, le=1000),
    account_type: Optional[str] = Query(None),
    industry: Optional[str] = Query(None),
    assigned_to: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_async_session),
    current_user = Depends(get_current_user)
):
    """Get all accounts with filtering and pagination"""
    accounts = await crud_account.get_accounts(
        db, 
        skip=skip, 
        limit=limit, 
        account_type=account_type,
        industry=industry,
        assigned_to=assigned_to
    )
    return accounts

@router.get("/{account_id}", response_model=Account)
async def get_account(
    account_id: str,
    db: AsyncSession = Depends(get_async_session),
    current_user = Depends(get_current_user)
):
    """Get a specific account by ID"""
    account = await crud_account.get_account(db, account_id=account_id)
    if not account:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Account not found"
        )
    return account

@router.post("/", response_model=Account, status_code=status.HTTP_201_CREATED)
async def create_account(
    account: AccountCreate,
    db: AsyncSession = Depends(get_async_session),
    current_user = Depends(get_current_user)
):
    """Create a new account"""
    return await crud_account.create_account(db=db, account=account, created_by=current_user.email)

@router.put("/{account_id}", response_model=Account)
async def update_account(
    account_id: str,
    account_update: AccountUpdate,
    db: AsyncSession = Depends(get_async_session),
    current_user = Depends(get_current_user)
):
    """Update an existing account"""
    account = await crud_account.update_account(db, account_id=account_id, account_update=account_update)
    if not account:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Account not found"
        )
    return account

@router.delete("/{account_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_account(
    account_id: str,
    db: AsyncSession = Depends(get_async_session),
    current_user = Depends(get_current_user)
):
    """Soft delete an account"""
    success = await crud_account.delete_account(db, account_id=account_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Account not found"
        )