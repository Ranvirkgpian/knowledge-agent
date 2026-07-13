import chromadb
from config import VECTOR_DB_PATH


class VectorDatabase:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path=str(VECTOR_DB_PATH)
        )

        self.collection = self.client.get_or_create_collection(
            name="meraki_knowledge"
        )

    def reset(self):

        try:
            self.client.delete_collection("meraki_knowledge")
        except:
            pass

        self.collection = self.client.get_or_create_collection(
            name="meraki_knowledge"
        )

    def add_documents(self, chunks, embeddings):

        ids = []

        metadatas = []

        for i in range(len(chunks)):
            ids.append(f"chunk_{i}")

            metadatas.append({
                "chunk": i,
                "source": "Meraki_SDWAN_Fulfillment_Knowledge_Doc.docx"
            })

        self.collection.add(
            ids=ids,
            documents=chunks,
            embeddings=embeddings,
            metadatas=metadatas
        )

    def search(self, embedding, top_k=5):

        return self.collection.query(
            query_embeddings=[embedding],
            n_results=top_k
        )