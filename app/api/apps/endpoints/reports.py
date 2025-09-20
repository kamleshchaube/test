from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import Optional, Dict, Any
from datetime import datetime, date
from app.core.database import get_db
from app.core.security import get_current_user
from app.models.user import User
from app.crud import lead as crud_lead
from app.crud import opportunity as crud_opportunity
from app.crud import activity as crud_activity

router = APIRouter()

@router.get("/dashboard")
def get_dashboard_metrics(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> Dict[str, Any]:
    """Get dashboard metrics and KPIs"""
    
    # Lead metrics
    lead_analytics = crud_lead.get_leads_analytics(db)
    
    # Opportunity metrics
    try:
        opportunity_analytics = crud_opportunity.get_opportunities_analytics(db)
    except:
        opportunity_analytics = {"total": 0, "won": 0, "pipeline_value": 0}
    
    # Activity metrics
    try:
        activity_analytics = crud_activity.get_activities_analytics(db)
    except:
        activity_analytics = {"total": 0, "completed": 0, "pending": 0}
    
    return {
        "leads": lead_analytics,
        "opportunities": opportunity_analytics,
        "activities": activity_analytics,
        "generated_at": datetime.utcnow()
    }

@router.get("/leads-summary")
def get_leads_summary(
    start_date: Optional[date] = Query(None),
    end_date: Optional[date] = Query(None),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> Dict[str, Any]:
    """Get leads summary report"""
    
    # Get lead statistics
    analytics = crud_lead.get_leads_analytics(db)
    
    return {
        "summary": analytics,
        "period": {
            "start_date": start_date,
            "end_date": end_date
        },
        "generated_at": datetime.utcnow(),
        "generated_by": current_user.email
    }

@router.get("/sales-pipeline")
def get_sales_pipeline(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> Dict[str, Any]:
    """Get sales pipeline report"""
    
    try:
        pipeline_data = crud_opportunity.get_pipeline_analytics(db)
    except:
        pipeline_data = {"stages": [], "total_value": 0}
    
    return {
        "pipeline": pipeline_data,
        "generated_at": datetime.utcnow(),
        "generated_by": current_user.email
    }

@router.get("/activity-summary")
def get_activity_summary(
    start_date: Optional[date] = Query(None),
    end_date: Optional[date] = Query(None),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> Dict[str, Any]:
    """Get activity summary report"""
    
    try:
        activity_data = crud_activity.get_activities_analytics(db)
    except:
        activity_data = {"total": 0, "by_type": {}, "by_status": {}}
    
    return {
        "activities": activity_data,
        "period": {
            "start_date": start_date,
            "end_date": end_date
        },
        "generated_at": datetime.utcnow(),
        "generated_by": current_user.email
    }