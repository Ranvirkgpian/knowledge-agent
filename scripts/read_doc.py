from docx import Document

# Path to the knowledge document
DOC_PATH = r"D:\Projects\knowledge-agent\data\Meraki_SDWAN_Fulfillment_Knowledge_Doc.docx"

def read_document(path):
    document = Document(path)

    text = []

    for paragraph in document.paragraphs:
        if paragraph.text.strip():
            text.append(paragraph.text.strip())

    return "\n".join(text)


if __name__ == "__main__":
    content = read_document(DOC_PATH)

    print("=" * 80)
    print("DOCUMENT LOADED SUCCESSFULLY")
    print("=" * 80)

    print(content[:3000])  # Print only the first 3000 characters

    print("\n")
    print("=" * 80)
    print(f"Total Characters: {len(content)}")