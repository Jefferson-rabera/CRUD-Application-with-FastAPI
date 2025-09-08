#  FastAPI Products & Orders CRUD API

A complete RESTful API built with FastAPI for managing products and orders with SQLite database. This project demonstrates full CRUD operations, database relationships, input validation, and professional API development practices.

##  Table of Contents
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Installation & Setup](#-installation--setup)
- [API Documentation](#-api-documentation)
- [API Endpoints](#-api-endpoints)
- [Database Schema](#-database-schema)
- [Testing the API](#-testing-the-api)
- [Error Handling](#-error-handling)
- [Troubleshooting](#-troubleshooting)
- [Learning Journey](#-learning-journey)

##  Features

- **Complete CRUD Operations** - Create, Read, Update, Delete for Products and Orders
- **RESTful Design** - Proper HTTP methods and status codes
- **Database Relationships** - One-to-Many relationship between Products and Orders
- **Input Validation** - Pydantic schemas for robust data validation
- **Automatic Documentation** - Interactive Swagger UI and ReDoc
- **Error Handling** - Comprehensive error handling with meaningful messages
- **SQLite Database** - SQLAlchemy ORM with relationship management
- **Environment Configuration** - Proper configuration management with .env files

##  Tech Stack

- **Framework**: FastAPI 0.116.1
- **Database**: SQLite with SQLAlchemy 2.0.43
- **Validation**: Pydantic 2.11.7
- **Server**: Uvicorn 0.35.0
- **Environment**: python-dotenv 1.1.1
- **Language**: Python 3.8+

##  Project Structure

```
crud-app/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application setup
│   ├── database.py          # Database connection and configuration
│   ├── models.py            # SQLAlchemy database models
│   ├── schemas.py           # Pydantic schemas for validation
│   └── routes/
│       ├── __init__.py
│       ├── products.py      # Product-related endpoints
│       └── orders.py        # Order-related endpoints
├── requirements.txt         # Python dependencies
├── .env                    # Environment variables
├── start.bat               # Windows startup script
├── README.md               # This documentation
└── test.db                 # SQLite database (auto-generated)
```

##  Installation & Setup

### Prerequisites
- Python 3.8 or higher
- Git
- PowerShell or Command Prompt

### Step-by-Step Setup

1. **Clone and navigate to the project**
   ```bash
   cd C:\Users\JEFF\Desktop\PLP_actvities\MYSQL\week 8 Final Project\crud-app
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate virtual environment**
   ```bash
   # Windows
   venv\Scripts\activate
   
   # Mac/Linux
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**
   ```bash
   # Using the batch script (Windows)
   .\start.bat
   
   # Or manually
   uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
   ```

6. **Access the application**
   - API: http://127.0.0.1:8000
   - Interactive Docs: http://127.0.0.1:8000/docs
   - Alternative Docs: http://127.0.0.1:8000/redoc

##  API Documentation

FastAPI automatically generates interactive API documentation:

### Swagger UI
![Swagger UI](https://via.placeholder.com/800x400.png?text=Swagger+UI+Documentation)
Access at: http://127.0.0.1:8000/docs

### ReDoc
![ReDoc](https://via.placeholder.com/800x400.png?text=ReDoc+Documentation)
Access at: http://127.0.0.1:8000/redoc

## API Documentation
![Swagger UI](./screenshots/API%20successfully%20running.png)

## Product Management
![Create Product](./screenshots/create%20product.png)
![Get Products](./screenshots/get%20products.png)

## Order Management  
![Create Order](./screenshots/create%20order.png)
![Get Orders](./screenshots/get%20orders%202.png)

## Terminal Output
![Server Running](./screenshots/terminal%20output.png)

## API Endpoints

### Products Management

| Method | Endpoint | Description | Parameters |
|--------|----------|-------------|------------|
| `GET` | `/api/products/` | Get all products | `skip`, `limit` |
| `POST` | `/api/products/` | Create new product | `name`, `description`, `price` |
| `GET` | `/api/products/{id}` | Get specific product | `id` (path parameter) |
| `PUT` | `/api/products/{id}` | Update product | `id` + product data |
| `DELETE` | `/api/products/{id}` | Delete product | `id` |

### Orders Management

| Method | Endpoint | Description | Parameters |
|--------|----------|-------------|------------|
| `GET` | `/api/orders/` | Get all orders | `skip`, `limit` |
| `POST` | `/api/orders/` | Create new order | `customer_name`, `quantity`, `product_id` |
| `GET` | `/api/orders/{id}` | Get specific order | `id` |
| `DELETE` | `/api/orders/{id}` | Delete order | `id` |

##  Database Schema

### Products Table
```sql
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR NOT NULL UNIQUE,
    description TEXT,
    price FLOAT NOT NULL
);
```

### Orders Table
```sql
CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name VARCHAR NOT NULL,
    quantity INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products (id)
);
```

### Entity Relationship Diagram
```
Products (1) ──────── (∞) Orders
   │                        │
   ├─ id (PK)               ├─ id (PK)
   ├─ name (Unique)         ├─ customer_name
   ├─ description           ├─ quantity
   └─ price                 └─ product_id (FK to Products)
```

##  Testing the API

### Using Interactive Documentation
1. Visit http://127.0.0.1:8000/docs
2. Click on any endpoint
3. Click "Try it out"
4. Enter required parameters
5. Click "Execute"

### Using curl Commands

**Create a Product:**
```bash
curl -X POST "http://127.0.0.1:8000/api/products/" \
  -H "Content-Type: application/json" \
  -d '{"name": "Laptop", "description": "Gaming laptop", "price": 999.99}'
```

**Get All Products:**
```bash
curl "http://127.0.0.1:8000/api/products/"
```

**Create an Order:**
```bash
curl -X POST "http://127.0.0.1:8000/api/orders/" \
  -H "Content-Type: application/json" \
  -d '{"customer_name": "John Doe", "quantity": 2, "product_id": 1}'
```

**Update a Product:**
```bash
curl -X PUT "http://127.0.0.1:8000/api/products/1" \
  -H "Content-Type: application/json" \
  -d '{"name": "Gaming Laptop", "description": "Updated description", "price": 1099.99}'
```

**Delete a Product:**
```bash
curl -X DELETE "http://127.0.0.1:8000/api/products/1"
```

##  Error Handling

The API provides comprehensive error handling:

### Common Error Responses
- **400 Bad Request**: Validation errors or business rule violations
- **404 Not Found**: Resource not found
- **500 Internal Server Error**: Server-side errors

### Example Error Responses
```json
{
  "detail": "Product with name 'Laptop' already exists"
}
```

```json
{
  "detail": "Product not found"
}
```

## Troubleshooting

### Common Issues and Solutions

**Port Already in Use**
```bash
uvicorn app.main:app --reload --port 8001
```

**Module Not Found Errors**
```bash
# Reactivate virtual environment and reinstall
venv\Scripts\activate
pip install -r requirements.txt
```

**Database Connection Issues**
- Delete `test.db` file and restart application
- Check `.env` file exists with: `DATABASE_URL=sqlite:///./test.db`

**Browser Connection Issues**
- Use http://127.0.0.1:8000 instead of http://localhost:8000
- Check firewall settings

##  Learning Journey

### Key Concepts Demonstrated

1. **RESTful API Design**
   - Proper HTTP methods (GET, POST, PUT, DELETE)
   - Appropriate HTTP status codes
   - Resource-based URL design

2. **Database Management**
   - SQLAlchemy ORM integration
   - Database relationships (One-to-Many)
   - Migration-free development with SQLite

3. **Input Validation**
   - Pydantic schema validation
   - Type hints and data validation
   - Custom validation rules

4. **Error Handling**
   - HTTPException handling
   - Database constraint handling
   - User-friendly error messages

5. **Project Structure**
   - Modular architecture
   - Separation of concerns
   - Environment configuration

### Challenges Overcome

- **Circular Imports**: Resolved by proper import structure
- **Database Relationships**: Implemented One-to-Many relationships
- **Unique Constraints**: Handled database integrity errors
- **Environment Configuration**: Proper use of environment variables

## License

This project was developed for educational purposes as part of the PLP (Power Learn Project) DBMS Final project.


## TO-DO

If you encounter any issues:
1. Check the interactive documentation at http://127.0.0.1:8000/docs
2. Verify all files are in the correct locations
3. Ensure virtual environment is activated
4. Check that all dependencies are installed



