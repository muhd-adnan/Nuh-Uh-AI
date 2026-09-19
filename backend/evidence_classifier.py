from dotenv import load_dotenv
from pydantic import BaseModel
from typing import Literal
from google.genai import types
from gemini_client import client, GEMINI_MODEL

load_dotenv()


class Classification(BaseModel):
    classification: Literal[
        "supports",
        "contradicts",
        "neutral"
    ]


def classify_evidence(
    claim: str,
    evidence: str
) -> Classification:

    prompt = f"""
    Determine how the evidence relates to the claim.

    Classification options:
    - supports: The evidence provides information that supports the claim.
    - contradicts: The evidence provides information that conflicts with the claim.
    - neutral: The evidence does not meaningfully support or contradict the claim.

    Rules:
    - Judge only the relationship between the claim and the provided evidence.
    - Do not use outside knowledge.
    - Do not determine the overall truth of the claim.
    - Return exactly one classification.

    Claim:
    {claim}

    Evidence:
    {evidence}
    """

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=Classification,
        ),
    )

    return response.parsed