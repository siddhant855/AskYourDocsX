import streamlit as st
import os
import sys
import traceback

# Add the parent directory to Python path BEFORE importing custom modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now import the custom modules
from core.pdfreader import parse_file
from core.imagereader import save_image_text
from core.rag_chain import RAGChain
# The following imports are kept for completeness, though some might be indirectly used via run_multiagent_pipeline
from core.llm import generate_answer
from core.chunker import chunk_text
from core.embeder import embed_chunks
from core.vectorstore import FaissVectorStore
from agents.action_planner import plan_action
from agents.answer_agent import AnswerAgent
from agents.context_miner import ContextMiner
from agents.contradiction_hunter import find_contradictions
from agents.persona_shifter import shift_persona
from run_multiagent import run_multiagent_pipeline # Import the updated pipeline function

# --- Streamlit Page Configuration ---
st.set_page_config(page_title="AskYourDocsX", layout="wide", initial_sidebar_state="auto")

# --- Initialize Session State ---
# 'history' stores past questions and their multi-agent responses
if "history" not in st.session_state:
    st.session_state.history = []
# 'uploaded_texts' stores metadata and preview of uploaded documents
if "uploaded_texts" not in st.session_state:
    st.session_state.uploaded_texts = []
# 'all_document_text' stores the combined raw text content of all uploaded documents
if "all_document_text" not in st.session_state:
    st.session_state.all_document_text = ""
# 'rag_chain_initialized' helps prevent re-initializing RAGChain unnecessarily
if "rag_chain_initialized" not in st.session_state:
    st.session_state.rag_chain_initialized = False

# Initialize RAGChain only once
if not st.session_state.rag_chain_initialized:
    # Dimension 384 is common for sentence-transformers models like all-MiniLM-L6-v2
    st.session_state.rag = RAGChain(dimension=384, top_k=5)
    st.session_state.rag_chain_initialized = True

# --- Header Section ---
st.title("📄 AskYourDocsX")
st.caption("A multi-agent GenAI document cognition system that answers your questions from uploaded documents.")

# --- File Uploader Section ---
st.markdown("### 📂 Upload Documents")
upload_files = st.file_uploader(
    "Upload your documents (PDF, DOCX, or Images). Multiple files are supported.",
    type=["pdf", "docx", "png", "jpg", "jpeg"],
    accept_multiple_files=True,
    key="file_uploader" # Added a key for consistent behavior
)

# Process uploaded files
if upload_files:
    current_uploaded_files = {f["name"] for f in st.session_state.uploaded_texts}
    new_files_uploaded = False
    temp_all_text = ""

    # Check if new files are added or existing ones are re-uploaded
    for uploaded_file in upload_files:
        existing_file = next((item for item in st.session_state.uploaded_texts if item["name"] == uploaded_file.name), None)
        if uploaded_file.name not in current_uploaded_files or (existing_file and len(uploaded_file.getvalue()) != existing_file.get("size")):
            new_files_uploaded = True
            break

    if new_files_uploaded:
        st.session_state.uploaded_texts = [] # Clear previous uploads if new files detected
        st.session_state.all_document_text = "" # Reset combined text
        with st.spinner("Parsing and indexing documents... This may take a moment."):
            for file in upload_files:
                file_text = ""
                try:
                    # Check file extension and MIME types for parsing
                    if file.name.endswith('.pdf') or file.type == "application/pdf":
                        # Create a temporary file to save the uploaded content
                        import tempfile
                        with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_file:
                            temp_file.write(file.getvalue())
                            temp_path = temp_file.name
                        
                        file_text = parse_file(temp_path)
                        os.unlink(temp_path)  # Clean up temp file
                        
                    elif file.name.endswith(('.docx', '.doc')) or file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                        # Create a temporary file to save the uploaded content
                        import tempfile
                        with tempfile.NamedTemporaryFile(delete=False, suffix='.docx') as temp_file:
                            temp_file.write(file.getvalue())
                            temp_path = temp_file.name
                        
                        file_text = parse_file(temp_path)
                        os.unlink(temp_path)  # Clean up temp file
                        
                    elif file.type in ["image/jpeg", "image/png"] or file.name.lower().endswith(('.png', '.jpg', '.jpeg')):
                        file_text = save_image_text(file)
                    else:
                        st.warning(f"Unsupported file type: {file.type} for {file.name}. Skipping.")
                        continue
                except Exception as e:
                    st.error(f"Error processing file {file.name}: {str(e)}")
                    continue

                if file_text:
                    temp_all_text += file_text + "\n" # Accumulate text
                    st.session_state.uploaded_texts.append({
                        "name": file.name,
                        "size": len(file.getvalue()),
                        "preview": file_text[:300] + ("..." if len(file_text) > 300 else ""),
                        "type": file.type
                    })
            st.session_state.all_document_text = temp_all_text.strip() # Store combined text
            # Build RAG index with the combined text
            if st.session_state.all_document_text:
                st.session_state.rag.build_index(st.session_state.all_document_text)
                st.success("✅ Documents indexed and ready to answer questions.")
            else:
                st.warning("No text extracted from uploaded documents. Please ensure documents contain readable text.")
    else:
        st.info("Files already processed. Upload new files or clear cache to re-process.")


# Display summaries of uploaded documents
if st.session_state.uploaded_texts:
    with st.expander("📝 Uploaded Document Summaries"):
        for doc in st.session_state.uploaded_texts:
            st.markdown(f"**📄 {doc['name']}** ({doc['size'] // 1024} KB)")
            st.code(doc["preview"], language="text")

# --- Question Answering Section ---
st.markdown("## 💬 Ask Questions")

# Input for the question
question = st.text_input("Type your question here...", key="question_input")

# Dropdown for choosing an Agent Persona
persona = st.selectbox(
    "🤖 Choose an Agent Persona:",
    [
        "Legal Advisor",
        "General Assistant",
        "Medical Expert",
        "Finance Analyst",
        "Bullet Point Summarizer",
        "Tutor"
    ],
    key="persona_select"
)

# ASK button
if st.button("ASK", key="ask_button"):
    if not st.session_state.all_document_text:
        st.warning("Please upload and process documents first before asking a question.")
    elif not question.strip():
        st.warning("Please enter a question to get an answer!")
    else:
        with st.spinner("🤖 Running multi-agent analysis..."):
            try:
                # Call the updated run_multiagent_pipeline with the combined text
                results = run_multiagent_pipeline(
                    text_content=st.session_state.all_document_text,
                    persona=persona,
                    question=question
                )
                # Append the question and all results to history
                st.session_state.history.append({"question": question, "results": results})
            except Exception as e:
                st.error(f"❌ An error occurred during analysis: {e}")
                st.info("Please ensure your backend agents and core modules are correctly set up and accessible.")

# --- Display Chat History and Agent Outputs ---
st.markdown("---")
st.markdown("## 📜 Conversation History")

if not st.session_state.history:
    st.info("Your conversation history will appear here once you ask a question.")
else:
    # Display history in reverse chronological order (most recent first)
    for entry in reversed(st.session_state.history):
        st.markdown(f"**❓ You asked:** {entry['question']}")

        if 'results' in entry and entry['results']:
            results = entry['results']
            st.markdown(f"**🤖 Answer:** {results.get('answer', 'No answer generated.')}")

            # Use Streamlit tabs for organized display of agent outputs
            tab1, tab2, tab3, tab4 = st.tabs(
                ["🧠 Context", "⚠️ Contradictions", "📌 Action Plan", "🧑‍💼 Persona View"]
            )

            with tab1:
                st.markdown("### Context Miner Output")
                st.info(results.get('context', 'No context found.'))

            with tab2:
                st.markdown("### Contradiction Hunter Output")
                st.warning(results.get('contradictions', 'No contradictions found.'))

            with tab3:
                st.markdown("### Action Planner Output")
                st.success(results.get('actions', 'No action plan generated.'))

            with tab4:
                st.markdown("### Persona Shifter Output")
                st.write(f"**Persona: {persona}**") # Display the persona used for this entry
                st.markdown(results.get('persona_summary', 'No persona summary generated.'))
        else:
            st.error("No results found for this query.")
        st.markdown("---") # Separator for each conversation turn