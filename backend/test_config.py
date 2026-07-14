"""Print active config."""

import config

print("PROJECT_ROOT", config.PROJECT_ROOT)
print("DOCUMENT_PATH", config.DOCUMENT_PATH)
print("VECTOR_DB_PATH", config.VECTOR_DB_PATH)
print("LLM_PATH", config.LLM_PATH)
print("EMBEDDING_MODEL", config.EMBEDDING_MODEL)
print("TOP_K", config.TOP_K)
print("CHUNK_SIZE", config.CHUNK_SIZE)
print("MAX_HISTORY_TURNS", config.MAX_HISTORY_TURNS)
