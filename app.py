import os
import streamlit as st
from dotenv import load_dotenv

from langchain.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA

# -----------------------------------
# Load environment variables
# -----------------------------------
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# -----------------------------------
# Streamlit config
# -----------------------------------
st.set_page_config(
    page_title="🌊 Flood Gen-AI Assistant",
    page_icon="🌊",
    layout="centered"
)

st.title("🌊 Flood Gen-AI Assistant")
st.write(
    "Ask intelligent questions about flood conditions using "
    "satellite data + Gen-AI (Groq)."
)

# -----------------------------------
# Load RAG chain (cached)
# -----------------------------------
@st.cache_resource
def load_rag_chain():
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = FAISS.load_local(
        "flood_vector_db",
        embeddings,
        allow_dangerous_deserialization=True
    )

    llm = ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model_name="llama3-8b-8192",
        temperature=0.2
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=db.as_retriever(search_kwargs={"k": 3}),
        chain_type="stuff",
        return_source_documents=False
    )

    return qa_chain


qa = load_rag_chain()

# -----------------------------------
# User input
# -----------------------------------
question = st.text_input(
    "Ask a flood-related question",
    placeholder="e.g. Compare flood situation in Assam and Kerala"
)

# -----------------------------------
# Ask button
# -----------------------------------
if st.button("Ask AI"):
    if question.strip() == "":
        st.warning("⚠️ Please enter a question.")
    else:
        with st.spinner("Analyzing flood data..."):
            answer = qa.run(question)

        st.subheader("🧠 AI Answer")
        st.write(answer)

# -----------------------------------
# Footer
# -----------------------------------
st.markdown("---")
st.caption("Powered by Sentinel-1 • FAISS • Groq (LLaMA-3) • Streamlit")
