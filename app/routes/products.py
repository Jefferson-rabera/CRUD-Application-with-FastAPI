from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models import Product  # SQLAlchemy model
from app.schemas import ProductCreate, Product as ProductSchema  # Pydantic schemas

router = APIRouter()

@router.get("/products/", response_model=List[ProductSchema])
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = db.query(Product).offset(skip).limit(limit).all()  
    return products

@router.get("/products/{product_id}", response_model=ProductSchema)
def read_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()  
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.post("/products/", response_model=ProductSchema)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    # Check if product already exists 
    db_product = db.query(Product).filter(Product.name == product.name).first()
    if db_product:
        raise HTTPException(status_code=400, detail="Product already exists")
    
    # Create new product 
    new_product = Product(
        name=product.name,
        description=product.description,
        price=product.price
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

@router.put("/products/{product_id}", response_model=ProductSchema)
def update_product(product_id: int, product: ProductCreate, db: Session = Depends(get_db)):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    
    # Check if the new name conflicts with any other product (excluding current one)
    if product.name != db_product.name:
        existing_product = db.query(Product).filter(
            Product.name == product.name,
            Product.id != product_id
        ).first()
        if existing_product:
            raise HTTPException(
                status_code=400,
                detail=f"Product with name '{product.name}' already exists"
            )
    
    # Update product fields
    db_product.name = product.name
    db_product.description = product.description
    db_product.price = product.price
    
    db.commit()
    db.refresh(db_product)
    return db_product

@router.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()  
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    
    db.delete(product)
    db.commit()
    return {"message": "Product deleted successfully"}