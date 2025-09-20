from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.campaign import Campaign
from app.schemas.campaign import CampaignCreate, CampaignUpdate
import uuid

def get_campaign(db: Session, campaign_id: str) -> Optional[Campaign]:
    return db.query(Campaign).filter(Campaign.id == campaign_id).first()

def get_campaigns(db: Session, skip: int = 0, limit: int = 100) -> List[Campaign]:
    return db.query(Campaign).filter(Campaign.is_active == True).offset(skip).limit(limit).all()

def create_campaign(db: Session, campaign: CampaignCreate, created_by: str = None) -> Campaign:
    campaign_data = campaign.dict()
    campaign_data["id"] = str(uuid.uuid4())
    campaign_data["created_by"] = created_by
    db_campaign = Campaign(**campaign_data)
    db.add(db_campaign)
    db.commit()
    db.refresh(db_campaign)
    return db_campaign

def update_campaign(db: Session, campaign_id: str, campaign_update: CampaignUpdate) -> Optional[Campaign]:
    db_campaign = get_campaign(db, campaign_id)
    if not db_campaign:
        return None
    update_data = campaign_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_campaign, field, value)
    db.commit()
    db.refresh(db_campaign)
    return db_campaign

def delete_campaign(db: Session, campaign_id: str) -> bool:
    db_campaign = get_campaign(db, campaign_id)
    if not db_campaign:
        return False
    db_campaign.is_active = False
    db.commit()
    return True
