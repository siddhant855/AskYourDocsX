from ollama import Client
client = Client()

def plan_action(answer):
    prompt = f"""Given the response below, analyze it to identify immediate next steps, 
    potential improvements, and strategic follow-up questions. Translate insights into clear, 
    actionable recommendations that can be implemented in real time. 
    Prioritize suggestions based on impact and feasibility. Where relevant, include timelines, 
    responsible roles, tools or frameworks to apply, and any red flags to monitor

Answer:
{answer}

Plan:
"""
    result = client.chat(model="gemma:2b", messages=[{"role": "user", "content": prompt}])
    return result["message"]["content"]
