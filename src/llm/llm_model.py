# Local Ollama model

from langchain_ollama import OllamaLLM

from config.settings import (
    LLM_MODEL
)

from config.retrieval_config import (
    TEMPERATURE
)


class LocalLLM:


    @staticmethod
    def load_model():

        return OllamaLLM(
            model=LLM_MODEL,
            temperature=TEMPERATURE
        )
