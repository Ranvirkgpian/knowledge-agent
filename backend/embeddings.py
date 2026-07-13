from sentence_transformers import SentenceTransformer
from config import EMBEDDING_MODEL


class EmbeddingModel:

    def __init__(self):
        print("Loading Embedding Model...")
        self.model = SentenceTransformer(EMBEDDING_MODEL)
        print("Embedding Model Loaded!")

    def encode(self, text: str):

        return self.model.encode(
            text,
            normalize_embeddings=True
        ).tolist()

    def encode_batch(self, texts):

        return self.model.encode(
            texts,
            normalize_embeddings=True
        ).tolist()