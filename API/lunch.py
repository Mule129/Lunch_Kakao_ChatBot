from bs4 import BeautifulSoup as bs
import requests
import datetime as dt
import json
import traceback

class lunchAPI():
    def __init__(self) -> None:
        self.lunch = ""
        self.Dump = ""
        self.YMD = ""
        self.dinner = ""
        self.error_cont = 0

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
    

    def get_lunch(self):
        data = self.lunch
        return data

    def get_dinner(self):
        data = self.dinner
        return data


    def get_eat(self):
        Dump = str(dt.date.today()).split("-")
        self.YMD = Dump[0]+Dump[1]+Dump[2]
        url = "https://open.neis.go.kr/hub/mealServiceDietInfo?"
        ID = "KEY=723cb30d58e64de18c656de07de2f0b2"
        dataType = "&Type=json&pIndex=1&pSize=2"#size 2 : 석식
        schoolData = "&ATPT_OFCDC_SC_CODE=N10&SD_SCHUL_CODE=8140265"
        lunchData = "&MLSV_YMD="+ str(self.YMD)
        allUrl = url + ID + dataType + schoolData + lunchData

        try:
            res = requests.get(allUrl, verify=False)#verify = false : 신뢰할 수 없는 인증서 차단 해제
            html = res.text
            textCode = bs(html, "html.parser")
            textCode = json.loads(textCode.text)
            #textCode = textCode.get_attribute_list("test",textCode)
            with open("2022_kakaoChatBot\API\Menu.json", "w", encoding= "utf8", newline= "\n") as file:
                json.dump(textCode["mealServiceDietInfo"][1]["row"], file, indent=4, ensure_ascii= False)
            #print(textCode["mealServiceDietInfo"][1]["row"][0]["DDISH_NM"])
            self.lunch = textCode["mealServiceDietInfo"][1]["row"][0]["DDISH_NM"]
            if "석식" not in textCode:
                self.dinner = ["석식없는날"]
            else :
                self.dinner = textCode["mealServiceDietInfo"][1]["row"][1]["DDISH_NM"]
            self.lunch, self.dinner = lunchAPI.del_txt(self.lunch).split(), lunchAPI.del_txt(self.dinner).split()
        except requests.exceptions.ConnectionError:
            self.error_cont += 1
            try:
                self.get_eat()
            except RecursionError:
                "인증서에 치명적인 오류가 발생하였습니다. 소스코드를 확인해주세요"
                print(f"error_cont : {self.error_cont}")
        except (KeyError):
            traceback.print_exc()
            print("=============\n\n오늘은 급식이 없는 날이에요:(\n\n=============")
            self.lunch, self.denner = ["오늘은 급식이 없는 날이에요 :("], ""
        except (FileNotFoundError, IndexError):
            traceback.print_exc()
            print("=============\n\n파일 경로에 문제가 생겼습니다. 오류코드를 확인해주세요 :(\n\n(=============")
        except:
            traceback.print_exc()
            print("=============\n\n사이트를 불러오는데 실패했습니다. 인터넷 연결을 확인해주세요 :(\n\n=============")
