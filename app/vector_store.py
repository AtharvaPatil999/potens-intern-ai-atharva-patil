import faiss
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")


def create_vector_store(chunks):

    texts = [chunk["text"] for chunk in chunks]

    embeddings = model.encode(texts)

    index = faiss.IndexFlatL2(embeddings.shape[1])

    index.add(embeddings)

    return index, texts