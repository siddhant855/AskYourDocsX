import os
import re
import PyPDF2  # Updated from fitz to PyPDF2
from docx import Document

def extract_pdf(path):
    text = ""
    with open(path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() or ""  # fallback if None
    return text.strip()

def extract_doc(path):
    doc = Document(path)
    return "\n".join([para.text for para in doc.paragraphs]).strip()

def save_text(text, filename):
    os.makedirs("data/processed_text", exist_ok=True)  # Ensure the directory exists
    with open(f"data/processed_text/{filename}.txt", "w", encoding="utf-8") as f:
        f.write(text)

def parse_file(filepath):
    if filepath.endswith(".pdf"):
        text = extract_pdf(filepath)
    elif filepath.endswith(".txt"):
        return open(filepath, "r", encoding="utf-8").read()
    elif filepath.endswith(".docx"):
        text = extract_doc(filepath)
    else:
        raise ValueError("Unsupported file type.")
    
    filename = os.path.splitext(os.path.basename(filepath))[0]
    save_text(text, filename)
    print(f"[✓] Extracted and saved: {filepath}")
    return text
