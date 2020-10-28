import os
from flask import Flask, render_template
from makePack import make_m19_pack

app = Flask(__name__)

@app.route("/")

def index():
	cards_list = make_m19_pack()
	return render_template("index.html", cards = list(cards_list[1:]), info = list(cards_list[0])) 

if __name__ == "__main__":
	app.run(debug = True)
