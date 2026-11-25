# Case Study 03: ATM Transaction Sequence Simulation (Problem 13)

> **Course**: Python Programming - Activity-Based Learning (ABL) Assignment  
> **Institution**: Dr. RVR NRI Institute of Technology (Deemed to be University)  
> **Student Name**: Sai Chandra Nerella | **NRI ID**: 26000654 | **Section**: Section 3 | **Branch**: CSE (I B.Tech)

---

## 📋 1. Problem Statement
Process a sequential stream of ATM banking transactions (deposits and withdrawals) against an account, enforce single-transaction caps, daily cumulative withdrawal limits, and minimum balance constraints, reject invalid operations, and generate an audit ledger.

---

## 🎯 2. Objectives
1. Maintain real-time account balance across arbitrary transaction sequences.
2. Enforce minimum balance (₹2,000) and max single withdrawal limit (₹20,000).
3. Track cumulative daily withdrawals and enforce daily ceiling (₹50,000).
4. Reject negative amounts and unsupported transaction types.

---

## ⚙️ 3. Assumptions & Constraints
1. Opening balance is valid and meets minimum balance requirement.
2. Transactions occur in strict chronological sequence.
3. Rejected transactions do not alter running balance or daily caps.

---

## 🧠 4. Step-by-Step Algorithm
1. Initialize balance = opening_balance, total_withdrawn = 0.
2. For each transaction (txn_id, txn_type, amount): unpack.
3. If amount <= 0: reject as invalid amount.
4. If DEPOSIT: balance += amount; log success.
5. If WITHDRAWAL: check if amount > 20,000 (single cap), or total_withdrawn + amount > 50,000 (daily cap), or balance - amount < 2,000 (min balance). If any holds, reject; else balance -= amount, total_withdrawn += amount, log success.
6. Display audit table and summary statistics.

---

## 📝 5. Pseudocode
`	ext
FUNCTION simulate_atm(balance, transactions):
    FOR EACH (id, type, amount) IN transactions:
        IF amount <= 0 THEN REJECT
        ELSE IF type == 'DEPOSIT' THEN balance += amount
        ELSE IF type == 'WITHDRAWAL' THEN
            IF amount > MAX_SINGLE OR daily_sum + amount > DAILY_LIMIT OR balance - amount < MIN_BAL THEN
                REJECT
            ELSE
                balance -= amount; daily_sum += amount
        PRINT audit row
END FUNCTION
`

---

## 📊 6. System Flowchart Diagram
`	ext
[START]
   │
   ▼
[Initialize Balance & Cumulative Withdrawn Total]
   │
   ▼
[Read Next Transaction (TxnID, Type, Amount)]
   │
   ├── Amount <= 0? ──► [REJECT: Invalid Amount]
   │
   ├── Type == DEPOSIT? ──► [Balance += Amount] ──► [Log SUCCESS]
   │
   └── Type == WITHDRAWAL?
         │
         ├── Amount > 20K OR Daily + Amount > 50K OR Balance - Amount < 2K?
         │     │
         │     ├── YES ──► [REJECT: Policy Breach]
         │     │
         │     └── NO  ──► [Balance -= Amount, Daily += Amount] ──► [Log SUCCESS]
         │
         ▼
[Print Account Audit Ledger & Net Change]
   │
   ▼
 [END]
`

---

## 💻 7. Python Source Code
`python
"""
Case Study 3 (Problem 13): ATM Transaction Sequence Simulation
Syllabus Concepts: Computational thinking, variables, data types, operators,
                   conditional statements, loops, lists, tuples, tuple unpacking.

Problem Statement:
Process a sequence of deposits and withdrawals, maintain a simulated balance,
enforce withdrawal limits (per-transaction, daily cap, minimum balance requirement),
reject invalid transactions, and produce a comprehensive audit summary.
"""

def simulate_atm_ledger(account_id, holder_name, opening_balance, transactions):
    print("=" * 85)
    print(f"      APEX BANK ATM TRANSACTION SIMULATOR - ACCOUNT AUDIT LOG")
    print(f"      Account No: {account_id} | Account Holder: {holder_name}")
    print("=" * 85)
    print(f"Opening Balance: ₹{opening_balance:,.2f}")
    print("-" * 85)
    print(f"{'TxnID':<8} {'Type':<12} {'Requested(₹)':<14} {'Status':<10} {'Running Balance(₹)':<20} {'Remarks'}")
    print("-" * 85)

    balance = opening_balance
    MINIMUM_BALANCE = 2000.0
    MAX_SINGLE_WITHDRAWAL = 20000.0
    DAILY_WITHDRAWAL_LIMIT = 50000.0

    total_withdrawn_today = 0.0
    successful_txns = 0
    rejected_txns = 0

    # Store audit history as a list of tuples
    audit_history = []

    for txn in transactions:
        # Tuple unpacking: txn_id, txn_type, amount
        txn_id, txn_type, amount = txn
        status = "FAILED"
        remark = ""

        # Validate non-negative amounts
        if amount <= 0:
            status = "REJECTED"
            remark = "Invalid amount (<= 0)"
            rejected_txns += 1
        elif txn_type.upper() == "DEPOSIT":
            # Deposit processing
            balance += amount
            status = "SUCCESS"
            remark = f"Credited ₹{amount:,.2f}"
            successful_txns += 1
        elif txn_type.upper() == "WITHDRAWAL":
            # Withdrawal checks
            if amount > MAX_SINGLE_WITHDRAWAL:
                status = "REJECTED"
                remark = f"Exceeds single limit (₹{MAX_SINGLE_WITHDRAWAL:,.0f})"
                rejected_txns += 1
            elif total_withdrawn_today + amount > DAILY_WITHDRAWAL_LIMIT:
                status = "REJECTED"
                remark = f"Exceeds daily cap (₹{DAILY_WITHDRAWAL_LIMIT:,.0f})"
                rejected_txns += 1
            elif (balance - amount) < MINIMUM_BALANCE:
                status = "REJECTED"
                remark = f"Breaches Min Balance (₹{MINIMUM_BALANCE:,.0f})"
                rejected_txns += 1
            else:
                balance -= amount
                total_withdrawn_today += amount
                status = "SUCCESS"
                remark = f"Debited ₹{amount:,.2f}"
                successful_txns += 1
        else:
            status = "REJECTED"
            remark = "Unsupported operation type"
            rejected_txns += 1

        print(f"{txn_id:<8} {txn_type:<12} {amount:<14,.2f} {status:<10} {balance:<20,.2f} {remark}")
        audit_history.append((txn_id, txn_type, amount, status, balance, remark))

    # Summary Statistics
    print("-" * 85)
    print("                           TRANSACTION SUMMARY REPORT")
    print("-" * 85)
    print(f"Total Transactions Processed : {len(transactions)}")
    print(f"Successful Transactions       : {successful_txns}")
    print(f"Rejected / Failed Transactions: {rejected_txns}")
    print(f"Total Withdrawn Today         : ₹{total_withdrawn_today:,.2f} / ₹{DAILY_WITHDRAWAL_LIMIT:,.2f}")
    print(f"Closing Account Balance       : ₹{balance:,.2f}")
    net_change = balance - opening_balance
    if net_change >= 0:
        print(f"Net Account Change            : +₹{net_change:,.2f} (Net Inflow)")
    else:
        print(f"Net Account Change            : -₹{abs(net_change):,.2f} (Net Outflow)")
    print("=" * 85)


if __name__ == "__main__":
    initial_balance = 35000.0

    # Sequence of test transactions: (TxnID, Type, Amount)
    txn_stream = [
        ("TX1001", "DEPOSIT", 15000.0),       # Successful deposit -> 50,000
        ("TX1002", "WITHDRAWAL", 10000.0),    # Successful withdrawal -> 40,000
        ("TX1003", "WITHDRAWAL", 25000.0),    # Fails: Exceeds single limit 20,000
        ("TX1004", "WITHDRAWAL", 18000.0),    # Successful withdrawal -> 22,000 (total withdrawn: 28k)
        ("TX1005", "DEPOSIT", -500.0),        # Fails: Negative amount
        ("TX1006", "WITHDRAWAL", 15000.0),    # Successful withdrawal -> 7,000 (total withdrawn: 43k)
        ("TX1007", "WITHDRAWAL", 6000.0),     # Fails: Would breach min balance 2,000 (7k - 6k = 1k < 2k)
        ("TX1008", "WITHDRAWAL", 4000.0),     # Successful withdrawal -> 3,000 (total withdrawn: 47k)
        ("TX1009", "WITHDRAWAL", 5000.0),     # Fails: Exceeds daily cap (47k + 5k = 52k > 50k)
        ("TX1010", "DEPOSIT", 20000.0),       # Successful deposit -> 23,000
    ]

    simulate_atm_ledger("SB-98421045", "Sai Chandra Nerella", initial_balance, txn_stream)

`

---

## 🖥️ 8. Program Execution Output Log
`	ext
﻿=====================================================================================
      APEX BANK ATM TRANSACTION SIMULATOR - ACCOUNT AUDIT LOG
      Account No: SB-98421045 | Account Holder: Sai Chandra Nerella
=====================================================================================
Opening Balance: ₹35,000.00
-------------------------------------------------------------------------------------
TxnID    Type         Requested(₹)   Status     Running Balance(₹)   Remarks
-------------------------------------------------------------------------------------
TX1001   DEPOSIT      15,000.00      SUCCESS    50,000.00            Credited ₹15,000.00
TX1002   WITHDRAWAL   10,000.00      SUCCESS    40,000.00            Debited ₹10,000.00
TX1003   WITHDRAWAL   25,000.00      REJECTED   40,000.00            Exceeds single limit (₹20,000)
TX1004   WITHDRAWAL   18,000.00      SUCCESS    22,000.00            Debited ₹18,000.00
TX1005   DEPOSIT      -500.00        REJECTED   22,000.00            Invalid amount (<= 0)
TX1006   WITHDRAWAL   15,000.00      SUCCESS    7,000.00             Debited ₹15,000.00
TX1007   WITHDRAWAL   6,000.00       REJECTED   7,000.00             Breaches Min Balance (₹2,000)
TX1008   WITHDRAWAL   4,000.00       SUCCESS    3,000.00             Debited ₹4,000.00
TX1009   WITHDRAWAL   5,000.00       REJECTED   3,000.00             Exceeds daily cap (₹50,000)
TX1010   DEPOSIT      20,000.00      SUCCESS    23,000.00            Credited ₹20,000.00
-------------------------------------------------------------------------------------
                           TRANSACTION SUMMARY REPORT
-------------------------------------------------------------------------------------
Total Transactions Processed : 10
Successful Transactions       : 6
Rejected / Failed Transactions: 4
Total Withdrawn Today         : ₹47,000.00 / ₹50,000.00
Closing Account Balance       : ₹23,000.00
Net Account Change            : -₹12,000.00 (Net Outflow)
=====================================================================================
`

---

## 💡 9. Conclusion & Learning Outcome
The ATM simulator maintained state integrity across 10 sequential transactions. All policy breaches (single cap, daily cap, negative amount, and minimum balance breach) were rejected while valid deposits and withdrawals executed smoothly.
