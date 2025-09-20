from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.activity import Activity
from app.schemas.activity import ActivityCreate, ActivityUpdate
import uuid

def get_activity(db: Session, activity_id: str) -> Optional[Activity]:
    return db.query(Activity).filter(Activity.id == activity_id).first()

def get_activities(db: Session, skip: int = 0, limit: int = 100) -> List[Activity]:
    return db.query(Activity).filter(Activity.is_active == True).offset(skip).limit(limit).all()

def create_activity(db: Session, activity: ActivityCreate, created_by: str = None) -> Activity:
    activity_data = activity.dict()
    activity_data["id"] = str(uuid.uuid4())
    activity_data["created_by"] = created_by
    db_activity = Activity(**activity_data)
    db.add(db_activity)
    db.commit()
    db.refresh(db_activity)
    return db_activity

def update_activity(db: Session, activity_id: str, activity_update: ActivityUpdate) -> Optional[Activity]:
    db_activity = get_activity(db, activity_id)
    if not db_activity:
        return None
    update_data = activity_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_activity, field, value)
    db.commit()
    db.refresh(db_activity)
    return db_activity

def delete_activity(db: Session, activity_id: str) -> bool:
    db_activity = get_activity(db, activity_id)
    if not db_activity:
        return False
    db_activity.is_active = False
    db.commit()
    return True

def get_recent_activities(db: Session, limit: int = 5) -> List[Activity]:
    return db.query(Activity).filter(Activity.is_active == True).order_by(Activity.created_date.desc()).limit(limit).all()
