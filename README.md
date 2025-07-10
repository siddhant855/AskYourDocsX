# 🔍 AskYourDocsX

**AskYourDocsX** is an open-source, enterprise-grade GenAI system for intelligent document understanding. It enables users to upload multiple documents (PDF, DOCX, images), ask multiple questions at once, and receive accurate, context-aware answers using lightweight local LLMs and modular agents.

> 🧠 Built for researchers, professionals, and businesses who need deep insights from documents at scale.

---

## 🚀 Features

- 🧠 **Multi-Agent Architecture**  
  Agents like `ContextMiner`, `ContradictionHunter`, `PersonaShifter`, and `ActionPlanner` collaborate to process and reason over documents.

- 📄 **Multi-Document Support**  
  Upload and query multiple PDFs, DOCX, and images in one session.

- 🤖 **Lightweight Local LLMs**  
  Runs on models like `gemma:2b` via [Ollama](https://ollama.com), ensuring fast and private inference.

- 🔍 **Custom RAG Pipeline**  
  Combines semantic chunking, embedding, and vector search (e.g., Pinecone or FAISS) to enhance retrieval.

- 🧭 **Temporal & Organizational Reasoning**  
  Extracts event timelines, hierarchies, contradictions, and decision flows.

- 💻 **Streamlit Frontend**  
  Simple and responsive UI that supports multi-question input and interactive feedback.

---

## 📂 Project Structure

AskYourDocsX/

├── agents/ # Modular agents for reasoning

├── core/ # RAG pipeline, parsing, temporal logic

├── frontend/ # Streamlit interface

├── data/ # Sample documents and output examples

├── requirements.txt

└── README.md


---

## ✅ Use Cases

- Legal document and policy analysis  
- Resume screening and role matching  
- Research paper Q&A  
- Hospital records summarization  

---

## 🛠️ Tech Stack

- Python, LangChain, Streamlit  
- Ollama, FAISS  
- Open-source LLMs: Gemma:2b

---

## 🔮 Future Scope

- OCR and voice input support  
- Domain-specific fine-tuning  
- SaaS dashboard with API access  
- Memory engine for follow-up Q&A

---

## 🤝 Contributing

Contributions, feedback, and PRs are welcome! Please open an issue or submit a pull request.

---

## 🧠 Built With Purpose

AskYourDocsX empowers anyone to turn static documents into dynamic, intelligent conversations.  
**Built for impact. Powered by open-source.**
