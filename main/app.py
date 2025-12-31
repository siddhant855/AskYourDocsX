import sys
import os 

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from core.rag_pipeline import process_file, ask_question
from tempfile import NamedTemporaryFile

st.set_page_config(page_title="AskYourDocs RAG Q&A System", layout="centered")

st.title("AskYourDocs")
st.write("Upload documents and ask questions using an AI-powered RAG system...")

uploaded_files = st.file_uploader(
    "Upload Your Documents(PDF/DOCX/TXT)",
    type=["pdf", "docx", "txt"],
    accept_multiple_files=True
)

if uploaded_files:
    with st.spinner("PROCESSING...."):
        file_paths = []

        for file in uploaded_files:
            filename, ext = os.path.splitext(file.name)
            with NamedTemporaryFile(delete=False, suffix=ext) as tmp:
                tmp.write(file.read())
                file_paths.append(tmp.name)

        
        process_file(file_paths)
    st.success("Document Processed!!!")

question = st.text_input("Ask a question for the uploaded documents: ")

if st.button("Ask"):
    if not question:
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking"):
            answer = ask_question(question)

        st.subheader("Answer")
        st.write(answer)