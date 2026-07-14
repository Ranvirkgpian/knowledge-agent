"""Manual script: encode a sample string."""

from services.embeddings import EmbeddingModel

model = EmbeddingModel()
vec = model.encode("What happens after BPMS triggers Meraki API?")
print("dims:", len(vec))
print("first 5:", vec[:5])
