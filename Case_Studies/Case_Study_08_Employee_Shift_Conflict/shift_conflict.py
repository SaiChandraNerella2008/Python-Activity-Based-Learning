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
