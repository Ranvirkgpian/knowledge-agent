"""Manual script: inspect chunks from the seed document."""

from config import CHUNK_OVERLAP, CHUNK_SIZE
from services.chunker import TextChunker
from services.parser import DocumentParser

parsed = DocumentParser().parse()
chunker = TextChunker(chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP)
chunks = chunker.split_with_metadata(sections=parsed.sections)

print("=" * 80)
print("TOTAL CHUNKS", len(chunks))
print("=" * 80)

for c in chunks:
    print("=" * 80)
    print(f"Chunk {c.chunk_index} | heading={c.heading!r}")
    print("=" * 80)
    print(c.text[:500])
    print()
