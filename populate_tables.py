import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("grocery_store.db")
cursor = conn.cursor()

# Populate Suppliers
suppliers = [
    ("Fresh Farms", "123-456-7890"),
    ("Dairy World", "234-567-8901"),
    ("Grain Supplies", "345-678-9012"),
    ("Bakery Supplies", "456-789-0123")
]
cursor.executemany("""
INSERT INTO Suppliers (SupplierName, ContactInfo) VALUES (?, ?)
""", suppliers)

# Populate Products
products = [
    ("Apple", "Fruits", 0.5, 100, 1),
    ("Banana", "Fruits", 0.2, 150, 1),
    ("Milk", "Dairy", 1.5, 50, 2),
    ("Bread", "Bakery", 2.0, 30, 4),
    ("Eggs", "Dairy", 3.0, 20, 2)
]
cursor.executemany("""
INSERT INTO Products (ProductName, Category, Price, StockQuantity, SupplierID) VALUES (?, ?, ?, ?, ?)
""", products)

# Populate Customers
customers = [
    ("John", "Doe", "johndoe@example.com", 50),
    ("Jane", "Smith", "janesmith@example.com", 100),
    ("Alice", "Johnson", "alicej@example.com", 200)
]
cursor.executemany("""
INSERT INTO Customers (FirstName, LastName, Email, LoyaltyPoints) VALUES (?, ?, ?, ?)
""", customers)

# Populate Orders
orders = [
    (1, "2024-11-18", 5.0),
    (2, "2024-11-18", 7.0),
    (3, "2024-11-19", 6.0)
]
cursor.executemany("""
INSERT INTO Orders (CustomerID, OrderDate, TotalAmount) VALUES (?, ?, ?)
""", orders)

# Populate OrderDetails
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

print("Sample data populated successfully!")
