import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain.chat_models import init_chat_model

load_dotenv()

general_llm = init_chat_model(
    model="openai/gpt-oss-20b",
    temperature=0.5,
    model_provider="groq",
    base_url=os.getenv("GROQ_BASE_URL")
)
    

chat_openai = ChatOpenAI(
    model_name="openai/gpt-oss-20b",
    temperature=0.5,
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
    # timeout=60,
    # max_retries=3,
    # max_tokens=2048,
)

chat_groq = ChatGroq(
    model_name="openai/gpt-oss-20b",
    temperature=0.5,
)