import csv

def money(value):
    return f"{value:.2f}"

def export_transactions_csv(transactions, filename="transactions.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as file:
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