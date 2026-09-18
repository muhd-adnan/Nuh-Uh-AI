from dotenv import load_dotenv
from tavily import TavilyClient
import os

load_dotenv()

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


def search_web(query: str):
    response = client.search(
        query=query,
        max_results=5
    )

    results = []

    for result in response["results"]:
        results.append({
            "title": result["title"],
            "url": result["url"],
            "content": result["content"],
            "score": result["score"]
        })

    return results


if __name__ == "__main__":
    results = search_web("Is the Earth flat?")

    for result in results:
        print("\nTITLE:", result["title"])
        print("URL:", result["url"])
        print("SCORE:", result["score"])
        print("CONTENT:", result["content"][:300])