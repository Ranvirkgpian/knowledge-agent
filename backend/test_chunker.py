from parser import DocumentParser
from chunker import TextChunker

parser = DocumentParser()

text = parser.load()

from config import CHUNK_SIZE, CHUNK_OVERLAP

chunker = TextChunker(
    chunk_size=CHUNK_SIZE,
    overlap=CHUNK_OVERLAP
)

chunks = chunker.split(text)

print("=" * 80)
print("TOTAL CHUNKS")
print("=" * 80)

print(len(chunks))

print("\n")

for i, chunk in enumerate(chunks, start=1):
    print("=" * 80)
    print(f"Chunk {i}")
    print("=" * 80)
    print(chunk[:500])
    print()