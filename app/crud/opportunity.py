from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.opportunity import Opportunity
from app.schemas.opportunity import OpportunityCreate, OpportunityUpdate
import uuid

def get_opportunity(db: Session, opportunity_id: str) -> Optional[Opportunity]:
    return db.query(Opportunity).filter(Opportunity.id == opportunity_id).first()

def get_opportunities(
    db: Session, 
    skip: int = 0, 
    limit: int = 100,
    stage: Optional[str] = None,
    assigned_to: Optional[str] = None
) -> List[Opportunity]:
    query = db.query(Opportunity).filter(Opportunity.is_active == True)
    
    if stage:
        query = query.filter(Opportunity.stage == stage)
    if assigned_to:
        query = query.filter(Opportunity.assigned_to == assigned_to)
        
    return query.order_by(Opportunity.created_date.desc()).offset(skip).limit(limit).all()

def create_opportunity(db: Session, opportunity: OpportunityCreate, created_by: str = None) -> Opportunity:
    opportunity_data = opportunity.dict()
    opportunity_data["id"] = str(uuid.uuid4())
    opportunity_data["created_by"] = created_by
    
    db_opportunity = Opportunity(**opportunity_data)
    db.add(db_opportunity)
    db.commit()
    db.refresh(db_opportunity)
    return db_opportunity

def update_opportunity(db: Session, opportunity_id: str, opportunity_update: OpportunityUpdate) -> Optional[Opportunity]:
    db_opportunity = get_opportunity(db, opportunity_id)
    if not db_opportunity:
        return None
    
    update_data = opportunity_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_opportunity, field, value)
    
    db.commit()
    db.refresh(db_opportunity)
    return db_opportunity

def get_pipeline_value(db: Session) -> float:
    opportunities = db.query(Opportunity).filter(
        Opportunity.stage.notin_(["won", "lost", "dropped"]),
        Opportunity.is_active == True
    ).all()
    return sum(opp.amount for opp in opportunities)

def get_opportunity_analytics(db: Session) -> dict:
    total_opportunities = db.query(Opportunity).filter(Opportunity.is_active == True).count()
    won_opportunities = db.query(Opportunity).filter(
        Opportunity.stage == "won",
        Opportunity.is_active == True
    ).count()
    
    win_rate = (won_opportunities / total_opportunities * 100) if total_opportunities > 0 else 0
    pipeline_value = get_pipeline_value(db)
    
    return {
        "total_opportunities": total_opportunities,
        "won_opportunities": won_opportunities,
        "win_rate": round(win_rate, 2),
        "pipeline_value": pipeline_value
    }