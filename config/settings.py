from dotenv import load_dotenv
import os

load_dotenv()


BASE_DIR=os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

CHROMA_DIR = os.getenv(
    "CHROMA_DIR"
)

COLLECTION_NAME = os.getenv(
    "COLLECTION_NAME",
    "documents"
)

DATA_PATH = os.getenv(
    "DATA_PATH",
    "data/raw"
)

EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL"
)

HF_TOKEN = os.getenv(
    "HF_TOKEN"
)

LLM_MODEL = os.getenv(
    "LLM_MODEL",
    "gemma3:4b"
)
