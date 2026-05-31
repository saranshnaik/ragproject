# Ingestion pipeline

import os

from langchain_chroma import Chroma

from src.loaders.pdf_loader import PDFLoader

from src.processing.text_splitter import (
    DocumentSplitter
)

from src.embeddings.embedding_model import (
    EmbeddingModel
)

from config.settings import (
    CHROMA_DIR
)


class DocumentIngestion:

    def __init__(self):
        
        self.embedding_model = (
            EmbeddingModel.load_model()
        )


    def ingest(
        self,
        pdf_path
    ):
        
        print("\nLoading PDF...")

        documents = (
            PDFLoader(
                pdf_path
            ).load_pdf()
        )

        print("Splitting...")

        chunks = (
            DocumentSplitter()
            .split_documents(
                documents
            )
        )

        print("Creating embeddings...")

        Chroma.from_documents(
            documents=chunks,
            embedding=self.embedding_model,
            persist_directory=CHROMA_DIR
        )

        print("Ingestion complete.")
