from fastapi import FastAPI
from pydantic import BaseModel

from claim_extractor import extract_claims
from web_search import search_web
from evidence_extractor import extract_evidence
from webpage_fetcher import fetch_webpage
from evidence_classifier import classify_evidence


app = FastAPI()


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {"message": "Nuh Uh AI backend is running!"}


@app.post("/chat")
def chat(request: ChatRequest):

    # V1: Extract claims
    claim_result = extract_claims(request.message)

    results = []

    # Process each claim
    for claim in claim_result.claims:

        # V2: Search the web
        search_results = search_web(claim)

        evidence_results = []

        # V3: Retrieve webpages and extract evidence
        for result in search_results:

            # Try to fetch the actual webpage
            webpage_text = fetch_webpage(result["url"])

            # If webpage retrieval fails, use Tavily content
            if webpage_text:
                source_text = webpage_text
            else:
                source_text = result["content"]

            # Extract relevant evidence
            evidence = extract_evidence(
                claim,
                source_text
            )

            # V4: Classify the evidence
            classification = "neutral"

            if evidence.evidence:
                classification_result = classify_evidence(
                    claim,
                    evidence.evidence
                )

                classification = classification_result.classification

            evidence_results.append({
                "title": result["title"],
                "url": result["url"],
                "score": result["score"],
                "evidence": evidence.evidence,
                "classification": classification
            })

        results.append({
            "claim": claim,
            "evidence": evidence_results
        })

    return {
        "claims": results
    }
