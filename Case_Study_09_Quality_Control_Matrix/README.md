# Case Study 09: Manufacturing Quality Control Matrix (Problem 60)

> **Course**: Python Programming - Activity-Based Learning (ABL) Assignment  
> **Institution**: Dr. RVR NRI Institute of Technology (Deemed to be University)  
> **Student Name**: Sai Chandra Nerella | **NRI ID**: 26000654 | **Section**: Section 3 | **Branch**: CSE (I B.Tech)

---

## 📋 1. Problem Statement
Analyse industrial manufacturing batch records across automotive component lines, calculate defect percentages and lot yield rates, evaluate each batch against a 3.5% defect tolerance threshold, classify batches into ISO quality grades, and generate an actionable quarantine report.

---

## 🎯 2. Objectives
1. Process batch records containing total produced and defective units.
2. Compute component pass counts, defect percentages, and yield rates.
3. Categorize batches: Grade-A (<=1.5%), Grade-B (<=3.5%), Quarantined (>3.5%).
4. Highlight quarantined batches requiring root cause analysis and line stoppage.

---

## ⚙️ 3. Assumptions & Constraints
1. Defective units cannot exceed produced units.
2. Standard allowable defect threshold is 3.50%.

---

## 🧠 4. Step-by-Step Algorithm
1. Initialize factory totals for produced, passed, and defective.
2. For each batch (batch_id, product, produced, defective): passed = produced - defective; defect_pct = (defective/produced)*100; yield_pct = (passed/produced)*100.
3. Check defect_pct against 1.5% and 3.5% thresholds. Assign status Grade-A, Grade-B, or Quarantined.
4. Aggregate totals, calculate overall factory defect and yield rates.
5. Output full quality matrix and quarantine action list.

---

## 📝 5. Pseudocode
`	ext
FUNCTION analyze_quality(batches, threshold):
    FOR EACH (id, name, produced, defective) IN batches:
        passed = produced - defective
        defect_pct = (defective / produced) * 100
        yield_pct = (passed / produced) * 100
        IF defect_pct <= 1.5 THEN status = 'GRADE-A'
        ELSE IF defect_pct <= threshold THEN status = 'GRADE-B'
        ELSE status = 'QUARANTINED'
    PRINT factory audit table and quarantined lines
END FUNCTION
`

---

## 📊 6. System Flowchart Diagram
`	ext
[START]
   │
   ▼
[Load Batch Records: (BatchID, Product, ProducedUnits, DefectiveUnits)]
   │
   ▼
[Calculate: Passed = Produced - Defective]
[Calculate: Defect% = (Defective / Produced) * 100]
[Calculate: Yield%  = (Passed / Produced) * 100]
   │
   ▼
<Is Defect% <= 1.5%?>
   ├── YES ──► [Status: GRADE-A (PASS)]
   └── NO
         │
         <Is Defect% <= 3.5% (Threshold)?>
           ├── YES ──► [Status: GRADE-B (ACCEPTABLE)]
           └── NO  ──► [Status: QUARANTINED (FAIL) -> Add to Rework List]
         │
         ▼
[Print Factory Quality Audit and Mandatory Action Items]
   │
   ▼
 [END]
`

---

## 💻 7. Python Source Code
`python
"""
Case Study 9 (Problem 60): Manufacturing Quality Control Matrix
Syllabus Concepts: Computational thinking, variables, data types, operators,
                   conditional statements, loops, nested lists, tuples, tuple unpacking,
                   string formatting.

Problem Statement:
Analyse factory production volumes and defective unit counts across multiple
product lines and batches, calculate defect percentages and lot yield rates,
classify batches based on ISO quality tolerance thresholds, and generate an
actionable scrap and rework audit.
"""

def analyze_manufacturing_quality(batch_records, defect_threshold_pct):
    print("=" * 95)
    print("        PRECISION AUTOMOTIVE MANUFACTURING - QUALITY CONTROL MATRIX")
    print(f"        Standard Defect Tolerance Threshold: {defect_threshold_pct:.2f}%")
    print("=" * 95)
    print(f"{'BatchID':<9} {'Product Line':<18} {'Produced':<10} {'Passed':<9} {'Defective':<11} {'Defect(%)':<11} {'Yield(%)':<10} {'Status'}")
    print("-" * 95)

    total_units_produced = 0
    total_units_passed = 0
    total_defective_units = 0

    quarantined_batches = []
    approved_batches = []

    # Process nested batch records: (batch_id, product_name, units_produced, defective_units)
    for record in batch_records:
        batch_id, product_name, produced, defective = record

        passed = produced - defective
        defect_pct = (defective / produced) * 100.0 if produced > 0 else 0.0
        yield_pct = (passed / produced) * 100.0 if produced > 0 else 0.0

        total_units_produced += produced
        total_units_passed += passed
        total_defective_units += defective

        # Quality Threshold Verification
        if defect_pct <= 1.5:
            status = "GRADE-A (PASS)"
            approved_batches.append(batch_id)
        elif defect_pct <= defect_threshold_pct:
            status = "GRADE-B (ACCEPTABLE)"
            approved_batches.append(batch_id)
        else:
            status = "QUARANTINED (FAIL)"
            quarantined_batches.append((batch_id, product_name, defect_pct, defective))

        print(f"{batch_id:<9} {product_name:<18} {produced:<10} {passed:<9} {defective:<11} {defect_pct:<11.2f} {yield_pct:<10.2f} {status}")

    # Overall Factory Summary
    overall_defect_pct = (total_defective_units / total_units_produced) * 100.0
    overall_yield_pct = (total_units_passed / total_units_produced) * 100.0

    print("-" * 95)
    print("                           QUALITY AUDIT SUMMARY")
    print("-" * 95)
    print(f"Total Batches Inspected      : {len(batch_records)}")
    print(f"Total Components Manufactured : {total_units_produced:,}")
    print(f"Total Passed Components       : {total_units_passed:,}")
    print(f"Total Defective / Scrap Units : {total_defective_units:,}")
    print(f"Overall Factory Defect Rate   : {overall_defect_pct:.2f}%")
    print(f"Overall Factory Yield Rate    : {overall_yield_pct:.2f}%")

    print("\n" + "=" * 95)
    print("                     FLAGGED BATCHES REQUIRING REWORK")
    print("=" * 95)
    if quarantined_batches:
        print(f"{'BatchID':<10} {'Product Line':<22} {'Defect Rate':<14} {'Defective Units':<16} {'Mandatory Action'}")
        print("-" * 95)
        for q in quarantined_batches:
            b_id, p_name, d_rate, d_units = q
            print(f"{b_id:<10} {p_name:<22} {d_rate:<14.2f}% {d_units:<16} Immediate Line Stoppage & Root Cause Analysis")
    else:
        print("[✓] All production batches adhere strictly to quality limits.")
    print("=" * 95)


if __name__ == "__main__":
    threshold = 3.5  # Max allowable defect %

    # List of Tuples: (BatchID, ProductName, ProducedUnits, DefectiveUnits)
    production_data = [
        ("BAT-101", "Brake Rotors",       5000, 45),   # 0.90% - Grade A
        ("BAT-102", "Alloy Wheels",       2500, 85),   # 3.40% - Grade B
        ("BAT-103", "Fuel Injectors",     8000, 360),  # 4.50% - Quarantined (Fail)
        ("BAT-104", "Spark Plugs",        12000, 110), # 0.92% - Grade A
        ("BAT-105", "Transmission Gears", 3500, 160),  # 4.57% - Quarantined (Fail)
        ("BAT-106", "Camshaft Assemblies", 1800, 35),   # 1.94% - Grade B
        ("BAT-107", "Turbocharger Blades", 4000, 75),   # 1.88% - Grade B
    ]

    analyze_manufacturing_quality(production_data, threshold)

`

---

## 🖥️ 8. Program Execution Output Log
`	ext
﻿===============================================================================================
        PRECISION AUTOMOTIVE MANUFACTURING - QUALITY CONTROL MATRIX
        Standard Defect Tolerance Threshold: 3.50%
===============================================================================================
BatchID   Product Line       Produced   Passed    Defective   Defect(%)   Yield(%)   Status
-----------------------------------------------------------------------------------------------
BAT-101   Brake Rotors       5000       4955      45          0.90        99.10      GRADE-A (PASS)
BAT-102   Alloy Wheels       2500       2415      85          3.40        96.60      GRADE-B (ACCEPTABLE)
BAT-103   Fuel Injectors     8000       7640      360         4.50        95.50      QUARANTINED (FAIL)
BAT-104   Spark Plugs        12000      11890     110         0.92        99.08      GRADE-A (PASS)
BAT-105   Transmission Gears 3500       3340      160         4.57        95.43      QUARANTINED (FAIL)
BAT-106   Camshaft Assemblies 1800       1765      35          1.94        98.06      GRADE-B (ACCEPTABLE)
BAT-107   Turbocharger Blades 4000       3925      75          1.88        98.12      GRADE-B (ACCEPTABLE)
-----------------------------------------------------------------------------------------------
                           QUALITY AUDIT SUMMARY
-----------------------------------------------------------------------------------------------
Total Batches Inspected      : 7
Total Components Manufactured : 36,800
Total Passed Components       : 35,930
Total Defective / Scrap Units : 870
Overall Factory Defect Rate   : 2.36%
Overall Factory Yield Rate    : 97.64%

===============================================================================================
                     FLAGGED BATCHES REQUIRING REWORK
===============================================================================================
BatchID    Product Line           Defect Rate    Defective Units  Mandatory Action
-----------------------------------------------------------------------------------------------
BAT-103    Fuel Injectors         4.50          % 360              Immediate Line Stoppage & Root Cause Analysis
BAT-105    Transmission Gears     4.57          % 160              Immediate Line Stoppage & Root Cause Analysis
===============================================================================================
`

---

## 💡 9. Conclusion & Learning Outcome
Evaluated manufacturing lots across seven automotive component lines. Flagged batches BAT-103 (Fuel Injectors) and BAT-105 (Transmission Gears) for exceeding defect tolerance thresholds.
