import sys
from bs4 import BeautifulSoup as bs
import requests
import re

YMD = 20220504
url = "https://open.neis.go.kr/hub/mealServiceDietInfo?"
ID = "KEY=723cb30d58e64de18c656de07de2f0b2"
dataType = "&Type=json&pIndex=1&pSize=1"
schoolData = "&ATPT_OFCDC_SC_CODE=N10&SD_SCHUL_CODE=8140265"
lunchData = "&MLSV_YMD="+ str(YMD)
allUrl = url + ID + dataType + schoolData + lunchData

try:
    res = requests.get(allUrl)
    html = res.text
    textCode = bs(html, "html.parser")
    textCode = textCode.get_text()
    print(textCode)
except:
    print("사이트를 불러오는데 실패했습니다")
