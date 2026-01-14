from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings

EMBEDDINGS = OllamaEmbeddings(model="nomic-embed-text")
PERSIST_DIR = "../data/vectordb"

def get_vectorstore():
    return Chroma(
        persist_directory=PERSIST_DIR,
        embedding_function=EMBEDDINGS
    )

def add_documents(docs):
    vectordb = get_vectorstore()
    vectordb.add_documents(docs)


