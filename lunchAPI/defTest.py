import requests
import json

url = "https://kauth.kakao.com/oauth/token"

data = {
    "grant_type" : "authorization_code",
    "client_id" : "ff3f67cf71dc18a928a0ef1ef67e9cec",
    "redirect_uri" : "https://localhost",
    "code"         : "EM9XR53qFEkBSjPO-lWKq3htAoIeYh0gXXwbXPEl6M7guZBeqKodUPnGOdLkdPcBgknZ7Ao9cpgAAAGBWM49og"
    
}
response = requests.post(url, data=data)

tokens = response.json()

with open("kakao_token.json", "w") as fp:
    json.dump(tokens, fp, indent=4)
