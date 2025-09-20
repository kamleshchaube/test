from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate
import uuid

def get_product(db: Session, product_id: str) -> Optional[Product]:
    """Get a single product by ID"""
    return db.query(Product).filter(Product.id == product_id).first()

def get_product_by_sku(db: Session, sku: str) -> Optional[Product]:
    """Get product by SKU"""
    return db.query(Product).filter(Product.sku == sku).first()

def get_products(
    db: Session, 
    skip: int = 0, 
    limit: int = 100,
    category: Optional[str] = None,
    is_active: bool = True
) -> List[Product]:
    """Get list of products with filtering"""
    query = db.query(Product).filter(Product.is_active == is_active)
    
    if category:
        query = query.filter(Product.category == category)
        
    return query.order_by(Product.name).offset(skip).limit(limit).all()

def create_product(db: Session, product: ProductCreate, created_by: str = None) -> Product:
    """Create a new product"""
    product_data = product.dict()
    product_data['id'] = str(uuid.uuid4())
    product_data['created_by'] = created_by
    
    db_product = Product(**product_data)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update_product(db: Session, product_id: str, product_update: ProductUpdate) -> Optional[Product]:
    """Update an existing product"""
    db_product = get_product(db, product_id)
    if not db_product:
        return None
    
    update_data = product_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_product, field, value)
    
    db.commit()
    db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: str) -> bool:
    """Soft delete a product"""
    db_product = get_product(db, product_id)
    if not db_product:
        return False
    
    db_product.is_active = False
    db.commit()
    return True

def get_active_products(db: Session) -> List[Product]:
    """Get all active products"""
    return db.query(Product).filter(Product.is_active == True).all()