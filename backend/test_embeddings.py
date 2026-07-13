from embeddings import EmbeddingModel

model = EmbeddingModel()

embedding = model.encode(
    "What happens after BPMS triggers Meraki API?"
)

print()

print("Embedding Length :", len(embedding))

print()

print("First 10 Values")

print(embedding[:10])