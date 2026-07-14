"""Manual script: inspect document sections."""

from services.parser import DocumentParser

parsed = DocumentParser().parse()
print("Source:", parsed.source)
print("Sections:", len(parsed.sections))
print("Chars:", len(parsed.text))
print()
for i, sec in enumerate(parsed.sections, 1):
    print(f"--- Section {i} | heading={sec.heading!r} ---")
    print(sec.text[:300])
    print()
