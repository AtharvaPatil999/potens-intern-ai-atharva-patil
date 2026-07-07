import faiss
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")


def create_vector_store(chunks):

    texts = [chunk["text"] for chunk in chunks]

    embeddings = model.encode(texts)

    index = faiss.IndexFlatL2(embeddings.shape[1])

    index.add(embeddings)

    return index, chunks

def search(index, chunks, question, top_k=3):

    question_embedding = model.encode([question])

    distances, indices = index.search(question_embedding, top_k)

    results = []

    for i in indices[0]:
        results.append(chunks[i])

    return results