from src.importers.folder_importer import get_pdf_files

from src.exporters.text_exporter import export_transactions_text
from src.exporters.csv_exporter import export_transactions_csv

from src.reporters.validation_reporter import print_validation_results

from src.services.import_pipeline import process_pdf

def main():

    folder_path = "samples/cimb"

    export_path = input("Enter export folder (default=exports): ").strip()

    if not export_path:
        export_path =  "exports"

    pdf_files = get_pdf_files(folder_path)

    all_transactions = []

    for pdf_path in pdf_files:

        print(f"Processing {pdf_path.name}")

        transactions, errors, warnings = process_pdf(pdf_path)

        print_validation_results(errors, warnings)

        all_transactions.extend(transactions)

        if not errors:
            export_transactions_text(transactions, output_dir = export_path, filename=f"{pdf_path.stem}.txt")
            export_transactions_csv(transactions, output_dir = export_path, filename=f"{pdf_path.stem}.csv")

        print (f"Parsed {len(transactions)} transactions.")

if __name__ == "__main__":
    main()

