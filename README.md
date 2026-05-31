# RAG-Powered Document Q&A System

A Retrieval-Augmented Generation (RAG) application that enables users to upload PDF documents and ask natural language questions about their contents. The system retrieves relevant document chunks from a vector database and uses a local Large Language Model (LLM) to generate context-aware answers grounded in the source documents.

## Features

* PDF document upload and ingestion
* Automatic text cleaning and chunking
* Embedding generation for semantic search
* Vector storage using ChromaDB
* Context-aware question answering with local LLMs
* Source document retrieval for transparency
* Streamlit-based user interface
* Modular and scalable architecture

## Tech Stack

* Python
* LangChain
* Ollama
* ChromaDB
* Streamlit
* PyPDF
* Sentence Transformers / Embedding Models

## Project Structure

```text
.
├── config
│   ├── retrieval_config.py
│   └── settings.py
│
├── data
│   ├── processed
│   └── raw
│
├── src
│   ├── chains
│   │   └── rag_chain.py
│   ├── embeddings
│   │   └── embedding_model.py
│   ├── ingestion
│   │   └── ingest.py
│   ├── llm
│   │   └── llm_model.py
│   ├── loaders
│   │   └── pdf_loader.py
│   ├── pages
│   │   └── document_chat.py
│   ├── processing
│   │   ├── text_cleaner.py
│   │   └── text_splitter.py
│   ├── prompts
│   │   └── qa_prompt.py
│   ├── retrieval
│   │   └── retriever.py
│   ├── test
│   └── utils
│
├── storage
│   └── chroma
│
├── app.py
├── requirements.txt
└── README.md
```

## System Architecture

```text
PDF Documents
      │
      ▼
 PDF Loader
      │
      ▼
 Text Cleaning
      │
      ▼
 Text Chunking
      │
      ▼
 Embedding Model
      │
      ▼
 ChromaDB Vector Store
      │
      ▼
    Retriever
      │
      ▼
 Retrieved Context
      │
      ▼
   RAG Prompt
      │
      ▼
 Local LLM (Ollama)
      │
      ▼
 Generated Answer
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/saranshnaik/ragproject.git
cd ragproject
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. ## Environment Configuration

Create a `.env` file in the project root:

```env
CHROMA_DIR=storage/chroma

COLLECTION_NAME=documents

DATA_PATH=data/raw

EMBEDDING_MODEL=BAAI/bge-small-en-v1.5

HF_TOKEN=your_huggingface_token

LLM_MODEL=gemma3:4b
```

### Configuration Details

| Variable          | Description                                             |
| ----------------- | ------------------------------------------------------- |
| `CHROMA_DIR`      | Directory where ChromaDB persists vector embeddings     |
| `COLLECTION_NAME` | Name of the Chroma collection used for document storage |
| `DATA_PATH`       | Location of uploaded PDF documents                      |
| `EMBEDDING_MODEL` | Hugging Face embedding model used for semantic search   |
| `HF_TOKEN`        | Hugging Face access token for downloading models        |
| `LLM_MODEL`       | Ollama model used for answer generation                 |

### Download Required Models

Pull the LLM from Ollama:

```bash
ollama pull gemma3:4b
```

The embedding model will be downloaded automatically on first execution.

## Usage

### Launch the Application

```bash
streamlit run app.py
```

### Ingest Documents

1. Upload PDF documents through the Streamlit interface.
2. Documents are processed and converted into vector embeddings.
3. Embeddings are stored in ChromaDB.

### Ask Questions

Once documents are ingested, users can ask questions such as:

```text
What are the key findings of the report?

What optimizer was used?

What eligibility criteria are mentioned in the document?
```

The system retrieves relevant document chunks and generates grounded responses using the local LLM.

## Testing

The project includes test scripts for validating individual components:

* PDF loading
* Text chunking
* Embedding generation
* Vector ingestion
* Retrieval
* RAG pipeline
* Source retrieval
* LLM integration

Run a test script:

```bash
python -m src.test.test_rag
```

## Key Learning Outcomes

* Retrieval-Augmented Generation (RAG)
* Vector Databases and Semantic Search
* Embedding Models
* Local LLM Deployment with Ollama
* LangChain Pipelines
* Prompt Engineering
* Streamlit Application Development

## Future Enhancements

* Multi-document collections
* Conversation memory
* Hybrid retrieval (keyword + semantic search)
* Response reranking
* Support for additional document formats
* User authentication and document management

## License

This project is licensed under the MIT License.
