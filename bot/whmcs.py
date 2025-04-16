import aiohttp
import os

WHMCS_API_URL = os.getenv("WHMCS_API_URL")
WHMCS_IDENTIFIER = os.getenv("WHMCS_IDENTIFIER")
WHMCS_SECRET = os.getenv("WHMCS_SECRET")

async def get_user_products(email):
    payload = {
        "identifier": WHMCS_IDENTIFIER,
        "secret": WHMCS_SECRET,
        "action": "GetClientsProducts",
        "responsetype": "json",
        "email": email
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(WHMCS_API_URL, data=payload) as response:
            data = await response.json()
            return data.get("products", {}).get("product", [])