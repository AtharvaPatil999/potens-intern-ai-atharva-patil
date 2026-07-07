from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    all_chunks = []

    for filename, text in documents.items():

        chunks = splitter.split_text(text)

        for chunk in chunks:

            all_chunks.append({
                "document": filename,
                "text": chunk
            })

    return all_chunks