import requests
from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("StartPage.HTML")

@app.route("/filloutform")
def form():
    return render_template("FormPage.HTML")

@app.route("/info", methods=['POST', 'GET'])
def jackpot():
    return render_template("info.json")

@app.route("/Popular")
def home():
    return render_template("PopularPage.HTML")


if  __name__ == "__main__":
    app.run()
