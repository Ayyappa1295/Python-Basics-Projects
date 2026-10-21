
from datetime import datetime


def get_text(prompt, required=True):
    while True:
        value = input(prompt).strip()

        if value or not required:
            return value

        print("This field is required. Please try again.")


def get_integer(prompt, minimum=0, maximum=120):
    while True:
        try:
            value = int(input(prompt))

            if minimum <= value <= maximum:
                return value

            print(f"Enter a value between {minimum} and {maximum}.")
        except ValueError:
            print("Please enter a valid whole number.")


def get_salary(prompt="Enter salary: "):
    while True:
        try:
            salary = float(input(prompt))

            if 0 <= salary <= 100000000:
                return round(salary, 2)

            print("Enter a valid non-negative salary.")
        except ValueError:
            print("Please enter a valid salary.")


def get_date(prompt="Joining date (YYYY-MM-DD): "):
    while True:
        value = input(prompt).strip()

        try:
            datetime.strptime(value, "%Y-%m-%d")
            return value
        except ValueError:
            print("Invalid date. Example: 2026-10-12")


def generate_employee_id(employees):
    numbers = []

    for employee in employees:
        employee_id = employee.get("id", "")

        if employee_id.startswith("EMP"):
            try:
                numbers.append(int(employee_id[3:]))
            except ValueError:
                pass

    next_number = max(numbers, default=1000) + 1
    return f"EMP{next_number}"


def print_employee(employee):
    print("-" * 65)
    print(f"Employee ID : {employee.get('id', '')}")
    print(f"Name        : {employee.get('name', '')}")
    print(f"Age         : {employee.get('age', '')}")
    print(f"Gender      : {employee.get('gender', '')}")
    print(f"Email       : {employee.get('email', '')}")
    print(f"Phone       : {employee.get('phone', '')}")
    print(f"Department  : {employee.get('department', '')}")
    print(f"Designation : {employee.get('designation', '')}")
    print(f"Salary      : Rs. {employee.get('salary', 0):,.2f}")
    print(f"Joining Date: {employee.get('joining_date', '')}")
    print(f"Status      : {employee.get('status', '')}")
    print("-" * 65)
