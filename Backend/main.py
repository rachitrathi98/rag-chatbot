import shutil
from fastapi import FastAPI, UploadFile, File
from pdf_loader import load_pdf
from vectorstore import add_documents
from rag import ask_rag
from text_splitter import split_docs

app = FastAPI()

@app.get("/")
def health():
    return {"status": "Backend running"}

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    path = f"../data/pdfs/{file.filename}"
    with open(path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    docs = load_pdf(path)
    chunks = split_docs(docs)
    add_documents(chunks)

    return {"status": "PDF indexed successfully"}

@app.post("/chat")
async def chat(query: str):
    answer = ask_rag(query)
    return {"answer": answer}
