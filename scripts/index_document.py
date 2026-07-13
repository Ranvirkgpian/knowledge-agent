from docx import Document
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings

DOC_PATH = r"D:\Projects\knowledge-agent\data\Meraki_SDWAN_Fulfillment_Knowledge_Doc.docx"

CHROMA_PATH = r"D:\Projects\knowledge-agent\vector_db"


def read_document(path):
    doc = Document(path)

    paragraphs = []

    for p in doc.paragraphs:
        text = p.text.strip()
        if text:
            paragraphs.append(text)

    return paragraphs


print("Loading embedding model...")

model = SentenceTransformer("BAAI/bge-small-en-v1.5")

print("Loading ChromaDB...")

client = chromadb.PersistentClient(path=CHROMA_PATH)

collection = client.get_or_create_collection(
    name="meraki_knowledge"
)

paragraphs = read_document(DOC_PATH)

print(f"Found {len(paragraphs)} paragraphs")

for i, text in enumerate(paragraphs):

    embedding = model.encode(text).tolist()

    collection.upsert(
        ids=[f"chunk_{i}"],
        documents=[text],
        embeddings=[embedding]
    )

print()

print("===================================")
print("Indexing Complete")
print("===================================")
print(f"Indexed Chunks : {len(paragraphs)}")