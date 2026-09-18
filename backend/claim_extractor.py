from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel

load_dotenv()

client = genai.Client()


class Claims(BaseModel):
    claims: list[str]


def extract_claims(message: str) -> Claims:

    prompt = f"""
    Extract the factual claims from the user's message.

    Rules:
    - Return only claims that could be checked against evidence.
    - Split multiple claims into separate items.
    - Do not verify or judge the claims.
    - Do not add information that the user did not state.

    User message:
    {message}
    """

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt,
        config={
            "response_mime_type": "application/json",
            "response_schema": Claims,
        },
    )

    return response.parsed


if __name__ == "__main__":
    result = extract_claims(
        "I think the Earth is flat and humans only use 10% of their brains."
    )

    print(result)
    print(result.claims)