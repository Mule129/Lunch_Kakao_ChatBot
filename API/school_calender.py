from bs4 import BeautifulSoup as bs
import requests
import datetime as dt
import json
import traceback

error_cnt = 0
date = str(dt.date.today()).split("-")[:2]
date = date[0]+date[1]

def get_calender():
    try:
        with open(f"2022_kakaoChatBot\API\calender_{date}.json", "r", encoding="utf8") as file:
            textCode = json.load(file)
    except FileNotFoundError:
        traceback.print_exc()
        print("=============\n\nDon't find Data . . retry get data\n\n=============")
        if error_cnt < 5:
            get_data()
            with open(f"2022_kakaoChatBot\API\calender_{date}.json", "r", encoding="utf8") as file:
                textCode = json.load(file)
        else:
            print("=============\n\n프로그램에 예기치 못한 오류가 발생하였습니다. 프로그램을 다시 시작해주세요 :( \n\n=============")
    except:
        traceback.print_exc()
        print("=============\n\n프로그램에 예기치 못한 오류가 발생하였습니다. 프로그램을 다시 시작해주세요 :( \n\n=============")
    
    file_c = {}
    dump = []
    dump_d = ""
    dump_t = ""
    cnt = 0
    for i in textCode:
        cnt += 1
        v_name, v_date = i["EVENT_NM"].replace(" ", ""), i["AA_YMD"]
        print(v_name, v_date)
        if "토요" in v_name:
            if dump_t != "" and len(textCode) == cnt:
                file_c[dump_d] = "_"+dump_t
            continue
        elif v_name in dump:
            if len(textCode) == cnt:
                file_c[v_date] = "_"+v_name
            else:
                dump_t, dump_d = v_name, v_date
                print("!",dump_t, dump_d, cnt, len(textCode))
        elif v_name not in dump:
            if dump_t != "":
                print("?",dump_t, dump_d)
                file_c[dump_d] = "_"+dump_t
                dump_d, dump_t = "", ""
            dump.append(v_name)
            file_c[v_date] = v_name
        else:
            file_c[v_date] = v_name
    return file_c


def get_data():
    url = "https://open.neis.go.kr/hub/SchoolSchedule?"
    api_key = "&KEY=93bcc0a93e1d4d3fbdfbda50f6e48c6f"
    dataType = "&Type=json&pIndex=1&pSize=100"
    schoolData = "&ATPT_OFCDC_SC_CODE=N10&SD_SCHUL_CODE=8140265"
    push = f"&AA_YMD={date}"
    allUrl = url+api_key+dataType+schoolData+push
    print(allUrl)
    try:
        res = requests.get(allUrl)
        html = res.text
        textCode = bs(html, "html.parser")
    
        textCode = json.loads(textCode.text)
    
        #textCode = textCode.get_attribute_list("test",textCode)
        with open(f"2022_kakaoChatBot\API\calender_{date}.json", "w", encoding= "utf8", newline= "\n") as file:
            json.dump(textCode["SchoolSchedule"][1]["row"][:], file, indent=4, ensure_ascii= False)
        textCode = textCode["SchoolSchedule"][1]["row"][:]

    except (KeyError, IndexError):
        traceback.print_exc()
        print("=============\n\n일정에 문제가 생겼어요. 에러코드를 확인해주세요:(\n\n=============")
    except:
        traceback.print_exc()
        print("=============\n\n사이트를 불러오는데 실패했습니다. 인터넷 연결을 확인해주세요 :(\n\n=============")
    
