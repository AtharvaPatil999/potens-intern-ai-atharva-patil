import fitz
import os


def read_all_pdfs(folder_path):

    documents = {}

    for file in os.listdir(folder_path):

        if file.endswith(".pdf"):

            path = os.path.join(folder_path, file)

            pdf = fitz.open(path)

            pages = []

            for page_number, page in enumerate(pdf):

                pages.append({
                    "page": page_number + 1,
                    "text": page.get_text()
                })

            documents[file] = pages

            pdf.close()

    return documents