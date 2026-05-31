# Text splitter utility (chunking)

from langchain_text_splitters import RecursiveCharacterTextSplitter

from config.retrieval_config import (
    CHUNK_SIZE,
    CHUNK_OVERLAP
)


class DocumentSplitter:

    def __init__(self):
        
        self.splitter = (
            RecursiveCharacterTextSplitter(
                chunk_size=CHUNK_SIZE,
                chunk_overlap=CHUNK_OVERLAP,
                separators=[
                    "\n\n",
                    "\n",
                    ".",
                    " ",
                    ""
                ]
            )
        )

    
    def split_documents(
        self,
        documents
    ):
        
        split_docs = (
            self.splitter.split_documents(
                documents
            )
        )

        return split_docs
