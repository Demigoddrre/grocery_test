import sqlite3

# Connect to the database
conn = sqlite3.connect("grocery_store.db")
cursor = conn.cursor()

# List of queries to run
queries = [
    "SELECT * FROM Customers;",
    "SELECT * FROM Products;",
    "SELECT * FROM Suppliers;",
    "SELECT * FROM Orders WHERE TotalAmount > 6;",
    "SELECT ProductName, Category, Price FROM Products WHERE StockQuantity > 50;",
    """
    SELECT C.FirstName || ' ' || C.LastName AS Customer, O.OrderDate, O.TotalAmount
    FROM Customers C
    INNER JOIN Orders O ON C.CustomerID = O.CustomerID
    WHERE O.TotalAmount > 5;
    """
]

# Run each query and print the results
for query in queries:
    print(f"Running query: {query}")
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print(row)
    print("-" * 50)

# Close the connection
conn.close()
