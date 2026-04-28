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
