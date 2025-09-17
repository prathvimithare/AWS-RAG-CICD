import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    GROQ_API_KEY = os.getenv('GROQ_API_KEY')
    OLLAMA_HOST = os.getenv('OLLAMA_HOST')
    VECTOR_DB_PATH = 'vector_db'