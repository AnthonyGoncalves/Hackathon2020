import requests
import json
from flask import Flask, redirect, url_for, render_template, request
from webdriver import GroupMeBot


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
		userData = []
		print (code)
		userData.append([str(number),str(user)])
		with open('client_data.json', 'w') as f:
			json.dump(userData, f)

		return redirect(url_for("user",usr = user))
	else:
		return render_template("FormPage.HTML")

@app.route("/<usr>")
def user(usr):
	return "<h1>{usr}</h1>"

@app.route("/Popular", methods=['POST', 'GET'])
def gang():
	if request.method == 'POST':
		dict = {"1":"Sports","2":"Fashion","3":"Movies","4":"Food",
		"5":"Music", "6":"Videogames", "7":"Languages","8":"Coding" }
		sports = request.form.get('front')
		fashion = request.form.get('fash')
		movie = request.form.get('movies')
		food = request.form.get('food')
		music = request.form.get('music')
		vg = request.form.get('vgames')
		lang = request.form.get('lang')
		code = request.form.get('code')
		user = request.form.get('fname')
		number = request.form.get('phone')

		pref = ""
		whichOne = [sports, fashion, movie, food, music, vg, lang, code]
		for i in whichOne:
			if i != None:
				pref = dict[str(i)]
		if pref != "":
			my_bot = GroupMeBot()
			my_bot.logIn()
			my_bot.addClientToGroup(str(number), str(user), str(pref))
		return render_template("PopularPage.HTML")

	else:
		return render_template("PopularPage.HTML")

#@app.route("/info", methods=['POST', 'GET'])
#def jackpot():
	#return render_template("info.json")



if  __name__ == "__main__":
	app.run()
