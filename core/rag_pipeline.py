from core.load_data import read_data
from core.text_splitter import split_text
from core.embedding import embedder
from core.vectore_base import (create_vectorStore, save_vector, load_vectorData)
from core.retreiver import retrieve_docs
from core.llm import response

def process_file(file_paths, save_path="faissIndex"):
    all_docs = []

    for f in file_paths:
        docs = read_data(f)  
        all_docs.extend(docs)
    
    
    chunks = split_text(all_docs) 
    embeddings = embedder()
    vs = create_vectorStore(chunks, embeddings)
    save_vector(vs, save_path)
        
    print("Document processed and indexed")
    return all_docs

def ask_question(question, vector_path="faissIndex", k=3):
    embeddings = embedder()
    vs = load_vectorData(vector_path, embeddings)
    chunks = retrieve_docs(vs, question, k)
    return response(chunks, question)