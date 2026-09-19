from dotenv import load_dotenv
from pydantic import BaseModel
from typing import Literal
from google.genai import types
from gemini_client import client, GEMINI_MODEL

load_dotenv()


class EvidenceStrength(BaseModel):
    strength: Literal[
        "strong",
        "moderate",
        "weak",
        "insufficient"
    ]


def assess_evidence_strength(
    claim: str,
    evidence: str,
    classification: str,
    credibility: str
) -> EvidenceStrength:

    prompt = f"""
    Assess the strength of the provided evidence in relation to the claim.

    Strength levels:
    - strong: The evidence directly and clearly addresses the claim,
      and the source has strong credibility.
    - moderate: The evidence meaningfully addresses the claim,
      but has some limitations.
    - weak: The evidence has limited relevance, specificity, or
      source credibility.
    - insufficient: The evidence does not provide enough information
      to meaningfully assess the claim.

    Consider:
    - How directly the evidence addresses the claim
    - How specific the evidence is
    - The source credibility
    - The relationship between the evidence and the claim

    Important:
    - Do not determine the overall truth of the claim.
    - Do not use outside knowledge.
    - Do not change the provided classification.
    - Judge only the strength of this particular evidence item.

    Claim:
    {claim}

    Evidence:
    {evidence}

    Classification:
    {classification}

    Source credibility:
    {credibility}
    """

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=EvidenceStrength,
        ),
    )

    return response.parsed