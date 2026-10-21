
from employee_manager import load_employees


def salary_report():
    employees = [
        employee for employee in load_employees()
        if employee.get("status") == "Active"
    ]

    if not employees:
        print("No active employees available.")
        return

    print("\n========== SALARY REPORT ==========")
    print(f"{'EMPLOYEE':<22}{'DEPARTMENT':<16}{'MONTHLY SALARY':>16}")
    print("-" * 56)

    for employee in employees:
        print(
            f"{employee.get('name', '')[:20]:<22}"
            f"{employee.get('department', ''):<16}"
            f"Rs. {employee.get('salary', 0):>12,.2f}"
        )

    total = sum(employee.get("salary", 0) for employee in employees)
    average = total / len(employees)
    highest = max(employees, key=lambda e: e.get("salary", 0))

    print("-" * 56)
    print(f"Active Employees : {len(employees)}")
    print(f"Monthly Payroll  : Rs. {total:,.2f}")
    print(f"Annual Estimate  : Rs. {total * 12:,.2f}")
    print(f"Average Salary   : Rs. {average:,.2f}")
    print(
        f"Highest Paid     : {highest.get('name', '')} "
        f"(Rs. {highest.get('salary', 0):,.2f})"
    )
    print("===================================")


def department_payroll():
    employees = [
        employee for employee in load_employees()
        if employee.get("status") == "Active"
    ]

    if not employees:
        print("No active employees available.")
        return

    totals = {}

    for employee in employees:
        department = employee.get("department", "Unknown")
        salary = employee.get("salary", 0)

        totals[department] = totals.get(department, 0) + salary

    print("\n====== DEPARTMENT PAYROLL ======")

    for department, total in sorted(totals.items()):
        print(f"{department:<20} Rs. {total:,.2f}")

    print("-" * 40)
    print(f"{'Total':<20} Rs. {sum(totals.values()):,.2f}")
