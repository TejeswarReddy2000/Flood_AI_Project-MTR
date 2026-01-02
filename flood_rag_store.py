from langchain_core.documents import Document
from langchain.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

reports = [
    {
        "state": "Assam",
        "text": "Flood detected in Assam with high severity. Flooded area is around 180 sq km."
    },
    {
        "state": "Kerala",
        "text": "Moderate flooding observed in Kerala. Flood area approximately 45 sq km."
    }
]

documents = [
    Document(page_content=r["text"], metadata={"state": r["state"]})
    for r in reports
]

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = FAISS.from_documents(documents, embeddings)
db.save_local("flood_vector_db")

print("✅ Flood reports stored successfully in vector DB")
