# RAG Chain

from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from src.retrieval.retriever import VectorRetriever
from src.llm.llm_model import LocalLLM
from src.prompts.qa_prompt import QA_PROMPT


def format_docs(documents):

    return "\n\n".join(
        doc.page_content
        for doc in documents
    )


class RAGChain:

    def __init__(self):
        self.retriever = VectorRetriever().get_retriever()

        self.llm = LocalLLM.load_model()

    
    def build_chain(self):

        chain = (
            {
                "context": self.retriever | format_docs,
                "question": RunnablePassthrough()
            }
            | QA_PROMPT
            | self.llm
            | StrOutputParser()
        )

        return chain


    def get_sources(
        self,
        question
    ):
        
        docs = self.retriever.invoke(question)

        seen_pages = set()
        unique_docs = []

        for doc in docs:

            page = doc.metadata.get("page"), 
                
            if page not in seen_pages:
                seen_pages.add(page)
                unique_docs.append(doc)
            
        return unique_docs
