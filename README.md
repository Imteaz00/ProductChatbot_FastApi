# ProductChatbot_FastAPI

Short, minimal backend for a product-focused chatbot built with FastAPI. Provides HTTP endpoints to query product information and chat with a model (embeddings/LLM integration assumed). Intended as the server component of the ProductChatbot_Fastapi project.

## Features
- FastAPI application
- JSON REST endpoints for chat and product queries
- Ready for local development and containerization

## Prerequisites
- Python 3.10+ (or latest 3.x)
- pip

## Quick setup (local)
1. Open a terminal and go to the server folder:
    cd ProductChatbot_Fastapi/server

2. Install dependencies:
    pip install -r requirements.txt

4. Configure environment:
    - Creat a .env file with your API key:
        echo "GROQ_API_KEY= API KEY" > .env
    - Edit .env and set your API key.

5. Run the development server:
    uvicorn app.main:app --reload
    or
    python -m uvicorn app.main:app --reload

6. Open the API docs:
    - http://127.0.0.1:8000/docs#
