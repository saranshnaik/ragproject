# Load existing chroma db

from langchain_chroma import Chroma

from src.embeddings.embedding_model import (
    EmbeddingModel
)

from config.settings import (
    CHROMA_DIR,
    COLLECTION_NAME
)

from config.retrieval_config import (
    TOP_K,
    SEARCH_TYPE
)


class VectorRetriever:


    def __init__(self):
        self.embeddings = EmbeddingModel.load_model()
        
        self.vectorstore = Chroma(
            collection_name=COLLECTION_NAME,
            persist_directory=CHROMA_DIR,
            embedding_function=self.embeddings
        )


    def get_retriever(self):

        return self.vectorstore.as_retriever(
            search_type=SEARCH_TYPE,
            search_kwargs={
                "k": TOP_K,
                "fetch_k": 20,
            }
        )
