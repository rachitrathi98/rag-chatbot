import streamlit as st
import requests

API_URL = "http://localhost:8000"

st.set_page_config(page_title="RAG Chatbot")

st.title("📚 RAG Chatbot (Ollama + Chroma)")

uploaded_file = st.file_uploader("Upload PDF", type="pdf")
if uploaded_file:
    files = {"file": uploaded_file.getvalue()}
    requests.post(f"{API_URL}/upload", files={"file": uploaded_file})
    st.success("PDF uploaded and indexed")

query = st.text_input("Ask a question")

if st.button("Ask") and query:
    response = requests.post(
        f"{API_URL}/chat",
        params={"query": query}
    )
    st.write("🤖:", response.json()["answer"])
