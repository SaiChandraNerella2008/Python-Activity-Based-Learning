"""
Case Study 2 (Problem 4): Employee Payroll and Deduction Analysis
Syllabus Concepts: Computational thinking, variables, data types, operators,
                   conditional statements, loops, strings, lists, tuples, tuple unpacking.

Problem Statement:
Calculate gross salary from basic pay, allowances, overtime, and incentives; apply
progressive deductions (Income Tax, PF, Professional Tax) and generate a formatted
salary statement.
"""

def generate_payroll_statement(employees):
    print("=" * 105)
    print("                      CORPORATE MONTHLY PAYROLL & SALARY STATEMENT")
    print("=" * 105)
    print(f"{'EmpID':<7} {'Name':<15} {'Basic(₹)':<10} {'Allow(₹)':<9} {'OT+Inc(₹)':<10} {'Gross(₹)':<11} {'PF(₹)':<8} {'Tax(₹)':<8} {'PT(₹)':<6} {'Net Pay(₹)':<11} {'Grade'}")
    print("-" * 105)

    total_gross_disbursed = 0.0
    total_net_disbursed = 0.0
    total_tax_collected = 0.0

    for emp in employees:
        # Tuple unpacking: emp_id, name, basic_pay, hra_percent, da_percent, ot_hours, ot_rate, incentives
        emp_id, name, basic, hra_pct, da_pct, ot_hrs, ot_rate, incentives = emp

        # 1. Allowances calculation
        hra = (basic * hra_pct) / 100.0
        da = (basic * da_pct) / 100.0
        allowances = hra + da

        # 2. Overtime & Incentives
        overtime_pay = ot_hrs * ot_rate
        variable_pay = overtime_pay + incentives

        # 3. Gross Salary
        gross_salary = basic + allowances + variable_pay
        total_gross_disbursed += gross_salary

        # 4. Progressive Deductions:
        # a) Provident Fund (PF): 12% of basic pay (capped if basic exceeds threshold)
        pf_deduction = 0.12 * basic

        # b) Professional Tax (PT): slab-based
        if gross_salary > 50000:
            pt_deduction = 250.0
        elif gross_salary > 25000:
            pt_deduction = 150.0
        else:
            pt_deduction = 0.0

        # c) Progressive Monthly Income Tax (TDS) based on annualized gross:
        annual_gross = gross_salary * 12.0
        annual_tax = 0.0

        # Tax Slabs:
        # Up to ₹3,00,000 : Nil
        # ₹3,00,001 to ₹6,00,000 : 5%
        # ₹6,00,001 to ₹9,00,000 : 10%
        # ₹9,00,001 to ₹12,00,000 : 15%
        # Above ₹12,00,000 : 20%
        if annual_gross > 1200000:
            annual_tax += (annual_gross - 1200000) * 0.20
            annual_tax += 300000 * 0.15
            annual_tax += 300000 * 0.10
            annual_tax += 300000 * 0.05
        elif annual_gross > 900000:
            annual_tax += (annual_gross - 900000) * 0.15
            annual_tax += 300000 * 0.10
            annual_tax += 300000 * 0.05
        elif annual_gross > 600000:
            annual_tax += (annual_gross - 600000) * 0.10
            annual_tax += 300000 * 0.05
        elif annual_gross > 300000:
            annual_tax += (annual_gross - 300000) * 0.05
        else:
            annual_tax = 0.0

        monthly_tax = annual_tax / 12.0
        total_tax_collected += monthly_tax

        # Total Deductions & Net Pay
        total_deductions = pf_deduction + pt_deduction + monthly_tax
        net_salary = gross_salary - total_deductions
        total_net_disbursed += net_salary

        # Pay Grade Classification
        if gross_salary >= 100000:
            grade = "Exec-A"
        elif gross_salary >= 60000:
            grade = "Sr-B"
        elif gross_salary >= 35000:
            grade = "Mid-C"
        else:
            grade = "Jr-D"

        print(f"{emp_id:<7} {name:<15} {basic:<10.2f} {allowances:<9.2f} {variable_pay:<10.2f} {gross_salary:<11.2f} {pf_deduction:<8.2f} {monthly_tax:<8.2f} {pt_deduction:<6.2f} {net_salary:<11.2f} {grade}")

    print("-" * 105)
    print(f"Total Employees Processed : {len(employees)}")
    print(f"Total Monthly Gross Payroll: ₹{total_gross_disbursed:,.2f}")
    print(f"Total Income Tax Deducted  : ₹{total_tax_collected:,.2f}")
    print(f"Total Net Salaries Paid    : ₹{total_net_disbursed:,.2f}")
    print("=" * 105)


if __name__ == "__main__":
    # Test Data: (EmpID, Name, BasicPay, HRAPercent, DAPercent, OTHours, OTRate, Incentives)
    employee_records = [
        ("EMP001", "Rajesh Kumar",  85000, 20.0, 15.0, 10, 500, 12000),
        ("EMP002", "Pooja Hegde",   45000, 18.0, 12.0, 15, 300, 5000),
        ("EMP003", "Vikram Rathore", 120000, 25.0, 15.0, 0, 0, 25000),
        ("EMP004", "Sneha Roy",     28000, 15.0, 10.0, 20, 200, 2000),
        ("EMP005", "Amitabh Sen",   62000, 20.0, 12.0, 8, 400, 8000),
    ]

    generate_payroll_statement(employee_records)
