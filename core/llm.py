from langchain_groq import ChatGroq
from dotenv import load_dotenv

def get_llm():
    load_dotenv()
    model = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0
    )
    return model  

def response(chunks, question):
    llm = get_llm()
    context = "\n\n".join(chunks)
    prompt = f"""
You are an expert Assistant. 
Answer the question in a detailed, clear, and exam-ready manner using the context below. 
Your response should be structured in full sentences and cover all important aspects of the topic. 
Where applicable, give examples and explain technical terms in simple language.

Context: {context}

Question: {question}

Answer:
"""
    response = llm.invoke(prompt)
    answer = response.content

    return answer 