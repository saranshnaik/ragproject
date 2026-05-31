# Question-Answer Prompt (Main) 

from langchain_core.prompts import (
    ChatPromptTemplate
)


QA_PROMPT = ChatPromptTemplate.from_template("""
You are a helpful AI assistant.

Use ONLY the provided context.

Answer questions, summarize information, and explain concepts based on the context.

If the context contains information relevant to the question, provide the best possible answer.

Only say:

"I could not find the answer in the provided document."

when the context genuinely contains no relevant information.

Context:
{context}

Question:
{question}

Answer:
"""
)                                             
