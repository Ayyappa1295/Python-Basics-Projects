
from collections import Counter
from employee_manager import load_employees


def show_dashboard():
    employees = load_employees()

    active = [
        employee for employee in employees
        if employee.get("status") == "Active"
    ]

    inactive = [
        employee for employee in employees
        if employee.get("status") == "Inactive"
    ]

    departments = Counter(
        employee.get("department", "Unknown")
        for employee in employees
    )

    total_payroll = sum(
        employee.get("salary", 0) for employee in active
    )

    average_salary = (
        total_payroll / len(active) if active else 0
    )

    print("\n" + "=" * 45)
    print("       EMPLOYEE MANAGEMENT DASHBOARD")
    print("=" * 45)

    print(f"Total Employees       : {len(employees)}")
    print(f"Active Employees      : {len(active)}")
    print(f"Inactive Employees    : {len(inactive)}")
    print(f"Departments           : {len(departments)}")
    print(f"Monthly Active Payroll: Rs. {total_payroll:,.2f}")
    print(f"Average Active Salary : Rs. {average_salary:,.2f}")

    print("\n--- Department Summary ---")

    if departments:
        for department, count in sorted(departments.items()):
            print(f"{department:<20}: {count} employee(s)")
    else:
        print("No department data available.")

    print("=" * 45)
