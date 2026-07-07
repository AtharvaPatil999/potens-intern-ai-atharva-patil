from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = []

    for document_name, pages in documents.items():

        for page in pages:

            split_chunks = splitter.split_text(page["text"])

            for chunk in split_chunks:

                chunks.append({
                    "document": document_name,
                    "page": page["page"],
                    "text": chunk
                })

    return chunks