from flask import Flask as fl
import sys
import time
sys.path.append(r"E:\document\Project\2022_kakaoChatBot\lunchAPI")
import lunchAPI

app = fl(__name__)

@app.route("/")
def hello_world():
    value = lunchAPI.get_lunch()
    data = ""
    for i in value:
        if i == "":
            continue
        data += (i+", ")
    return "오늘의 점심 : "+str(data)

if __name__ == "__main__":
    app.run(debug=True)
    #print("test")