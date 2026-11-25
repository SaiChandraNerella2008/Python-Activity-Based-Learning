# Case Study 10: Comprehensive Smart Campus Management Simulation (Problem 100)

> **Course**: Python Programming - Activity-Based Learning (ABL) Assignment  
> **Institution**: Dr. RVR NRI Institute of Technology (Deemed to be University)  
> **Student Name**: Sai Chandra Nerella | **NRI ID**: 26000654 | **Section**: Section 3 | **Branch**: CSE (I B.Tech)

---

## 📋 1. Problem Statement
Develop an integrated smart campus management simulation combining student directories, attendance shortage detention warnings (<75%), Dean's merit honor roll (CGPA >= 8.5), event registration and capacity management, lab workstation utilization monitoring, and real-time transaction processing.

---

## 🎯 2. Objectives
1. Integrate multiple heterogeneous campus datasets using lists, nested lists, and tuples.
2. Implement student directory, attendance auditing, and merit classification modules.
3. Manage campus event capacity and dynamically enforce booking rules.
4. Audit computing lab hardware utilization percentages.
5. Execute a live event registration transaction with duplicate validation and seat count updates.

---

## ⚙️ 3. Assumptions & Constraints
1. Attendance below 75% requires condonation or triggers detention.
2. CGPA >= 8.5 earns Dean's Honor Roll standing; CGPA >= 9.5 earns Gold Scholar standing.
3. Event registration requires verifying student existence, capacity availability, and preventing duplicate enrollments.

---

## 🧠 4. Step-by-Step Algorithm
1. Define master student tuples, event tuples, and lab resource nested lists.
2. Module 1: Display student directory.
3. Module 2: Audit attendance; flag students < 75% for condonation or detention.
4. Module 3: Filter CGPA >= 8.5 for Gold and Distinction Scholar honor rolls.
5. Module 4: Calculate event vacant seats and flag full events.
6. Module 5: Calculate workstation utilization percentages.
7. Module 6: Simulate transaction: verify student exists, check duplicate registration, update seat count if capacity permits.
8. Print execution summary.

---

## 📝 5. Pseudocode
`	ext
FUNCTION run_smart_campus():
    DISPLAY_STUDENT_DIRECTORY(students)
    AUDIT_ATTENDANCE_SHORTAGES(students)
    GENERATE_HONOR_ROLL(students)
    AUDIT_EVENT_CAPACITY(events)
    AUDIT_LAB_RESOURCES(labs)
    EXECUTE_EVENT_REGISTRATION(student_id, event_code)
END FUNCTION
`

---

## 📊 6. System Flowchart Diagram
`	ext
[START]
   │
   ▼
[Initialize Master Campus Datasets: Students, Events, Labs, Registrations]
   │
   ▼
[Module 1: Display Master Student Directory]
   │
   ▼
[Module 2: Audit Attendance Shortage (<75%) -> Condonation / Detention]
   │
   ▼
[Module 3: Generate Dean's Merit Honor Roll (CGPA >= 8.50)]
   │
   ▼
[Module 4: Check Campus Event Capacities and Vacancies]
   │
   ▼
[Module 5: Calculate Computing Lab Hardware Utilization %]
   │
   ▼
[Module 6: Execute Real-Time Event Registration Transaction with Duplicate Checks]
   │
   ▼
[Display Smart Campus Administrative Execution Summary]
   │
   ▼
 [END]
`

---

## 💻 7. Python Source Code
`python
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
        ("26000654", "EV01"),
        ("24NR1A0504", "EV02"),
        ("26000654", "EV02"),
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

`

---

## 🖥️ 8. Program Execution Output Log
`	ext
﻿=====================================================================================
      DR. RVR NRI INSTITUTE OF TECHNOLOGY - SMART CAMPUS SIMULATION
=====================================================================================
  1. Display Master Student Directory
  2. Attendance Shortage & Condonation Audit (< 75%)
  3. Academic Merit Honor Roll (CGPA >= 8.5)
  4. Campus Event Registrations & Seat Availability
  5. Lab Computing Resource Utilization Audit
  6. Execute Student Event Registration
  7. Exit Simulation
-------------------------------------------------------------------------------------

>>> [MODULE 1] MASTER STUDENT DIRECTORY
Roll No        Student Name       Branch   Year   Attnd(%)   CGPA
----------------------------------------------------------------------
24NR1A0501     Aarav Sharma       CSE      1      88.5       9.20 
24NR1A0502     Bhavya Reddy       CSE      1      72.0       7.80 
24NR1A0503     Chaitanya Roy      ECE      1      94.0       9.60 
24NR1A0504     Divya Patel        CSE      1      81.0       8.40 
24NR1A0505     Eshwar Naik        IT       1      64.5       6.90 
26000654     Sai Chandra N      CSE      1      96.0       9.80 

>>> [MODULE 2] ATTENDANCE DETENTION & CONDONATION AUDIT (< 75.0%)
Roll No        Student Name       Attendance   Academic Action
----------------------------------------------------------------------
24NR1A0502     Bhavya Reddy       72.0        % Condonation Fee Applicable (Eligible on Medical Grounds)
24NR1A0505     Eshwar Naik        64.5        % DETENTION WARNING (Severe Shortage)

>>> [MODULE 3] DEAN'S MERIT HONOR ROLL (CGPA >= 8.50)
Roll No        Student Name       CGPA     Standing
----------------------------------------------------------------------
24NR1A0501     Aarav Sharma       9.20     Distinction Scholar
24NR1A0503     Chaitanya Roy      9.60     Gold Scholar (Top 1%)
26000654     Sai Chandra N      9.80     Gold Scholar (Top 1%)

>>> [MODULE 4] CAMPUS EVENT CAPACITY STATUS
Code     Event Title                Capacity   Filled   Vacant Seats   Booking Status
--------------------------------------------------------------------------------
EV01     AI Hackathon 2026          50         48       2              2 Seats Left
EV02     Web Dev Bootcamp           40         32       8              8 Seats Left
EV03     Robotics Expo              30         30       0              HOUSEFULL

>>> [MODULE 5] LAB COMPUTING INFRASTRUCTURE AUDIT
Lab Name                 Total PCs    In-Use     Available    Utilization(%)
---------------------------------------------------------------------------
Turing Lab (CSE)         60           45         15           75.0%
Babbage Lab (IT)         50           48         2            96.0%
Tesla Lab (ECE)          40           22         18           55.0%

>>> [MODULE 6] REAL-TIME REGISTRATION TRANSACTION TEST
  [✓] Registration Confirmed: Student 24NR1A0502 enrolled in 'Web Dev Bootcamp' successfully!
      Updated Seats: 33 / 40

=====================================================================================
         SMART CAMPUS SIMULATION EXECUTION COMPLETED SUCCESSFULLY
=====================================================================================
`

---

## 💡 9. Conclusion & Learning Outcome
Synthesized all syllabus constructs (loops, conditionals, strings, lists, nested lists, tuples, and tuple unpacking) into a unified smart campus operational system.
