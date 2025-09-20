from sqlalchemy import Column, String, Boolean, Enum
from sqlalchemy.orm import relationship
from app.models.base import BaseModel
import enum

class UserStatus(str, enum.Enum):
    ACTIVE = "active"
    INACTIVE = "inactive" 
    PENDING = "pending"
    SUSPENDED = "suspended"

class User(BaseModel):
    __tablename__ = "users"

    # Basic Information
    email = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String, nullable=False)
    first_name = Column(String)
    last_name = Column(String)
    phone = Column(String)
    job_title = Column(String)
    
    # Organizational Structure
    department_id = Column(String)
    role_id = Column(String)
    manager_id = Column(String)
    
    # Account Status
    status = Column(Enum(UserStatus), default=UserStatus.PENDING)
    is_superuser = Column(Boolean, default=False)
    is_verified = Column(Boolean, default=False)
    
    # Authentication
    hashed_password = Column(String)
    last_login = Column(String)
    login_attempts = Column(String, default="0")
    
    # Privacy & Compliance
    gdpr_consent = Column(Boolean, default=False)
    
    # Relationships (defined as foreign keys for now)
    # department = relationship("Department", foreign_keys=[department_id])
    # role = relationship("Role", foreign_keys=[role_id]) 
    # manager = relationship("User", remote_side=[id])
    # audit_logs = relationship("AuditLog", back_populates="user")
    
    def __repr__(self):
        return "<User(id={0}, email={1}, full_name={2})>".format(
            self.id, self.email, self.full_name
        )
    
    @property
    def is_admin(self):
        """Check if user is admin"""
        return self.is_superuser
    
    @property
    def display_name(self):
        """Get display name for user"""
        return self.full_name or self.email
    
    def can_access_admin(self):
        """Check if user can access admin features"""
        return self.is_superuser and self.is_active and self.status == UserStatus.ACTIVE