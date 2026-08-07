import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()


def get_llm():

    api_key = None

    # Try Streamlit Secrets first
    if "GROQ_API_KEY" in st.secrets:
        api_key = st.secrets["GROQ_API_KEY"]

    # Fall back to local .env
    if not api_key:
        api_key = os.getenv("GROQ_API_KEY")

    # Fail with a clear message
    if not api_key:
        raise RuntimeError(
            "GROQ_API_KEY not found. "
            "Set it in Streamlit Secrets or in a local .env file."
        )

    return ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0,
        api_key=api_key,
    )