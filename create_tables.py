import sqlite3

# Connect to SQLite database (or create it)
conn = sqlite3.connect("grocery_store.db")
cursor = conn.cursor()

# Drop tables if they already exist for a clean slate
cursor.execute("DROP TABLE IF EXISTS Customers")
cursor.execute("DROP TABLE IF EXISTS Products")
cursor.execute("DROP TABLE IF EXISTS Orders")
cursor.execute("DROP TABLE IF EXISTS OrderDetails")

# Create tables for the grocery store database
# 1. Customers Table
cursor.execute("""
CREATE TABLE Customers (
    CustomerID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Email TEXT NOT NULL UNIQUE,
    Phone TEXT,
    Address TEXT
)
""")

# 2. Products Table
cursor.execute("""
CREATE TABLE Products (
    ProductID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Category TEXT NOT NULL,
    Price REAL NOT NULL,
    Stock INTEGER NOT NULL
)
""")

# 3. Orders Table
cursor.execute("""
CREATE TABLE Orders (
    OrderID INTEGER PRIMARY KEY AUTOINCREMENT,
    CustomerID INTEGER,
    OrderDate TEXT NOT NULL,
    TotalAmount REAL,
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

# Insert sample data
# Insert sample customers
customers = [
    ("John Doe", "johndoe@example.com", "123-456-7890", "123 Elm St, Springfield"),
    ("Jane Smith", "janesmith@example.com", "234-567-8901", "456 Oak St, Springfield"),
    ("Alice Johnson", "alicej@example.com", "345-678-9012", "789 Pine St, Springfield")
]
cursor.executemany("""
INSERT INTO Customers (Name, Email, Phone, Address) VALUES (?, ?, ?, ?)
""", customers)

# Insert sample products
products = [
    ("Apple", "Fruits", 0.5, 100),
    ("Banana", "Fruits", 0.2, 150),
    ("Milk", "Dairy", 1.5, 50),
    ("Bread", "Bakery", 2.0, 30),
    ("Eggs", "Dairy", 3.0, 20)
]
cursor.executemany("""
INSERT INTO Products (Name, Category, Price, Stock) VALUES (?, ?, ?, ?)
""", products)

# Insert sample orders
orders = [
    (1, "2024-11-18", 5.0),
    (2, "2024-11-18", 7.0),
    (3, "2024-11-19", 6.0)
]
cursor.executemany("""
INSERT INTO Orders (CustomerID, OrderDate, TotalAmount) VALUES (?, ?, ?)
""", orders)

# Insert sample order details
order_details = [
    (1, 1, 5, 0.5),  # OrderID 1, ProductID 1 (Apple), Quantity 5, Price 0.5
    (1, 2, 10, 0.2), # OrderID 1, ProductID 2 (Banana), Quantity 10, Price 0.2
    (2, 3, 2, 1.5),  # OrderID 2, ProductID 3 (Milk), Quantity 2, Price 1.5
    (2, 4, 1, 2.0),  # OrderID 2, ProductID 4 (Bread), Quantity 1, Price 2.0
    (3, 5, 1, 3.0)   # OrderID 3, ProductID 5 (Eggs), Quantity 1, Price 3.0
]
cursor.executemany("""
INSERT INTO OrderDetails (OrderID, ProductID, Quantity, Price) VALUES (?, ?, ?, ?)
""", order_details)

# Commit changes and close connection
conn.commit()
conn.close()

print("Database and tables created successfully with sample data!")
