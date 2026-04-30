# databaseconnectivty
Company Database – ER Diagram Documentation
🏢 Overview

This document describes the Entity-Relationship (ER) Model for a Company Database. It includes entities such as Employee, Branch, Client, and Supplier, along with their relationships.

📌 Entities and Attributes
1. 👨‍💼 Employee
emp_id (PK) – Unique employee ID
first_name
last_name
birth_date
sex
salary
age (derived attribute)
2. 🏬 Branch
branch_id (PK) – Unique branch ID
branch_name
#_employees (derived attribute)
3. 🤝 Client
client_id (PK) – Unique client ID
client_name
4. 🚚 Branch Supplier (Weak Entity)
supplier_name (Partial Key)
supply_type

🔹 Depends on Branch (owner entity)

🔗 Relationships
1. 🧑‍💼 Works For
Relationship between Employee → Branch
Type: 1 : N
One branch has many employees
Each employee works for one branch
2. 🧑‍💼 Manages
Relationship between Employee → Branch
Attribute: start_date
Type: 1 : 1
One employee manages one branch
Each branch has one manager
3. 👥 Works With
Relationship between Employee ↔ Client
Attribute: sales
Type: M : N
Employees work with multiple clients
Clients are served by multiple employees
4. 🔄 Handles
Relationship between Branch → Client
Type: 1 : N
One branch handles many clients
Each client belongs to one branch
5. 🚛 Supplies
Relationship between Branch Supplier ↔ Branch
Type: M : N
A supplier supplies to multiple branches
A branch has multiple suppliers
6. 👨‍🏫 Supervision (Recursive Relationship)
Relationship within Employee
Roles:
Supervisor (1)
Supervisee (N)
Type: 1 : N
One employee supervises many employees
🔑 Keys Summary
Entity	Primary Key	Notes
Employee	emp_id	Strong entity
Branch	branch_id	Strong entity
Client	client_id	Strong entity
Branch Supplier	supplier_name	Weak entity (partial key)
📌 Special Notes
Derived Attributes:
age (from birth_date)
#_employees (count of employees in branch)
Weak Entity:
Branch Supplier depends on Branch
Recursive Relationship:
Supervision in Employee
📷 ER Diagram

Replace er_diagram.png with your actual image file name.

✅ Conclusion

This ER model represents a company system with:

Multiple departments (branches)
Employee hierarchy
Client interactions
Supplier management.

# 📘 SQL Practice README – Company Database

---

## 🧭 Introduction

This document captures the SQL queries executed on a sample company database named `tech`, along with a clear step-by-step flow of what was done. It serves as both a learning reference and a revision guide.

The database includes:

* `employee`
* `branch`
* `client`
* `branch_supplier`
* `works_on`

---

## 🪜 Step-by-Step Process

### ✅ Step 1: Select the Database

Started by selecting the database to work on.

```sql
USE tech;
```

---

### ✅ Step 2: Perform Aggregation Queries

Counted employees based on gender and applied grouping.

```sql
SELECT COUNT(sex) FROM employee GROUP BY sex;

SELECT COUNT(sex), sex FROM employee GROUP BY sex;

SELECT COUNT(emp_id) 
FROM employee  
WHERE sex IN ("M", "F");
```

✔️ Learned:

* How to use `COUNT()`
* How `GROUP BY` works
* How to filter using `IN`

---

### ✅ Step 3: Apply Filtering with LIKE

Tried filtering client names using pattern matching.

```sql
SELECT * FROM client WHERE client_name LIKE 'LLC';
```

✔️ Understood:

* `'LLC'` → exact match
* `'%LLC'` → ends with LLC
* `'LLC%'` → starts with LLC
* `'%LLC%'` → contains LLC

---

### ✅ Step 4: Retrieve All Data

Fetched all records from the `client` table.

```sql
SELECT * FROM client;
```

✔️ Learned basic data retrieval.

---

### ✅ Step 5: Use UNION (Combine Results)

Combined employee names and branch names into one result.

```sql
SELECT employee.first_name FROM employee
UNION
SELECT branch.branch_name FROM branch;
```

✔️ Learned:

* How `UNION` merges results
* Removes duplicates automatically

---

### ✅ Step 6: Explore Table Structure

Checked table structures before applying joins.

```sql
DESC branch;
SELECT * FROM employee;
```

✔️ Important before joins to understand columns.

---

### ✅ Step 7: Perform INNER JOINs

Fetched common data across tables.

```sql
SELECT branch.branch_id, branch_name, first_name, salary 
FROM employee 
INNER JOIN branch 
ON employee.emp_id = branch.mgr_id;

SELECT client.client_name, branch.branch_name 
FROM branch 
INNER JOIN client 
ON branch.branch_id = client.branch_id;

SELECT branch.branch_id, branch_supplier.supplier_name, branch.branch_name
FROM branch 
INNER JOIN branch_supplier 
ON branch_supplier.branch_id = branch.branch_id;
```

✔️ Learned:

* How to connect tables
* How relationships work

---

### ✅ Step 8: Perform LEFT JOIN

Fetched all records from left table and matching from right.

```sql
SELECT branch.branch_name, branch_supplier.supplier_name 
FROM branch_supplier 
LEFT JOIN branch 
ON branch_supplier.branch_id = branch.branch_id;
```

✔️ Learned:

* Keeps all left table data

---

### ✅ Step 9: Perform RIGHT JOIN

Fetched all records from right table and matching from left.

```sql
SELECT branch.branch_name, branch_supplier.supplier_name 
FROM branch_supplier 
RIGHT JOIN branch 
ON branch_supplier.branch_id = branch.branch_id;
```

✔️ Learned:

* Keeps all right table data

---

### ✅ Step 10: Use Nested Query (Subquery)

Fetched employees who made sales greater than 50,000.

```sql
SELECT * 
FROM employee 
WHERE emp_id IN (
    SELECT DISTINCT works_on.emp_id  
    FROM works_on 
    WHERE works_on.total_sales > 50000
);
```

✔️ Learned:

* How subqueries work inside `WHERE`
* Use of `IN` with nested results

---

### ✅ Step 11: Identify and Fix Errors

❌ Incorrect:

```sql
WHERE sex IN("M" "F");
```

✅ Correct:

```sql
WHERE sex IN ("M", "F");
```

✔️ Learned:

* Proper syntax in `IN` condition

---

## 🧠 Key Concepts Covered

* Aggregation (`COUNT`)
* Grouping (`GROUP BY`)
* Filtering (`WHERE`, `LIKE`, `IN`)
* Combining results (`UNION`)
* Joins (`INNER`, `LEFT`, `RIGHT`)
* Nested queries (Subqueries)

---

## 🚀 Conclusion

This exercise builds a strong foundation in SQL. The step-by-step approach shows how to:

* Explore data
* Combine tables
* Filter results
* Solve real-world query problems
