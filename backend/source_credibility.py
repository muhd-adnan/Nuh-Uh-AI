from dotenv import load_dotenv
from pydantic import BaseModel
from typing import Literal
from google.genai import types
from gemini_client import client, GEMINI_MODEL

load_dotenv()


class Credibility(BaseModel):
    credibility: Literal[
        "high",
        "medium",
        "low",
        "unknown"
    ]


def assess_source_credibility(
    title: str,
    url: str,
    content: str
) -> Credibility:

    prompt = f"""
    Assess the credibility of the source based only on the information provided.

    Credibility levels:
    - high: The source appears to be from a highly authoritative or well-established institution.
    - medium: The source appears reasonably trustworthy but has limitations.
    - low: The source has significant credibility concerns.
    - unknown: There is not enough information to determine credibility.

    Consider:
    - Source type and domain
    - Author or organization
    - Citations or references
    - Whether the source appears authoritative
    - Whether the information appears to come from a primary source

    Important:
    - Do not determine whether the claim is true or false.
    - Do not use outside knowledge.
    - Judge only the credibility of the provided source information.

    Title:
    {title}

    URL:
    {url}

    Source content:
    {content[:5000]}
    """

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=Credibility,
        ),
    )

    return response.parsed