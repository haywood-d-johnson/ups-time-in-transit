import requests
import base64
from config import UPS_CLIENT_ID, UPS_CLIENT_SECRET, UPS_ACCESS_TOKEN_URL

def get_access_token():
    """Fetch OAuth token from UPS"""
    auth_string = f"{UPS_CLIENT_ID}:{UPS_CLIENT_SECRET}"
    base64_auth = base64.b64encode(auth_string.encode()).decode()

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": f"Basic {base64_auth}"
    }
    data = {"grant_type": "client_credentials"}

    res = requests.post(UPS_ACCESS_TOKEN_URL, headers=headers, data=data)

    if res.status_code == 200:
        return res.json().get("access_token")
    else:
        print("Error fetching access token: ", res.text)
        return None
