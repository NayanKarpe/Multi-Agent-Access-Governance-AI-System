import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def query_llama(prompt):

    payload = {
        "model" : "llama3.2:latest",
        "prompt" : prompt,
        "stream" : False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    return response.json()['response']