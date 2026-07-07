import fitz
import os


def read_pdf(pdf_path):
    document = fitz.open(pdf_path)

    text = ""

    for page in document:
        text += page.get_text()

    document.close()

    return text


def read_all_pdfs(folder_path):
    documents = {}

    for file in os.listdir(folder_path):
        if file.endswith(".pdf"):
            path = os.path.join(folder_path, file)
            documents[file] = read_pdf(path)

    return documents