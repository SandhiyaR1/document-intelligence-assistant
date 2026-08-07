# 📄 Document Intelligence Assistant

An AI-powered Document Intelligence Assistant built using Retrieval-Augmented Generation (RAG). Upload a PDF and ask natural language questions to get context-aware answers with source references.

---

## 🚀 Features

- 📄 Upload any PDF document
- 💬 Ask questions in natural language
- 🧠 Retrieval-Augmented Generation (RAG)
- 🔍 Semantic search using ChromaDB
- 📚 Source page references
- ⚡ Fast Llama 3.3 responses
- 🎨 Interactive Streamlit UI

---

## 🛠 Tech Stack

- Python
- Streamlit
- LangChain
- ChromaDB
- HuggingFace Embeddings (BAAI/bge-small-en-v1.5)
- Groq (Llama 3.3)
- PyMuPDF

---

## 📂 Project Structure

```
core/
models/
rag/
utils/

streamlit_app.py
requirements.txt
```

---

## ⚙️ Installation

```bash
git clone <repository-url>

cd document-intelligence-assistant

pip install -r requirements.txt

streamlit run streamlit_app.py
```

---

## 🔑 Environment Variables

Create a `.env` file.

```
GROQ_API_KEY=YOUR_API_KEY
```

---

## 📸 Application

- Upload PDF
- Process document
- Ask questions
- Get AI-generated answers with source pages

---

## 📈 Future Improvements

- Multiple PDF support
- Hybrid Search (BM25 + Vector Search)
- Streaming responses
- User authentication
- Docker deployment

---

## 👨‍💻 Author

**Sandhiya R**