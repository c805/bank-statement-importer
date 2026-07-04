from pdf_reader import read_pdf

from banks.cimb.cleaner import clean_lines
from banks.cimb.splitter import split_transactions
from banks.cimb.parser import parse_transactions, extract_opening_balance

from exporters.text_exporter import export_transactions_text
from exporters.csv_exporter import export_transactions_csv

from validators.transaction_validator import validate_transactions
from reporters.validation_reporter import print_validation_results

def main():

    text = read_pdf("samples/cimb/eStatementJan26.pdf")

    lines = clean_lines(text)

    blocks = split_transactions(lines)

    opening_balance = extract_opening_balance(lines)

    transactions = parse_transactions(blocks, opening_balance)

    errors, warnings = validate_transactions(transactions)

    print_validation_results(errors, warnings)

    if not errors:
        export_transactions_text(transactions)
        export_transactions_csv(transactions)

    print (f"Parsed {len(transactions)} transactions.")

if __name__ == "__main__":
    main()

