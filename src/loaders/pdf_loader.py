# Load pdfs
"""
OUTPUT:
[
    Document(
        page_content="...",
        metadata={"page":0}
    )
]
"""

from langchain_community.document_loaders import PyPDFLoader


class PDFLoader:

    def __init__(self, file_path):
        self.file_path = file_path


    def load_pdf(self):

        loader = PyPDFLoader(
            self.file_path
        )

        documents = loader.load()

        return documents
