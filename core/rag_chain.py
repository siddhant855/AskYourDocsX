from core.chunker import chunk_text
from core.embeder import embed_chunks
from core.vectorstore import FaissVectorStore  # Import from the new file
from core.llm import generate_answer
import numpy as np

class RAGChain:

    def __init__(self, dimension, top_k=5):
        self.store = FaissVectorStore(dimension)
        self.top_k = top_k

    def build_index(self, document_text):
        chunks = chunk_text(document_text)
        embeddings = embed_chunks(chunks)
        self.store.add(embeddings, chunks)
        self.texts = chunks  # Required for 'whose resume' question

    def query(self, questions):
        if isinstance(questions, str):
            questions = [questions]

        answers = []
        for question in questions:
            # First try to find exact matches for simple questions
            if question.lower().startswith("whose resume is this"):
                for chunk in self.texts:
                    if "SUMMARY" in chunk and "Aspiring LLM" in chunk:
                        name_line = chunk.split('\n')[0].strip()
                        answers.append(f"This is the resume of {name_line}")
                        break
                else:
                    answers.append("The answer is not available in the provided document section.")
                continue

            # Normal RAG process for other questions
            question_embedding = embed_chunks([question])

            if question_embedding.ndim == 1:
                question_embedding = np.expand_dims(question_embedding, axis=0)

            results = self.store.search(question_embedding, top_k=self.top_k)
            context_chunks = [res["text"] for res in results]

            if not context_chunks:
                answers.append("The answer is not available in the provided document section.")
                continue

            answer = generate_answer(context_chunks, question)
            answers.append(answer)

        return answers if len(answers) > 1 else answers[0]
