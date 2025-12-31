from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import Docx2txtLoader
from langchain_community.document_loaders import TextLoader
import os

def pdf_loader(file):
    p_loader = PyPDFLoader(file)
    pdf = p_loader.load()
    return pdf
def docx_loader(file):
    d_loader = Docx2txtLoader(file)
    doc = d_loader.load()
    return doc
def text_loader(file):
    t_loader = TextLoader(file)
    text = t_loader.load()
    return text

def read_data(file):
    if file.endswith(".pdf"):
        return pdf_loader(file)
    elif file.endswith(".docx"):
        return docx_loader(file)
    elif file.endswith(".txt"):
        return text_loader(file)
    else:
        raise ValueError("Wrong File Format...")
    
