from banks.cimb.parser import parse_transaction

balance = None

transaction_block = [
    "12/12/2025 DUITNOW QR",
    "251212083848367547822",
    "PUAN AMINA",
    "PUAN AMINAH BINTI OT",
    "200.00", #deposit
    "1234.56"
]

transaction, balance = parse_transaction(transaction_block)

print(transaction, "balance is", balance)