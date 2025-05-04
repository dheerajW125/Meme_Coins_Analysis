import time
import requests

# Define the base URL and your token details
base_url = "https://api.dexscreener.com/orders/v1/{chainId}/{tokenAddress}"
chain_id = "solana"
token_address = "A55XjvzRU4KtR3Lrys8PpLZQvPojPqvnv5bJVHMYy3Jv"

# Make the request
response = requests.get(base_url.format(chainId=chain_id, tokenAddress=token_address))

# Check for rate-limiting or successful response
if response.status_code == 200:
    print(response.json())
elif response.status_code == 429:
    # Handle rate-limit: wait before retrying
    print("Rate limit reached, retrying...")
    time.sleep(60)  # Wait for 60 seconds
    response = requests.get(base_url.format(chainId=chain_id, tokenAddress=token_address))
    print(response.json())
else:
    print(f"Error: {response.status_code}")
