"""Manual script: reindex seed doc and print hybrid search hits with confidence."""

from config import CHUNK_OVERLAP, CHUNK_SIZE
from services.chunker import TextChunker
from services.embeddings import EmbeddingModel
from services.hybrid_search import HybridRetriever
from services.parser import DocumentParser
from services.rag import distance_to_confidence
from services.vector_db import VectorDatabase

print("Loading document...")
parsed = DocumentParser().parse()
chunker = TextChunker(chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP)
chunks = chunker.split_with_metadata(sections=parsed.sections)
print(f"Chunks: {len(chunks)}")

embedder = EmbeddingModel()
texts = [c.text for c in chunks]
embeddings = embedder.encode_batch(texts)

db = VectorDatabase()
print("Resetting collection...")
db.reset()
db.add_documents(
    chunks=texts,
    embeddings=embeddings,
    source=parsed.source,
    headings=[c.heading for c in chunks],
)

hybrid = HybridRetriever()
hybrid.rebuild_from_store(db)
print("Vector + BM25 ready!")

query = "What happens after BPMS triggers Meraki API?"
dense = db.search(embedder.encode(query), top_k=5)
dense_ids = (dense.get("ids") or [[]])[0]
bm25_ids = hybrid.bm25_search(query, top_k=5)
fused = hybrid.fuse(dense_ids, bm25_ids, top_k=5)

print("=" * 80)
print("QUESTION:", query)
print("Dense IDs:", dense_ids[:3])
print("BM25 IDs:", bm25_ids[:3])
print("=" * 80)

docs_by_id = hybrid.get_by_ids([i for i, _ in fused])
for i, (doc_id, score) in enumerate(fused, 1):
    payload = docs_by_id.get(doc_id, {})
    text = (payload.get("document") or "")[:120]
    print(f"\n#{i} RRF={score:.4f} id={doc_id}")
    print(text)
