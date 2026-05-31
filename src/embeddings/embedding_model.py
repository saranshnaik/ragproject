# ML model to generate embeddings

from langchain_huggingface import HuggingFaceEmbeddings

from config.settings import (
    EMBEDDING_MODEL,
    HF_TOKEN
)


class EmbeddingModel:

    @staticmethod
    def load_model():

        embeddings = (
            HuggingFaceEmbeddings(
                model_name=EMBEDDING_MODEL,
                model_kwargs={
                    "device": "cpu",
                    "token": HF_TOKEN
                }
            )
        )

        return embeddings
