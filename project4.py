# Salary Calculator

employee = input("Employee name: ").title().strip()
basic_salary = float(input("Basic salary: "))
transport_allowance = float(input("Transport allowance: "))
total_salary = basic_salary + transport_allowance

print(f"Employee: {employee}")
print(f"Basic Salary: ₦{basic_salary:,.2f}")
print(f"Transport: ₦{transport_allowance:,.2f}")
print(f"Total Salary: ₦{total_salary:,.2f}")