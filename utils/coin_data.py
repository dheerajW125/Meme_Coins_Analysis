import requests

def get_latest_token_profiles():
    url = "https://api.dexscreener.com/token-profiles/latest/v1"
    response = requests.get(url)
    return response.json()

def get_latest_boosted_tokens():
    url = "https://api.dexscreener.com/token-boosts/latest/v1"
    response = requests.get(url)
    return response.json()

def search_pairs(query: str):
    url = "https://api.dexscreener.com/latest/dex/search"
    params = {"q": query}
    response = requests.get(url, params=params)
    return response.json().get("pairs", [])

def get_pairs_by_token_address(chain_id: str, token_address: str):
    url = f"https://api.dexscreener.com/token-pairs/v1/{chain_id}/{token_address}"
    response = requests.get(url)
    return response.json()
