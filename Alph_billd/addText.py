import datetime as dt
import random
import requests
import re
import pandas as pd
from bs4 import BeautifulSoup as bs
from PIL import Image, ImageFont, ImageDraw

def color_list(t):
    """
    색상리스트 "color"

    1번 = 흰색, 2번 = 검은색, 3번 = 회색 . . .
    """
    color = ["#FFFFFF", "#000000", "#555555",
             "#FFD8D8", "#FAE0D4", "#FAECC5", "#FAF4C0", "#E4F7BA", "#CEFBC9",
             "#D4F4FA", "#D9E5FF", "#DAD9FF", "#E8D9FF", "#FFD9FA", "#FFD9EC",
             "#FFA7A7", "#FFC19E", "#FFE08C", "#FAED7D", "#CEF279", "#B7F0B1",
             "#B2EBF4", "#B2CCFF", "#B5B2FF", "#D1B2FF", "#FFB2F5", "#FFB2D9"]
    return color[t]
#print(color_list.__doc__)

def random_color()->int:
    t = random.randint(3,26)
    number = color_list(t)
    return number

def day():
    """
    날짜계산
    :return:합산 날짜 출력
    """
    dday = dt.date(year=2022, month=11, day=17)
    today = dt.date.today()

    dday = dday - today
    dday = "D - " + str(dday).split()[0] + " day"

    return dday

def day_0(o : int):
    day_list = ["2022-4-25","2022-6-27"]#스크래핑 하기
    d_year, d_month, d_day = day_list[o].split("-")
    dday = dt.date(year=int(d_year),month=int(d_month),day=int(d_day))
    today = dt.date.today()

    dday = dday - today
    dday = "D - " + str(dday).split()[0] + " day"

    return dday

def test_day(t : int, o : int) ->int:
    """
    :param t: 시험 종류(0 = 내신, 1 = 수능
    :param o: 몇번째 시험인지 ..
    :return: date type로 출력
    """
    if t == 1:
        dday = day()
    elif t == 0:
        dday = day_0(o)

    return dday


def new_image(xy_size : tuple, color : int):
    """
    새 이미지 생성

    xy_size = 크기(튜플형), color = 배경색
    """
    new_image = Image.new("RGB", xy_size, random_color())

    return new_image

def find_text(data):
    for x in data:
        x.find(str(dt.date.today()).split("-")[1])

def week_day(number):
    data = {0: '월요일', 1:'화요일', 2:'수요일', 3:'목요일', 4:'금요일', 5:'토요일', 6:'일요일'}

    return data[number]

def lunch(to_month : str)->str:
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

    print(today, week, find_t)

    for i in eat_list:
        if i.find(find_t) != -1:
            print("찾음")
            return eat_list[x]
        else:
            x = x + 1
        print(x)

    return eat_list[int(today)]

#fnt = ImageFont.load("BMJUA_ttf.ttf")#<-비트맵(픽셀) 글꼴 파일 오픈
image = new_image((1000, 1000), color_list(random.randint(3,26)))

fntSet = ImageFont.truetype("BMJUA_ttf.ttf", size=130)

draw = ImageDraw.Draw(image)
font_x, font_y = image.size
font_x = float(font_x) / 2
font_y = float(font_y) / 2
font_pos = font_x, font_y

#today
today = str(dt.date.today()).split("-")
today = today[0]+today[1]

#수능dday
draw.text((250,270), str("수능까지"), color_list(0),
          font=ImageFont.truetype("BMJUA_ttf.ttf", size=50),
          anchor="mm", align=10, stroke_width=5, stroke_fill=color_list(2))
draw.text((500,350), str(day()), color_list(0),
          fntSet, anchor="mm", align=10, stroke_width=10, stroke_fill=color_list(2))
draw.text((500,450), str("화이팅"), color_list(0),
          font=ImageFont.truetype("BMJUA_ttf.ttf", size=30),
          anchor="mm", align=10, stroke_width=5, stroke_fill=color_list(2))
#내신dday
draw.text((250,50), str("중간고사까지"), color_list(0),
          font=ImageFont.truetype("BMJUA_ttf.ttf", size=50),
          anchor="mm", align=10, stroke_width=5, stroke_fill=color_list(2))
draw.text((500,150), str(test_day(0,0)), color_list(0),
          fntSet, anchor="mm", align=10, stroke_width=10, stroke_fill=color_list(2))
#오늘 날짜
draw.text((800,50), str(dt.date.today()), color_list(0),
          font=ImageFont.truetype("BMJUA_ttf.ttf", size=30),
          anchor="mm", align=10, stroke_width=5, stroke_fill=color_list(2))
#급식정보
draw.multiline_text((20,500), "오늘의 급식\n"+str(lunch(str(today))),
                    font=ImageFont.truetype("BMJUA_ttf.ttf", size=21),
                    spacing=1 , stroke_width=3, stroke_fill=color_list(2))
#공란
add_image = Image.open("제작중 로고_3.png")
image.paste(im=add_image, box = (550,550 ))
image.show()
image.save("test_image.png", format="png")

#print(len(a))