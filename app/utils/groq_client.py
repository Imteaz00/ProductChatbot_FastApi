import os
import httpx
from app.core.config import settings

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {settings.GROQ_API_KEY}",
    "Content-Type": "application/json"
}

async def query_groq_model(prompt: str) -> str:
    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant that answers product-related questions."},
            {"role": "user", "content": prompt}
        ]
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(GROQ_API_URL, headers=HEADERS, json=payload)
        data = response.json()
        print(data)
        try:
            r = data["choices"][0]["message"]["content"].strip()
        except:
            return "Error: Unable to fetch response from Groq API. Token limit might have been exceeded."
        return r
