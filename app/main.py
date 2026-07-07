from fastapi import FastAPI
from app.pdf_reader import read_all_pdfs

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Potens AI/ML Assignment API is running."
}


@app.get("/documents")
def documents():

    docs = read_all_pdfs("documents")

    return {
        "total_documents": len(docs),
        "documents": list(docs.keys())
    }