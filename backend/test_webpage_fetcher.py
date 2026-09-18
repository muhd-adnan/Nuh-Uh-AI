from webpage_fetcher import fetch_webpage


url = "https://example.com"

text = fetch_webpage(url)

if text:
    print("Webpage fetched successfully.")
    print(text[:1000])
else:
    print("Failed to fetch webpage.")