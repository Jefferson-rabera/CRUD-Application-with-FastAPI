from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# Defining base here to avoid circular imports
Base = declarative_base()

class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    price = Column(Float)
    
    # Relationship with orders
    orders = relationship("Order", back_populates="product")

class Order(Base):
    __tablename__ = "orders"
    
    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String, index=True)
    quantity = Column(Integer)
    product_id = Column(Integer, ForeignKey("products.id"))
    
    # Relationship with product
    product = relationship("Product", back_populates="orders")