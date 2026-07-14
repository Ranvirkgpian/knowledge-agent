import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

# Project Root
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Data
DATA_DIR = Path(os.getenv("DATA_DIR", PROJECT_ROOT / "data"))
UPLOAD_DIR = DATA_DIR / "uploads"
DOCUMENT_PATH = Path(
    os.getenv(
        "DOCUMENT_PATH",
        DATA_DIR / "Meraki_SDWAN_Fulfillment_Knowledge_Doc.docx",
    )
)

# Vector Database
VECTOR_DB_PATH = Path(os.getenv("VECTOR_DB_PATH", PROJECT_ROOT / "vector_db"))
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "meraki_knowledge")

# Hugging Face Models
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "BAAI/bge-small-en-v1.5")
LLM_PATH = os.getenv("LLM_PATH", r"D:\Programe_Data\models\Qwen2.5-3B-Instruct")

# Retrieval
TOP_K = int(os.getenv("TOP_K", "5"))
HYBRID_CANDIDATES = int(os.getenv("HYBRID_CANDIDATES", "12"))  # per channel before RRF
RRF_K = int(os.getenv("RRF_K", "60"))
RETRIEVAL_MODE = os.getenv("RETRIEVAL_MODE", "hybrid")  # hybrid | dense

# Chunking
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "120"))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "30"))

# Conversation (short-term memory = last N user/assistant turns)
MAX_HISTORY_TURNS = int(os.getenv("MAX_HISTORY_TURNS", "5"))
MAX_NEW_TOKENS = int(os.getenv("MAX_NEW_TOKENS", "220"))
SOURCE_PREVIEW_CHARS = int(os.getenv("SOURCE_PREVIEW_CHARS", "200"))
# Cap each source in the LLM prompt (keeps latency down on 3B models)
MAX_CONTEXT_CHARS_PER_SOURCE = int(os.getenv("MAX_CONTEXT_CHARS_PER_SOURCE", "900"))
MAX_SUGGESTIONS = int(os.getenv("MAX_SUGGESTIONS", "4"))

# Uploads
MAX_UPLOAD_MB = int(os.getenv("MAX_UPLOAD_MB", "15"))
ALLOWED_EXTENSIONS = {".pdf", ".docx", ".txt"}

# CORS
CORS_ORIGINS = [
    origin.strip()
    for origin in os.getenv("CORS_ORIGINS", "*").split(",")
    if origin.strip()
]

# Ensure runtime directories exist
DATA_DIR.mkdir(parents=True, exist_ok=True)
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
VECTOR_DB_PATH.mkdir(parents=True, exist_ok=True)
