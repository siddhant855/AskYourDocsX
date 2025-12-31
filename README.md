
---
## 💼 Portfolio Project Overview

**AskYourDocs** is a comprehensive portfolio project demonstrating my ability to design, build, and deploy production-ready AI applications using modern LLM and RAG (Retrieval-Augmented Generation) architectures.

The project focuses on transforming unstructured documents into an interactive knowledge base that can be queried using natural language.

---

### 🎯 Project Goals

This project was built to showcase:

1. **RAG Architecture Mastery**  
   End-to-end implementation of Retrieval-Augmented Generation from document ingestion to answer generation.

2. **LLM Integration**  
   Practical experience integrating high-performance LLM APIs for real-time inference.

3. **Production Deployment**  
   Deploying an AI application to cloud infrastructure with proper environment and dependency management.

4. **Full-Stack AI Development**  
   Designing both backend AI pipelines and an intuitive frontend user experience.

5. **Clean Code & Engineering Practices**  
   Modular, readable, and maintainable code with clear separation of concerns.

---

### 🛠️ Technical Skills Demonstrated

#### AI / ML Technologies
- **Large Language Models (LLMs)**: Integrated Groq LLM API for fast, low-latency inference  
- **Vector Databases**: Implemented FAISS for efficient semantic similarity search  
- **Embeddings**: Used HuggingFace sentence-transformers for document vectorization  
- **RAG Pipeline**: Designed a complete retrieval-augmented generation workflow  

#### Software Engineering
- **Python Development**: Modular, well-structured Python codebase  
- **Framework Integration**: LangChain used for orchestration of document loading, retrieval, and generation  
- **Document Processing**: Robust multi-format parsing (PDF, DOCX, TXT)  
- **UI / UX**: Built a clean, responsive Streamlit interface for document upload and Q&A  

#### DevOps & Deployment
- **Cloud Deployment**: Deployed as a live demo on Hugging Face Spaces  
- **Environment Management**: Secure use of environment variables for API keys  
- **Dependency Management**: Explicit versioned dependencies via `requirements.txt`  
- **Version Control**: Git best practices with clean commit history and `.gitignore` hygiene  

#### System Design
- **Chunking Strategy**: Recursive character-based splitting (500 characters, 100 overlap) for optimal retrieval  
- **Performance Awareness**: Designed to minimize recomputation and unnecessary model loading  
- **Error Handling**: Clear user feedback for invalid input and processing errors  
- **Scalability Mindset**: Architecture structured to support future extensions and higher usage  

---

### 📊 Key Technical Decisions

| Decision | Rationale |
|--------|-----------|
| **Groq LLM** | Selected for extremely fast inference compared to traditional LLM providers |
| **FAISS Vector Store** | Lightweight, efficient semantic search without external DB dependencies |
| **Streamlit UI** | Rapid development with Python-native UI framework |
| **LangChain** | Industry-standard orchestration for RAG workflows |
| **Sentence-Transformers** | Open-source embeddings with strong semantic performance |

---

### 🔬 Implementation Highlights

#### 1. Document Processing Pipeline
Upload → Parse → Chunk → Embed → Store → Retrieve → Generate


- Supports multiple document formats in a single session (PDF, DOCX, TXT)  
- Uses recursive text splitting to preserve semantic coherence across chunks  
- Maintains document context to improve answer accuracy  

---

#### 2. Semantic Search & Retrieval
- Dense vector embeddings generated using HuggingFace sentence-transformers  
- FAISS index enables fast similarity search over document chunks  
- Retrieves top-K most relevant chunks (K = 3) for each query  

---

#### 3. Response Generation (Portfolio Configuration)
- Uses a **server-managed API key** for LLM inference  
- All API calls are executed securely on the backend; the key is never exposed to users  
- Custom prompt ensures answers are grounded strictly in retrieved context  
- Designed as a **rate-limited demo** suitable for portfolio review and recruiter evaluation  

> ⚠️ This project intentionally uses a shared, server-side API key for demonstration purposes.  
> The architecture can be easily extended to a Bring-Your-Own-Key (BYOK) or hybrid model if required in a production environment.

---

### 📈 Performance Characteristics

- **Typical Response Time**: ~3–5 seconds for standard queries  
- **Supported Input**: Multiple documents per session  
- **Retrieval Speed**: Sub-second FAISS similarity search  
- **Deployment Target**: CPU-based cloud environment (Hugging Face Spaces)  

---

### 🎓 Learning Outcomes

Through this project, I gained hands-on experience with:

- ✅ Designing and implementing RAG pipelines  
- ✅ Vector embeddings and semantic search  
- ✅ Integrating and prompting LLM APIs  
- ✅ Deploying AI applications to the cloud  
- ✅ Managing secrets and environment variables securely  
- ✅ Building user-friendly interfaces for AI systems  

---

### 🚀 Future Enhancements

Planned improvements to extend functionality and demonstrate additional skills:

- [ ] Conversational memory for multi-turn Q&A  
- [ ] Advanced chunking strategies (semantic / adaptive chunking)  
- [ ] Metadata-aware retrieval and source attribution  
- [ ] REST API for programmatic access  
- [ ] Authentication and per-user usage limits  
- [ ] Dockerized deployment  
- [ ] Automated testing and CI/CD pipeline  

---

### ⚠️ Demo Usage Note

This is a **portfolio demonstration project**.

The live deployment uses a **shared, rate-limited API key** managed securely on the server side.  
Users are not required to provide their own API keys.

For extended usage or production deployment:
1. Clone this repository  
2. Configure your own API key via environment variables  
3. Deploy to your preferred platform  


---

## 📫 Connect With Me

I'm actively seeking opportunities in **AI/ML Engineering**, **LLM Applications**, and **Full-Stack AI Development**.

- **LinkedIn**: linkedin.com/in/siddhant-thete
- **Email**: siddhant.v.thete855@gmail.com

**Interested in discussing this project or potential opportunities?** Feel free to reach out!

---

