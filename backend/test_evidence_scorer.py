from evidence_scorer import assess_evidence_strength


tests = [
    {
        "claim": "Water freezes at 0 degrees Celsius at standard atmospheric pressure.",
        "evidence": "At standard atmospheric pressure, pure water freezes at 0 degrees Celsius.",
        "classification": "supports",
        "credibility": "high"
    },
    {
        "claim": "The Earth is flat.",
        "evidence": "Earth is approximately spherical.",
        "classification": "contradicts",
        "credibility": "high"
    },
    {
        "claim": "The Earth is flat.",
        "evidence": "Someone on an online forum says the Earth is flat.",
        "classification": "supports",
        "credibility": "low"
    },
    {
        "claim": "The Earth is flat.",
        "evidence": "The source discusses the Moon's phases.",
        "classification": "neutral",
        "credibility": "medium"
    }
]


for test in tests:

    result = assess_evidence_strength(
        test["claim"],
        test["evidence"],
        test["classification"],
        test["credibility"]
    )

    print("\nCLAIM:", test["claim"])
    print("EVIDENCE:", test["evidence"])
    print("CLASSIFICATION:", test["classification"])
    print("CREDIBILITY:", test["credibility"])
    print("STRENGTH:", result.strength)

