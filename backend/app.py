from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.deps import set_rag_engine
from api.routes import router
from config import CORS_ORIGINS
from services.rag import RAGEngine


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting Meraki Knowledge Agent...")
    engine = RAGEngine()
    set_rag_engine(engine)
    app.state.rag = engine
    yield
    print("Shutting down Meraki Knowledge Agent...")


app = FastAPI(
    title="Meraki SD-WAN Knowledge Agent",
    version="2.0.0",
    description="Offline RAG Knowledge Agent powered by Qwen + ChromaDB",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS if CORS_ORIGINS != ["*"] else ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
