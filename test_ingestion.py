from core.read_pdf import load_pdf

from rag.chunker import chunk_documents

from models.embedder import get_embedding_model

from rag.chroma_store import create_vector_store


docs = load_pdf("C:\\Users\\Sandy\\Desktop\\RAG-project\\uploads\\Companies_Act -17-20.pdf")


print("Pages:", len(docs))

chunks = chunk_documents(docs)

print("Chunks:", len(chunks))

embeddings = get_embedding_model()

db = create_vector_store(chunks, embeddings)

print("Done")