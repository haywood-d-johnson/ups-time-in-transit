import requests
from config import UPS_TIME_IN_TRANSIT_URL
from auth import get_access_token

def get_transit_time(origin_zip, dest_zip):
    """Query UPS Time in Transit API."""
    access_token = get_access_token()
    if not access_token:
        return None

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }

    payload = {
        "originCountryCode": "US",
        "originPostalCode": origin_zip,
        "destinationCountryCode": "US",
        "destinationPostalCode": dest_zip,
        "weight": {"value": 10, "unitOfMeasurement": "LBS"},
        "totalPackageCount": 1,
        "shipmentPickupDate": "2025-03-02"
    }

    res = requests.post(UPS_TIME_IN_TRANSIT_URL, json=payload, headers=headers)

    if res.status_code == 200:
        print(res)
        return res.json()
    else:
        print(f"{res.status_code} error for {dest_zip}: {res.text}")
        return None
