import datetime as dt
import random
import requests
import re
from bs4 import BeautifulSoup as bs
from PIL import Image, ImageFont, ImageDraw

def day_()->list:
    """
    today 함수의 dt 타입을 str 형식으로 변환
    
    :return: list   ex) [2022,02,02]
    """
    to_day = dt.date.today()
    to_day = str(to_day).split("-")
    return to_day

def color_list(t):
    """
    color list

    :param t: 1-흰색 2-검정색 3-회색 4~15-연한무지개 16~27-진한무지개
    :return: color str(list)
    """
    color = ["#FFFFFF", "#000000", "#555555",
             "#FFD8D8", "#FAE0D4", "#FAECC5", "#FAF4C0", "#E4F7BA", "#CEFBC9",
             "#D4F4FA", "#D9E5FF", "#DAD9FF", "#E8D9FF", "#FFD9FA", "#FFD9EC",
             "#FFA7A7", "#FFC19E", "#FFE08C", "#FAED7D", "#CEF279", "#B7F0B1",
             "#B2EBF4", "#B2CCFF", "#B5B2FF", "#D1B2FF", "#FFB2F5", "#FFB2D9"]
    return color[t]
#print(color_list.__doc__)

def week_day(number):
    """
    번호:날짜(dictionary type)

    :param number:날짜에 해당하는 숫자
    :return: str 형식 날짜

    """
    data = {0: '월요일', 1:'화요일', 2:'수요일', 3:'목요일', 4:'금요일', 5:'토요일', 6:'일요일'}

    return data[number]


def random_color()->int:
    """
    random color create

    :return: random color str(list)
    """
    t = random.randint(3,26)
    number = color_list(t)
    return number

def SAT_dday():
    """
    수능(korean SAT) dday 출력 함수

    :return:합산 날짜 출력
    """
    dday = dt.date(year=2022, month=11, day=17)
    today = dt.date.today()

    dday = dday - today
    dday = "D - " + str(dday).split()[0] + " day"

    return dday

def day_str(n:int):
    """
    나중에 파일 불러와서 갱신 가능하게 변경

    n = 0 ->> 날짜 출력
    n = 1 ->> 중간/기말 출력
    n = 2 ->> 요일 출력
    """
    day_list = [dt.datetime(2022,4,25),dt.datetime(2022,6,27),dt.datetime(2022,10,1),dt.datetime(2022,12,1)]
    month_list = ["중간고사까지", "기말고사까지"]
    print(dt.date.weekday(n))
    week_list = week_day(dt.date.weekday(n))
    today = dt.date.today
    
    for i in range(4):
        if (day_list(i) - today) == 0 : return "D"
        elif (day_list(i) - today) > 0 : number = i
        else : return "error"

    if n == 0: return day_list(number)
    elif n == 1 : return month_list
    elif n== 2 : return week_list    

    return None

def s_dday():
    """
    내신 시험(scholl exam) dday 출력 함수

    :param o: 시험 종류 
    :return: 남은 날짜(dday)
    """
    day_list = day_str(1)
    
    len_list = len(day_list)

    today = dt.date.today()

    for o in range(len_list):
        d_year, d_month, d_day = day_list[o].split("-")
        dday = dt.date(year=int(d_year),month=int(d_month),day=int(d_day))
        dday = dday - today
        dday = str(dday).split(" ")[0]
        if int(dday) < 0:
            pass
        elif int(dday) > 0:
            break

    dday = "D - " + str(dday).split()[0] + " day"

    return dday

def exam_day(t : int) ->int:
    """
    수능, 내신 dday 출력

    :param t: 시험 종류(0 = 내신, 1 = 수능
    :param o: 몇번째 시험인지 ..
    :return: date type로 출력
    """
    if t == 1:
        dday = SAT_dday()
    elif t == 0:
        dday = s_dday()

    return dday


def new_image(xy_size : tuple, color : int):
    """
    새 랜덤 배경색을 가진 이미지 생성

    xy_size = 크기(튜플형), color = 배경색
    """
    new_image = Image.new("RGB", xy_size, random_color())

    return new_image


def lunch(to_month : str)->str:
    r"""
    1. 날짜 파라미터(매개변수)를 입력받으면 bs4와 requests 모듈을 이용하여 급식조회사이트에서 그 달의 급식정보 표 조회
    2. 가져온 급식정보 표에서 re모듈-줄바꿈(\n) 횟수를 공백으로 치환, 이를 이용하여 날짜별 데이터 분리 -> eat_list list에 저장
    3. datetime.date.today 함수를 이용하여 오늘의 날짜 탐색
    4. for문과 find 함수를 이용하여 eat_list 내에 오늘의 날짜와 일치하는 급식 데이터 검출

    수정예정 - to_month 파라미터 제거, today 함수를 이용하여 자체적으로 오늘의 날짜 탐색

    :param to_month: 오늘의 날짜(ex:2001년02월02일 -> 200102 #월까지만 입력)
    :return: 오늘의 급식정보
    """
    month = to_month +".html"
    url = "https://school.koreacharts.com/school/meals/B000012894/"+month

    res = requests.get(url)

    try: #res.status_code == 200
        html = res.text
        soup = bs(html, "html.parser")
        lyrics = soup.select_one("body > div > div > div > section.content > div:nth-child(6) > div > div > div.box-body")
        try:
            eat_text = lyrics.get_text()
        except:
            print("사이트 정보를 읽어들이지 못했습니다")
        eat_text = re.sub("&nbsp; | &nbsp;|\t|\r","",eat_text)
        #eat_text = re.sub("\n\n\n\n\n","\n\n\n\n\n",eat_text)
        eat_text = re.sub("\n\n\n", "\n", eat_text)
        eat_text = re.sub("\n\n", "\n", eat_text)
    except:
        print("사이트를 불러오는데 실패했습니다")

    eat_list = eat_text.split("\n\n")
    today = str(int(str(dt.date.today()).split("-")[2]))
    week = dt.date.today().weekday()
    week = week_day(week)

    x = 0

    find_t = str(today+"\n"+ week)

    #print("오늘의 날짜, 요일, 찾은 날짜", today, week, find_t)

    for i in eat_list:
        if i.find(find_t) != -1:
            print("+====find today lunch====+")
            return eat_list[x]
        
        else:
            x = x + 1
            
    eat_list = "오늘은 급식이 없는 날이에요"
    return eat_list

#print(lunch.__doc__)# r""" doc test

def lunch_slice():
    """
    데이터 전처리(당일 급식 데이터 뒤에 붙은 성분표시 제거, 날짜 삭제)
    
    :return: 전처리 완료된 급식데이터
    """
    name = lunch(str(today))
    if name == "오늘은 급식이 없는 날이에요":
        return name
    name = name.split('\n')
    data_list = []

    for i in range(len(name)):#name 리스트 길이만큼 for문 실행
        data_pros = re.sub(r'[0-9]+', '', name[i])#problem : 날짜 또한 제거되어버림.
        if i != 0:
            data_list.append(data_pros.replace('.','') + str('\n'))
    print("a result : ", data_list)

    result = ''.join(s for s in data_list)#

    return(result)




#fnt = ImageFont.load("BMJUA_ttf.ttf")#<-비트맵(픽셀)형식 글꼴 파일 오픈
image = new_image((1000, 1000), color_list(random.randint(3,26)))

fntSet = ImageFont.truetype("font\BMJUA_ttf.ttf", size=130)

draw = ImageDraw.Draw(image)
font_x, font_y = image.size
font_x = float(font_x) / 2
font_y = float(font_y) / 2
font_pos = font_x, font_y

#today
today = str(dt.date.today()).split("-")
today = today[0]+today[1]

#수능dday
draw.text((250,260), str("수능까지"), color_list(0),
          font=ImageFont.truetype("BMJUA_ttf.ttf", size=50),
          anchor="mm", align=10, stroke_width=5, stroke_fill=color_list(2))
draw.text((500,350), str(SAT_dday()), color_list(0),
          fntSet, anchor="mm", align=10, stroke_width=10, stroke_fill=color_list(2))
draw.text((500,450), str("화이팅"), color_list(0),
          font=ImageFont.truetype("BMJUA_ttf.ttf", size=30),
          anchor="mm", align=10, stroke_width=5, stroke_fill=color_list(2))
#내신dday
draw.text((250,50), str("중간고사까지"), color_list(0),
          font=ImageFont.truetype("BMJUA_ttf.ttf", size=50),
          anchor="mm", align=10, stroke_width=5, stroke_fill=color_list(2))
draw.text((500,150), str(exam_day(0)), color_list(0),
          fntSet, anchor="mm", align=10, stroke_width=10, stroke_fill=color_list(2))
#오늘 날짜
draw.text((800,50), str(dt.date.today()), color_list(0),
          font=ImageFont.truetype("BMJUA_ttf.ttf", size=30),
          anchor="mm", align=10, stroke_width=5, stroke_fill=color_list(2))
#급식정보
draw.multiline_text((20,500), "오늘의 급식\n"+str(lunch_slice()),
                    font=ImageFont.truetype("BMJUA_ttf.ttf", size=21),
                    spacing=1 , stroke_width=3, stroke_fill=color_list(2))
#공란
add_image = Image.open("SettingIcon.png")
image.paste(im=add_image, box = (550,550))

#학사정보
#draw.multiline_text((550,550), "학사정보\n"+str(school_schedule()), font=ImageFont.truetype("BMJUA_ttf.ttf", size=21), spacing=1 , stroke_width=3, stroke_fill=color_list(2))


image.show()
image.save("test_image.png", format="png")
