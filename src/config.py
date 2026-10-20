"""Configuration: loads API key and creates the Gemini model."""
import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

MODEL_NAME = "gemini-3.8-flash" 


def get_llm() -> ChatGoogleGenerativeAI:
    if not os.getenv("GOOGLE_API_KEY"):
        raise RuntimeError(
            "GOOGLE_API_KEY not found. Copy .env.example to .env and add your key."
        )
    return ChatGoogleGenerativeAI(model=MODEL_NAME, temperature=0)
