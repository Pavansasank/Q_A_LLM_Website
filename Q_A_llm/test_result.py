# test_request.py

import requests

response = requests.get(
    "https://fastapi.tiangolo.com/",
    headers={
        "User-Agent":
        "Mozilla/5.0"
    },
    timeout=20
)

print(response.status_code)