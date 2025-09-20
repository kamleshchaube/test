from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.schemas.campaign import Campaign, CampaignCreate, CampaignUpdate
from app.crud import campaign as crud_campaign

router = APIRouter()

@router.get("/", response_model=List[Campaign])
def get_campaigns(db: Session = Depends(get_db)):
    return crud_campaign.get_campaigns(db)

@router.post("/", response_model=Campaign)
def create_campaign(campaign: CampaignCreate, db: Session = Depends(get_db)):
    return crud_campaign.create_campaign(db=db, campaign=campaign)

@router.get("/{campaign_id}", response_model=Campaign)
def get_campaign(campaign_id: str, db: Session = Depends(get_db)):
    campaign = crud_campaign.get_campaign(db, campaign_id=campaign_id)
    if not campaign:
        raise HTTPException(status_code=404, detail="Campaign not found")
    return campaign

@router.put("/{campaign_id}", response_model=Campaign)
def update_campaign(campaign_id: str, campaign_update: CampaignUpdate, db: Session = Depends(get_db)):
    db_campaign = crud_campaign.update_campaign(db, campaign_id, campaign_update)
    if not db_campaign:
        raise HTTPException(status_code=404, detail="Campaign not found")
    return db_campaign
