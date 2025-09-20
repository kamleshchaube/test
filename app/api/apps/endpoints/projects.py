from fastapi import APIRouter, Depends, HTTPException, status, Query, UploadFile, File
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from datetime import datetime
from app.core.database import get_async_session
from app.schemas.project import Project, ProjectCreate, ProjectUpdate, ProjectStatusUpdate
from app.crud import project as crud_project
from app.api.deps import get_current_user

router = APIRouter()

@router.get("/", response_model=List[Project])
async def get_projects(
    skip: int = 0,
    limit: int = Query(default=100, le=1000),
    status: Optional[str] = Query(None),
    project_manager: Optional[str] = Query(None),
    sd_owner: Optional[str] = Query(None),
    account_id: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_async_session),
    current_user = Depends(get_current_user)
):
    """Get all projects with filtering and pagination"""
    projects = await crud_project.get_projects(
        db, 
        skip=skip, 
        limit=limit, 
        status=status,
        project_manager=project_manager,
        sd_owner=sd_owner,
        account_id=account_id
    )
    return projects

@router.get("/analytics")
async def get_project_analytics(
    db: AsyncSession = Depends(get_async_session),
    current_user = Depends(get_current_user)
):
    """Get project analytics and metrics"""
    return await crud_project.get_project_analytics(db)

@router.get("/{project_id}", response_model=Project)
async def get_project(
    project_id: str,
    db: AsyncSession = Depends(get_async_session),
    current_user = Depends(get_current_user)
):
    """Get a specific project by ID"""
    project = await crud_project.get_project(db, project_id=project_id)
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found"
        )
    return project

@router.post("/", response_model=Project, status_code=status.HTTP_201_CREATED)
async def create_project(
    project: ProjectCreate,
    db: AsyncSession = Depends(get_async_session),
    current_user = Depends(get_current_user)
):
    """Create a new project"""
    return await crud_project.create_project(
        db=db, 
        project=project, 
        created_by=current_user.email
    )

@router.put("/{project_id}", response_model=Project)
async def update_project(
    project_id: str,
    project_update: ProjectUpdate,
    db: AsyncSession = Depends(get_async_session),
    current_user = Depends(get_current_user)
):
    """Update an existing project"""
    project = await crud_project.update_project(
        db, 
        project_id=project_id, 
        project_update=project_update
    )
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found"
        )
    return project

@router.patch("/{project_id}/status")
async def update_project_status(
    project_id: str,
    status_update: ProjectStatusUpdate,
    db: AsyncSession = Depends(get_async_session),
    current_user = Depends(get_current_user)
):
    """Update project status with history tracking"""
    project = await crud_project.update_project_status(
        db, 
        project_id=project_id, 
        new_status=status_update.status,
        reason=status_update.reason,
        comment=status_update.comment,
        changed_by=current_user.email
    )
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found"
        )
    return {"message": "Project status updated successfully", "project": project}

@router.post("/{project_id}/signoff")
async def upload_client_signoff(
    project_id: str,
    file: UploadFile = File(...),
    db: AsyncSession = Depends(get_async_session),
    current_user = Depends(get_current_user)
):
    """Upload client signoff document"""
    # Validate file type
    allowed_types = ['application/pdf', 'image/jpeg', 'image/png', 'image/jpg']
    if file.content_type not in allowed_types:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only PDF and image files are allowed"
        )
    
    # Upload file and update project
    file_url = await crud_project.upload_signoff_document(
        db,
        project_id=project_id,
        file=file,
        uploaded_by=current_user.email
    )
    
    if not file_url:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found"
        )
    
    return {"message": "Signoff document uploaded successfully", "file_url": file_url}

@router.get("/{project_id}/history")
async def get_project_history(
    project_id: str,
    db: AsyncSession = Depends(get_async_session),
    current_user = Depends(get_current_user)
):
    """Get project status change history"""
    history = await crud_project.get_project_history(db, project_id=project_id)
    if history is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found"
        )
    return history

@router.delete("/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_project(
    project_id: str,
    db: AsyncSession = Depends(get_async_session),
    current_user = Depends(get_current_user)
):
    """Soft delete a project"""
    success = await crud_project.delete_project(db, project_id=project_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found"
        )