from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

# ✅ LOAD ENV HERE
load_dotenv()

def get_llm():
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError("❌ OPENAI_API_KEY not found. Check your .env file")

    return ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.7,
        openai_api_key=api_key   # ✅ EXPLICIT PASS (IMPORTANT)
    )