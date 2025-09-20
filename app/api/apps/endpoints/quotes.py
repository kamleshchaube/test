from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from app.core.database import get_async_session
from app.schemas.quote import Quote, QuoteCreate, QuoteUpdate
from app.crud import quote as crud_quote
from app.api.deps import get_current_user

router = APIRouter()

@router.get("/", response_model=List[Quote])
async def get_quotes(
    skip: int = 0,
    limit: int = Query(default=100, le=1000),
    status: Optional[str] = Query(None),
    opportunity_id: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_async_session),
    current_user = Depends(get_current_user)
):
    """Get all quotes with filtering and pagination"""
    quotes = await crud_quote.get_quotes(
        db, 
        skip=skip, 
        limit=limit, 
        status=status,
        opportunity_id=opportunity_id
    )
    return quotes

@router.get("/{quote_id}", response_model=Quote)
async def get_quote(
    quote_id: str,
    db: AsyncSession = Depends(get_async_session),
    current_user = Depends(get_current_user)
):
    """Get a specific quote by ID"""
    quote = await crud_quote.get_quote(db, quote_id=quote_id)
    if not quote:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Quote not found"
        )
    return quote

@router.post("/", response_model=Quote, status_code=status.HTTP_201_CREATED)
async def create_quote(
    quote: QuoteCreate,
    db: AsyncSession = Depends(get_async_session),
    current_user = Depends(get_current_user)
):
    """Create a new quote"""
    return await crud_quote.create_quote(
        db=db, 
        quote=quote, 
        created_by=current_user.email
    )

@router.put("/{quote_id}", response_model=Quote)
async def update_quote(
    quote_id: str,
    quote_update: QuoteUpdate,
    db: AsyncSession = Depends(get_async_session),
    current_user = Depends(get_current_user)
):
    """Update an existing quote"""
    quote = await crud_quote.update_quote(
        db, 
        quote_id=quote_id, 
        quote_update=quote_update
    )
    if not quote:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Quote not found"
        )
    return quote

@router.patch("/{quote_id}/approve")
async def approve_quote(
    quote_id: str,
    db: AsyncSession = Depends(get_async_session),
    current_user = Depends(get_current_user)
):
    """Approve a quote (manager/admin only)"""
    if not hasattr(current_user, 'role') or current_user.role not in ['manager', 'admin']:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Insufficient permissions"
        )
    
    quote = await crud_quote.approve_quote(
        db, 
        quote_id=quote_id, 
        approved_by=current_user.email
    )
    if not quote:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Quote not found"
        )
    return {"message": "Quote approved successfully", "quote": quote}

@router.patch("/{quote_id}/reject")
async def reject_quote(
    quote_id: str,
    rejection_data: dict,
    db: AsyncSession = Depends(get_async_session),
    current_user = Depends(get_current_user)
):
    """Reject a quote with reason"""
    if not hasattr(current_user, 'role') or current_user.role not in ['manager', 'admin']:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Insufficient permissions"
        )
    
    quote = await crud_quote.reject_quote(
        db, 
        quote_id=quote_id,
        rejection_reason=rejection_data.get("reason"),
        rejected_by=current_user.email
    )
    if not quote:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Quote not found"
        )
    return {"message": "Quote rejected", "quote": quote}

@router.patch("/{quote_id}/send-to-client")
async def send_quote_to_client(
    quote_id: str,
    db: AsyncSession = Depends(get_async_session),
    current_user = Depends(get_current_user)
):
    """Mark quote as sent to client"""
    quote = await crud_quote.send_to_client(db, quote_id=quote_id)
    if not quote:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Quote not found"
        )
    return {"message": "Quote sent to client", "quote": quote}

@router.delete("/{quote_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_quote(
    quote_id: str,
    db: AsyncSession = Depends(get_async_session),
    current_user = Depends(get_current_user)
):
    """Soft delete a quote"""
    success = await crud_quote.delete_quote(db, quote_id=quote_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Quote not found"
        )