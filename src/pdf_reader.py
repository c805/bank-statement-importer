import fitz  # PyMuPDF

DEBUG = False

def read_pdf(pdf_path):
    document = fitz.open(pdf_path)

    text = ""

    for page in document:
        text += page.get_text()
        text += "\n\n"
    
    document.close()

    return text
    
if DEBUG:
    pdf_path = "samples/cimb/eStatementJan26.pdf"

    text = read_pdf(pdf_path)

    with open("output.txt", "w", encoding="utf-8") as file:
        file.write(text)

    print("Text saved to output.txt")