import requests
import json
from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("StartPage.HTML")

@app.route("/filloutform", methods=['POST', 'GET'])
def form():
	if request.method == 'POST':
		sports = request.form.get('front')
		fashion = request.form.get('name')
		movie = request.form.get('movie')
		food = request.form.get('find')
		music = request.form.get('keeping')
		vg = request.form.get('ambiance')
		lang = request.form.get('lang')
		code = request.form.get('code')
		user = request.form.get('fname')
		number = request.form.get('phone')
		client_data = []

		client_data.append([str(number),str(user)])
		json.dump(open('client_data', 'w'))
		return redirect(url_for("user",usr = user))
	else:
		return render_template("FormPage.HTML")

@app.route("/<usr>")
def user(usr):
	return "<h1>{usr}</h1>"

@app.route("/Popular")
def gang():
	return render_template("PopularPage.HTML")

#@app.route("/info", methods=['POST', 'GET'])
#def jackpot():
	#return render_template("info.json")



if  __name__ == "__main__":
	app.run()
