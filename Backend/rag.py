from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from vectorstore import get_vectorstore
from memory import load_memory, save_memory

# -----------------------------
# LLM
# -----------------------------
llm = OllamaLLM(
    model="llama3.2",
    base_url="http://localhost:11434"
)

# -----------------------------
# Prompt Template
# -----------------------------
PROMPT = PromptTemplate.from_template("""
You are a helpful assistant answering questions based on provided documents.

Conversation history:
{history}

Context from documents:
{context}

Question:
{question}

Answer clearly and concisely.
If the answer is not in the context, say you do not know.
""")

# -----------------------------
# Helper: format retrieved docs
# -----------------------------
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# -----------------------------
# Helper: format chat history
# -----------------------------
def format_history(history):
    return "\n".join(
        f"User: {h['user']}\nAssistant: {h['bot']}"
        for h in history[-5:]   # last 5 turns
    )

# -----------------------------
# Main RAG function
# -----------------------------
def ask_rag(question: str) -> str:
    # Load vector store
    vectordb = get_vectorstore()
    retriever = vectordb.as_retriever(search_kwargs={"k": 4})

    # Load memory
    history = load_memory()
    history_text = format_history(history)

    # Build LCEL RAG chain
    rag_chain = (
        {
            "context": retriever | format_docs,
            "question": RunnablePassthrough(),
            "history": lambda _: history_text
        }
        | PROMPT
        | llm
        | StrOutputParser()
    )

    # Run chain
    answer = rag_chain.invoke(question)

    # Save to memory
    history.append({
        "user": question,
        "bot": answer
    })
    save_memory(history)

    return answer
