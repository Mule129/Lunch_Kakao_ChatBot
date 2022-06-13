import requests
import json
reset_api_key = "ff3f67cf71dc18a928a0ef1ef67e9cec"
redirect_uri = "https://localhost"
url = f"https://kauth.kakao.com/oauth/authorize?response_type=code&client_id={reset_api_key}&redirect_uri={redirect_uri}"
print(url)
requests.post(url)