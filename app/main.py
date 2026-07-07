from fastapi import FastAPI
from pydantic import BaseModel

from app.pdf_reader import read_all_pdfs
from app.chunker import chunk_documents
from app.vector_store import create_vector_store, search
from app.llm import generate_answer

app = FastAPI()


class Question(BaseModel):
    question: str


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


@app.get("/vector-store")
def vector_store():
    docs = read_all_pdfs("documents")

    chunks = chunk_documents(docs)

    index, texts = create_vector_store(chunks)

    return {
        "vectors_created": index.ntotal
    }


@app.post("/ask")
def ask(question: Question):
    docs = read_all_pdfs("documents")

    chunks = chunk_documents(docs)

    index, chunk_data = create_vector_store(chunks)

    results = search(index, chunk_data, question.question)

    context = ""
    citations = []

    for chunk in results:
        context += chunk["text"] + "\n\n"

        citations.append({
            "document": chunk["document"],
            "page": chunk["page"],
            "snippet": chunk["text"][:200]
        })

    answer = generate_answer(context, question.question)

    return {
        "answer": answer,
        "citations": citations
    }

@app.post("/contradict")
def contradict(doc1: str, doc2: str):

    docs = read_all_pdfs("documents")

    text1 = ""
    text2 = ""

    for page in docs[doc1]:
        text1 += page["text"]

    for page in docs[doc2]:
        text2 += page["text"]

    prompt = f"""
Compare these two documents.

Document 1:
{text1[:4000]}

Document 2:
{text2[:4000]}

Tell me:

1. Do they contradict each other?

2. Explain why.
"""

    answer = generate_answer(prompt, "")

    return {
        "document_1": doc1,
        "document_2": doc2,
        "result": answer
    }