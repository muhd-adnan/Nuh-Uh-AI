from dotenv import load_dotenv
from pydantic import BaseModel
from google.genai import types
from gemini_client import client, GEMINI_MODEL

load_dotenv()


class Evidence(BaseModel):
    evidence: str


def extract_evidence(claim: str, content: str) -> Evidence:
    content = content[:10000]

    print("Sending request to Gemini...")

    prompt = f"""
    Identify the evidence in the source text that is relevant to the claim.

    Rules:
    - Extract only information from the provided source text.
    - Do not add outside knowledge.
    - Do not decide whether the claim is true or false.
    - If the source contains no relevant evidence, return an empty string.
    - Keep the evidence concise.

    Claim:
    {claim}

    Source text:
    {content}
    """

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=Evidence,
        ),
    )

    print("Gemini response received.")

    return response.parsed