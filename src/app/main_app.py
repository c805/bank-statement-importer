import tkinter as tk
from tkinter import filedialog, messagebox

from src.importers.folder_importer import get_pdf_files
from src.pdf_reader import read_pdf
from src.banks.cimb.cleaner import clean_lines
from src.banks.cimb.splitter import split_transactions
from src.banks.cimb.parser import parse_transactions
from src.validators.transaction_validator import validate_transactions
from src.exporters.csv_exporter import export_transactions_csv

from src.services.import_pipeline import process_pdf

class App:

    def __init__(self, root):
        self.root = root
        self.root.title("Bank Statement Importer")

        self.folder_path = None
        self.export_path = None

        self.label = tk.Label(root, text="No folder selected")
        self.label.pack(pady=10)

        self.export_label = tk.Label(root, text="Export folder not selected")
        self.export_label.pack(pady=10)

        self.select_btn = tk.Button(root, text="Select Folder", command=self.select_folder)
        self.select_btn.pack(pady=5)

        self.export_btn = tk.Button(root, text="Select Export Folder", command=self.select_export_folder)
        self.export_btn.pack(pady=5)

        self.run_btn = tk.Button(root, text="Import", command=self.run_import)
        self.run_btn.pack(pady=5)

        

    def select_folder(self):
        self.folder_path = filedialog.askdirectory()
        self.label.config(text=self.folder_path)

    def select_export_folder(self):
        self.export_path = filedialog.askdirectory()

        if self.export_path:
            self.export_label.config(text=f"Export: {self.export_path}")

    def run_import(self):

        if not self.folder_path:
            messagebox.showerror("Error", "Please select a folder first")
            return

        pdf_files = get_pdf_files(self.folder_path)

        all_transactions = []

        for pdf_path in pdf_files:

            transactions, errors, warnings = process_pdf(pdf_path)

            if errors:
                messagebox.showwarning(
                    "Validation Errors",
                    f"{pdf_path.name} has {len(errors)} errors"
                )

            export_transactions_csv(
                transactions,
                output_dir = self.export_path or "exports",
                filename=f"{pdf_path.stem}.csv"
            )

            all_transactions.extend(transactions)

        messagebox.showinfo(
            "Done",
            f"Imported {len(pdf_files)} files successfully"
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()