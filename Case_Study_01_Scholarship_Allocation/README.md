# Case Study 01: University Scholarship Allocation System (Problem 01)

> **Course**: Python Programming - Activity-Based Learning (ABL) Assignment  
> **Institution**: Dr. RVR NRI Institute of Technology (Deemed to be University)  
> **Student Name**: Sai Chandra Nerella | **Roll No**: 24NR1A0506 | **Branch**: CSE (I B.Tech)

---

## 📋 1. Problem Statement
Design an automated scholarship allocation system that evaluates applicants against aggregate marks, subject-wise minimum scores, attendance percentages, and family income criteria. Rank eligible candidates and resolve ties using deterministic rules (Aggregate Marks > Lower Annual Income > Higher Attendance).

---

## 🎯 2. Objectives
1. Validate applicant eligibility against 4 strict thresholds.
2. Classify awards into Fee Waiver Tiers (100%, 75%, 50%).
3. Implement deterministic tie-breaking logic using list sorting.
4. Produce detailed allocation and funds disbursement reports.

---

## ⚙️ 3. Assumptions & Constraints
1. Aggregate marks >= 80.0%, minimum subject mark >= 65.0%.
2. Attendance must be at least 75.0%.
3. Annual family income must not exceed ₹3,00,000.
4. Income and marks are non-negative numeric quantities.

---

## 🧠 4. Step-by-Step Algorithm
1. Initialize eligible_candidates list.
2. For each applicant tuple (id, name, agg, min_sub, att, inc): unpack tuple.
3. Check all 4 eligibility conditions. If passed, determine fee waiver tier and append to eligible list; else record rejection reason.
4. Apply bubble sort on eligible list comparing Aggregate (desc), Income (asc), Attendance (desc).
5. Iterate through ranked list, assign rank numbers, calculate total funds, and display report.

---

## 📝 5. Pseudocode
`	ext
FUNCTION evaluate_scholarships(applicants):
    SET eligible_list = []
    FOR EACH (id, name, agg, min_sub, att, inc) IN applicants:
        IF agg >= 80 AND min_sub >= 65 AND att >= 75 AND inc <= 300000 THEN
            tier = DETERMINE_TIER(agg)
            eligible_list.APPEND([id, name, agg, inc, att, tier])
        ELSE
            PRINT rejection reason
    SORT eligible_list BY agg DESC, inc ASC, att DESC
    DISPLAY final ranked recipients and total funds
END FUNCTION
`

---

## 📊 6. System Flowchart Diagram
`	ext
[START]
   │
   ▼
[Read Applicant Record (ID, Marks, Att, Income)]
   │
   ▼
<Is Agg >= 80 AND MinSub >= 65 AND Att >= 75 AND Inc <= 300K?>
   ├── YES ──► [Assign Waiver Tier (100% / 75% / 50%)] ──► [Add to Eligible Pool]
   │                                                               │
   └── NO  ──► [Record Specific Rejection Reason]                  ▼
                                                      [Apply Multi-Key Tie-Breaker Sort]
                                                               │
                                                               ▼
                                                      [Print Final Ranked Disbursal Table]
                                                               │
                                                               ▼
                                                             [END]
`

---

## 💻 7. Python Source Code
`python
"""
Case Study 1: University Scholarship Allocation System
Syllabus Concepts: Computational thinking, variables, data types, operators,
                   conditional statements, loops, lists, tuples, tuple unpacking.

Problem Statement:
Design a system that evaluates applicants using aggregate marks, subject-wise
minimum scores, attendance, and income criteria, ranks eligible students, and
resolves ties using predefined rules.
"""

def evaluate_scholarships(applicants):
    print("=" * 75)
    print("       UNIVERSITY SCHOLARSHIP ALLOCATION SYSTEM - EVALUATION REPORT")
    print("=" * 75)
    print(f"{'ID':<6} {'Name':<15} {'Aggregate':<10} {'Min Sub':<9} {'Attnd(%)':<9} {'Income(₹)':<11} {'Status'}")
    print("-" * 75)

    eligible_candidates = []

    # Process each applicant tuple: (id, name, agg_marks, min_sub_mark, attendance, annual_income)
    for applicant in applicants:
        app_id, name, agg_marks, min_sub, attendance, income = applicant

        # Eligibility Criteria:
        # 1. Aggregate Marks >= 80.0
        # 2. Minimum in any subject >= 65.0
        # 3. Attendance >= 75.0%
        # 4. Annual Family Income <= 300,000
        is_eligible = True
        reasons = []

        if agg_marks < 80.0:
            is_eligible = False
            reasons.append("Low Agg")
        if min_sub < 65.0:
            is_eligible = False
            reasons.append("Low Sub")
        if attendance < 75.0:
            is_eligible = False
            reasons.append("Low Att")
        if income > 300000:
            is_eligible = False
            reasons.append("High Inc")

        if is_eligible:
            status = "ELIGIBLE"
            # Category based on aggregate:
            if agg_marks >= 95.0:
                tier = "Tier-1 (100% Fee Waiver)"
                benefit = 100000
            elif agg_marks >= 90.0:
                tier = "Tier-2 (75% Fee Waiver)"
                benefit = 75000
            else:
                tier = "Tier-3 (50% Fee Waiver)"
                benefit = 50000
            eligible_candidates.append([app_id, name, agg_marks, min_sub, attendance, income, tier, benefit])
        else:
            status = "REJECTED (" + ", ".join(reasons) + ")"

        print(f"{app_id:<6} {name:<15} {agg_marks:<10.1f} {min_sub:<9.1f} {attendance:<9.1f} {income:<11} {status}")

    # Sorting & Tie-breaking using manual sorting logic (bubble sort for algorithmic demonstration)
    # Tie-breaking priority: 1) Aggregate Marks (descending), 2) Annual Income (ascending - needy first), 3) Attendance (descending)
    n = len(eligible_candidates)
    for i in range(n):
        for j in range(0, n - i - 1):
            cand1 = eligible_candidates[j]
            cand2 = eligible_candidates[j + 1]

            # Primary criterion: Aggregate marks (higher is better)
            swap = False
            if cand1[2] < cand2[2]:
                swap = True
            elif cand1[2] == cand2[2]:
                # Tie-breaker 1: Annual Income (lower is better)
                if cand1[5] > cand2[5]:
                    swap = True
                elif cand1[5] == cand2[5]:
                    # Tie-breaker 2: Attendance (higher is better)
                    if cand1[4] < cand2[4]:
                        swap = True

            if swap:
                eligible_candidates[j], eligible_candidates[j + 1] = eligible_candidates[j + 1], eligible_candidates[j]

    print("\n" + "=" * 75)
    print("                  FINAL RANKED SCHOLARSHIP RECIPIENTS")
    print("=" * 75)
    print(f"{'Rank':<6} {'ID':<6} {'Name':<15} {'Aggregate':<10} {'Income(₹)':<11} {'Attendance':<11} {'Award Category'}")
    print("-" * 75)

    rank = 1
    total_disbursed = 0
    for cand in eligible_candidates:
        c_id, c_name, c_agg, c_min, c_att, c_inc, c_tier, c_amt = cand
        print(f"{rank:<6} {c_id:<6} {c_name:<15} {c_agg:<10.1f} {c_inc:<11} {c_att:<11.1f}% {c_tier}")
        total_disbursed += c_amt
        rank += 1

    print("-" * 75)
    print(f"Total Eligible Candidates: {len(eligible_candidates)}")
    print(f"Total Scholarship Funds Allocated: ₹{total_disbursed:,}")
    print("=" * 75)


if __name__ == "__main__":
    # Test Data: List of tuples (ID, Name, AggregateMarks, MinSubjectMarks, AttendancePercent, AnnualIncome)
    dataset = [
        ("S101", "Aarav Sharma",   92.5, 78.0, 88.0, 180000),
        ("S102", "Bhavya Reddy",   78.0, 60.0, 82.0, 150000),  # Rejected: Agg < 80, MinSub < 65
        ("S103", "Chaitanya Roy",  96.0, 85.0, 94.0, 220000),  # Eligible: Tier-1
        ("S104", "Divya Patel",    92.5, 80.0, 85.0, 140000),  # Tie with S101, but lower income
        ("S105", "Eshwar Naik",    88.0, 72.0, 68.0, 120000),  # Rejected: Att < 75
        ("S106", "Fatima Zahra",   89.0, 70.0, 91.0, 280000),  # Eligible: Tier-3
        ("S107", "Gautam Verma",   94.0, 62.0, 89.0, 110000),  # Rejected: MinSub < 65
        ("S108", "Harika Devi",    96.0, 88.0, 96.0, 220000),  # Tie with S103 on Agg & Income, higher att
        ("S109", "Ishaan Joshi",   84.5, 68.0, 80.0, 350000),  # Rejected: Income > 300,000
        ("S110", "Jaspreet Kaur",  90.0, 74.0, 86.0, 190000),  # Eligible: Tier-2
    ]

    evaluate_scholarships(dataset)

`

---

## 🖥️ 8. Program Execution Output Log
`	ext
﻿===========================================================================
       UNIVERSITY SCHOLARSHIP ALLOCATION SYSTEM - EVALUATION REPORT
===========================================================================
ID     Name            Aggregate  Min Sub   Attnd(%)  Income(₹)   Status
---------------------------------------------------------------------------
S101   Aarav Sharma    92.5       78.0      88.0      180000      ELIGIBLE
S102   Bhavya Reddy    78.0       60.0      82.0      150000      REJECTED (Low Agg, Low Sub)
S103   Chaitanya Roy   96.0       85.0      94.0      220000      ELIGIBLE
S104   Divya Patel     92.5       80.0      85.0      140000      ELIGIBLE
S105   Eshwar Naik     88.0       72.0      68.0      120000      REJECTED (Low Att)
S106   Fatima Zahra    89.0       70.0      91.0      280000      ELIGIBLE
S107   Gautam Verma    94.0       62.0      89.0      110000      REJECTED (Low Sub)
S108   Harika Devi     96.0       88.0      96.0      220000      ELIGIBLE
S109   Ishaan Joshi    84.5       68.0      80.0      350000      REJECTED (High Inc)
S110   Jaspreet Kaur   90.0       74.0      86.0      190000      ELIGIBLE

===========================================================================
                  FINAL RANKED SCHOLARSHIP RECIPIENTS
===========================================================================
Rank   ID     Name            Aggregate  Income(₹)   Attendance  Award Category
---------------------------------------------------------------------------
1      S108   Harika Devi     96.0       220000      96.0       % Tier-1 (100% Fee Waiver)
2      S103   Chaitanya Roy   96.0       220000      94.0       % Tier-1 (100% Fee Waiver)
3      S104   Divya Patel     92.5       140000      85.0       % Tier-2 (75% Fee Waiver)
4      S101   Aarav Sharma    92.5       180000      88.0       % Tier-2 (75% Fee Waiver)
5      S110   Jaspreet Kaur   90.0       190000      86.0       % Tier-2 (75% Fee Waiver)
6      S106   Fatima Zahra    89.0       280000      91.0       % Tier-3 (50% Fee Waiver)
---------------------------------------------------------------------------
Total Eligible Candidates: 6
Total Scholarship Funds Allocated: ₹475,000
===========================================================================
`

---

## 💡 9. Conclusion & Learning Outcome
The system successfully evaluated, filtered, and ranked scholarship candidates. Ties between candidates with identical aggregates were deterministically resolved by prioritizing lower annual family income and higher attendance.
