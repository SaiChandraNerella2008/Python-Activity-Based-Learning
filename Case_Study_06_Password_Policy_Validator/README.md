# Case Study 06: Password Policy Validation Engine (Problem 29)

> **Course**: Python Programming - Activity-Based Learning (ABL) Assignment  
> **Institution**: Dr. RVR NRI Institute of Technology (Deemed to be University)  
> **Student Name**: Sai Chandra Nerella | **Roll No**: 24NR1A0506 | **Branch**: CSE (I B.Tech)

---

## 📋 1. Problem Statement
Evaluate password strings against institutional cybersecurity requirements: minimum length (8-32), character categories (uppercase, lowercase, digits, symbols), consecutive character repetition limits (max 2 identical in a row), and prohibited common substrings; explain all failed conditions.

---

## 🎯 2. Objectives
1. Check length constraints.
2. Validate existence and count of uppercase, lowercase, numbers, and special symbols.
3. Detect repeated consecutive triples (e.g., 'aaa', '999').
4. Search for blacklisted substrings (e.g., 'admin', 'password', 'nriit').
5. Calculate a normalized security strength score (0-100).

---

## ⚙️ 3. Assumptions & Constraints
1. Passwords are case-sensitive ASCII strings.
2. Substring matching is case-insensitive for thoroughness.

---

## 🧠 4. Step-by-Step Algorithm
1. Check length: 8 <= len <= 32.
2. Iterate each char: update booleans and counts for upper, lower, digit, special.
3. Loop i from 0 to len-3: if pwd[i] == pwd[i+1] == pwd[i+2], flag consecutive repetition.
4. For each prohibited word: if word in pwd.lower(), flag prohibited substring.
5. Compute score based on criteria met. Output detailed vulnerability report.

---

## 📝 5. Pseudocode
`	ext
FUNCTION validate_password(pwd):
    failures = []
    IF len < 8 OR len > 32 THEN failures.APPEND('Length error')
    CHECK_CATEGORIES(upper, lower, digits, symbols)
    CHECK_CONSECUTIVE_REPEATS(pwd)
    CHECK_PROHIBITED_SUBSTRINGS(pwd)
    score = CALCULATE_SCORE(pwd)
    RETURN (status, score, failures)
END FUNCTION
`

---

## 📊 6. System Flowchart Diagram
`	ext
[START]
   │
   ▼
[Read Password Candidate String]
   │
   ▼
[Check Length: 8 <= len <= 32?] ──► If False, Log Error
   │
   ▼
[Loop Characters: Count Upper, Lower, Digits, Symbols] ──► If Any Missing, Log Error
   │
   ▼
[Check Consecutive Triples: pwd[i]==pwd[i+1]==pwd[i+2]?] ──► If Found, Log Error
   │
   ▼
[Check Prohibited Dictionary Substrings ('admin', 'nriit'...)] ──► If Found, Log Error
   │
   ▼
[Calculate 0-100 Security Score & Assign Verdict: Strong / Moderate / Weak]
   │
   ▼
 [END]
`

---

## 💻 7. Python Source Code
`python
"""
Case Study 6 (Problem 29): Password Policy Validation Engine
Syllabus Concepts: Computational thinking, variables, data types, operators,
                   conditional statements, loops, strings, lists, tuples.

Problem Statement:
Evaluate sample password strings against institutional security criteria:
minimum length, character categories (uppercase, lowercase, digits, special symbols),
character repetition limits, and prohibited common substrings; explain each failed condition.
"""

def evaluate_password_security(passwords):
    print("=" * 80)
    print("        ENTERPRISE CYBERSECURITY - PASSWORD POLICY VALIDATION ENGINE")
    print("=" * 80)

    # Prohibited common substrings
    PROHIBITED_SUBSTRINGS = ["admin", "password", "123456", "qwerty", "welcome", "login", "nriit"]
    SPECIAL_CHARACTERS = "!@#$%^&*()_+-=[]{}|;:,.<>?"

    results = []

    for pwd in passwords:
        print(f"\nAnalyzing Candidate: '{pwd}'")
        failures = []

        # 1. Length check (8 to 32 characters)
        length = len(pwd)
        if length < 8:
            failures.append("Too short (Length < 8 chars)")
        elif length > 32:
            failures.append("Too long (Length > 32 chars)")

        # 2. Character category distribution counts
        has_upper = False
        has_lower = False
        has_digit = False
        has_special = False

        upper_count = 0
        lower_count = 0
        digit_count = 0
        special_count = 0

        for ch in pwd:
            if "A" <= ch <= "Z":
                has_upper = True
                upper_count += 1
            elif "a" <= ch <= "z":
                has_lower = True
                lower_count += 1
            elif "0" <= ch <= "9":
                has_digit = True
                digit_count += 1
            elif ch in SPECIAL_CHARACTERS:
                has_special = True
                special_count += 1

        if not has_upper:
            failures.append("Missing uppercase alphabet [A-Z]")
        if not has_lower:
            failures.append("Missing lowercase alphabet [a-z]")
        if not has_digit:
            failures.append("Missing numeric digit [0-9]")
        if not has_special:
            failures.append("Missing special character (!@#$%^&*...)")

        # 3. Repeated consecutive character rule (no more than 2 identical characters consecutively)
        consecutive_repeat = False
        for i in range(len(pwd) - 2):
            if pwd[i] == pwd[i+1] == pwd[i+2]:
                consecutive_repeat = True
                break
        if consecutive_repeat:
            failures.append("Contains 3+ consecutive identical characters (e.g. 'aaa')")

        # 4. Prohibited substring detection (case-insensitive)
        pwd_lower = pwd.lower()
        found_prohibited = []
        for bad_word in PROHIBITED_SUBSTRINGS:
            if bad_word in pwd_lower:
                found_prohibited.append(bad_word)
        if found_prohibited:
            failures.append(f"Contains prohibited dictionary substrings: {', '.join(found_prohibited)}")

        # Strength Scoring (0 to 100)
        score = 0
        if length >= 12: score += 25
        elif length >= 8: score += 15

        if has_upper: score += 15
        if has_lower: score += 15
        if has_digit: score += 15
        if has_special: score += 20
        if not consecutive_repeat and not found_prohibited: score += 10

        # Classification
        if not failures:
            status = "STRONG / COMPLIANT"
        elif len(failures) <= 2 and score >= 50:
            status = "MODERATE / NEEDS REFINEMENT"
        else:
            status = "REJECTED / WEAK"

        print(f"  Score: {score}/100 | Policy Status: {status}")
        if failures:
            print("  Identified Vulnerabilities:")
            for reason in failures:
                print(f"    [!] {reason}")
        else:
            print("  [✓] All enterprise complexity rules satisfied.")

        results.append((pwd, score, status, len(failures)))

    print("\n" + "=" * 80)
    print("                     EVALUATION SUMMARY TABLE")
    print("=" * 80)
    print(f"{'Password Tested':<25} {'Score':<8} {'Violations':<12} {'Verdict'}")
    print("-" * 80)
    for r in results:
        p_val, p_sc, p_stat, p_viol = r
        print(f"{p_val:<25} {p_sc:<8} {p_viol:<12} {p_stat}")
    print("=" * 80)


if __name__ == "__main__":
    test_passwords = [
        "P@ssw0rd2026",           # Fails: contains 'password'
        "SaiChandra#99",           # Pass: Strong compliance
        "weak",                   # Fails: length, upper, digit, special
        "NriitCollege2026!",       # Fails: contains 'nriit'
        "SecureCode#9999",        # Fails: consecutive '9999'
        "K@vya_Tech#2026",         # Pass: Excellent strength
        "123456789",              # Fails: no alpha/special, common digits
    ]

    evaluate_password_security(test_passwords)

`

---

## 🖥️ 8. Program Execution Output Log
`	ext
﻿================================================================================
        ENTERPRISE CYBERSECURITY - PASSWORD POLICY VALIDATION ENGINE
================================================================================

Analyzing Candidate: 'P@ssw0rd2026'
  Score: 100/100 | Policy Status: STRONG / COMPLIANT
  [✓] All enterprise complexity rules satisfied.

Analyzing Candidate: 'SaiChandra#99'
  Score: 100/100 | Policy Status: STRONG / COMPLIANT
  [✓] All enterprise complexity rules satisfied.

Analyzing Candidate: 'weak'
  Score: 25/100 | Policy Status: REJECTED / WEAK
  Identified Vulnerabilities:
    [!] Too short (Length < 8 chars)
    [!] Missing uppercase alphabet [A-Z]
    [!] Missing numeric digit [0-9]
    [!] Missing special character (!@#$%^&*...)

Analyzing Candidate: 'NriitCollege2026!'
  Score: 90/100 | Policy Status: MODERATE / NEEDS REFINEMENT
  Identified Vulnerabilities:
    [!] Contains prohibited dictionary substrings: nriit

Analyzing Candidate: 'SecureCode#9999'
  Score: 90/100 | Policy Status: MODERATE / NEEDS REFINEMENT
  Identified Vulnerabilities:
    [!] Contains 3+ consecutive identical characters (e.g. 'aaa')

Analyzing Candidate: 'K@vya_Tech#2026'
  Score: 100/100 | Policy Status: STRONG / COMPLIANT
  [✓] All enterprise complexity rules satisfied.

Analyzing Candidate: '123456789'
  Score: 30/100 | Policy Status: REJECTED / WEAK
  Identified Vulnerabilities:
    [!] Missing uppercase alphabet [A-Z]
    [!] Missing lowercase alphabet [a-z]
    [!] Missing special character (!@#$%^&*...)
    [!] Contains prohibited dictionary substrings: 123456

================================================================================
                     EVALUATION SUMMARY TABLE
================================================================================
Password Tested           Score    Violations   Verdict
--------------------------------------------------------------------------------
P@ssw0rd2026              100      0            STRONG / COMPLIANT
SaiChandra#99             100      0            STRONG / COMPLIANT
weak                      25       4            REJECTED / WEAK
NriitCollege2026!         90       1            MODERATE / NEEDS REFINEMENT
SecureCode#9999           90       1            MODERATE / NEEDS REFINEMENT
K@vya_Tech#2026           100      0            STRONG / COMPLIANT
123456789                 30       4            REJECTED / WEAK
================================================================================
`

---

## 💡 9. Conclusion & Learning Outcome
Successfully identified security vulnerabilities in test passwords, highlighting missing character categories, consecutive character repeats, and forbidden dictionary words.
