from pdf_reader import read_pdf

from importers.folder_importer import get_pdf_files

from banks.cimb.cleaner import clean_lines
from banks.cimb.splitter import split_transactions
from banks.cimb.parser import parse_transactions, extract_opening_balance

from exporters.text_exporter import export_transactions_text
from exporters.csv_exporter import export_transactions_csv

from validators.transaction_validator import validate_transactions
from reporters.validation_reporter import print_validation_results

def main():

    folder_path = "samples/cimb"

    pdf_files = get_pdf_files(folder_path)

    all_transactions = []

    for pdf_path in pdf_files:

        print(f"Processing {pdf_path.name}")

        text = read_pdf(pdf_path)

        lines = clean_lines(text)

        blocks = split_transactions(lines)

        opening_balance = extract_opening_balance(lines)

        transactions = parse_transactions(blocks, opening_balance)

        errors, warnings = validate_transactions(transactions)

        print_validation_results(errors, warnings)

        all_transactions.extend(transactions)

        if not errors:
            export_transactions_text(transactions, filename=f"{pdf_path.stem}.txt")
            export_transactions_csv(transactions, filename=f"{pdf_path.stem}.csv")

        print (f"Parsed {len(transactions)} transactions.")

if __name__ == "__main__":
    main()

