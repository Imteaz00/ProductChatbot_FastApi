from app.services.product_service import get_products_by_names, get_all_products
from app.utils.groq_client import query_groq_model
import json


async def extract_product_and_intent(message: str) -> dict:
    """Uses Groq to determine the most relevant product and user intent from the message."""
    
    all_products = await get_all_products()
    product_titles = [[product['title'], product['category'], product['price'], product['discountPercentage'], product['rating'], product['stock']] for product in all_products]

    product_list_str = json.dumps(product_titles, indent=2)

    prompt = f"""
You are an intelligent assistant. Your job is to help identify which product the user is referring to, and what their intent is.

Here is the customer's message:
"{message}"

Here is a list of available products with their details:
{product_list_str}

From this message, determine the relevant product names and what the user want to know. If you cannot determine the product or intent, return null for that field.

Respond ONLY in this JSON format:
{{"product": [<all the exact product name from the list>], "intent": "<user's intent>"}}
"""

    response = await query_groq_model(prompt)

    try:
        data = json.loads(response)
        return {"product": data.get("product"), "intent": data.get("intent")}
    except Exception:
        return {"product": None, "intent": None}



async def process_chat(message: str) -> str:
    extracted = await extract_product_and_intent(message)
    product_name = extracted.get("product")
    intent = extracted.get("intent")

    if not intent:
        return "Sorry, I couldn't understand your request. Can you please rephrase it?"

    if not product_name:
        return f"Sorry, I don't have any information on this product/s."
    
    product = await get_products_by_names(product_name)

    product_json = json.dumps(product, indent=2)
    final_prompt = f"""
You are a helpful AI assistant. The users intent for question {intent}.

Here is the product information:
{product_json}

Write a helpful, human-like, and informative response.
"""

    final_response = await query_groq_model(final_prompt)
    return final_response
