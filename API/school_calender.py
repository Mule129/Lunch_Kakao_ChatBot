from bs4 import BeautifulSoup as bs
import requests
import datetime as dt
import json
import traceback

def get_calender():
    for i in textCode:
        if i["EVENT_NM"] == "토요휴업일":
            continue
        print(i["EVENT_NM"],i["AA_YMD"])
    
    return #file_c

date = str(dt.date.today()).split("-")[:2]
date = date[0]+date[1]

url = "https://open.neis.go.kr/hub/SchoolSchedule?"
api_key = "&KEY=93bcc0a93e1d4d3fbdfbda50f6e48c6f"
dataType = "&Type=json&pIndex=1&pSize=100"
schoolData = "&ATPT_OFCDC_SC_CODE=N10&SD_SCHUL_CODE=8140265"
push = f"&AA_YMD={date}"
allUrl = url+api_key+dataType+schoolData+push

try:
    res = requests.get(allUrl)
    html = res.text
    textCode = bs(html, "html.parser")
    
    textCode = json.loads(textCode.text)
    
    #textCode = textCode.get_attribute_list("test",textCode)
    with open("API/calender.json", "w", encoding= "utf8", newline= "\n") as file:
        json.dump(textCode["SchoolSchedule"][1]["row"][:], file, indent=4, ensure_ascii= False)
    textCode = textCode["SchoolSchedule"][1]["row"][:]

except (KeyError, IndexError):
    traceback.print_exc()
    print("=============\n\n일정에 문제가 생겼어요. 에러코드를 확인해주세요:(\n\n=============")
except:
    traceback.print_exc()
    print("=============\n\n사이트를 불러오는데 실패했습니다. 인터넷 연결을 확인해주세요 :(\n\n=============")
    

a = get_calender()
print(type(a), print(a))