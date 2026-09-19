from dotenv import load_dotenv
from pydantic import BaseModel
from gemini_client import client, GEMINI_MODEL

load_dotenv()

class Claims(BaseModel):
    claims: list[str]

def extract_claims(message: str) -> Claims:
    prompt = f"""
    Extract the factual claims from the user's message.

    Rules:
    - Return only claims that could be checked against evidence.
    - Split multiple claims into separate items.
    - Do not verify or judge the claims.
    - Do not add information that the user did not state.

    User message:
    {message}
    """

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
        config={
            "response_mime_type": "application/json",
            "response_schema": Claims,
        },
    )

    return response.parsed