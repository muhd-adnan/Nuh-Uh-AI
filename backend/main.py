from fastapi import FastAPI
from pydantic import BaseModel

from claim_extractor import extract_claims
from web_search import search_web
from evidence_extractor import extract_evidence
from webpage_fetcher import fetch_webpage
from evidence_classifier import classify_evidence
from source_credibility import assess_source_credibility
from evidence_scorer import assess_evidence_strength


app = FastAPI()


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {"message": "Nuh Uh AI backend is running!"}


@app.post("/chat")
def chat(request: ChatRequest):
    claim_result = extract_claims(request.message)

    results = []

    for claim in claim_result.claims:
        search_results = search_web(claim)

        evidence_results = []

        for result in search_results:
            webpage_text = fetch_webpage(result["url"])

            if webpage_text:
                source_text = webpage_text
            else:
                source_text = result["content"]

            evidence = extract_evidence(
                claim,
                source_text
            )

            classification = "neutral"

            if evidence.evidence:
                classification_result = classify_evidence(
                    claim,
                    evidence.evidence
                )

                classification = (
                    classification_result.classification
                )

            credibility_result = assess_source_credibility(
                result["title"],
                result["url"],
                source_text
            )

            credibility = credibility_result.credibility

            strength_result = assess_evidence_strength(
                claim,
                evidence.evidence,
                classification,
                credibility
            )

            strength = strength_result.strength

            evidence_results.append({
                "title": result["title"],
                "url": result["url"],
                "score": result["score"],
                "evidence": evidence.evidence,
                "classification": classification,
                "credibility": credibility,
                "strength": strength
            })

        results.append({
            "claim": claim,
            "evidence": evidence_results
        })

    return {
        "claims": results
    }