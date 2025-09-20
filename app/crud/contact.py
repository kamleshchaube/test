from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.contact import Contact
from app.schemas.contact import ContactCreate, ContactUpdate
import uuid

def get_contact(db: Session, contact_id: str) -> Optional[Contact]:
    return db.query(Contact).filter(Contact.id == contact_id).first()

def get_contacts(db: Session, skip: int = 0, limit: int = 100) -> List[Contact]:
    return db.query(Contact).filter(Contact.is_active == True).offset(skip).limit(limit).all()

def create_contact(db: Session, contact: ContactCreate, created_by: str = None) -> Contact:
    contact_data = contact.dict()
    contact_data["id"] = str(uuid.uuid4())
    contact_data["created_by"] = created_by
    db_contact = Contact(**contact_data)
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact

def update_contact(db: Session, contact_id: str, contact_update: ContactUpdate) -> Optional[Contact]:
    db_contact = get_contact(db, contact_id)
    if not db_contact:
        return None
    update_data = contact_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_contact, field, value)
    db.commit()
    db.refresh(db_contact)
    return db_contact

def delete_contact(db: Session, contact_id: str) -> bool:
    db_contact = get_contact(db, contact_id)
    if not db_contact:
        return False
    db_contact.is_active = False
    db.commit()
    return True
