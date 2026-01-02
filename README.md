<img width="1920" height="1080" alt="Screenshot (187)" src="https://github.com/user-attachments/assets/73b7b355-73fa-43f5-b05a-be31139079bb" /><img width="1920" height="1080" alt="Screenshot (185)" src="https://github.com/user-attachments/assets/5a1b9669-6d8f-4df9-ae70-b5b86ff5359d" /># 🌊 Flood Detection & Gen-AI Assistant

Satellite-based flood analysis using Sentinel-1 SAR data and Generative AI (RAG)

An end-to-end project that detects floods using Sentinel-1 satellite imagery, stores flood knowledge in a FAISS vector database, and answers natural-language questions using a Groq-powered LLM, all through a Streamlit web app.

##🛰️ Satellite Used

Satellite: Sentinel-1
Agency: ESA (Copernicus Programme)
Sensor: Synthetic Aperture Radar (SAR)

Why Sentinel-1?

Works day & night

Penetrates clouds, rain, and storms

Highly reliable for flood detection

Widely used for disaster monitoring

How it’s used

SAR imagery is analyzed to detect flooded areas

Flood extent is calculated state-wise

Results are converted into text reports

These reports power the Gen-AI (RAG) system

Data Access: Google Earth Engine API

## Flood Detected Satelite Images

<img width="1920" height="1080" alt="Screenshot (184)" src="https://github.com/user-attachments/assets/96d7a83f-1f01-4182-bcc2-881a17402c70" />
<img width="1920" height="1080" alt="Screenshot (185)" src="https://github.com/user-attachments/assets/724a17dc-825d-44b5-bfb6-f695ef9d42ee" />
<img width="1920" height="1080" alt="Screenshot (186)" src="https://github.com/user-attachments/assets/dc1699f6-944e-4bbf-a360-f62587a59898" />
<img width="1920" height="1080" alt="Screenshot (187)" src="https://github.com/user-attachments/assets/fa96ba2b-ae65-41a2-b346-f8401edd9a54" />

## Code Struture

<img width="1920" height="1080" alt="Screenshot (188)" src="https://github.com/user-attachments/assets/326e3c44-fa51-431d-bd81-4909a229e103" />

## ✨ Features

🛰️ Satellite-based flood detection (Sentinel-1)

🗺️ State-wise flood analysis

📦 FAISS vector database for semantic search

🤖 Retrieval-Augmented Generation (RAG)

💬 Natural-language flood Q&A

🌐 Interactive Streamlit web interface


## Workflow

Sentinel-1 Satellite Data
        ↓
Flood Detection (SAR)
        ↓
State-wise Flood Reports
        ↓
Text Embeddings
        ↓
FAISS Vector Database
        ↓
Retriever
        ↓
Groq LLM (LLaMA-3)
        ↓
Streamlit Web App


## 🛠️ Tech Stack

Language: Python 3.11

Satellite & Geospatial: Sentinel-1, Google Earth Engine, Geemap

Embeddings: Sentence-Transformers

Vector DB: FAISS

LLM: Groq (LLaMA-3)

Framework: LangChain

Frontend: Streamlit

## 📁 Project Structure


Flood_AI_Project/
├── app.py                  # Streamlit Gen-AI app
├── flood_by_state.py       # Sentinel-1 flood detection logic
├── flood_rag_store.py      # Vector DB creation
├── flood_vector_db/        # FAISS database
├── requirements.txt
├── .env                    # API keys (gitignored)
└── README.md


### ⚙️ Installation

git clone https://github.com/your-username/Flood_AI_Project.git
cd Flood_AI_Project
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt


## 🔑 Environment Variables
Create a .env file in the project root

GROQ_API_KEY=your_groq_api_key


## ▶️ Run the Application

streamlit run app.py

## 🧪 Example Queries

Is Assam under high flood risk?

Compare flood situations in Assam and Kerala

Explain flood severity in simple words

How does satellite data help in flood monitoring?


## 🎯 Use Cases

Disaster management & early warning systems

Climate and environmental monitoring

Smart city flood analytics

AI-driven decision support systems


## 📌 Summary
This project demonstrates a real-world integration of satellite remote sensing and Generative AI, showing how Sentinel-1 SAR data + vector search + LLM reasoning can be used to build scalable and explainable flood analysis systems.
