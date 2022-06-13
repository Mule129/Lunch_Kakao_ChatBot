from flask import Flask as fl
import lunchAPI
import sys

app = fl(__name__)

@app.route("/")
def hello_world():
    return "Hello, World"

if __name__ == "__main__":
    app.run(host = "https://schoollunchbot.herokuapp.com/")