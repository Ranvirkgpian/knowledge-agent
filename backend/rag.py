import torch

from transformers import AutoTokenizer
from transformers import AutoModelForCausalLM

from config import LLM_PATH
from config import TOP_K

from embeddings import EmbeddingModel
from vector_db import VectorDatabase


class RAGEngine:

    def __init__(self):

        print("Loading Embedding Model...")
        self.embedder = EmbeddingModel()

        print("Loading Vector Database...")
        self.db = VectorDatabase()

        print("Loading Qwen Model...")

        self.tokenizer = AutoTokenizer.from_pretrained(
            LLM_PATH
        )

        self.model = AutoModelForCausalLM.from_pretrained(
            LLM_PATH,
            dtype=torch.float16,
            device_map="auto"
        )

        print("RAG Engine Ready!")

    def ask(self, question):

        query_embedding = self.embedder.encode(question)

        results = self.db.search(
            query_embedding,
            top_k=TOP_K
        )

        context = "\n\n".join(results["documents"][0])

        prompt = f"""
You are an expert Cisco Meraki SD-WAN support assistant.

Answer ONLY using the information in the context.

If the answer is not present in the context, reply:

"I don't know based on the provided knowledge document."

Context:

{context}

Question:

{question}

Answer:
"""

        messages = [
            {
                "role": "user",
                "content": prompt
            }
        ]

        text = self.tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True
        )

        inputs = self.tokenizer(
            text,
            return_tensors="pt"
        ).to(self.model.device)

        outputs = self.model.generate(
              **inputs,
        max_new_tokens=250,
        do_sample=False
        )

        generated_tokens = outputs[0][inputs.input_ids.shape[-1]:]

        answer = self.tokenizer.decode(
        generated_tokens,
        skip_special_tokens=True
        ).strip()

        return answer, results