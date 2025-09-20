from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.core.database import get_db
from app.schemas.product import Product, ProductCreate, ProductUpdate
from app.crud import product as crud_product
from app.core.security import get_current_user
from app.models.user import User

router = APIRouter()

@router.get("/", response_model=List[Product])
def get_products(
    skip: int = 0,
    limit: int = Query(default=100, le=1000),
    category: Optional[str] = Query(None),
    is_active: bool = Query(default=True),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get all products with filtering"""
    products = crud_product.get_products(
        db, skip=skip, limit=limit, category=category, is_active=is_active
    )
    return products

@router.get("/{product_id}", response_model=Product)
def get_product(
    product_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get a specific product by ID"""
    product = crud_product.get_product(db, product_id=product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    return product

@router.post("/", response_model=Product, status_code=status.HTTP_201_CREATED)
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Create a new product"""
    # Check if SKU already exists
    existing_product = crud_product.get_product_by_sku(db, sku=product.sku)
    if existing_product:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="SKU already exists"
        )
    
    return crud_product.create_product(db=db, product=product, created_by=current_user.email)

@router.put("/{product_id}", response_model=Product)
def update_product(
    product_id: str,
    product_update: ProductUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Update an existing product"""
    product = crud_product.update_product(db, product_id=product_id, product_update=product_update)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    return product

@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(
    product_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Soft delete a product"""
    success = crud_product.delete_product(db, product_id=product_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )