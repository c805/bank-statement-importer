def validate_transactions(transactions):
    errors = []
    warnings = []

    for index, transaction in enumerate(transactions, start=1):
        if not transaction.date:
            errors.append(f"Transaction {index}: Missing date.")
        
        if not transaction.header:
            warnings.append(f"Transaction {index}: Missing header.")

        #temporary, to consider converting 0 to None
        if transaction.balance == 0:
            warnings.append(f"Transaction {index}: Balance is zero.")

        previous = transactions[i - 1]
        current = transactions[i]

        expected_balance = (
            previous.balance
            - current.withdrawal
            + current.deposit
            - current.tax
        )   

        #indirect checking for small floating differences
        if abs(expected_balance - current.balance) > 0.01:
            errors.append(
                f"Transaction {i+1}: "
                f"Expected balance {expected_balance:.2f}, "
                f"found {current.balance:.2f}"
            )

    return errors, warnings