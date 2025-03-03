import os
from dotenv import load_dotenv

load_dotenv()

UPS_CLIENT_ID = os.getenv("UPS_CLIENT_ID")
UPS_CLIENT_SECRET = os.getenv("UPS_CLIENT_SECRET")
UPS_ACCESS_TOKEN_URL = os.getenv("UPS_ACCESS_TOKEN_URL")
UPS_TIME_IN_TRANSIT_URL = os.getenv("UPS_TIME_IN_TRANSIT_URL")
