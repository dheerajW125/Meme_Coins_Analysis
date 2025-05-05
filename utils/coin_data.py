import requests

import time

import requests

def get_latest_token_profiles():
    url = "https://api.dexscreener.com/token-profiles/latest/v1"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        
        # Extract chainId and tokenAddress for each token
        tokens = []
        for token in data:
            chain_id = token.get("chainId")
            token_address = token.get("tokenAddress")
            if chain_id and token_address:
                tokens.append({
                    "chainId": chain_id,
                    "tokenAddress": token_address
                })
        
        return tokens
    else:
        print(f"Error {response.status_code}: {response.text}")
        return []


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


def get_orders_paid_with_retry(chain_id: str, token_address: str, retries=3, delay=60):
    for attempt in range(retries):
        response = requests.get(f"https://api.dexscreener.com/orders/v1/{chain_id}/{token_address}")
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 429:
            print("Rate limit hit, waiting...")
            time.sleep(delay)
        else:
            print(f"Error {response.status_code}: {response.text}")
            break
    return None

