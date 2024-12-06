
---

# Grocery Store SQL Practice - README

This guide explains how to set up and practice SQL queries using the grocery store database. This project is designed for **testing and practicing SQL queries** using a sample SQLite database.

---

## **Overview**

The project provides a SQLite database (`grocery_store.db`) preloaded with sample data to help you practice writing and executing SQL queries. You can interact with the database through the SQLite terminal or Python scripts.

---

## **1. Using SQLite Terminal**

### **Step 1: Open SQLite Shell**
1. Run the following command in your terminal to open the SQLite command-line interface:
   ```bash
   sqlite3 grocery_store.db
   ```
2. This connects to the `grocery_store.db` database.

---

### **Step 2: List All Tables**
1. To verify the database structure, use the command:
   ```sql
   .tables
   ```
2. Output:
   ```
   Customers  OrderDetails  Orders  Products  Suppliers
   ```

---

### **Step 3: Run Queries**
Use SQL commands to interact with the database.

- **Example 1:** View all customers.
  ```sql
  SELECT * FROM Customers;
  ```
- **Example 2:** View all products.
  ```sql
  SELECT * FROM Products;
  ```
- **Example 3:** Find orders with a total amount greater than $6.
  ```sql
  SELECT * FROM Orders WHERE TotalAmount > 6;
  ```
- **Example 4:** View all suppliers.
  ```sql
  SELECT * FROM Suppliers;
  ```

---

### **Step 4: Exit SQLite**
To close the SQLite terminal, type:
```bash
.quit
```

---

## **2. Using a Python File**

### **Step 1: Save the Python Script**
1. Create a file called `run_queries.py`.
2. Add the following code to execute SQL queries programmatically:

```python
import sqlite3

# Connect to the database
conn = sqlite3.connect("grocery_store.db")
cursor = conn.cursor()

# List of queries to run
queries = [
    "SELECT * FROM Customers;",
    "SELECT * FROM Products;",
    "SELECT * FROM Orders WHERE TotalAmount > 6;",
    "SELECT Name, Category, Price FROM Products WHERE Stock > 50;",
    "SELECT * FROM Suppliers;",
    """
    SELECT C.Name AS Customer, O.OrderDate, O.TotalAmount
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
```

---

### **Step 2: Run the Python Script**
Run the file in your terminal using:
```bash
python run_queries.py
```

---

## **Database Schema**

This project uses the following schema:

1. **Customers Table**:
   - `CustomerID`: Unique identifier for each customer.
   - `Name`: Full name of the customer.
   - `Email`: Email address of the customer (must be unique).
   - `Phone`: Contact number of the customer.
   - `Address`: Residential address of the customer.

2. **Products Table**:
   - `ProductID`: Unique identifier for each product.
   - `Name`: Product name.
   - `Category`: Product category (e.g., Fruits, Dairy).
   - `Price`: Price of the product.
   - `Stock`: Quantity of the product in stock.

3. **Orders Table**:
   - `OrderID`: Unique identifier for each order.
   - `CustomerID`: Reference to the `CustomerID` in the `Customers` table.
   - `OrderDate`: Date the order was placed.
   - `TotalAmount`: Total amount for the order.

4. **OrderDetails Table**:
   - `OrderDetailID`: Unique identifier for each order detail.
   - `OrderID`: Reference to the `OrderID` in the `Orders` table.
   - `ProductID`: Reference to the `ProductID` in the `Products` table.
   - `Quantity`: Quantity of the product in the order.
   - `Price`: Price of the product at the time of the order.

5. **Suppliers Table**:
   - `SupplierID`: Unique identifier for each supplier.
   - `SupplierName`: Name of the supplier.
   - `ContactInfo`: Contact information for the supplier.

---

## **Purpose**

This project is intended for **SQL practice only**:
- Experiment with writing and running queries against a sample SQLite database.
- Explore `JOIN`, `GROUP BY`, `WHERE`, and other SQL clauses.
- Use Python to automate query execution and analyze results.

---

## **Getting Started**

### **Step 1: Clone the Repository**
Clone this repository to your local machine:
```bash
git clone <repository-url>
cd grocery_store_sql_practice
```

### **Step 2: Install SQLite (if not already installed)**
SQLite is typically pre-installed on most systems. To check:
```bash
sqlite3 --version
```
If not installed, follow [SQLite Installation Guide](https://www.sqlite.org/download.html).

---

## **Tips for Practice**
- Modify the provided queries to match your learning objectives.
- Combine `JOIN`, `WHERE`, and `GROUP BY` clauses for advanced practice.
- Try creating new tables or adding more sample data to expand your practice.

---

If you have any questions or need assistance, feel free to ask! 🚀