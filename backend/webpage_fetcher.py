import requests
from bs4 import BeautifulSoup


def fetch_webpage(url: str) -> str | None:

    try:
        response = requests.get(
            url,
            timeout=10,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Remove elements that usually don't contain useful article text
        for element in soup(["script", "style", "nav", "footer", "header"]):
            element.decompose()

        text = soup.get_text(separator=" ", strip=True)

        return text

    except requests.RequestException:
        return None