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
