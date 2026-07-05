from src.pdf_reader import read_pdf

from src.banks.cimb.cleaner import clean_lines
from src.banks.cimb.splitter import split_transactions
from src.banks.cimb.parser import parse_transactions, extract_opening_balance

from src.validators.transaction_validator import validate_transactions


def process_pdf(pdf_path):
    """
    Full pipeline for a single PDF.
    Returns: transactions, errors, warnings
    """

    text = read_pdf(str(pdf_path))
    lines = clean_lines(text)
    blocks = split_transactions(lines)
    opening_balance = extract_opening_balance(lines)
    transactions = parse_transactions(blocks, opening_balance)

    errors, warnings = validate_transactions(transactions)

    return transactions, errors, warnings