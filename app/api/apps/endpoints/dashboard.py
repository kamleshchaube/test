from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.crud import lead as crud_lead
from app.crud import opportunity as crud_opportunity
from app.crud import activity as crud_activity

router = APIRouter()

@router.get("/metrics")
def get_dashboard_metrics(db: Session = Depends(get_db)):
    total_leads = crud_lead.get_leads_analytics(db)["total_leads"]
    total_opportunities = crud_opportunity.get_opportunity_analytics(db)["total_opportunities"]
    pipeline_value = crud_opportunity.get_pipeline_value(db)
    recent_activities = crud_activity.get_recent_activities(db, limit=10)
    
    return {
        "total_leads": total_leads,
        "total_opportunities": total_opportunities,
        "pipeline_value": pipeline_value,
        "recent_activities": recent_activities
    }

@router.get("/sales-funnel")
def get_sales_funnel(db: Session = Depends(get_db)):
    return {
        "stages": [
            {"name": "New Leads", "count": crud_lead.get_leads_analytics(db)["total_leads"]},
            {"name": "Qualified Leads", "count": crud_lead.get_leads_analytics(db)["qualified_leads"]},
            {"name": "Opportunities", "count": crud_opportunity.get_opportunity_analytics(db)["total_opportunities"]}
        ]
    }