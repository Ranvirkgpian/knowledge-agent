from docx import Document
from config import DOCUMENT_PATH


class DocumentParser:
    def __init__(self, document_path=DOCUMENT_PATH):
        self.document_path = document_path

    def load(self):
        """
        Load the Word document and return clean text.
        """

        document = Document(self.document_path)

        paragraphs = []

        for paragraph in document.paragraphs:
            text = paragraph.text.strip()

            if text:
                paragraphs.append(text)

        return "\n".join(paragraphs)