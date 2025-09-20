from typing import Generator, Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from jose import JWTError, jwt

from app.core.config import settings
from app.core.database import SessionLocal
from app.models.user import User
from app.crud.user import get_user_by_email

security = HTTPBearer()

def get_db() -> Generator:
    """
    Database dependency
    """
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
) -> User:
    """
    Get current authenticated user from JWT token
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        # Decode JWT token
        token = credentials.credentials
        payload = jwt.decode(
            token, 
            settings.SECRET_KEY, 
            algorithms=[settings.ALGORITHM]
        )
        
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
            
    except JWTError:
        raise credentials_exception
    
    # Get user from database
    user = get_user_by_email(db, email=email)
    if user is None:
        raise credentials_exception
        
    return user

async def get_current_active_user(
    current_user: User = Depends(get_current_user)
) -> User:
    """
    Get current active user (not disabled)
    """
    if not current_user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Inactive user"
        )
    return current_user

async def get_current_superuser(
    current_user: User = Depends(get_current_user)
) -> User:
    """
    Get current superuser
    """
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions"
        )
    return current_user

# Optional user dependency (no authentication required)
async def get_current_user_optional(
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(HTTPBearer(auto_error=False)),
    db: Session = Depends(get_db)
) -> Optional[User]:
    """
    Get current user if authenticated, None if not
    """
    if not credentials:
        return None
        
    try:
        token = credentials.credentials
        payload = jwt.decode(
            token, 
            settings.SECRET_KEY, 
            algorithms=[settings.ALGORITHM]
        )
        
        email: str = payload.get("sub")
        if email is None:
            return None
            
        user = get_user_by_email(db, email=email)
        return user
        
    except JWTError:
        return None

# Pagination dependency
def get_pagination_params(
    skip: int = 0,
    limit: int = 100
):
    """
    Common pagination parameters
    """
    return {"skip": skip, "limit": min(limit, 1000)}  # Max 1000 items per request

# Search dependency
def get_search_params(
    search: Optional[str] = None,
    sort_by: Optional[str] = None,
    sort_order: Optional[str] = "asc"
):
    """
    Common search and sorting parameters
    """
    return {
        "search": search,
        "sort_by": sort_by,
        "sort_order": sort_order if sort_order in ["asc", "desc"] else "asc"
    }