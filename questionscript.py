import requests
from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("StartPage.HTML")

@app.route("/filloutform", methods = ['POST', 'GET'])
def form():
	if request.method == 'POST':
		football = request.form.get('How interested in sports are you?')
		return '<h1>If this doesnt say a number IM gonna fucking kill myself: {}</h1>'.format(football)

	return render_template("FormPage.HTML")

@app.route("/info", methods=['POST'])
def jackpot():
	return render_template("info.json")



if  __name__ == "__main__":
	app.run()
