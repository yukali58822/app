from flask import Flask, render_template, request
from datetime import datetime,timezone,timedelta

app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>資管二B 411150480 謝佩宸的網頁</h1>"
    homepage += "<a href=/home>關於我</a><br>"
    homepage += "<a href=/mis>MIS相關工作</a><br>"
    homepage += "<a href=/planning>學習規劃</a><br>"
    return homepage


@app.route("/all")
def course():
    return "<h1>資管二B 411150480 謝佩宸的網頁</h1>"

@app.route("/home")
def self():
    return render_template("home.html")

@app.route("/mis")
def mis():
    return render_template("work1.html")

@app.route("/planning")
def planning():
    return render_template("planning.html")

#if __name__ == "__main__":
#   app.run()