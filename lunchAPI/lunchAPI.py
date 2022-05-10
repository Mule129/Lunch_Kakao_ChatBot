import sys
from bs4 import BeautifulSoup as bs
import requests
import datetime as dt
import re
import json

Dump = str(dt.date.today()).split("-")
YMD = Dump[0]+Dump[1]+Dump[2]

url = "https://open.neis.go.kr/hub/mealServiceDietInfo?"
ID = "KEY=723cb30d58e64de18c656de07de2f0b2"
dataType = "&Type=json&pIndex=1&pSize=2"#size 2 : 석식
schoolData = "&ATPT_OFCDC_SC_CODE=N10&SD_SCHUL_CODE=8140265"
lunchData = "&MLSV_YMD="+ str(YMD)
allUrl = url + ID + dataType + schoolData + lunchData

if True:
    res = requests.get(allUrl)
    html = res.text
    textCode = bs(html, "html.parser")
    textCode = textCode.get_text()
    with open("2022_kakaoChatBot/Menu.json", "w") as file:
        json.dump(textCode, file)
    print(textCode)
    #print(textCode["mealServiceDietInfo"][1]["row"][0]["DDISH_NM"])
else:
    print("사이트를 불러오는데 실패했습니다")
