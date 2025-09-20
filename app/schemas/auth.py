from pydantic import BaseModel, EmailStr
from typing import Optional

class Token(BaseModel):
    """JWT Token response model"""
    access_token: str
    token_type: str

class TokenData(BaseModel):
    """Token payload data model"""
    email: Optional[str] = None

class UserLogin(BaseModel):
    """User login request model"""
    email: EmailStr
    password: str

class UserRegister(BaseModel):
    """User registration request model"""
    email: EmailStr
    full_name: str
    password: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None
    job_title: Optional[str] = None