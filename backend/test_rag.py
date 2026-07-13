from rag import RAGEngine

rag = RAGEngine()

question = "What happens after BPMS triggers Meraki API?"

answer, results = rag.ask(question)

print()

print("=" * 80)

print("QUESTION")

print("=" * 80)

print(question)

print()

print("=" * 80)

print("ANSWER")

print("=" * 80)

print(answer)

print()

print("=" * 80)

print("SOURCES")

print("=" * 80)

for i, doc in enumerate(results["documents"][0], start=1):

    print(f"\nSource {i}\n")

    print(doc[:250])