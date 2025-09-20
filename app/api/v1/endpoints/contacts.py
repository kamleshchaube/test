from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.schemas.contact import Contact, ContactCreate, ContactUpdate
from app.crud import contact as crud_contact

router = APIRouter()

@router.get("/", response_model=List[Contact])
def get_contacts(db: Session = Depends(get_db)):
    return crud_contact.get_contacts(db)

@router.post("/", response_model=Contact)
def create_contact(contact: ContactCreate, db: Session = Depends(get_db)):
    return crud_contact.create_contact(db=db, contact=contact)

@router.get("/{contact_id}", response_model=Contact)
def get_contact(contact_id: str, db: Session = Depends(get_db)):
    contact = crud_contact.get_contact(db, contact_id=contact_id)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact

@router.put("/{contact_id}", response_model=Contact)
def update_contact(contact_id: str, contact_update: ContactUpdate, db: Session = Depends(get_db)):
    db_contact = crud_contact.update_contact(db, contact_id, contact_update)
    if not db_contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return db_contact

@router.delete("/{contact_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_contact(contact_id: str, db: Session = Depends(get_db)):
    if not crud_contact.delete_contact(db, contact_id):
        raise HTTPException(status_code=404, detail="Contact not found")
    return {"message": "Contact deleted successfully"}
