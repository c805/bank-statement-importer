from pathlib import Path

def get_pdf_files(folder_path):
    folder = Path(folder_path)

    pdf_files = sorted(folder.glob("*.pdf"))

    return pdf_files