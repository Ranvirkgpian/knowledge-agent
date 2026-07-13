from pathlib import Path

# Project Root
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Data
DATA_DIR = PROJECT_ROOT / "data"
DOCUMENT_PATH = DATA_DIR / "Meraki_SDWAN_Fulfillment_Knowledge_Doc.docx"

# Vector Database
VECTOR_DB_PATH = PROJECT_ROOT / "vector_db"

# Hugging Face Models
EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"

LLM_PATH = r"D:\Programe_Data\models\Qwen2.5-3B-Instruct"

# Retrieval
TOP_K = 5

# Chunking
CHUNK_SIZE = 120
CHUNK_OVERLAP = 30