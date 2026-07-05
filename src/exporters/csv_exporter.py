import csv
from pathlib import Path

def ensure_export_dir(path: Path):
    path.mkdir(parents=True, exist_ok=True)

def money(value):
    return f"{value:.2f}"

def export_transactions_csv(transactions, output_dir = "exports", filename="transactions.csv"):
    
    output_dir = Path(output_dir)
    ensure_export_dir(output_dir)
    
    file_path = output_dir / filename

    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Date",
            "Header",
            "Description",
            "Withdrawal",
            "Deposit",
            "Tax",
            "Balance"
        ])

        for transaction in transactions:

            description = " | ".join(transaction.description_lines)

            writer.writerow([
                transaction.date,
                transaction.header,
                description,
                money(transaction.withdrawal),
                money(transaction.deposit),
                money(transaction.tax),
                money(transaction.balance)
            ])