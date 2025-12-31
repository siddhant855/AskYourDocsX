from langchain_community.vectorstores import FAISS
from core.text_splitter import split_text
from core.embedding import embedder

def create_vectorStore(chunks,embeddings):
    vectorStore = FAISS.from_documents(
    documents=chunks,
    embedding=embeddings
    )
    return vectorStore

def save_vector(vectorStore,path='faissIndex'):
    vectorStore.save_local(path)
                    
def load_vectorData(path,embeddings):
    vec = FAISS.load_local(
        path,
        embeddings,
        allow_dangerous_deserialization=True
    )
    return vec