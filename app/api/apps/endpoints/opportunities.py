from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from app.core.database import get_async_session
from app.schemas.opportunity import Opportunity, OpportunityCreate, OpportunityUpdate
from app.crud import opportunity as crud_opportunity
from app.api.deps import get_current_user

router = APIRouter()

@router.get("/", response_model=List[Opportunity])
async def get_opportunities(
    skip: int = 0,
    limit: int = Query(default=100, le=1000),
    stage: Optional[str] = Query(None),
    assigned_to: Optional[str] = Query(None),
    account_id: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_async_session),
    current_user = Depends(get_current_user)
):
    """Get all opportunities with filtering and pagination"""
    opportunities = await crud_opportunity.get_opportunities(
        db, 
        skip=skip, 
        limit=limit, 
        stage=stage,
        assigned_to=assigned_to,
        account_id=account_id
    )
    return opportunities

@router.get("/{opportunity_id}", response_model=Opportunity)
async def get_opportunity(
    opportunity_id: str,
    db: AsyncSession = Depends(get_async_session),
    current_user = Depends(get_current_user)
):
    """Get a specific opportunity by ID"""
    opportunity = await crud_opportunity.get_opportunity(db, opportunity_id=opportunity_id)
    if not opportunity:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Opportunity not found"
        )
    return opportunity

@router.post("/", response_model=Opportunity, status_code=status.HTTP_201_CREATED)
async def create_opportunity(
    opportunity: OpportunityCreate,
    db: AsyncSession = Depends(get_async_session),
    current_user = Depends(get_current_user)
):
    """Create a new opportunity"""
    return await crud_opportunity.create_opportunity(
        db=db, 
        opportunity=opportunity, 
        created_by=current_user.email
    )

@router.put("/{opportunity_id}", response_model=Opportunity)
async def update_opportunity(
    opportunity_id: str,
    opportunity_update: OpportunityUpdate,
    db: AsyncSession = Depends(get_async_session),
    current_user = Depends(get_current_user)
):
    """Update an existing opportunity"""
    opportunity = await crud_opportunity.update_opportunity(
        db, 
        opportunity_id=opportunity_id, 
        opportunity_update=opportunity_update
    )
    if not opportunity:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Opportunity not found"
        )
    return opportunity

@router.patch("/{opportunity_id}/stage")
async def update_opportunity_stage(
    opportunity_id: str,
    stage_data: dict,
    db: AsyncSession = Depends(get_async_session),
    current_user = Depends(get_current_user)
):
    """Update opportunity stage"""
    opportunity = await crud_opportunity.update_stage(
        db, 
        opportunity_id=opportunity_id, 
        new_stage=stage_data["stage"],
        changed_by=current_user.email
    )
    if not opportunity:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Opportunity not found"
        )
    return opportunity