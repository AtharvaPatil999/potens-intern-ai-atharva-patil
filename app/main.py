from fastapi import FastAPI
from app.pdf_reader import read_all_pdfs
from app.chunker import chunk_documents

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

@app.get("/chunks")
def chunks():

    docs = read_all_pdfs("documents")

    chunks = chunk_documents(docs)

    return {
        "total_chunks": len(chunks),
        "sample_chunk": chunks[0]
    }