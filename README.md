# Bank Statement Importer

## Overview
Extract transactions from Malaysian bank statement PDFs into structured CSV files.

## Features
- Import one or multiple CIMB PDF statements
- Parse transactions
- Validate balances
- Export CSV
- Desktop GUI

## Tech Stack
- Python 3.12+
- pdfplumber

## Installation
pip install -r requirements.txt


Running (GUI)
Run GUI.bat  or  python -m src.app.main_app

Running (CLI)
Run CLI.bat  or  python -m src.main

## Future Improvements
- OCR support
- Excel export
- Support for other Banks (Maybank, Bank Islam, RHB, OCB, SCB, etc.)
