from typing import Any, Dict, Optional, Union, List
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate

# FIXED: Import security functions at function level to avoid circular import
def get_user(db: Session, user_id: str) -> Optional[User]:
    """Get user by ID"""
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email: str) -> Optional[User]:
    """Get user by email"""
    return db.query(User).filter(User.email == email).first()

def get_users(
    db: Session, skip: int = 0, limit: int = 100
) -> List[User]:
    """Get multiple users with pagination"""
    return db.query(User).offset(skip).limit(limit).all()

def create_user(db: Session, *, obj_in: UserCreate) -> User:
    """Create new user"""
    # FIXED: Import inside function to avoid circular import
    from app.core.security import get_password_hash
    
    db_obj = User(
        email=obj_in.email,
        full_name=obj_in.full_name,
        first_name=obj_in.first_name,
        last_name=obj_in.last_name,
        phone=obj_in.phone,
        job_title=obj_in.job_title,
        department_id=obj_in.department_id,
        role_id=obj_in.role_id,
        manager_id=obj_in.manager_id,
        status=obj_in.status,
        is_active=obj_in.is_active,
        gdpr_consent=obj_in.gdpr_consent,
        hashed_password=get_password_hash(obj_in.password)
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_user(
    db: Session, *, db_obj: User, obj_in: Union[UserUpdate, Dict[str, Any]]
) -> User:
    """Update existing user"""
    if isinstance(obj_in, dict):
        update_data = obj_in
    else:
        update_data = obj_in.model_dump(exclude_unset=True)
    
    for field in update_data:
        if hasattr(db_obj, field):
            setattr(db_obj, field, update_data[field])
    
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def authenticate(db: Session, *, email: str, password: str) -> Optional[User]:
    """Authenticate user with email and password"""
    # FIXED: Import inside function to avoid circular import
    from app.core.security import verify_password
    
    user = get_user_by_email(db, email=email)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user

def is_active(user: User) -> bool:
    """Check if user is active"""
    return user.is_active

def delete_user(db: Session, *, user_id: str) -> User:
    """Delete user"""
    obj = db.query(User).get(user_id)
    db.delete(obj)
    db.commit()
    return obj