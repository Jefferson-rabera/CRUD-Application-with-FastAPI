from fastapi import FastAPI
from app.database import engine
from app.models import Base

# Import routes 
from app.routes import products, orders 

# Create database tables
Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI(
    title="Products & Orders API",
    description="A simple CRUD API for managing products and orders",
    version="1.0.0"
)

# Include routers
app.include_router(products.router, prefix="/api", tags=["products"])
app.include_router(orders.router, prefix="/api", tags=["orders"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Products & Orders API!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}