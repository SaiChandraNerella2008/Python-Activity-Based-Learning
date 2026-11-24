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
