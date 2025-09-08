from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models import Order, Product  # SQLAlchemy models
from app.schemas import OrderCreate, Order as OrderSchema  # Pydantic schemas

router = APIRouter()

@router.get("/orders/", response_model=List[OrderSchema])
def read_orders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    orders = db.query(Order).offset(skip).limit(limit).all()  # Use of SQLAlchemy model
    return orders

@router.get("/orders/{order_id}", response_model=OrderSchema)
def read_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id).first()  # Use of SQLAlchemy model
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.post("/orders/", response_model=OrderSchema)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    # Check if product exists - Use of SQLAlchemy model
    product = db.query(Product).filter(Product.id == order.product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    
    # Create new order - Use of SQLAlchemy model
    new_order = Order(
        customer_name=order.customer_name,
        quantity=order.quantity,
        product_id=order.product_id
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order

@router.delete("/orders/{order_id}")
def delete_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id).first()  # Use SQLAlchemy model
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    
    db.delete(order)
    db.commit()
    return {"message": "Order deleted successfully"}