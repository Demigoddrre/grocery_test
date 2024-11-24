# Grocery Store SQL Practice - README

This guide explains how to set up and practice SQL queries using the grocery store database in two ways: directly via the SQLite terminal and using Python scripts.

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
   Customers  OrderDetails  Orders  Products
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

## **Tips for Practice**
- Experiment with modifying the queries to match your learning objectives.
- Combine `JOIN`, `WHERE`, and `GROUP BY` clauses for advanced practice.
- Use the `sqlite3` Python library to automate data analysis and reporting tasks.

---

If you need help with additional SQL problems or debugging, feel free to ask!