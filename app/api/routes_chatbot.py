from fastapi import APIRouter
from app.models.schemas import ChatRequest, ChatResponse
from app.services.chatbot_service import process_chat
from app.services.product_service import get_all_products

router = APIRouter()

@router.get("/products")
async def fetch_products():
    return await get_all_products()

@router.post("/chat", response_model=ChatResponse)
async def chat_with_bot(request: ChatRequest):
    response_text = await process_chat(request.message)
    return ChatResponse(response=response_text)
