from source_credibility import assess_source_credibility


tests = [
    {
        "title": "NASA: Earth",
        "url": "https://www.nasa.gov/",
        "content": """
        NASA is the United States government agency responsible for
        space exploration, aeronautics, and space science.
        """
    },
    {
        "title": "Example Personal Blog",
        "url": "https://example.com/blog",
        "content": """
        This is a personal blog with no references and no information
        about the author's qualifications.
        """
    },
    {
        "title": "Unknown Source",
        "url": "https://example.com/",
        "content": """
        This article provides information but does not identify the
        author, organization, references, or source of the information.
        """
    }
]


for test in tests:

    result = assess_source_credibility(
        test["title"],
        test["url"],
        test["content"]
    )

    print("\nTITLE:", test["title"])
    print("URL:", test["url"])
    print("CREDIBILITY:", result.credibility)
