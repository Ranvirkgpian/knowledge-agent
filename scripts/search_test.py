from sentence_transformers import SentenceTransformer
import chromadb

CHROMA_PATH = r"D:\Projects\knowledge-agent\vector_db"

print("Loading embedding model...")

model = SentenceTransformer("BAAI/bge-small-en-v1.5")

print("Loading ChromaDB...")

client = chromadb.PersistentClient(path=CHROMA_PATH)

collection = client.get_collection("meraki_knowledge")

query = "What happens after BPMS triggers Meraki API?"

embedding = model.encode(query).tolist()

results = collection.query(
    query_embeddings=[embedding],
    n_results=3
)

print("\n==============================")
print("QUESTION")
print("==============================")
print(query)

print("\n==============================")
print("TOP RESULTS")
print("==============================")

for i, doc in enumerate(results["documents"][0], start=1):
    print(f"\nResult {i}:")
    print(doc)