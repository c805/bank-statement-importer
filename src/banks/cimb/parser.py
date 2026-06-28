import re

from models.transaction import Transaction

NUMBER_PATTERN = r"^\d+(?:,\d{3})*\.\d{2}$"


def is_amount(line):
    return re.match(NUMBER_PATTERN, line) is not None

def parse_transactions(blocks):

    transactions = []
    previous_balance = None

    for block in blocks:

        transaction = parse_transaction(block)

        if previous_balance is not None:

            delta = transaction.balance - previous_balance

            if delta < 0:
                transaction.withdrawal = abs(delta)
            else:
                transaction.deposit = delta

        previous_balance = transaction.balance

        transactions.append(transaction)

    return transactions

def parse_transaction(transaction_block):
    transaction = Transaction()

    #temporarily segregate withdrawals/deposits/tax/balance
    amount_lines = [] 

    header_line = transaction_block[0]

    parts = header_line.split(maxsplit=1)

    transaction.date = parts[0]

    if len(parts) > 1:
        transaction.header = parts[1]

    # Remaining description lines
    for line in transaction_block[1:]:

        amount = extract_amount(line)

        if amount is not None:
            amount_lines.append(amount)
        else: 
            transaction.description_lines.append(line)

    
    #temporary
    transaction.balance = amount_lines[1]
    balance = amount_lines[1]

    print("DESC:", transaction.description_lines)
    print("AMOUNTS:", amount_lines)

    return transaction


def extract_amount(line):
    match = re.search(r"\d+(?:,\d{3})*\.\d{2}", line)
    if not match:
        return None

    return float(match.group().replace(",", ""))