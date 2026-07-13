from typing import List


class TextChunker:
    def __init__(self, chunk_size=400, overlap=75):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def split(self, text: str) -> List[str]:

        words = text.split()

        chunks = []

        start = 0

        while start < len(words):

            end = min(start + self.chunk_size, len(words))

            chunk = " ".join(words[start:end])

            chunks.append(chunk)

            if end == len(words):
                break

            start = end - self.overlap

        return chunks