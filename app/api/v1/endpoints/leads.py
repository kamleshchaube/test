from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.core.database import get_db
from app.schemas.lead import Lead, LeadCreate, LeadUpdate
from app.crud import lead as crud_lead
from app.core.security import get_current_user
from app.models.user import User

router = APIRouter()

@router.get("/", response_model=List[Lead])
def get_leads(
    skip: int = 0,
    limit: int = Query(default=100, le=1000),
    status: Optional[str] = Query(None),
    assigned_to: Optional[str] = Query(None),
    tender_type: Optional[str] = Query(None),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get all leads with filtering and pagination"""
    leads = crud_lead.get_leads(
        db, 
        skip=skip, 
        limit=limit, 
        status=status,
        assigned_to=assigned_to,
        tender_type=tender_type
    )
    return leads

@router.get("/analytics")
def get_leads_analytics(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get lead analytics and metrics"""
    return crud_lead.get_leads_analytics(db)

@router.get("/{lead_id}", response_model=Lead)
def get_lead(
    lead_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get a specific lead by ID"""
    lead = crud_lead.get_lead(db, lead_id=lead_id)
    if not lead:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Lead not found"
        )
    return lead

@router.post("/", response_model=Lead, status_code=status.HTTP_201_CREATED)
def create_lead(
    lead: LeadCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Create a new lead"""
    # Check if email already exists
    existing_lead = crud_lead.get_lead_by_email(db, email=lead.email)
    if existing_lead:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    return crud_lead.create_lead(db=db, lead=lead, created_by=current_user.email)

@router.put("/{lead_id}", response_model=Lead)
def update_lead(
    lead_id: str,
    lead_update: LeadUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Update an existing lead"""
    lead = crud_lead.update_lead(db, lead_id=lead_id, lead_update=lead_update)
    if not lead:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Lead not found"
        )
    return lead

@router.delete("/{lead_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_lead(
    lead_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Soft delete a lead"""
    success = crud_lead.delete_lead(db, lead_id=lead_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Lead not found"
        )