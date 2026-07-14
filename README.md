# 🚀 Meraki SD-WAN Knowledge Agent

> An **offline AI-powered Retrieval-Augmented Generation (RAG) Knowledge Assistant** for Cisco Meraki SD-WAN documentation using **FastAPI, React, ChromaDB, Qwen2.5-3B, and BAAI Embeddings**.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![React](https://img.shields.io/badge/React-Frontend-61DAFB)
![ChromaDB](https://img.shields.io/badge/VectorDB-ChromaDB-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Offline%20AI-success)

---

# 📖 Overview

Meraki SD-WAN Knowledge Agent is an **offline enterprise AI assistant** that answers questions from Cisco Meraki SD-WAN knowledge documents using **Retrieval-Augmented Generation (RAG)**.

Unlike traditional chatbots, every answer is generated from the indexed documents and includes the supporting source chunks, making responses trustworthy and explainable.

---

# ✨ Features

- 🤖 Fully Offline AI Assistant
- 📚 Multi-document Knowledge Base
- 🔍 Hybrid Search (Dense Embeddings + BM25 + RRF)
- 🧠 Local Qwen2.5-3B-Instruct LLM
- 📄 DOCX Knowledge Base Support
- ⚡ ChromaDB Vector Database
- 📑 Expandable Source Citations
- 📊 Confidence Score for Retrieved Chunks
- 🎨 Modern React + Tailwind UI
- 🚀 FastAPI REST API
- 💻 GPU Accelerated (CUDA Supported)

---

# 🏗️ Architecture

```text
                ┌─────────────────────────┐
                │      React Frontend     │
                └────────────┬────────────┘
                             │
                       REST API
                             │
                ┌────────────▼────────────┐
                │      FastAPI Backend    │
                └────────────┬────────────┘
                             │
                ┌────────────▼────────────┐
                │     Hybrid Retrieval    │
                │ Dense + BM25 + RRF      │
                └────────────┬────────────┘
                             │
              ┌──────────────▼──────────────┐
              │        ChromaDB             │
              │      Vector Database        │
              └──────────────┬──────────────┘
                             │
              ┌──────────────▼──────────────┐
              │ BAAI/bge-small-en-v1.5      │
              │     Embedding Model         │
              └──────────────┬──────────────┘
                             │
              ┌──────────────▼──────────────┐
              │   Qwen2.5-3B-Instruct LLM   │
              └─────────────────────────────┘
```

---

# 📂 Project Structure

```text
knowledge-agent/
│
├── backend/
│   ├── app.py
│   ├── rag.py
│   ├── parser.py
│   ├── chunker.py
│   ├── embeddings.py
│   ├── vector_db.py
│   ├── config.py
│   ├── schemas.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── vite.config.js
│
├── data/
│   └── Sample_Document.docx
│
├── scripts/
│   └── build_vector_db.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# 🛠️ Prerequisites

- Python **3.11+**
- Node.js **20+**
- Git
- NVIDIA GPU (Recommended)
- CUDA 12.8 (Optional but recommended)

---

# 🚀 Installation

## 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/knowledge-agent.git

cd knowledge-agent
```

---

## 2. Create Virtual Environment

Windows

```powershell
python -m venv venv

.\venv\Scripts\Activate.ps1
```

Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3. Install Backend Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Install Frontend

```bash
cd frontend

npm install
```

---

# 🤖 Download AI Models

GitHub cannot store large AI models.

Download them separately.

## Qwen2.5-3B-Instruct

```bash
hf download Qwen/Qwen2.5-3B-Instruct --local-dir models/Qwen2.5-3B-Instruct
```

## Embedding Model

```bash
hf download BAAI/bge-small-en-v1.5 --local-dir models/bge-small-en-v1.5
```

---

# ⚙️ Configure Model Paths

Edit

```text
backend/config.py
```

Example

```python
MODEL_PATH = r"models/Qwen2.5-3B-Instruct"

EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"
```

---

# 📄 Add Knowledge Documents

Place your documents inside

```text
data/
```

Example

```text
data/

Meraki_SDWAN_Fulfillment_Knowledge_Doc.docx
```

---

# 🧠 Build the Vector Database

Run

```bash
python scripts/build_vector_db.py
```

This will

- Read the document
- Split it into chunks
- Generate embeddings
- Store vectors in ChromaDB

---

# ▶️ Start Backend

```bash
cd backend

uvicorn app:app --reload
```

Backend API

```
http://127.0.0.1:8000
```

Swagger UI

```
http://127.0.0.1:8000/docs
```

---

# 🌐 Start Frontend

```bash
cd frontend

npm run dev
```

Frontend

```
http://localhost:5173
```

---

# 💬 Example Questions

- Explain the Meraki SD-WAN fulfillment flow.
- What happens after BPMS triggers Meraki API?
- How does TrackCPE work?
- What is InputValidation?
- Explain Provisioning.
- What happens if validation fails?
- Describe the complete order lifecycle.

---

# 📸 Screenshots

## Home Page

> Add screenshot here

---

## Chat Interface

> Add screenshot here

---

## Source Viewer

> Add screenshot here

---

## API Documentation

> Add screenshot here

---

# 🛠️ Tech Stack

### Backend

- Python
- FastAPI
- ChromaDB
- PyTorch
- HuggingFace Transformers
- Sentence Transformers

### Frontend

- React
- Vite
- Tailwind CSS
- Axios
- React Markdown
- Lucide Icons

### AI Models

- Qwen2.5-3B-Instruct
- BAAI/bge-small-en-v1.5

### Retrieval

- Dense Embeddings
- BM25
- Reciprocal Rank Fusion (RRF)

---

# 🔮 Future Improvements

- Multi-document chat
- PDF support
- Streaming responses
- Conversation memory
- Authentication
- Docker deployment
- Dark mode
- Keyword highlighting
- Source navigation
- Multi-user knowledge bases

---

# 🐞 Troubleshooting

### AI model not found

Verify the model path in

```text
backend/config.py
```

---

### ChromaDB empty

Rebuild the vector database

```bash
python scripts/build_vector_db.py
```

---

### Frontend cannot connect

Ensure FastAPI is running

```
http://127.0.0.1:8000
```

---

### CUDA not detected

Run

```bash
python -c "import torch; print(torch.cuda.is_available())"
```

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Ranvir Kumar**

B.Tech Dual Degree | Civil Engineering  
Indian Institute of Technology Kharagpur

GitHub: https://github.com/YOUR_USERNAME

LinkedIn: https://linkedin.com/in/YOUR_PROFILE

---

⭐ If you found this project useful, consider giving it a **Star** on GitHub!
