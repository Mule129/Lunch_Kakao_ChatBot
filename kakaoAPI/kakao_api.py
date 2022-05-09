import json
import requests

url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
sendData = ""
restApikey = "ff3f67cf71dc18a928a0ef1ef67e9cec"
#https://gosmcom.tistory.com/130
requests.post(url, json=sendData)