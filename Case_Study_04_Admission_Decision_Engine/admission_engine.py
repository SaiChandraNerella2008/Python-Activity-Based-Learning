"""
Case Study 4 (Problem 20): University Admission Decision Engine
Syllabus Concepts: Computational thinking, variables, data types, operators,
                   conditional statements, loops, lists, nested lists, tuples, tuple unpacking.

Problem Statement:
Evaluate candidates for competitive engineering programs (e.g., Computer Science,
Electronics) using subject eligibility criteria (Maths, Physics, CS), overall aggregate,
entrance exam percentiles, and deterministic tie-breaking rules.
"""

def process_university_admissions(course_name, intake_seats, applicants):
    print("=" * 95)
    print(f"       METROPOLITAN UNIVERSITY - ADMISSION ALLOCATION ENGINE")
    print(f"       Target Department: {course_name} | Sanctioned Seat Capacity: {intake_seats}")
    print("=" * 95)
    print(f"{'AppID':<7} {'Name':<16} {'Entrance%':<11} {'Maths':<7} {'Physics':<8} {'CS/Chem':<8} {'12th Agg':<9} {'Status'}")
    print("-" * 95)

    # Cutoffs & Minimum Eligibility Standards:
    # 1. Entrance Percentile >= 85.0
    # 2. Maths Marks >= 75.0
    # 3. Physics Marks >= 65.0
    # 4. 12th Aggregate >= 75.0
    eligible_applicants = []

    for app in applicants:
        # Tuple unpacking: app_id, name, entrance_pct, maths_marks, physics_marks, cs_marks, agg_12th
        app_id, name, entrance_pct, maths, physics, cs_chem, agg = app

        is_eligible = True
        rejections = []

        if entrance_pct < 85.0:
            is_eligible = False
            rejections.append("Low Entrance")
        if maths < 75.0:
            is_eligible = False
            rejections.append("Low Maths")
        if physics < 65.0:
            is_eligible = False
            rejections.append("Low Physics")
        if agg < 75.0:
            is_eligible = False
            rejections.append("Low 12th Agg")

        if is_eligible:
            status = "ELIGIBLE"
            eligible_applicants.append([app_id, name, entrance_pct, maths, physics, cs_chem, agg])
        else:
            status = "NOT ELIGIBLE (" + ", ".join(rejections) + ")"

        print(f"{app_id:<7} {name:<16} {entrance_pct:<11.2f} {maths:<7.1f} {physics:<8.1f} {cs_chem:<8.1f} {agg:<9.1f} {status}")

    # Sorting & Tie-Breaking Algorithm (Bubble Sort implementation using syllabus concepts)
    # Tie-Breaking Priority:
    # 1. Entrance Percentile (Highest first)
    # 2. Maths Marks (Highest first)
    # 3. Physics Marks (Highest first)
    # 4. 12th Aggregate (Highest first)
    n = len(eligible_applicants)
    for i in range(n):
        for j in range(0, n - i - 1):
            a1 = eligible_applicants[j]
            a2 = eligible_applicants[j + 1]

            swap = False
            # Criteria 1: Entrance percentile
            if a1[2] < a2[2]:
                swap = True
            elif a1[2] == a2[2]:
                # Criteria 2: Maths
                if a1[3] < a2[3]:
                    swap = True
                elif a1[3] == a2[3]:
                    # Criteria 3: Physics
                    if a1[4] < a2[4]:
                        swap = True
                    elif a1[4] == a2[4]:
                        # Criteria 4: 12th Aggregate
                        if a1[6] < a2[6]:
                            swap = True

            if swap:
                eligible_applicants[j], eligible_applicants[j + 1] = eligible_applicants[j + 1], eligible_applicants[j]

    print("\n" + "=" * 95)
    print("                     FINAL MERIT ALLOTMENT & WAITING LIST")
    print("=" * 95)
    print(f"{'Merit':<6} {'AppID':<7} {'Name':<16} {'Entrance%':<11} {'Maths':<7} {'Physics':<8} {'12th Agg':<9} {'Allotment Result'}")
    print("-" * 95)

    allocated_count = 0
    waiting_count = 0

    for idx in range(len(eligible_applicants)):
        merit_rank = idx + 1
        cand = eligible_applicants[idx]
        c_id, c_name, c_ent, c_m, c_p, c_cs, c_agg = cand

        if merit_rank <= intake_seats:
            result = f"CONFIRMED SEAT (Seat #{merit_rank})"
            allocated_count += 1
        else:
            wl_number = merit_rank - intake_seats
            result = f"WAITLISTED (WL-{wl_number})"
            waiting_count += 1

        print(f"{merit_rank:<6} {c_id:<7} {c_name:<16} {c_ent:<11.2f} {c_m:<7.1f} {c_p:<8.1f} {c_agg:<9.1f} {result}")

    print("-" * 95)
    print(f"Total Applicants Processed : {len(applicants)}")
    print(f"Eligible Applicants Found  : {len(eligible_applicants)}")
    print(f"Confirmed Seats Allocated  : {allocated_count} / {intake_seats}")
    print(f"Candidates on Waitlist     : {waiting_count}")
    print("=" * 95)


if __name__ == "__main__":
    seats = 4
    # Dataset: (AppID, Name, EntrancePercentile, Maths, Physics, CS/Chem, 12thAggregate)
    applicant_pool = [
        ("ADM101", "Kavya Sree",       98.45, 96.0, 92.0, 95.0, 94.2),
        ("ADM102", "Rohan Mehta",      94.10, 88.0, 78.0, 82.0, 86.5),
        ("ADM103", "Ananya Sharma",    96.50, 91.0, 85.0, 90.0, 92.0),
        ("ADM104", "Girish Varma",     96.50, 94.0, 81.0, 88.0, 90.5), # Tie with ADM103 on Entrance, higher Maths
        ("ADM105", "Tanvi Joshi",      82.00, 90.0, 80.0, 85.0, 88.0), # Rejected: Entrance < 85
        ("ADM106", "Siddharth Rao",    91.20, 72.0, 80.0, 84.0, 81.0), # Rejected: Maths < 75
        ("ADM107", "Meera Nambiar",    95.20, 89.0, 84.0, 87.0, 89.4),
        ("ADM108", "Pranav Chandra",   94.10, 88.0, 82.0, 80.0, 88.0), # Tie with ADM102 on Entrance & Maths, higher Physics
        ("ADM109", "Zoya Khan",        89.75, 82.0, 60.0, 78.0, 79.5), # Rejected: Physics < 65
    ]

    process_university_admissions("B.Tech Computer Science & Engineering", seats, applicant_pool)
