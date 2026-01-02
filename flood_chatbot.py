from langchain.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = FAISS.load_local(
    "flood_vector_db",
    embeddings,
    allow_dangerous_deserialization=True
)

def ask_flood_question(question):
    docs = db.similarity_search(question, k=2)
    print("\n🧠 AI Flood Assistant Answer:\n")
    for doc in docs:
        print("-", doc.page_content)

ask_flood_question("Which state has high flood risk?")
ask_flood_question("Tell me about floods in Assam")
