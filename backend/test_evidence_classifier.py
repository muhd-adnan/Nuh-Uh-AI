from evidence_classifier import classify_evidence


tests = [
    {
        "claim": "Water freezes at 0 degrees Celsius at standard atmospheric pressure.",
        "evidence": "At standard atmospheric pressure, water freezes at 0 degrees Celsius.",
    },
    {
        "claim": "The Earth is flat.",
        "evidence": "The Moon is Earth's natural satellite.",
    },
    {
        "claim": "The Earth is flat.",
        "evidence": "Earth is a roughly spherical planet.",
    }
]


for test in tests:

    result = classify_evidence(
        test["claim"],
        test["evidence"]
    )

    print("\nCLAIM:", test["claim"])
    print("EVIDENCE:", test["evidence"])
    print("CLASSIFICATION:", result.classification)