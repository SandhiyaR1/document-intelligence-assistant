from models.embedder import get_embedding_model
from models.llm import get_llm

from rag.vector_store import get_retriever
from rag.prompt import PROMPT

from langchain_core.output_parsers import StrOutputParser


llm = get_llm()


def ask_question(question):

    embedding_model = get_embedding_model()

    retriever = get_retriever(
        embedding_model
    )

    docs = retriever.invoke(question)

    context = ""

    for doc in docs:

        context += f"""
==============================
Page Number : {doc.metadata['page']}s

{doc.page_content}

"""

    pages = sorted(
        list(
            set(
                doc.metadata["page"]
                for doc in docs
            )
        )
    )

    chain = (
        PROMPT
        | llm
        | StrOutputParser()
    )

    answer = chain.invoke(
        {
            "context": context,
            "question": question
        }
    )

    return {
        "answer": answer,
        "pages": pages,
        "context": context
    }