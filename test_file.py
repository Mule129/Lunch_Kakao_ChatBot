import datetime as dt
import random

day_list = ["2022-2-25","2022-6-27","2022-10-1","2022-12-1"]#스크래핑 하기
len_list = len(day_list)

today = dt.date.today()



for o in range(len_list):
    d_year, d_month, d_day = day_list[o].split("-")
    dday = dt.date(year=int(d_year),month=int(d_month),day=int(d_day))
    dday = dday - today

    print("test:",str(dday).split(" ")[0],"t")


