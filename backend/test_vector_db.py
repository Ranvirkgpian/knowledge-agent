from parser import DocumentParser
from chunker import TextChunker
from embeddings import EmbeddingModel
from vector_db import VectorDatabase
from config import CHUNK_SIZE, CHUNK_OVERLAP

print("Loading document...")

text = DocumentParser().load()

chunker = TextChunker(
    chunk_size=CHUNK_SIZE,
    overlap=CHUNK_OVERLAP
)

chunks = chunker.split(text)

print(f"Chunks : {len(chunks)}")

embedder = EmbeddingModel()

embeddings = embedder.encode_batch(chunks)

db = VectorDatabase()

print("Resetting collection...")

db.reset()

print("Saving vectors...")

db.add_documents(
    chunks,
    embeddings
)

print()

print("Vector Database Ready!")

print()

query = "What happens after BPMS triggers Meraki API?"

query_embedding = embedder.encode(query)

results = db.search(query_embedding)

print("=" * 80)

print("QUESTION")

print("=" * 80)

print(query)

print()

print("=" * 80)

print("RESULTS")

print("=" * 80)

for i, doc in enumerate(results["documents"][0], start=1):

    print(f"\nResult {i}\n")

    print(doc[:400])