from parser import DocumentParser

parser = DocumentParser()

text = parser.load()

print("=" * 80)
print("DOCUMENT LOADED")
print("=" * 80)

print(text[:1500])

print("\n")
print("=" * 80)
print("Characters :", len(text))