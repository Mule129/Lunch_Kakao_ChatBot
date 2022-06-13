from bs4 import BeautifulSoup as bs
import requests
import datetime as dt
import json

Dump = str(dt.date.today()).split("-")
YMD = Dump[0]+Dump[1]+Dump[2]

def del_txt(data):
    jud = 0
    value = ""
    for i in data:
        if i == "(" and jud == 0:
            jud = 1
        elif i == ")" and jud != 0:
            jud = 0
        elif jud == 0:
            value += i
    return value

def get_lunch():
    return lunch

def get_dinner():
    return dinner

url = "https://open.neis.go.kr/hub/mealServiceDietInfo?"
ID = "KEY=723cb30d58e64de18c656de07de2f0b2"
dataType = "&Type=json&pIndex=1&pSize=2"#size 2 : 석식
schoolData = "&ATPT_OFCDC_SC_CODE=N10&SD_SCHUL_CODE=8140265"
lunchData = "&MLSV_YMD="+ str(YMD)
allUrl = url + ID + dataType + schoolData + lunchData


try:
    res = requests.get(allUrl)
    html = res.text
    textCode = bs(html, "html.parser")
    textCode = json.loads(textCode.text)
    
    #textCode = textCode.get_attribute_list("test",textCode)
    with open("lunchAPI\Menu.json", "w", encoding= "utf8", newline= "\n") as file:
        json.dump(textCode, file, indent=4, ensure_ascii= False)
    
    lunch = textCode["mealServiceDietInfo"][1]["row"][0]["DDISH_NM"]
    dinner = textCode["mealServiceDietInfo"][1]["row"][1]["DDISH_NM"]
    lunch, dinner = del_txt(lunch).split("  "), del_txt(dinner).split("  ")
    
except KeyError:
    print("오늘은 급식이 없는 날이에요 :(")
except:
    print("사이트를 불러오는데 실패했습니다. 인터넷 연결을 확인해주세요 :(")

#print(lunch, "\ndinner : ", dinner)