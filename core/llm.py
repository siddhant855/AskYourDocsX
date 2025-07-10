from ollama import Client

client = Client()

def generate_answer(context_chunks, question):
    context_text = "\n\n---\n\n".join(context_chunks)

    prompt = f"""
You are an expert Assistant.

Answer the question in a detailed, clear, and exam-ready manner using the context below. 
Your response should be structured in full sentences and cover all important aspects of the topic. 
Where applicable, give examples and explain technical terms in simple language.

Context:
{context_text}

Question: {question}
Answer:
"""

    response = client.chat(
        model="gemma:2b",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['message']['content']
