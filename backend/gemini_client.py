import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

GEMINI_MODEL = os.getenv(
    "GEMINI_MODEL",
    "gemini-3.6-flash"
)

client = genai.Client()