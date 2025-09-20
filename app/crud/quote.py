from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.quote import Quote
from app.schemas.quote import QuoteCreate, QuoteUpdate
import uuid

def get_quote(db: Session, quote_id: str) -> Optional[Quote]:
    return db.query(Quote).filter(Quote.id == quote_id).first()

def get_quotes(db: Session, skip: int = 0, limit: int = 100) -> List[Quote]:
    return db.query(Quote).filter(Quote.is_active == True).offset(skip).limit(limit).all()

def create_quote(db: Session, quote: QuoteCreate, created_by: str = None) -> Quote:
    quote_data = quote.dict()
    quote_data["id"] = str(uuid.uuid4())
    quote_data["created_by"] = created_by
    db_quote = Quote(**quote_data)
    db.add(db_quote)
    db.commit()
    db.refresh(db_quote)
    return db_quote

def update_quote(db: Session, quote_id: str, quote_update: QuoteUpdate) -> Optional[Quote]:
    db_quote = get_quote(db, quote_id)
    if not db_quote:
        return None
    update_data = quote_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_quote, field, value)
    db.commit()
    db.refresh(db_quote)
    return db_quote

def delete_quote(db: Session, quote_id: str) -> bool:
    db_quote = get_quote(db, quote_id)
    if not db_quote:
        return False
    db_quote.is_active = False
    db.commit()
    return True
