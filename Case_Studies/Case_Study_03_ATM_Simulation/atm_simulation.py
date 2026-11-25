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
