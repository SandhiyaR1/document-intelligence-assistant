import shutil
import os
import tempfile

from langchain_chroma import Chroma

#CHROMA_PATH = "chroma_db"
CHROMA_PATH = os.path.join(tempfile.gettempdir(), "chroma_db")


def create_vector_store(chunks, embedding_model):

    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=CHROMA_PATH
    )

    return vectordb


def load_vector_store(embedding_model):

    vectordb = Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=embedding_model
    )

    return vectordb