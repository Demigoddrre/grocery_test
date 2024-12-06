import sqlite3

# Connect to SQLite database (or create it)
conn = sqlite3.connect("grocery_store.db")
cursor = conn.cursor()

# Drop tables if they already exist for a clean slate
cursor.execute("DROP TABLE IF EXISTS Suppliers")
cursor.execute("DROP TABLE IF EXISTS Customers")
cursor.execute("DROP TABLE IF EXISTS Products")
cursor.execute("DROP TABLE IF EXISTS Orders")
cursor.execute("DROP TABLE IF EXISTS OrderDetails")

# Create tables for the grocery store database
# 1. Products Table
cursor.execute("""
CREATE TABLE Products (
    ProductID INTEGER PRIMARY KEY AUTOINCREMENT,
    ProductName TEXT NOT NULL,
    Category TEXT,
    Price REAL NOT NULL,
    StockQuantity INTEGER NOT NULL,
    SupplierID INTEGER,
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID)
)
""")

# 2. Customers Table
cursor.execute("""
CREATE TABLE Customers (
    CustomerID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL,
    Email TEXT UNIQUE,
    LoyaltyPoints INTEGER DEFAULT 0
)
""")

# 3. Orders Table
cursor.execute("""
CREATE TABLE Orders (
    OrderID INTEGER PRIMARY KEY AUTOINCREMENT,
    CustomerID INTEGER,
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    TotalAmount REAL NOT NULL,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
)
""")

# 4. OrderDetails Table
cursor.execute("""
CREATE TABLE OrderDetails (
    OrderDetailID INTEGER PRIMARY KEY AUTOINCREMENT,
    OrderID INTEGER,
    ProductID INTEGER,
    Quantity INTEGER NOT NULL,
    Price REAL NOT NULL,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
)
""")

# 5. Suppliers Table
cursor.execute("""
CREATE TABLE Suppliers (
    SupplierID INTEGER PRIMARY KEY AUTOINCREMENT,
    SupplierName TEXT NOT NULL,
    ContactInfo TEXT
)
""")

# Commit changes and close connection
conn.commit()
conn.close()

print("Database schema updated successfully!")
