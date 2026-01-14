# 📚 RAG Chatbot – Local LLM (Ollama)

A **Retrieval-Augmented Generation (RAG) chatbot** that allows users to query PDF documents using a **fully local Large Language Model (LLM)** powered by **Ollama**.  
The application uses **FastAPI** for the backend, **Streamlit** for the frontend, and **LangChain** for RAG orchestration — with **no external APIs or cloud dependencies**.

---

## ✨ Features

- 📄 Query PDF documents
- ✂️ Intelligent text chunking
- 🧠 Semantic search using vector embeddings
- 🤖 Fully local LLM inference via Ollama
- 💬 Conversational memory
- ⚡ FastAPI backend
- 🖥️ Streamlit frontend
- 🔒 Works fully offline

---


---

## 🛠️ Tech Stack

- **Python 3.10+**
- **FastAPI**
- **Streamlit**
- **LangChain**
- **Ollama (Local LLM)**
- **ChromaDB / FAISS**
- **PyPDF**

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/rag-chatbot.git
## ⚙️ Setup & Installation

### 1️⃣ Create a virtual environment

From the project root directory:

```bash
python -m venv .venv

cd rag-chatbot
python -m venv .venv
source .venv/bin/activate
.venv\Scripts\activate
pip install -r requirements.txt
Install Ollama

Open New Terminal for locally running Ollama

ollama pull llama3
ollama serve (http://localhost:11434)
source .venv/bin/activate
.venv\Scripts\activate
pip install -r requirements.txt

Open New Terminal for Running Backend
cd rag-chatbot
source .venv/bin/activate   # macOS / Linux
# OR
.venv\Scripts\activate      # Windows
cd Backend


python -m uvicorn main:app --reload;  (http://localhost:8000
)

Open New Terminal for Running Frontend

cd rag-chatbot
source .venv/bin/activate   # macOS / Linux
# OR
.venv\Scripts\activate      # Windows
cd Frontend

streamlit run Frontend/app.py (http://localhost:8501
)

For PDfs add in here --> data/pdfs/ they will be automatically indexed if not added from browser




