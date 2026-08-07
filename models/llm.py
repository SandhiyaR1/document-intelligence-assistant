import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()


def get_llm():

    api_key = None

    # Streamlit Cloud
    try:
        api_key = st.secrets["GROQ_API_KEY"]
    except Exception:
        pass

    # Local .env
    if not api_key:
        api_key = os.getenv("GROQ_API_KEY")

    return ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0,
        api_key=api_key,
    )