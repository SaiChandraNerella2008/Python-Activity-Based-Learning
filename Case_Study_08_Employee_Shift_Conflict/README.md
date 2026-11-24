# Case Study 08: Tuple-Based Employee Shift Conflict Detection (Problem 48)

> **Course**: Python Programming - Activity-Based Learning (ABL) Assignment  
> **Institution**: Dr. RVR NRI Institute of Technology (Deemed to be University)  
> **Student Name**: Sai Chandra Nerella | **Roll No**: 24NR1A0506 | **Branch**: CSE (I B.Tech)

---

## 📋 1. Problem Statement
Represent employee hospital shifts as immutable tuples, parse 24-hour time strings into total minutes, perform pairwise comparison to detect overlapping shift assignments on the same day, check for mandatory 8-hour rest period violations, and generate an operational conflict audit.

---

## 🎯 2. Objectives
1. Store shift rosters using immutable tuples.
2. Convert 24-hour time strings into integer minutes for precise comparison.
3. Detect interval overlaps: max(start1, start2) < min(end1, end2) for identical employees on same day.
4. Detect rest period violations (gap < 8 hours between consecutive shifts).
5. Generate conflict logs with exact clash periods.

---

## ⚙️ 3. Assumptions & Constraints
1. Shift times are supplied in valid 'HH:MM' 24-hour format.
2. Shifts are compared only when assigned to the same employee ID on the same day of the week.

---

## 🧠 4. Step-by-Step Algorithm
1. Define parse_time(time_str) -> hours*60 + mins.
2. Print roster table with duration in hours.
3. Pairwise nested loop i from 0..n, j from i+1..n.
4. If emp1 == emp2 and day1 == day2: compute start/end minutes. If max(start1, start2) < min(end1, end2): record DIRECT OVERLAP. If 0 <= start2 - end1 < 480: record REST VIOLATION.
5. Output audit summary and flagged staff.

---

## 📝 5. Pseudocode
`	ext
FUNCTION detect_conflicts(roster):
    FOR i FROM 0 TO len(roster)-1:
        FOR j FROM i+1 TO len(roster):
            IF emp[i] == emp[j] AND day[i] == day[j] THEN
                IF max(start_i, start_j) < min(end_i, end_j) THEN
                    FLAG_OVERLAP(shift[i], shift[j])
                ELSE IF 0 <= (start_j - end_i) < 480 THEN
                    FLAG_REST_VIOLATION(shift[i], shift[j])
    PRINT conflict audit report
END FUNCTION
`

---

## 📊 6. System Flowchart Diagram
`	ext
[START]
   │
   ▼
[Read Shift Roster Tuples: (ShiftID, EmpID, Name, Dept, Day, Start, End)]
   │
   ▼
[Convert 'HH:MM' Times to Total Minutes from Midnight]
   │
   ▼
[Pairwise Nested Loops: Compare Shift i and Shift j]
   │
   <Is Same Employee AND Same Day?>
     ├── NO ──► Continue
     └── YES
           │
           ├── Overlap: max(Start_i, Start_j) < min(End_i, End_j)?
           │     └── YES ──► [Log DIRECT CLASH with Overlap Minutes]
           │
           └── Insufficient Rest: Gap < 8 Hours (480 mins)?
                 └── YES ──► [Log MANDATORY REST VIOLATION]
           │
           ▼
[Print Audit Summary and Action Recommendations]
   │
   ▼
 [END]
`

---

## 💻 7. Python Source Code
`python
"""
Case Study 8 (Problem 48): Tuple-Based Employee Shift Conflict Detection
Syllabus Concepts: Computational thinking, variables, data types, operators,
                   conditional statements, loops, lists, tuples, tuple operations,
                   tuple unpacking.

Problem Statement:
Represent employee work shifts as immutable tuples, parse and compare start and
end time intervals, detect overlapping shift assignments (double-booking or
mandatory rest period violations), and generate an operational conflict audit.
"""

def parse_time_to_minutes(time_str):
    """Converts 'HH:MM' 24-hour time format string into total minutes from midnight."""
    parts = time_str.split(":")
    hours = int(parts[0])
    minutes = int(parts[1])
    return hours * 60 + minutes


def minutes_to_time_str(total_minutes):
    """Converts total minutes back into formatted 'HH:MM' string."""
    hours = total_minutes // 60
    mins = total_minutes % 60
    return f"{hours:02d}:{mins:02d}"


def detect_shift_conflicts(shift_roster):
    print("=" * 95)
    print("          HOSPITAL / INDUSTRY EMPLOYEE SHIFT CONFLICT & OVERLAP AUDITOR")
    print("=" * 95)
    print(f"{'ShiftID':<9} {'EmpID':<8} {'Employee Name':<18} {'Role/Dept':<14} {'Day':<10} {'Start':<7} {'End':<7} {'Duration'}")
    print("-" * 95)

    # 1. Print current roster schedule
    for shift in shift_roster:
        # Tuple unpacking: shift_id, emp_id, emp_name, dept, day, start_time, end_time
        s_id, e_id, name, dept, day, start, end = shift

        start_min = parse_time_to_minutes(start)
        end_min = parse_time_to_minutes(end)
        duration_hrs = (end_min - start_min) / 60.0

        print(f"{s_id:<9} {e_id:<8} {name:<18} {dept:<14} {day:<10} {start:<7} {end:<7} {duration_hrs:.1f} hrs")

    print("-" * 95)
    print("                         DETECTED SCHEDULE CONFLICTS")
    print("-" * 95)

    conflict_count = 0
    flagged_employees = []

    # 2. Pairwise comparison using nested loops to detect overlapping intervals for the SAME employee on the SAME day
    n = len(shift_roster)
    for i in range(n):
        for j in range(i + 1, n):
            shift1 = shift_roster[i]
            shift2 = shift_roster[j]

            # Unpack tuples
            s1_id, e1_id, name1, dept1, day1, start1, end1 = shift1
            s2_id, e2_id, name2, dept2, day2, start2, end2 = shift2

            # Check if same employee and same day
            if e1_id == e2_id and day1 == day2:
                s1_start = parse_time_to_minutes(start1)
                s1_end = parse_time_to_minutes(end1)

                s2_start = parse_time_to_minutes(start2)
                s2_end = parse_time_to_minutes(end2)

                # Overlap condition:
                # Two intervals [A_start, A_end] and [B_start, B_end] overlap if:
                # max(A_start, B_start) < min(A_end, B_end)
                overlap_start = max(s1_start, s2_start)
                overlap_end = min(s1_end, s2_end)

                if overlap_start < overlap_end:
                    conflict_count += 1
                    overlap_duration = overlap_end - overlap_start
                    print(f"[!] DIRECT OVERLAP DETECTED for {name1} ({e1_id}) on {day1}:")
                    print(f"    Shift 1: {s1_id} ({start1} - {end1}) in {dept1}")
                    print(f"    Shift 2: {s2_id} ({start2} - {end2}) in {dept2}")
                    print(f"    Overlap Period: {minutes_to_time_str(overlap_start)} to {minutes_to_time_str(overlap_end)} ({overlap_duration} minutes clash)")
                    print()
                    if name1 not in flagged_employees:
                        flagged_employees.append(name1)

                # Rest period violation check: Less than 8 hours (480 mins) between consecutive shifts on same day
                gap = s2_start - s1_end
                if 0 <= gap < 480 and overlap_start >= overlap_end:
                    conflict_count += 1
                    print(f"[!] INSUFFICIENT REST PERIOD (< 8 hrs) for {name1} ({e1_id}) on {day1}:")
                    print(f"    Shift {s1_id} ends at {end1}; Shift {s2_id} starts at {start2} (Gap: {gap / 60:.1f} hrs)")
                    print()
                    if name1 not in flagged_employees:
                        flagged_employees.append(name1)

    print("-" * 95)
    print("                            AUDIT SUMMARY")
    print("-" * 95)
    print(f"Total Scheduled Shifts Analyzed : {len(shift_roster)}")
    print(f"Total Conflict Violations Found : {conflict_count}")
    print(f"Employees Requiring Rescheduling: {len(flagged_employees)} -> {', '.join(flagged_employees) if flagged_employees else 'None'}")
    if conflict_count == 0:
        print("[✓] Perfect roster schedule! Zero overlaps detected.")
    else:
        print("[!] ACTION REQUIRED: Resolve flagged shifts before finalizing the operational roster.")
    print("=" * 95)


if __name__ == "__main__":
    # Shift Tuple: (ShiftID, EmployeeID, EmployeeName, Department, DayOfWeek, StartTime24h, EndTime24h)
    roster = [
        ("SH01", "EMP101", "Dr. Arvind Rao",    "Emergency ICU", "Monday", "08:00", "16:00"),
        ("SH02", "EMP102", "Nurse Priya Nair",  "Pediatrics",    "Monday", "09:00", "17:00"),
        ("SH03", "EMP101", "Dr. Arvind Rao",    "Outpatient OPD","Monday", "14:00", "20:00"),  # Clash with SH01 (14:00 to 16:00)
        ("SH04", "EMP103", "Tech. Sumanth V",   "Radiology",     "Monday", "08:00", "14:00"),
        ("SH05", "EMP103", "Tech. Sumanth V",   "CT Scan Unit",  "Monday", "16:00", "22:00"),  # Rest violation: gap 2 hrs < 8 hrs
        ("SH06", "EMP104", "Dr. Shalini Roy",   "Cardiology",    "Monday", "10:00", "18:00"),
        ("SH07", "EMP102", "Nurse Priya Nair",  "Night Triage",  "Tuesday","20:00", "04:00"),  # Valid next day
    ]

    detect_shift_conflicts(roster)

`

---

## 🖥️ 8. Program Execution Output Log
`	ext
﻿===============================================================================================
          HOSPITAL / INDUSTRY EMPLOYEE SHIFT CONFLICT & OVERLAP AUDITOR
===============================================================================================
ShiftID   EmpID    Employee Name      Role/Dept      Day        Start   End     Duration
-----------------------------------------------------------------------------------------------
SH01      EMP101   Dr. Arvind Rao     Emergency ICU  Monday     08:00   16:00   8.0 hrs
SH02      EMP102   Nurse Priya Nair   Pediatrics     Monday     09:00   17:00   8.0 hrs
SH03      EMP101   Dr. Arvind Rao     Outpatient OPD Monday     14:00   20:00   6.0 hrs
SH04      EMP103   Tech. Sumanth V    Radiology      Monday     08:00   14:00   6.0 hrs
SH05      EMP103   Tech. Sumanth V    CT Scan Unit   Monday     16:00   22:00   6.0 hrs
SH06      EMP104   Dr. Shalini Roy    Cardiology     Monday     10:00   18:00   8.0 hrs
SH07      EMP102   Nurse Priya Nair   Night Triage   Tuesday    20:00   04:00   -16.0 hrs
-----------------------------------------------------------------------------------------------
                         DETECTED SCHEDULE CONFLICTS
-----------------------------------------------------------------------------------------------
[!] DIRECT OVERLAP DETECTED for Dr. Arvind Rao (EMP101) on Monday:
    Shift 1: SH01 (08:00 - 16:00) in Emergency ICU
    Shift 2: SH03 (14:00 - 20:00) in Outpatient OPD
    Overlap Period: 14:00 to 16:00 (120 minutes clash)

[!] INSUFFICIENT REST PERIOD (< 8 hrs) for Tech. Sumanth V (EMP103) on Monday:
    Shift SH04 ends at 14:00; Shift SH05 starts at 16:00 (Gap: 2.0 hrs)

-----------------------------------------------------------------------------------------------
                            AUDIT SUMMARY
-----------------------------------------------------------------------------------------------
Total Scheduled Shifts Analyzed : 7
Total Conflict Violations Found : 2
Employees Requiring Rescheduling: 2 -> Dr. Arvind Rao, Tech. Sumanth V
[!] ACTION REQUIRED: Resolve flagged shifts before finalizing the operational roster.
===============================================================================================
`

---

## 💡 9. Conclusion & Learning Outcome
Leveraged tuple immutability and interval overlap formulas to detect conflicting hospital shifts and insufficient rest breaks, protecting staff welfare and scheduling compliance.
