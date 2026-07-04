import re

from models.transaction import Transaction

from utils.parsing import (
    is_amount,
    extract_amount
)

def parse_transactions(blocks, opening_balance = None):

    transactions = []
    previous_balance = opening_balance

    if opening_balance is not None:
        opening_transaction = Transaction()
        opening_transaction.header = "OPENING BALANCE"
        opening_transaction.balance = opening_balance

        transactions.append(opening_transaction)

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

    return transaction

def extract_opening_balance(lines):
    for index, line in enumerate(lines):
        if line == "OPENING BALANCE":
            amount = extract_amount(lines[index + 1])
            return amount

    return None