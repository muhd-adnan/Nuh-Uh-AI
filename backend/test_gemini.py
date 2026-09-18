from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Explain what an API is in one sentence."
)

print(response.text)