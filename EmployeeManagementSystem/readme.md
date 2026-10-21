
# 👨‍💼 Employee Management System

### A Python-Based Employee Record and Salary Management Application

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![JSON](https://img.shields.io/badge/Storage-JSON-orange)
![Status](https://img.shields.io/badge/Project-Completed-success)
![License](https://img.shields.io/badge/License-MIT-green)

## 📌 Project Overview

The **Employee Management System** is a Python-based application
designed to simplify employee record management and salary tracking.

The application allows an administrator to add new employees, view
employee information, search records, update existing details, delete
records, manage department information, and generate salary reports.

It uses Python's built-in libraries and JSON files for data storage,
making it suitable for beginners who want to learn Python programming,
file handling, modular programming, and real-world application logic.

## 🎯 Project Objectives

- Maintain employee records in an organized format.
- Reduce manual work involved in managing employee information.
- Provide quick employee search and update functionality.
- Generate salary summaries and department-wise payroll reports.
- Display employee statistics through a dashboard.
- Demonstrate practical Python programming concepts.

## ✨ Key Features

### 1. 🔐 Admin Login
- Login using a username and password.
- Limit login attempts.
- Access the application menu after successful login.

### 2. ➕ Employee Management
- Add new employee records.
- Generate employee IDs automatically.
- Store personal and professional information.
- View all registered employees.
- Update existing employee information.
- Delete employee records after confirmation.

### 3. 🔍 Employee Search
- Search employees by employee ID.
- Search employees by name.
- Display matching employee records.

### 4. 🏢 Department Management
- View available departments.
- Display employees department-wise.
- Count employees in each department.
- View department-wise payroll summaries.

### 5. 💰 Salary Management
- Store employee salary details.
- Generate salary reports for active employees.
- Calculate total monthly payroll.
- Estimate annual payroll.
- Calculate average salary.
- Identify the highest-paid active employee.

### 6. 📊 Dashboard
- Display total employees.
- Show active and inactive employees.
- Display the number of departments.
- Calculate total monthly payroll.
- Display average active employee salary.
- Summarize employee distribution by department.

### 7. 💾 Data Storage
- Store employee records in `employees.json`.
- Store department information in `departments.json`.
- Store demonstration login credentials in `users.json`.
- Retain saved records between application sessions.

### 8. 🛡️ Input Validation and Error Handling
- Validate numeric inputs.
- Check salary values.
- Validate joining dates.
- Handle invalid menu choices.
- Handle missing or malformed JSON files.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Application logic |
| JSON | Employee and department data storage |
| `json` module | Reading and writing JSON data |
| `pathlib` module | File path management |
| `datetime` module | Joining date validation |
| `collections.Counter` | Department statistics |

**External dependencies:** None.

## 📂 Project Structure

```text
EmployeeManagementSystem/
│
├── main.py
│   └── Application entry point, login and main menu
│
├── employee_manager.py
│   └── Employee CRUD operations and record management
│
├── salary_manager.py
│   └── Salary reports and department payroll
│
├── dashboard.py
│   └── Employee statistics and dashboard summary
│
├── utils.py
│   └── Input validation, employee IDs and formatting
│
├── employees.json
│   └── Employee records
│
├── departments.json
│   └── Department information
│
├── users.json
│   └── Demonstration login credentials
│
└── README.md
    └── Project documentation
```

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.10 or newer recommended.
- Visual Studio Code or another Python editor.
- Terminal or command prompt.

### Step 1: Clone the Repository

Replace `YOUR_USERNAME` with your GitHub username.

```bash
git clone https://github.com/YOUR_USERNAME/EmployeeManagementSystem.git
```

### Step 2: Navigate to the Project Folder

```bash
cd EmployeeManagementSystem
```

### Step 3: Verify Python Installation

```bash
python3 --version
```

On Windows, you can use:

```bash
python --version
```

### Step 4: Run the Application

On macOS or Linux:

```bash
python3 main.py
```

On Windows:

```bash
python main.py
```

No additional package installation is required.

## 🔑 Demo Login Credentials

Use the following credentials to access the demonstration application.

| Field | Value |
|---|---|
| Username | `admin` |
| Password | `admin123` |
| Role | Admin |

**Security note:** These credentials are for demonstration purposes
only. The current implementation stores passwords as plain text.
Do not use real or sensitive credentials in this project.

## 🖥️ Application Menu

After successful login, the application displays the following menu:

```text
========== MAIN MENU ==========

1. Dashboard
2. Add Employee
3. View All Employees
4. Search Employee
5. Update Employee
6. Delete Employee
7. Department-wise Employees
8. View Departments
9. Salary Report
10. Department Payroll
0. Exit

===============================
```

Select the required option to perform an operation.

## 🧪 Sample Employee Data

The project includes sample employee records for testing.

| Employee ID | Name | Department | Designation | Status |
|---|---|---|---|---|
| EMP1001 | Rahul Kumar | IT | Python Developer | Active |
| EMP1002 | Priya Sharma | HR | HR Executive | Active |
| EMP1003 | Arjun Reddy | Finance | Accountant | Inactive |

These records are fictional examples. You can add, update, or remove
records through the application.

## 📈 Sample Salary Report

The application calculates payroll using the salary values of active
employees only.

Example output:

```text
========== SALARY REPORT ==========

Active Employees : 2
Monthly Payroll  : Rs. 63,000.00
Annual Estimate  : Rs. 756,000.00
Average Salary   : Rs. 31,500.00
Highest Paid     : Rahul Kumar (Rs. 35,000.00)

===================================
```

The report values depend on the employee records stored in
`employees.json`.

## 🧠 Python Concepts Demonstrated

This project demonstrates the practical use of:

- Variables and data types
- Lists and dictionaries
- Conditional statements
- Loops and functions
- File handling
- JSON serialization and deserialization
- Exception handling
- Modules and imports
- List comprehensions
- Lambda functions
- The `max()` and `sum()` functions
- The `pathlib` and `datetime` modules
- Basic CRUD operations
- Data validation and reporting

## 🔄 CRUD Operations

CRUD stands for Create, Read, Update, and Delete.

| Operation | Description |
|---|---|
| Create | Add a new employee |
| Read | View or search employee details |
| Update | Modify employee information |
| Delete | Remove an employee record |

These operations form the foundation of many business applications.

## 🔮 Future Enhancements

The project can be extended with the following features:

- [ ] Flask or Django web interface
- [ ] HTML, CSS, and JavaScript frontend
- [ ] MySQL or SQLite database integration
- [ ] Secure password hashing
- [ ] Role-based access control
- [ ] Employee attendance management
- [ ] Leave management system
- [ ] Payroll deductions and allowances
- [ ] Export employee reports to CSV or Excel
- [ ] Pagination and advanced filtering
- [ ] Automated unit testing
- [ ] Employee profile photographs
- [ ] Cloud deployment

## ⚠️ Limitations

- The current application runs in the terminal.
- JSON files are used instead of a database.
- The demonstration login is not production-secure.
- Concurrent access and advanced user permissions are not supported.
- Salary calculations are basic estimates and do not include
  taxes, deductions, bonuses, or other payroll rules.

## 🎓 Learning Outcomes

By completing this project, beginners can gain practical experience in
Python programming, modular application design, data persistence,
employee record management, input validation, and report generation.

It is a useful foundation for progressing toward database-driven
applications and full-stack Python development.

## 👨‍💻 Author

Kaveri Ayyappa

GitHub: https://github.com/Ayyappa1295

## 📄 License

This project is distributed under the MIT License.

You can add a `LICENSE` file containing the standard MIT License text
if you intend to publish the project under that license.

---

⭐ If you find this project useful, consider giving the repository a star!
