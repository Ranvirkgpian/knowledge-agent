"""Manual end-to-end RAG smoke test (loads Qwen — slow / GPU)."""

from schemas import HistoryMessage
from services.rag import RAGEngine

rag = RAGEngine()

question = "What happens after BPMS triggers Meraki API?"
answer, sources, meta = rag.ask(question)

print("=" * 80)
print("QUESTION")
print(question)
print()
print("ANSWER")
print(answer)
print()
print("META", meta.model_dump())
print()
print("SOURCES")
for s in sources:
    print(
        f"  [{s.confidence}%][{s.retrieval}] {s.source} "
        f"chunk#{s.chunk_index}: {s.preview[:100]}..."
    )

follow = "What happens after that?"
history = [
    HistoryMessage(role="user", content=question),
    HistoryMessage(role="assistant", content=answer),
]
answer2, sources2, meta2 = rag.ask(follow, history=history)
print()
print("=" * 80)
print("FOLLOW-UP:", follow)
print(answer2)
print("META", meta2.model_dump())
