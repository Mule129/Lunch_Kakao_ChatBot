import datetime as dt
import random, json ,sys, requests
from PIL import Image, ImageFont, ImageDraw
from lunch import lunchAPI
import school_calender

sys.path.append("2022_kakaoChatBot")

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
    with open(r"2022_kakaoChatBot\API\SAT_Dday.json", "r") as file:
        day = json.load(file)
        day = str(day[day_()[0]])
        dday = str(dt.date(int(day[:4]), int(day[4:6]), int(day[6:])) - dt.date.today()).split()
        dday = f"D - {dday[0]} Day"   
    return dday

def new_image(xy_size : tuple, color : int):
    """
    새 랜덤 배경색을 가진 이미지 생성

    xy_size = 크기(튜플형), color = 배경색
    """
    new_image = Image.new("RGB", xy_size, random_color())

    return new_image

###########
input_t = ""
dump = ""
while True:
    dump = str(input())
    if dump == "0":
        break
    else : input_t += (dump+"\n")

#fnt = ImageFont.load("BMJUA_ttf.ttf")#<-비트맵(픽셀)형식 글꼴 파일 오픈
image = new_image((1000, 1000), color_list(random.randint(3,26)))
fntSet = ImageFont.truetype(r"font\BMJUA_ttf.ttf", size=130)

draw = ImageDraw.Draw(image)
font_x, font_y = image.size
font_x = float(font_x) / 2
font_y = float(font_y) / 2
font_pos = font_x, font_y

#today
today = str(dt.date.today()).split("-")
today = today[0]+today[1]

lp = lunchAPI()
try:
    lp.get_eat()
except requests.exceptions.ConnectionError:
    lp.get_eat()

lunch_data, dinner_data = lp.get_lunch(),lp.get_dinner()
lunch_data, dinner_data = "\n".join(map(str, lunch_data)), "\n".join(map(str, dinner_data))

#font setting
font_path = r"font\BMJUA_ttf.ttf"

#수능dday
draw.text((250,100), str("수능까지"), color_list(0),
          font=ImageFont.truetype(font_path, size=50),
          anchor="mm", align=10, stroke_width=5, stroke_fill=color_list(2))
draw.text((500,200), str(SAT_dday()), color_list(0),
          fntSet, anchor="mm", align=10, stroke_width=10, stroke_fill=color_list(2))
draw.multiline_text((100,300), f"선생님 한마디 : {input_t}",
                    font=ImageFont.truetype(font_path, size=30),
                    spacing=1 , stroke_width=4, stroke_fill=color_list(2))
#내신dday
#draw.text((250,50), str("중간고사까지"), color_list(0),
#          font=ImageFont.truetype("BMJUA_ttf.ttf", size=50),
#          anchor="mm", align=10, stroke_width=5, stroke_fill=color_list(2))
#draw.text((500,150), str(exam_day(0)), color_list(0),
#          fntSet, anchor="mm", align=10, stroke_width=10, stroke_fill=color_list(2))
#오늘 날짜
draw.text((780,40), str(dt.date.today())+"  3학년 6반 알리미", color_list(0),
          font=ImageFont.truetype(font_path, size=30),
          anchor="mm", align=10, stroke_width=4, stroke_fill=color_list(2))
#급식정보
draw.text((250,500), "오늘의 급식", color_list(0),
          font=ImageFont.truetype(font_path, size=40),
          anchor="mm", align=10, stroke_width=5, stroke_fill=color_list(2))

draw.multiline_text((50,550), f"중식\n\n{lunch_data}",
                    font=ImageFont.truetype(font_path, size=30),
                    spacing=1 , stroke_width=4, stroke_fill=color_list(2), align='center')
draw.multiline_text((300,550), f"석식\n\n{dinner_data}",
                    font=ImageFont.truetype(font_path, size=30),
                    spacing=1 , stroke_width=4, stroke_fill=color_list(2), align='center')
#공란
draw.text((750,500), "오늘의 뉴스", color_list(0),
          font=ImageFont.truetype(font_path, size=40),
          anchor="mm", align=10, stroke_width=5, stroke_fill=color_list(2))

add_image = Image.open(r"SettingIcon.png")
image.paste(im=add_image, box = (580,550))

#학사정보
#draw.multiline_text((550,550), "학사정보\n"+str(school_schedule()), font=ImageFont.truetype("BMJUA_ttf.ttf", size=21), spacing=1 , stroke_width=3, stroke_fill=color_list(2))


image.show()
#image.save("test_image.png", format="png")
