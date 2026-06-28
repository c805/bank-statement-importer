import re

DATE_PATTERN = r"^\d{2}/\d{2}/\d{4}\s+.+"
NUMBER_PATTERN = r"^\d+(?:,\d{3})*\.\d{2}$"

def is_transaction_header(line):
    return re.match(DATE_PATTERN, line) is not None

def is_amount(line):
    return re.match(NUMBER_PATTERN, line) is not None

def split_transactions(lines):
    transactions = []
    current_transaction = []
    has_amount = False

    for line in lines:

        line = line.strip()

        if not line:
            continue

        if is_transaction_header(line):
            
            if not current_transaction:
                current_transaction = [line]

            elif has_amount:
                transactions.append(current_transaction)
                current_transaction = [line]
                has_amount = False

            else:
                current_transaction.append(line)
        
        else:
            if current_transaction:
                current_transaction.append(line)
                
                if is_amount(line):
                    has_amount = True

    if current_transaction:
        transactions.append(current_transaction)
    
    return transactions