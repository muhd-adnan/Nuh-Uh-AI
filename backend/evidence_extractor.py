from urllib import response

from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel
from google.genai import types

load_dotenv()

client = genai.Client()


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
        model="gemini-3.8-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=Evidence,
        ),
    )

    print("Gemini response received.")

    return response.parsed

if __name__ == "__main__":

    claim = "The Earth is flat"

    content = """
    Earth is a roughly spherical planet. Its shape explains
    seasons, changes in weather, and many other natural phenomena.
    """

    result = extract_evidence(claim, content)

    print(result)
    print(result.evidence)