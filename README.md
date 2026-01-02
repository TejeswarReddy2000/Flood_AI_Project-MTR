🌊 Flood Detection & Gen-AI Assistant (Satellite-Based)

An AI-powered flood detection and analysis system that uses Sentinel-1 satellite data and Generative AI (RAG) to provide state-wise flood insights through an interactive web application.

This project demonstrates how remote sensing + vector search + LLMs can be combined to support disaster monitoring and flood-risk analysis.

🛰️ Satellite Used
Sentinel-1 (ESA – Copernicus Programme)

This project uses Sentinel-1 Synthetic Aperture Radar (SAR) satellite imagery for flood detection.

Why Sentinel-1?

🌙 Works day and night

☁️ Penetrates clouds, rain, and storms

🌊 Highly reliable for flood and water-body detection

🛰️ Ideal for disaster monitoring

Usage in this project:

Sentinel-1 SAR imagery is analyzed to identify flooded regions

Flood extent is calculated state-wise

Results are converted into textual flood reports

These reports act as the knowledge base for the Gen-AI system

Data Access:
Satellite data is accessed using the Google Earth Engine API.

🚀 Features

🛰️ Satellite-based flood detection (Sentinel-1)

🗺️ State-wise flood analysis

📦 FAISS vector database for semantic search

🤖 Retrieval-Augmented Generation (RAG)

💬 Natural-language flood Q&A

🌐 Interactive Streamlit web application

🧠 System Workflow

Sentinel-1 Satellite Data → Flood detection using SAR imagery

Flood Report Generation → State-wise summaries

Embeddings Creation → Sentence Transformers

Vector Storage → FAISS database

Retriever → Fetch relevant flood data

Groq LLM (LLaMA-3) → Generate contextual answers

Streamlit UI → Display results to users

🛠️ Tech Stack

Language: Python 3.11

Satellite & Geospatial: Sentinel-1, Google Earth Engine, Geemap

Embeddings: Sentence-Transformers

Vector Database: FAISS

LLM: Groq (LLaMA-3)

Framework: LangChain

Frontend: Streamlit

📂 Project Structure
Flood_AI_Project/
│
├── app.py                  # Streamlit Gen-AI web app
├── flood_by_state.py       # Sentinel-1 flood detection logic
├── flood_rag_store.py      # Vector DB creation
├── flood_vector_db/        # FAISS database
├── requirements.txt
├── .env                    # API keys (ignored in GitHub)
└── README.md

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/Flood_AI_Project.git
cd Flood_AI_Project

2️⃣ Create Virtual Environment (Python 3.11)
python -m venv venv


Activate (Windows):

venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

🔑 Environment Variables

Create a .env file in the root directory:

GROQ_API_KEY=your_groq_api_key_here


⚠️ Do not upload .env to GitHub.

▶️ Run the Application
streamlit run app.py


The application will open automatically in your browser.

🧪 Example Questions

Is Assam under high flood risk?

Compare flood situations in Assam and Kerala

Explain flood severity in simple words

How does satellite data help in flood monitoring?

🎯 Use Cases

Disaster management & early warning systems

Climate and environmental monitoring

Smart city flood analytics

AI-driven decision support systems

⚠️ Notes

Python 3.11 is recommended

Python 3.13+ may cause compatibility issues with Gen-AI libraries

Satellite analysis can be extended for near-real-time updates

📌 Conclusion

This project showcases a real-world Gen-AI application that integrates satellite remote sensing, vector databases, and LLM reasoning to deliver scalable and explainable flood analysis.
