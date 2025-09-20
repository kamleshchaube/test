from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.project import Project, ProjectStatus
from app.schemas.project import ProjectCreate, ProjectUpdate
import uuid

def get_project(db: Session, project_id: str) -> Optional[Project]:
    """Get a single project by ID"""
    return db.query(Project).filter(Project.id == project_id).first()

def get_projects(
    db: Session, 
    skip: int = 0, 
    limit: int = 100,
    status: Optional[ProjectStatus] = None,
    sd_owner: Optional[str] = None
) -> List[Project]:
    """Get list of projects with filtering"""
    query = db.query(Project).filter(Project.is_active == True)
    
    if status:
        query = query.filter(Project.status == status)
    if sd_owner:
        query = query.filter(Project.sd_owner == sd_owner)
        
    return query.order_by(Project.created_date.desc()).offset(skip).limit(limit).all()

def create_project(db: Session, project: ProjectCreate, created_by: str = None) -> Project:
    """Create a new project"""
    project_data = project.dict()
    project_data['id'] = str(uuid.uuid4())
    project_data['created_by'] = created_by
    
    db_project = Project(**project_data)
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

def update_project(db: Session, project_id: str, project_update: ProjectUpdate) -> Optional[Project]:
    """Update an existing project"""
    db_project = get_project(db, project_id)
    if not db_project:
        return None
    
    update_data = project_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_project, field, value)
    
    db.commit()
    db.refresh(db_project)
    return db_project

def get_projects_by_status(db: Session, status: ProjectStatus) -> List[Project]:
    """Get projects by status"""
    return db.query(Project).filter(
        Project.status == status, 
        Project.is_active == True
    ).all()