from pathlib import Path

def ensure_export_dir(path: Path):
    path.mkdir(parents=True, exist_ok=True)

def export_transactions_text(transactions, output_dir = "exports", filename="parsed_transaction.txt"):
    
    output_dir = Path(output_dir)
    ensure_export_dir(output_dir)

    file_path = output_dir / filename
    
    with open(file_path, "w", encoding="utf-8") as output:

        for i, transaction in enumerate(transactions, start=1):

            output.write(f"Transaction {i}\n")
            output.write("=" * 50 + "\n")

            output.write(f"Date: {transaction.date}\n")
            output.write(f"Header: {transaction.header}\n")

            output.write("Description:\n")

            for line in transaction.description_lines:
                output.write(f"    {line}\n")

            output.write(f"Withdrawal: {transaction.withdrawal:.2f}\n")
            output.write(f"Deposit: {transaction.deposit:.2f}\n")
            output.write(f"Tax: {transaction.tax:.2f}\n")
            output.write(f"Balance: {transaction.balance:.2f}\n")

            output.write("\n\n")