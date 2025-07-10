from agents.context_miner import ContextMiner
from agents.contradiction_hunter import find_contradictions
from agents.action_planner import plan_action
from agents.persona_shifter import shift_persona
from agents.answer_agent import AnswerAgent

from core.rag_chain import RAGChain
from core.embeder import embed_chunks

# Modified to accept text_content directly instead of a file_path
def run_multiagent_pipeline(text_content: str, persona: str = "HR", question: str = "Whose resume is this?"):
    """
    Runs the multi-agent pipeline on the provided text content.

    Args:
        text_content (str): The combined text content from all uploaded documents.
        persona (str): The chosen persona for the Persona Shifter agent.
        question (str): The user's question.

    Returns:
        dict: A dictionary containing the outputs from all agents (context, contradictions, actions, persona_summary, answer).
    """
    print("🔍 Running AskYourDocsX Multi-Agent System...\n")

    # Step 1: RAG setup
    # The RAGChain is initialized and built with the provided text content.
    # This ensures the AnswerAgent has access to the document's information.
    dummy_emb = embed_chunks(["dummy"])
    dim = dummy_emb.shape[1]
    rag_chain = RAGChain(dimension=dim)
    rag_chain.build_index(text_content)
    answer_agent = AnswerAgent(rag_chain)

    # Step 2: Context + Answer
    # The ContextMiner extracts key context from the entire document text.
    context = ContextMiner().run(text_content)
    print("🧠 Context Miner Output:\n", context, "\n")

    # The AnswerAgent uses the RAGChain to generate an answer to the question.
    print(f"❓ Querying RAG: '{question}'")
    answer = answer_agent.run(question)
    print("🤖 Answer Agent Response:\n", answer, "\n")

    # Step 3: Contradictions — needs both context & answer
    # The Contradiction Hunter identifies any inconsistencies between the answer and the context.
    contradictions = find_contradictions([answer], context) # Pass answer as a list
    print("⚠️ Contradiction Hunter Output:\n", contradictions, "\n")

    # Step 4: Action Planner
    # The Action Planner suggests next steps based on the document's content.
    actions = plan_action(text_content) # Action Planner also needs the full text
    print("📌 Action Planner Output:\n", actions, "\n")

    # Step 5: Persona View
    # The Persona Shifter re-interprets the combined information from a specific persona's viewpoint.
    combined_info = f"Context: {context}\nContradictions: {contradictions}\nActions: {actions}\nAnswer: {answer}"
    persona_summary = shift_persona(combined_info, persona)
    print("🧑‍💼 Persona Shifter Output:\n", persona_summary, "\n")

    # Return all outputs for display in the frontend
    return {
        "context": context,
        "contradictions": contradictions,
        "actions": actions,
        "persona_summary": persona_summary,
        "answer": answer,
    }

if __name__ == "__main__":
    # Example usage for testing (assuming a dummy text file exists or create one)
    # For a real test, ensure 'data/processed_text/SiddhantResume.txt' exists
    # or replace with a string of text.
    dummy_text_for_test = "This is a dummy resume text. John Doe, aspiring LLM engineer. Summary: Experienced in AI."
    # To run this, you might need to create a dummy file or pass a string directly.
    # If you have a file, you can load it like:
    # with open("data/processed_text/SiddhantResume.txt", "r", encoding="utf-8") as f:
    #     test_text = f.read()
    # results = run_multiagent_pipeline(test_text, persona="HR", question="can the person get a machine learning job with this resume?")

    # For demonstration without a file:
    results = run_multiagent_pipeline(
        dummy_text_for_test,
        persona="HR",
        question="Whose resume is this?"
    )
    print("\n--- Full Multi-Agent Results ---")
    for key, value in results.items():
        print(f"{key.capitalize()}:\n{value}\n")
