# Derek Green
# November 1, 2026
# P4HW2 - Multiple Employee Payroll
# Calculate individual pay and totals until the employee name is exactly Done.
# Newly prepared with AI assistance; no earlier source file was available.

# Pseudocode:
# Initialize total overtime pay, regular pay, gross pay, and employee count to zero.
# Ask for an employee name.
# While the name is not exactly Done, collect pay rate and hours worked.
# If hours exceed 40, calculate overtime hours and time-and-a-half overtime pay.
# Otherwise, set overtime hours and pay to zero.
# Calculate regular pay and gross pay, then display the employee's pay details.
# Add the pay amounts to the totals and increase the employee count.
# Ask for the next name.
# When Done is entered, display employee count and all pay totals.

print("P4HW2 - Derek Green")
total_overtime_pay = 0.0
total_regular_pay = 0.0
total_gross_pay = 0.0
employee_count = 0

employee_name = input('Enter employee name or "Done" to terminate: ')
while employee_name != "Done":
    pay_rate = float(input(f"Enter {employee_name}'s pay rate: "))
    hours_worked = float(input(f"Enter hours worked by {employee_name}: "))

    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * pay_rate * 1.5
        regular_pay = 40 * pay_rate
    else:
        overtime_hours = 0.0
        overtime_pay = 0.0
        regular_pay = hours_worked * pay_rate

    gross_pay = regular_pay + overtime_pay
    print(f"\nEmployee name: {employee_name}")
    print(f"{'Hours Worked':<15}{'Pay Rate':<12}{'Overtime':<12}{'Overtime Pay':<15}{'Regular Pay':<15}{'Gross Pay'}")
    print("----------------------------------------------------------------------------")
    print(f"{hours_worked:<15.2f}{pay_rate:<12.2f}{overtime_hours:<12.2f}{overtime_pay:<15.2f}{regular_pay:<15.2f}{gross_pay:.2f}\n")

    total_overtime_pay = total_overtime_pay + overtime_pay
    total_regular_pay = total_regular_pay + regular_pay
    total_gross_pay = total_gross_pay + gross_pay
    employee_count = employee_count + 1
    employee_name = input('Enter employee name or "Done" to terminate: ')

print(f"\nTotal number of employees entered: {employee_count}")
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")
