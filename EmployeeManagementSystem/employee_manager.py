
import json
from pathlib import Path

from utils import (
    get_text,
    get_integer,
    get_salary,
    get_date,
    generate_employee_id,
    print_employee
)

DATA_FILE = Path(__file__).with_name("employees.json")


def load_employees():
    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data, list):
            return data

        print("Invalid employee data format.")
        return []

    except (json.JSONDecodeError, OSError) as error:
        print(f"Could not read employee data: {error}")
        return []


def save_employees(employees):
    try:
        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(employees, file, indent=4)
        return True
    except OSError as error:
        print(f"Could not save employee data: {error}")
        return False


def list_employees():
    employees = load_employees()

    if not employees:
        print("\nNo employees found.")
        return

    print(f"\n{'ID':<12}{'NAME':<22}{'DEPARTMENT':<15}{'STATUS':<12}")
    print("-" * 61)

    for employee in employees:
        print(
            f"{employee.get('id', ''):<12}"
            f"{employee.get('name', '')[:20]:<22}"
            f"{employee.get('department', ''):<15}"
            f"{employee.get('status', ''):<12}"
        )

    print(f"\nTotal records: {len(employees)}")


def add_employee():
    employees = load_employees()

    print("\n--- ADD NEW EMPLOYEE ---")

    name = get_text("Full name: ")

    age = get_integer("Age: ", 18, 100)

    gender = get_text("Gender: ")
    email = get_text("Email: ")
    phone = get_text("Phone number: ")
    department = get_text("Department: ")
    designation = get_text("Designation: ")
    salary = get_salary()
    joining_date = get_date()

    employee = {
        "id": generate_employee_id(employees),
        "name": name,
        "age": age,
        "gender": gender,
        "email": email,
        "phone": phone,
        "department": department,
        "designation": designation,
        "salary": salary,
        "joining_date": joining_date,
        "status": "Active"
    }

    employees.append(employee)

    if save_employees(employees):
        print(f"\nEmployee added successfully!")
        print(f"Employee ID: {employee['id']}")


def search_employee():
    employees = load_employees()

    query = get_text("Enter employee ID or name: ").lower()

    matches = [
        employee for employee in employees
        if query in employee.get("id", "").lower()
        or query in employee.get("name", "").lower()
    ]

    if not matches:
        print("\nNo matching employee found.")
        return

    for employee in matches:
        print_employee(employee)


def update_employee():
    employees = load_employees()

    employee_id = get_text("Enter employee ID to update: ").upper()

    employee = next(
        (item for item in employees
         if item.get("id", "").upper() == employee_id),
        None
    )

    if employee is None:
        print("Employee not found.")
        return

    print_employee(employee)
    print("\nPress Enter to keep an existing value.")

    fields = {
        "name": "Name",
        "email": "Email",
        "phone": "Phone",
        "department": "Department",
        "designation": "Designation"
    }

    for field, label in fields.items():
        new_value = input(
            f"{label} [{employee.get(field, '')}]: "
        ).strip()

        if new_value:
            employee[field] = new_value

    new_age = input(f"Age [{employee['age']}]: ").strip()

    if new_age:
        try:
            age = int(new_age)
            if 18 <= age <= 100:
                employee["age"] = age
            else:
                print("Invalid age. Keeping the old value.")
        except ValueError:
            print("Invalid age. Keeping the old value.")

    new_salary = input(
        f"Salary [{employee['salary']}]: "
    ).strip()

    if new_salary:
        try:
            salary = float(new_salary)
            if 0 <= salary <= 100000000:
                employee["salary"] = round(salary, 2)
            else:
                print("Invalid salary. Keeping the old value.")
        except ValueError:
            print("Invalid salary. Keeping the old value.")

    new_status = input(
        f"Status [{employee['status']}] (Active/Inactive): "
    ).strip().title()

    if new_status in ("Active", "Inactive"):
        employee["status"] = new_status
    elif new_status:
        print("Invalid status. Keeping the old value.")

    if save_employees(employees):
        print("Employee updated successfully!")


def delete_employee():
    employees = load_employees()

    employee_id = get_text("Enter employee ID to delete: ").upper()

    employee = next(
        (item for item in employees
         if item.get("id", "").upper() == employee_id),
        None
    )

    if employee is None:
        print("Employee not found.")
        return

    print_employee(employee)

    confirm = input(
        "Are you sure you want to delete this employee? (yes/no): "
    ).strip().lower()

    if confirm != "yes":
        print("Deletion cancelled.")
        return

    remaining = [
        item for item in employees
        if item.get("id", "").upper() != employee_id
    ]

    if save_employees(remaining):
        print("Employee deleted successfully!")


def department_employees():
    employees = load_employees()
    department = get_text("Enter department name: ").lower()

    matches = [
        employee for employee in employees
        if employee.get("department", "").lower() == department
    ]

    if not matches:
        print("No employees found in this department.")
        return

    for employee in matches:
        print_employee(employee)
