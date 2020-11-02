import os
from flask import Flask, render_template
from makePack import make_m19_pack
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)

@app.route("/")

def index():
	return render_template("index.html")

@app.route("/pullPack")
def pull_pack():

	cards_list = make_m19_pack()
	return render_template("card_pack.html", cards = list(cards_list[1:]), info = list(cards_list[0])) 
	


if __name__ == "__main__":
	app.run(debug = True)
