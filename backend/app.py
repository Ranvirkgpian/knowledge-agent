from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from rag import RAGEngine
from schemas import ChatRequest

print("Starting Meraki Knowledge Agent...")

# Load the RAG engine once when the server starts
rag = RAGEngine()

app = FastAPI(
    title="Meraki SD-WAN Knowledge Agent",
    version="1.0.0",
    description="Offline RAG Knowledge Agent powered by Qwen + ChromaDB"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def health():
    return {
        "status": "running",
        "model": "Qwen2.5-3B-Instruct",
        "database": "ChromaDB"
    }


@app.post("/chat")
def chat(request: ChatRequest):

    answer, results = rag.ask(request.question)

    return {
        "question": request.question,
        "answer": answer,
        "sources": results["documents"][0]
    }