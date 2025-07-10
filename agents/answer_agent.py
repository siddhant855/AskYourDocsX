from core.rag_chain import RAGChain
from core.embeder import embed_chunks

class AnswerAgent:
    def __init__(self, rag_chain: RAGChain):
        self.rag_chain = rag_chain

    def run(self, question: str):
        # Uses the rag_chain's query() method
        return self.rag_chain.query(question)
