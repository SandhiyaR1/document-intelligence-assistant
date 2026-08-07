from rag.chroma_store import load_vector_store


def get_retriever(embedding_model):

    vectordb = load_vector_store(embedding_model)

    retriever = vectordb.as_retriever(
        search_type="similarity",
        search_kwargs={
            "k": 10
        }
    )

    return retriever