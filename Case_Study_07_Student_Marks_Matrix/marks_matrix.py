"""
Case Study 7 (Problem 42): Student Marks Matrix Analysis
Syllabus Concepts: Computational thinking, variables, data types, operators,
                   conditional statements, nested loops, nested lists (2D arrays),
                   tuples, string formatting.

Problem Statement:
Analyse a matrix of student marks across core academic subjects, calculate
row-wise student totals and averages, compute column-wise subject averages and
standard performance metrics, identify top performers, and detect difficult
subjects requiring academic intervention.
"""

def analyze_marks_matrix(student_names, subject_names, marks_matrix):
    print("=" * 90)
    print("             ACADEMIC PERFORMANCE MATRIX & BATCH STATISTICAL AUDIT")
    print("=" * 90)

    num_students = len(student_names)
    num_subjects = len(subject_names)

    # 1. Print Matrix Table with Subject Headers
    header = f"{'Roll/Name':<18}"
    for sub in subject_names:
        header += f"{sub:<10}"
    header += f"{'Total':<8} {'Average':<9} {'Grade':<6} {'Status'}"
    print(header)
    print("-" * 90)

    student_stats = []
    # Row-wise Analysis (Student Performance)
    for i in range(num_students):
        name = student_names[i]
        scores = marks_matrix[i]

        row_total = 0.0
        has_failed_subject = False

        for mark in scores:
            row_total += mark
            if mark < 40.0:  # Minimum passing cutoff per subject
                has_failed_subject = True

        row_avg = row_total / num_subjects

        # Grade Assignment
        if row_avg >= 90.0 and not has_failed_subject:
            grade = "A+"
        elif row_avg >= 80.0 and not has_failed_subject:
            grade = "A"
        elif row_avg >= 70.0 and not has_failed_subject:
            grade = "B"
        elif row_avg >= 60.0 and not has_failed_subject:
            grade = "C"
        elif row_avg >= 40.0 and not has_failed_subject:
            grade = "D"
        else:
            grade = "F"

        status = "PASSED" if not has_failed_subject else "BACKLOG"
        student_stats.append((name, scores, row_total, row_avg, grade, status))

        row_line = f"{name:<18}"
        for mark in scores:
            row_line += f"{mark:<10.1f}"
        row_line += f"{row_total:<8.1f} {row_avg:<9.2f} {grade:<6} {status}"
        print(row_line)

    print("-" * 90)

    # 2. Column-wise Analysis (Subject Performance across all students)
    subject_totals = [0.0] * num_subjects
    subject_highest = [0.0] * num_subjects
    subject_lowest = [100.0] * num_subjects
    subject_failures = [0] * num_subjects

    for j in range(num_subjects):
        for i in range(num_students):
            score = marks_matrix[i][j]
            subject_totals[j] += score
            if score > subject_highest[j]:
                subject_highest[j] = score
            if score < subject_lowest[j]:
                subject_lowest[j] = score
            if score < 40.0:
                subject_failures[j] += 1

    subject_averages = [tot / num_students for tot in subject_totals]

    # Print Summary Row for Averages
    avg_line = f"{'Subject Average':<18}"
    for avg in subject_averages:
        avg_line += f"{avg:<10.2f}"
    print(avg_line)

    highest_line = f"{'Highest Mark':<18}"
    for hi in subject_highest:
        highest_line += f"{hi:<10.1f}"
    print(highest_line)

    lowest_line = f"{'Lowest Mark':<18}"
    for lo in subject_lowest:
        lowest_line += f"{lo:<10.1f}"
    print(lowest_line)

    print("=" * 90)
    print("                        EXECUTIVE INSIGHTS & RANKINGS")
    print("=" * 90)

    # Find Top Performer (Highest Average without backlogs)
    top_student = ""
    top_avg = -1.0
    for st in student_stats:
        if st[5] == "PASSED" and st[3] > top_avg:
            top_avg = st[3]
            top_student = st[0]

    print(f"★ Batch Topper: {top_student} with an aggregate average of {top_avg:.2f}%")

    # Detect lowest performing subject
    min_sub_avg = 101.0
    tough_subject_index = -1
    for j in range(num_subjects):
        if subject_averages[j] < min_sub_avg:
            min_sub_avg = subject_averages[j]
            tough_subject_index = j

    tough_subject = subject_names[tough_subject_index]
    fail_count = subject_failures[tough_subject_index]
    print(f"[!] Critical Subject Detected: {tough_subject} has the lowest average ({min_sub_avg:.2f}%) with {fail_count} failing student(s).")
    print(f"    Recommendation: Remedial classes and tutorial sessions advised for {tough_subject}.")
    print("=" * 90)


if __name__ == "__main__":
    subjects = ["Maths", "Physics", "Python", "DataStruct", "DigitalLogic"]

    students = [
        "Aarav Sharma",
        "Bhavya Reddy",
        "Chaitanya Roy",
        "Divya Patel",
        "Eshwar Naik",
        "Fatima Zahra",
        "Gautam Verma"
    ]

    # 7x5 Nested List (Matrix) of Marks
    matrix = [
        [92.0, 85.0, 96.0, 90.0, 88.0],  # Aarav
        [78.0, 68.0, 82.0, 74.0, 70.0],  # Bhavya
        [95.0, 91.0, 98.0, 94.0, 92.0],  # Chaitanya (Topper)
        [64.0, 58.0, 72.0, 65.0, 60.0],  # Divya
        [88.0, 72.0, 85.0, 36.0, 68.0],  # Eshwar (Fail in DataStruct)
        [90.0, 82.0, 94.0, 89.0, 86.0],  # Fatima
        [52.0, 48.0, 60.0, 42.0, 55.0],  # Gautam
    ]

    analyze_marks_matrix(students, subjects, matrix)
