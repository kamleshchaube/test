from typing import Optional
from pydantic import BaseModel, EmailStr, Field, ConfigDict

# Base user schema
class UserBase(BaseModel):
    email: EmailStr
    full_name: str = Field(..., min_length=1, max_length=100)
    is_active: bool = True
    is_superuser: bool = False
    department_id: Optional[str] = None
    role_id: Optional[str] = None
    phone: Optional[str] = Field(None, max_length=20)
    job_title: Optional[str] = Field(None, max_length=100)

# Schema for creating a user
class UserCreate(UserBase):
    password: str = Field(..., min_length=8, max_length=100)
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "email": "user@example.com",
                "full_name": "John Doe",
                "password": "securepassword123",
                "job_title": "Sales Representative",
                "department_id": "sales-dept-001"
            }
        }
    )

# Schema for updating a user
class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    full_name: Optional[str] = Field(None, min_length=1, max_length=100)
    password: Optional[str] = Field(None, min_length=8, max_length=100)
    is_active: Optional[bool] = None
    is_superuser: Optional[bool] = None
    department_id: Optional[str] = None
    role_id: Optional[str] = None
    phone: Optional[str] = Field(None, max_length=20)
    job_title: Optional[str] = Field(None, max_length=100)

# Schema for password change
class UserPasswordChange(BaseModel):
    current_password: str
    new_password: str = Field(..., min_length=8, max_length=100)

# Schema for user response (no password)
class User(UserBase):
    id: str
    created_date: str
    updated_date: str
    created_by: Optional[str] = None
    
    model_config = ConfigDict(from_attributes=True)  # Pydantic v2 way

# Schema for user with password hash (internal use)
class UserInDB(User):
    hashed_password: Optional[str] = None

# Schema for user login
class UserLogin(BaseModel):
    email: EmailStr
    password: str
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "email": "user@example.com",
                "password": "securepassword123"
            }
        }
    )

# Authentication schemas
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in: int
    user: User

class TokenPayload(BaseModel):
    sub: Optional[str] = None  # Subject (user email)
    exp: Optional[int] = None  # Expiration timestamp