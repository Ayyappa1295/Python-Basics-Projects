
import json
from pathlib import Path

from employee_manager import (
    add_employee,
    list_employees,
    search_employee,
    update_employee,
    delete_employee,
    department_employees
)

from salary_manager import (
    salary_report,
    department_payroll
)

from dashboard import show_dashboard


BASE_DIR = Path(__file__).resolve().parent
USERS_FILE = BASE_DIR / "users.json"
DEPARTMENTS_FILE = BASE_DIR / "departments.json"


def load_json_file(path, default):
    try:
        with path.open("r", encoding="utf-8") as file:
            return json.load(file)
    except (OSError, json.JSONDecodeError):
        return default


def login():
    users = load_json_file(USERS_FILE, [])

    if not users:
        print("No user accounts configured.")
        return False

    print("\n" + "=" * 42)
    print("       EMPLOYEE MANAGEMENT SYSTEM")
    print("=" * 42)

    for attempt in range(3):
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        user = next(
            (
                item for item in users
                if item.get("username") == username
                and item.get("password") == password
            ),
            None
        )

        if user:
            print(f"\nWelcome, {user['username']}!")
            return True

        print(f"Invalid credentials. Attempts left: {2 - attempt}")

    print("Too many failed attempts.")
    return False


def show_departments():
    departments = load_json_file(DEPARTMENTS_FILE, [])

    print("\n====== DEPARTMENTS ======")

    for number, department in enumerate(departments, start=1):
        print(f"{number}. {department}")

    print("=========================")


def main_menu():
    while True:
        print("""
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
""")

        choice = input("Enter your choice: ").strip()

        actions = {
            "1": show_dashboard,
            "2": add_employee,
            "3": list_employees,
            "4": search_employee,
            "5": update_employee,
            "6": delete_employee,
            "7": department_employees,
            "8": show_departments,
            "9": salary_report,
            "10": department_payroll
        }

        if choice == "0":
            print("Thank you for using Employee Management System!")
            break

        action = actions.get(choice)

        if action:
            try:
                action()
            except (ValueError, KeyError, TypeError) as error:
                print(f"Operation could not be completed: {error}")
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    if login():
        main_menu()
