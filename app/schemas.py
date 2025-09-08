from pydantic import BaseModel
from typing import Optional

# Product Schemas
class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int
    
    class Config:
        from_attributes = True

# Order Schemas
class OrderBase(BaseModel):
    customer_name: str
    quantity: int
    product_id: int

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    id: int
    
    class Config:
        from_attributes = True