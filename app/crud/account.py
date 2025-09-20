from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.account import Account
from app.schemas.account import AccountCreate, AccountUpdate
import uuid

def get_account(db: Session, account_id: str) -> Optional[Account]:
    return db.query(Account).filter(Account.id == account_id).first()

def get_accounts(db: Session, skip: int = 0, limit: int = 100) -> List[Account]:
    return db.query(Account).filter(Account.is_active == True).offset(skip).limit(limit).all()

def create_account(db: Session, account: AccountCreate, created_by: str = None) -> Account:
    account_data = account.dict()
    account_data["id"] = str(uuid.uuid4())
    account_data["created_by"] = created_by
    db_account = Account(**account_data)
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account

def update_account(db: Session, account_id: str, account_update: AccountUpdate) -> Optional[Account]:
    db_account = get_account(db, account_id)
    if not db_account:
        return None
    update_data = account_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_account, field, value)
    db.commit()
    db.refresh(db_account)
    return db_account

def delete_account(db: Session, account_id: str) -> bool:
    db_account = get_account(db, account_id)
    if not db_account:
        return False
    db_account.is_active = False
    db.commit()
    return True
