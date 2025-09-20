from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.core.database import get_db
from app.schemas.activity import Activity, ActivityCreate, ActivityUpdate
from app.crud import activity as crud_activity
from app.core.security import get_current_user
from app.models.user import User

router = APIRouter()

@router.get("/", response_model=List[Activity])
def get_activities(
    skip: int = 0,
    limit: int = Query(default=100, le=1000),
    activity_type: Optional[str] = Query(None),
    status: Optional[str] = Query(None),
    assigned_to: Optional[str] = Query(None),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get all activities with filtering"""
    activities = crud_activity.get_activities(
        db, skip=skip, limit=limit, activity_type=activity_type, 
        status=status, assigned_to=assigned_to
    )
    return activities

@router.get("/{activity_id}", response_model=Activity)
def get_activity(
    activity_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get specific activity by ID"""
    activity = crud_activity.get_activity(db, activity_id=activity_id)
    if not activity:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Activity not found"
        )
    return activity

@router.post("/", response_model=Activity, status_code=status.HTTP_201_CREATED)
def create_activity(
    activity: ActivityCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Create new activity"""
    return crud_activity.create_activity(
        db=db, activity=activity, created_by=current_user.email
    )

@router.put("/{activity_id}", response_model=Activity)
def update_activity(
    activity_id: str,
    activity_update: ActivityUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Update existing activity"""
    activity = crud_activity.update_activity(
        db, activity_id=activity_id, activity_update=activity_update
    )
    if not activity:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Activity not found"
        )
    return activity

@router.delete("/{activity_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_activity(
    activity_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Delete activity"""
    success = crud_activity.delete_activity(db, activity_id=activity_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Activity not found"
        )