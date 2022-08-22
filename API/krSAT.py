import datetime as dt
import calendar
import json
import time

from pandas import read_json


def fileOpen():
    with open("2022_kakaoChatBot\API\SAT_Dday.json", "r") as file:
        data = json.load(file)
    return data


def savefile(data):
    with open("2022_kakaoChatBot\API\SAT_Dday.json", "w")as file:
        value = json.dump(file)
        value += "\n"+data


def count():
    
    #todate = calendar.calendar()
    data = fileOpen()
    print(data)


count()
