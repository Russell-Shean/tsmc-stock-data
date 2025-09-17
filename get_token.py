import requests
from dotenv import load_dotenv
import os

load_dotenv()


# Load credentials from environment variables
USER_ID = os.environ["FINMIND_USER_ID"]
PASSWORD = os.environ["FINMIND_PASSWORD"]





url = "https://api.finmindtrade.com/api/v4/login"
payload = {
    "user_id": USER_ID,
    "password": PASSWORD,
}
data = requests.post(url, data=payload)
data = data.json()
print(data)