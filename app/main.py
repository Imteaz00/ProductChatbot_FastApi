from fastapi import FastAPI
from app.api.routes_chatbot import router as chatbot_router

app = FastAPI(title="Product Chatbot API")

@app.get("/")
async def root():
    return {"message": "Welcome to the Product Chatbot API. Visit /docs for Swagger UI."}

app.include_router(chatbot_router, prefix="/api")
