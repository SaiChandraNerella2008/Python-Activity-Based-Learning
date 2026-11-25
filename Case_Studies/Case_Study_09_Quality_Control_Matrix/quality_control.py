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
