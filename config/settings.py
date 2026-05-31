from dotenv import load_dotenv
import os

load_dotenv()


BASE_DIR=os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

EMBEDDING_MODEL=os.getenv(
    "EMBEDDING_MODEL"
)

LLM_MODEL=os.getenv(
    "LLM_MODEL"
)

CHROMA_DIR=os.getenv(
    "CHROMA_DIR"
)

DATA_PATH=os.getenv(
    "DATA_PATH"
)
