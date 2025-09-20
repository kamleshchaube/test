from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.lead import Lead
from app.schemas.lead import LeadCreate, LeadUpdate
import uuid

def get_lead(db: Session, lead_id: str) -> Optional[Lead]:
    return db.query(Lead).filter(Lead.id == lead_id).first()

def get_lead_by_email(db: Session, email: str) -> Optional[Lead]:
    return db.query(Lead).filter(Lead.email == email).first()

def get_leads(
    db: Session, 
    skip: int = 0, 
    limit: int = 100,
    status: Optional[str] = None,
    assigned_to: Optional[str] = None,
    tender_type: Optional[str] = None
) -> List[Lead]:
    query = db.query(Lead).filter(Lead.is_active == True)
    
    if status:
        query = query.filter(Lead.status == status)
    if assigned_to:
        query = query.filter(Lead.assigned_to == assigned_to)
    if tender_type:
        query = query.filter(Lead.tender_type == tender_type)
        
    return query.order_by(Lead.created_date.desc()).offset(skip).limit(limit).all()

def create_lead(db: Session, lead: LeadCreate, created_by: str = None) -> Lead:
    lead_data = lead.dict()
    lead_data["id"] = str(uuid.uuid4())
    lead_data["created_by"] = created_by
    
    db_lead = Lead(**lead_data)
    db.add(db_lead)
    db.commit()
    db.refresh(db_lead)
    return db_lead

def update_lead(db: Session, lead_id: str, lead_update: LeadUpdate) -> Optional[Lead]:
    db_lead = get_lead(db, lead_id)
    if not db_lead:
        return None
    
    update_data = lead_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_lead, field, value)
    
    db.commit()
    db.refresh(db_lead)
    return db_lead

def delete_lead(db: Session, lead_id: str) -> bool:
    db_lead = get_lead(db, lead_id)
    if not db_lead:
        return False
    
    db_lead.is_active = False
    db.commit()
    return True

def get_leads_analytics(db: Session) -> dict:
    total_leads = db.query(Lead).filter(Lead.is_active == True).count()
    qualified_leads = db.query(Lead).filter(
        Lead.status == "qualified",
        Lead.is_active == True
    ).count()
    converted_leads = db.query(Lead).filter(
        Lead.status == "converted",
        Lead.is_active == True
    ).count()
    
    conversion_rate = (converted_leads / total_leads * 100) if total_leads > 0 else 0
    
    return {
        "total_leads": total_leads,
        "qualified_leads": qualified_leads,
        "converted_leads": converted_leads,
        "conversion_rate": round(conversion_rate, 2)
    }