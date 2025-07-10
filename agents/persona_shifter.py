from ollama import Client
client = Client()

def shift_persona(answer, persona):
    prompt = f"""Rewrite the following answer in the style, tone, and mindset of a {persona}. 
    Reflect their unique voice, values, priorities, and communication style. Maintain the original meaning,
      but adapt phrasing, structure, and emphasis to match how this persona would genuinely express the content..
    
Answer:
{answer}

Persona-style answer:
"""
    result = client.chat(model="gemma:2b", messages=[{"role": "user", "content": prompt}])
    return result["message"]["content"]
