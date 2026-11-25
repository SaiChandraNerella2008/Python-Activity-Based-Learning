"""
Case Study 10 (Problem 100): Comprehensive Smart Campus Management Simulation
Syllabus Concepts: Computational thinking, variables, data types, operators,
                   conditional statements, loops, strings, pattern generation,
                   lists, nested lists, tuples, tuple operations, and tuple unpacking.

Problem Statement:
Develop a modular, menu-driven program that integrates student records, attendance
monitoring, academic grades, campus event registrations, lab resource allocations,
and statistical administrative reporting using all core syllabus constructs.
"""

def run_smart_campus_simulation():
    # 1. Core Data Structures:
    # Students List of Tuples: (RollNo, Name, Branch, Year, AttendancePct, CGPA)
    students = [
        ("24NR1A0501", "Aarav Sharma",    "CSE", 1, 88.5, 9.2),
        ("24NR1A0502", "Bhavya Reddy",    "CSE", 1, 72.0, 7.8),
        ("24NR1A0503", "Chaitanya Roy",   "ECE", 1, 94.0, 9.6),
        ("24NR1A0504", "Divya Patel",     "CSE", 1, 81.0, 8.4),
        ("24NR1A0505", "Eshwar Naik",     "IT",  1, 64.5, 6.9),
        ("26000654", "Sai Chandra N",   "CSE", 1, 96.0, 9.8),
    ]

    # Campus Events: List of Tuples: (EventCode, EventName, Capacity, RegisteredCount)
    events = [
        ("EV01", "AI Hackathon 2026", 50, 48),
        ("EV02", "Web Dev Bootcamp",   40, 32),
        ("EV03", "Robotics Expo",      30, 30),
    ]

    # Lab Computing Resources: Nested List (LabName, TotalPCs, OccupiedPCs)
    lab_resources = [
        ["Turing Lab (CSE)", 60, 45],
        ["Babbage Lab (IT)", 50, 48],
        ["Tesla Lab (ECE)",  40, 22],
    ]

    # Pre-registered event mapping: List of tuples (RollNo, EventCode)
    event_registrations = [
        ("24NR1A0501", "EV01"),
        ("24NR1A0503", "EV01"),
        ("26000654",   "EV01"),
        ("24NR1A0504", "EV02"),
        ("26000654",   "EV02"),
    ]

    print("=" * 85)
    print("      DR. RVR NRI INSTITUTE OF TECHNOLOGY - SMART CAMPUS SIMULATION")
    print("=" * 85)

    menu_options = [
        "1. Display Master Student Directory",
        "2. Attendance Shortage & Condonation Audit (< 75%)",
        "3. Academic Merit Honor Roll (CGPA >= 8.5)",
        "4. Campus Event Registrations & Seat Availability",
        "5. Lab Computing Resource Utilization Audit",
        "6. Execute Student Event Registration",
        "7. Exit Simulation"
    ]

    # Simulated Automated Execution of all operational modules
    for option in menu_options:
        print(f"  {option}")
    print("-" * 85)

    # MODULE 1: Student Directory
    print("\n>>> [MODULE 1] MASTER STUDENT DIRECTORY")
    print(f"{'Roll No':<14} {'Student Name':<18} {'Branch':<8} {'Year':<6} {'Attnd(%)':<10} {'CGPA'}")
    print("-" * 70)
    for st in students:
        roll, name, branch, yr, att, cgpa = st
        print(f"{roll:<14} {name:<18} {branch:<8} {yr:<6} {att:<10.1f} {cgpa:<5.2f}")

    # MODULE 2: Attendance Shortage Audit
    print("\n>>> [MODULE 2] ATTENDANCE DETENTION & CONDONATION AUDIT (< 75.0%)")
    print(f"{'Roll No':<14} {'Student Name':<18} {'Attendance':<12} {'Academic Action'}")
    print("-" * 70)
    shortage_count = 0
    for st in students:
        roll, name, branch, yr, att, cgpa = st
        if att < 75.0:
            shortage_count += 1
            if att >= 65.0:
                action = "Condonation Fee Applicable (Eligible on Medical Grounds)"
            else:
                action = "DETENTION WARNING (Severe Shortage)"
            print(f"{roll:<14} {name:<18} {att:<12.1f}% {action}")
    if shortage_count == 0:
        print("  [✓] Zero students with attendance shortage.")

    # MODULE 3: Academic Merit Honor Roll
    print("\n>>> [MODULE 3] DEAN'S MERIT HONOR ROLL (CGPA >= 8.50)")
    print(f"{'Roll No':<14} {'Student Name':<18} {'CGPA':<8} {'Standing'}")
    print("-" * 70)
    for st in students:
        roll, name, branch, yr, att, cgpa = st
        if cgpa >= 9.5:
            standing = "Gold Scholar (Top 1%)"
            print(f"{roll:<14} {name:<18} {cgpa:<8.2f} {standing}")
        elif cgpa >= 8.5:
            standing = "Distinction Scholar"
            print(f"{roll:<14} {name:<18} {cgpa:<8.2f} {standing}")

    # MODULE 4: Event Availability Audit
    print("\n>>> [MODULE 4] CAMPUS EVENT CAPACITY STATUS")
    print(f"{'Code':<8} {'Event Title':<26} {'Capacity':<10} {'Filled':<8} {'Vacant Seats':<14} {'Booking Status'}")
    print("-" * 80)
    for ev in events:
        e_code, e_name, cap, reg = ev
        vacant = cap - reg
        status = "HOUSEFULL" if vacant == 0 else f"{vacant} Seats Left"
        print(f"{e_code:<8} {e_name:<26} {cap:<10} {reg:<8} {vacant:<14} {status}")

    # MODULE 5: Lab Infrastructure Utilization
    print("\n>>> [MODULE 5] LAB COMPUTING INFRASTRUCTURE AUDIT")
    print(f"{'Lab Name':<24} {'Total PCs':<12} {'In-Use':<10} {'Available':<12} {'Utilization(%)'}")
    print("-" * 75)
    for lab in lab_resources:
        l_name, total_pcs, in_use = lab
        avail = total_pcs - in_use
        util_pct = (in_use / total_pcs) * 100.0
        print(f"{l_name:<24} {total_pcs:<12} {in_use:<10} {avail:<12} {util_pct:.1f}%")

    # MODULE 6: Process Event Registration Simulation
    print("\n>>> [MODULE 6] REAL-TIME REGISTRATION TRANSACTION TEST")
    target_roll = "24NR1A0502"  # Bhavya Reddy
    target_event = "EV02"       # Web Dev Bootcamp

    # Check if student exists
    student_found = False
    for st in students:
        if st[0] == target_roll:
            student_found = True
            break

    # Check if already registered
    already_registered = False
    for reg in event_registrations:
        if reg[0] == target_roll and reg[1] == target_event:
            already_registered = True
            break

    if already_registered:
        print(f"  [!] Registration Failed: Student {target_roll} is already registered for {target_event}.")
    else:
        # Update count in events
        for idx in range(len(events)):
            e_code, e_name, cap, reg_count = events[idx]
            if e_code == target_event:
                if reg_count < cap:
                    events[idx] = (e_code, e_name, cap, reg_count + 1)
                    event_registrations.append((target_roll, target_event))
                    print(f"  [✓] Registration Confirmed: Student {target_roll} enrolled in '{e_name}' successfully!")
                    print(f"      Updated Seats: {reg_count + 1} / {cap}")
                else:
                    print(f"  [!] Registration Denied: '{e_name}' has reached full capacity.")

    print("\n" + "=" * 85)
    print("         SMART CAMPUS SIMULATION EXECUTION COMPLETED SUCCESSFULLY")
    print("=" * 85)


if __name__ == "__main__":
    run_smart_campus_simulation()
