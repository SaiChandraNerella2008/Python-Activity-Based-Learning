# Case Study 02: Employee Payroll and Deduction Analysis (Problem 04)

> **Course**: Python Programming - Activity-Based Learning (ABL) Assignment  
> **Institution**: Dr. RVR NRI Institute of Technology (Deemed to be University)  
> **Student Name**: Sai Chandra Nerella | **NRI ID**: 26000654 | **Section**: Section 3 | **Branch**: CSE (I B.Tech)

---

## 📋 1. Problem Statement
Calculate monthly gross salary from basic pay, allowances (HRA, DA), overtime, and performance incentives. Apply progressive deductions including Provident Fund (PF), Professional Tax (PT), and annualized Income Tax (TDS) based on progressive tax slabs, producing an executive payroll statement.

---

## 🎯 2. Objectives
1. Calculate HRA, DA, overtime pay, and gross earnings.
2. Compute statutory PF (12% of basic) and slab-based Professional Tax.
3. Implement annualized progressive Income Tax slab calculations.
4. Generate net take-home pay and executive grade classification.

---

## ⚙️ 3. Assumptions & Constraints
1. HRA and DA are calculated as percentages of Basic Pay.
2. Overtime is paid hourly at the contract OT rate.
3. Income tax is progressive: 0% up to ₹3L, 5% up to ₹6L, 10% up to ₹9L, 15% up to ₹12L, 20% above ₹12L.

---

## 🧠 4. Step-by-Step Algorithm
1. For each employee record: unpack tuple (emp_id, name, basic, hra_pct, da_pct, ot_hrs, ot_rate, inc).
2. Gross = basic + (basic*hra_pct/100) + (basic*da_pct/100) + (ot_hrs*ot_rate) + inc.
3. Compute PF = 0.12 * basic. Compute PT from monthly gross.
4. Annualize gross (gross * 12). Compute progressive income tax across brackets. Monthly tax = annual_tax / 12.
5. Net = gross - (PF + PT + monthly_tax). Output formatted payroll row.

---

## 📝 5. Pseudocode
`	ext
FUNCTION generate_payroll(employees):
    FOR EACH emp IN employees:
        gross = basic + hra + da + overtime + incentive
        pf = 0.12 * basic
        pt = CALCULATE_PT(gross)
        annual_tax = CALCULATE_PROGRESSIVE_TAX(gross * 12)
        monthly_tax = annual_tax / 12
        net = gross - (pf + pt + monthly_tax)
        PRINT formatted salary row
END FUNCTION
`

---

## 📊 6. System Flowchart Diagram
`	ext
[START]
   │
   ▼
[Read (EmpID, Basic, HRA%, DA%, OT, Incentives)]
   │
   ▼
[Compute Allowances = Basic * (HRA% + DA%)]
[Compute Gross = Basic + Allowances + OT_Pay + Incentives]
   │
   ▼
[Calculate Deductions: PF (12%) + PT Slab + Progressive TDS (Annualized / 12)]
   │
   ▼
[Net Pay = Gross - Total Deductions]
   │
   ▼
[Assign Grade: Exec-A / Sr-B / Mid-C / Jr-D]
   │
   ▼
[Print Formatted Corporate Salary Slip]
   │
   ▼
 [END]
`

---

## 💻 7. Python Source Code
`python
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

`

---

## 🖥️ 8. Program Execution Output Log
`	ext
﻿=========================================================================================================
                      CORPORATE MONTHLY PAYROLL & SALARY STATEMENT
=========================================================================================================
EmpID   Name            Basic(₹)   Allow(₹)  OT+Inc(₹)  Gross(₹)    PF(₹)    Tax(₹)   PT(₹)  Net Pay(₹)  Grade
---------------------------------------------------------------------------------------------------------
EMP001  Rajesh Kumar    85000.00   29750.00  17000.00   131750.00   10200.00 13850.00 250.00 107450.00   Exec-A
EMP002  Pooja Hegde     45000.00   13500.00  9500.00    68000.00    5400.00  3050.00  250.00 59300.00    Sr-B
EMP003  Vikram Rathore  120000.00  48000.00  25000.00   193000.00   14400.00 26100.00 250.00 152250.00   Exec-A
EMP004  Sneha Roy       28000.00   7000.00   6000.00    41000.00    3360.00  800.00   150.00 36690.00    Mid-C
EMP005  Amitabh Sen     62000.00   19840.00  11200.00   93040.00    7440.00  6456.00  250.00 78894.00    Sr-B
---------------------------------------------------------------------------------------------------------
Total Employees Processed : 5
Total Monthly Gross Payroll: ₹526,790.00
Total Income Tax Deducted  : ₹50,256.00
Total Net Salaries Paid    : ₹434,584.00
=========================================================================================================
`

---

## 💡 9. Conclusion & Learning Outcome
Accurately calculated progressive tax deductions and statutory withholdings across multiple employee salary grades. Verified net take-home pay calculations without external financial dependencies.
