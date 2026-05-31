# Main page (app.py)

import streamlit as st

from src.utils.save_uploaded_files import save_uploaded_path

from src.ingestion.ingest import DocumentIngestion

from src.chains.rag_chain import RAGChain


st.set_page_config(
    page_title="RAG Document Assistant",
    page_icon="📄",
    layout="wide"
)

st.title("📄 RAG Document Assistant")

st.write("Upload a PDF and ask questions.")

if "messages" not in st.session_state:
    st.session_state.messages = []

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if "document_processed" not in st.session_state:
    st.session_state.document_processed = False

if uploaded_file:
    if st.button("Process Document"):
        
        with st.spinner("Processing..."):
            pdf_path = save_uploaded_path(uploaded_file)

            DocumentIngestion().ingest(pdf_path)
        
        st.success("Document processed.")
        st.session_state.document_processed = True


for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

question = st.chat_input(
    "Ask a question..."
)

if "rag" not in st.session_state:
    st.session_state.rag = RAGChain()


if "chain" not in st.session_state:
    st.session_state.chain = st.session_state.rag.build_chain()


if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    answer = st.session_state.chain.invoke(question)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    sources = st.session_state.rag.get_sources(question)
    
    with st.chat_message("assistant"):
        st.markdown(answer)

        with st.expander("Sources"):
            
            for doc in sources:
            
                page = doc.metadata.get("page", "unknown")

                st.markdown(f"**Page {page}**")
                
                st.write(doc.page_content[:500])
