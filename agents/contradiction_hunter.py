from ollama import Client
client = Client()

def find_contradictions(answer, context):
    prompt = f"""Review the following answer against the provided context to detect any contradictions, 
    inconsistencies, or logical fallacies. Flag discrepancies clearly and explain why they are contradictory, 
    referencing specific elements from the context. Recommend how to resolve or reframe the contradictions for clarity,
     accuracy, and alignment with the original context.

Context:
{context}

Answer:
{answer}

List any contradictions or write 'None':"""
    result = client.chat(model="gemma:2b", messages=[{"role": "user", "content": prompt}])
    return result["message"]["content"]
