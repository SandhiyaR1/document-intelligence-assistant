import os
import shutil
import streamlit as st

from core.read_pdf import load_pdf
from rag.chunker import chunk_documents
from models.embedder import get_embedding_model
from rag.chroma_store import create_vector_store
from rag.pipeline import ask_question

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

st.set_page_config(
    page_title="Document Intelligence Assistant",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Document Intelligence Assistant")
st.caption("Upload a PDF and ask questions about it.")

if "processed" not in st.session_state:
    st.session_state.processed = False

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file is not None:

    filepath = os.path.join(
        UPLOAD_FOLDER,
        uploaded_file.name
    )

    if st.button("Process PDF"):

        with st.spinner("Processing PDF..."):

            if os.path.exists("chroma_db"):
                shutil.rmtree("chroma_db")

            with open(filepath, "wb") as f:
                f.write(uploaded_file.getbuffer())

            docs = load_pdf(filepath)

            chunks = chunk_documents(docs)

            embeddings = get_embedding_model()

            create_vector_store(
                chunks,
                embeddings
            )

            st.session_state.processed = True
            st.session_state.chat_history = []

        st.success("PDF indexed successfully!")

st.divider()

if st.session_state.processed:

    question = st.chat_input(
        "Ask anything about the uploaded document..."
    )

    if question:

        response = ask_question(question)

        st.session_state.chat_history.append(
            (
                question,
                response
            )
        )

    for question, response in st.session_state.chat_history:

        with st.chat_message("user"):
            st.write(question)

        with st.chat_message("assistant"):

            st.write(response["answer"])

            st.caption(
                f"📄 Source Pages: {response['pages']}"
            )

            with st.expander("Retrieved Context"):

                st.write(response["context"])