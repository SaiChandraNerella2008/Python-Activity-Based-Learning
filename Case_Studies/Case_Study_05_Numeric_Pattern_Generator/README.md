# Case Study 05: Advanced Numeric Pattern Generator (Problem 27)

> **Course**: Python Programming - Activity-Based Learning (ABL) Assignment  
> **Institution**: Dr. RVR NRI Institute of Technology (Deemed to be University)  
> **Student Name**: Sai Chandra Nerella | **NRI ID**: 26000654 | **Section**: Section 3 | **Branch**: CSE (I B.Tech)

---

## 📋 1. Problem Statement
Generate symmetric numerical pyramids, hollow numeric diamonds, and right-angled number grids based on user-specified dimensions with validation for invalid or out-of-range dimensions.

---

## 🎯 2. Objectives
1. Construct palindromic numerical pyramid patterns with leading whitespace alignment.
2. Generate hollow numeric diamonds with boundary numbering and odd-dimension validation.
3. Implement Floyd's sequential number grid with formatted column widths.
4. Validate boundary conditions (even dimensions for diamonds, out-of-range bounds).

---

## ⚙️ 3. Assumptions & Constraints
1. Pyramid heights must be between 1 and 9 for single-digit symmetry.
2. Diamond dimensions must be positive odd integers >= 3.
3. All patterns generated purely using loops and string concatenation.

---

## 🧠 4. Step-by-Step Algorithm
1. Palindromic Pyramid: outer loop i from 1 to n. Inner loops for leading spaces (n-i)*2, ascending 1..i, descending (i-1)..1.
2. Hollow Diamond: validate n is odd. Top half (mid+1 rows): print spaces, value, inner spaces, value. Bottom half (mid rows): reverse sequence.
3. Sequential Triangle: outer loop 1..rows, inner loop 1..i printing running counter with 4-width padding.
4. Test with valid inputs and assert rejection on invalid even inputs.

---

## 📝 5. Pseudocode
`	ext
FUNCTION generate_pyramid(n):
    FOR i FROM 1 TO n:
        PRINT spaces(2*(n-i)) + ASCENDING(1..i) + DESCENDING((i-1)..1)
FUNCTION generate_hollow_diamond(n):
    IF n % 2 == 0 THEN RETURN Error
    mid = n // 2
    FOR i FROM 0 TO mid: PRINT_HOLLOW_LINE(i, mid)
    FOR i FROM mid-1 DOWNTO 0: PRINT_HOLLOW_LINE(i, mid)
END FUNCTION
`

---

## 📊 6. System Flowchart Diagram
`	ext
[START]
   │
   ▼
[Select Pattern: Pyramid / Hollow Diamond / Triangle]
   │
   ▼
<Validate Dimension Limits (e.g. Diamond must be Odd, Pyramid 1-9)?>
   ├── INVALID ──► [Display Error Message & Abort]
   └── VALID
         │
         ├── [Pattern A: Outer Loop Rows, Inner Ascending + Descending Digits]
         ├── [Pattern B: Compute Midpoint, Render Top Half + Mirrored Bottom Half]
         └── [Pattern C: Running Counter with Formatted Tabular Spacing]
         │
         ▼
[Print Symmetric Formatted Grid Output]
   │
   ▼
 [END]
`

---

## 💻 7. Python Source Code
`python
"""
Case Study 5 (Problem 27): Advanced Numeric Pattern Generator
Syllabus Concepts: Computational thinking, variables, data types, operators,
                   conditional statements, nested loops, pattern generation, strings.

Problem Statement:
Produce symmetric numerical pyramids, hollow numeric diamonds, and inverted
number triangles based on user-specified dimensions with robust validation for
invalid input sizes, ensuring precise tabular alignment.
"""

def generate_symmetric_number_pyramid(n):
    """Generates a centered symmetric pyramid of numbers."""
    print(f"\n--- [Pattern A] Symmetric Palindromic Number Pyramid (Height: {n}) ---")
    if n <= 0 or n > 9:
        print("Error: Dimension must be an integer between 1 and 9 for single-digit alignment.")
        return

    for i in range(1, n + 1):
        # Leading spaces for centering
        line = " " * (2 * (n - i))
        # Ascending numbers
        for j in range(1, i + 1):
            line += str(j) + " "
        # Descending numbers
        for j in range(i - 1, 0, -1):
            line += str(j) + " "
        print(line)


def generate_hollow_numeric_diamond(n):
    """
    Generates a hollow diamond pattern displaying boundary numbers.
    n must be an odd positive integer for perfect symmetry.
    """
    print(f"\n--- [Pattern B] Advanced Hollow Numeric Diamond (Dimension: {n}) ---")
    if n % 2 == 0 or n < 3:
        print("Error: Dimension must be an odd integer >= 3 to generate a symmetric diamond.")
        return

    mid = n // 2

    # Top half (including middle line)
    for i in range(mid + 1):
        leading_spaces = " " * (mid - i) * 2
        if i == 0:
            print(leading_spaces + "1")
        else:
            inner_spaces = " " * (2 * i - 1) * 2
            val = str(i + 1)
            print(leading_spaces + val + inner_spaces + " " + val)

    # Bottom half
    for i in range(mid - 1, -1, -1):
        leading_spaces = " " * (mid - i) * 2
        if i == 0:
            print(leading_spaces + "1")
        else:
            inner_spaces = " " * (2 * i - 1) * 2
            val = str(i + 1)
            print(leading_spaces + val + inner_spaces + " " + val)


def generate_floyds_custom_triangle(rows):
    """Generates continuous numbered right-angled triangle with column alignment."""
    print(f"\n--- [Pattern C] Formatted Right-Angled Number Grid (Rows: {rows}) ---")
    if rows <= 0 or rows > 15:
        print("Error: Rows must be between 1 and 15.")
        return

    current = 1
    for i in range(1, rows + 1):
        row_str = ""
        for _ in range(i):
            row_str += f"{current:4d}"
            current += 1
        print(row_str)


def run_pattern_suite():
    print("=" * 65)
    print("       ADVANCED MATHEMATICAL NUMERIC PATTERN GENERATION SUITE")
    print("=" * 65)

    # Test Case 1: Valid Palindromic Pyramid (Height 5)
    generate_symmetric_number_pyramid(5)

    # Test Case 2: Hollow Diamond (Dimension 7 - valid odd)
    generate_hollow_numeric_diamond(7)

    # Test Case 3: Continuous Sequential Triangle (Rows 6)
    generate_floyds_custom_triangle(6)

    # Test Case 4: Invalid input handling validation
    print("\n--- [Validation Tests for Boundary & Invalid Inputs] ---")
    generate_hollow_numeric_diamond(6)  # Even dimension rejection
    generate_symmetric_number_pyramid(12)  # Out of range rejection
    print("=" * 65)


if __name__ == "__main__":
    run_pattern_suite()

`

---

## 🖥️ 8. Program Execution Output Log
`	ext
﻿=================================================================
       ADVANCED MATHEMATICAL NUMERIC PATTERN GENERATION SUITE
=================================================================

--- [Pattern A] Symmetric Palindromic Number Pyramid (Height: 5) ---
        1 
      1 2 1 
    1 2 3 2 1 
  1 2 3 4 3 2 1 
1 2 3 4 5 4 3 2 1 

--- [Pattern B] Advanced Hollow Numeric Diamond (Dimension: 7) ---
      1
    2   2
  3       3
4           4
  3       3
    2   2
      1

--- [Pattern C] Formatted Right-Angled Number Grid (Rows: 6) ---
   1
   2   3
   4   5   6
   7   8   9  10
  11  12  13  14  15
  16  17  18  19  20  21

--- [Validation Tests for Boundary & Invalid Inputs] ---

--- [Pattern B] Advanced Hollow Numeric Diamond (Dimension: 6) ---
Error: Dimension must be an odd integer >= 3 to generate a symmetric diamond.

--- [Pattern A] Symmetric Palindromic Number Pyramid (Height: 12) ---
Error: Dimension must be an integer between 1 and 9 for single-digit alignment.
=================================================================
`

---

## 💡 9. Conclusion & Learning Outcome
Demonstrated nested loop control and mathematical character alignment. Input boundary checks prevented malformed or asymmetric pattern outputs.
