import os
from flask import Flask, render_template
from makePack import make_m19_pack, make_war_pack, make_mh1_pack, make_rix_pack
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)
#notes for future improvements:
#change so that set name is passes by make_x_pack()
#make the p_name and p_img on the fly in the appropriate files 


@app.route("/")
def index():

	cards_list = make_m19_pack()
	return render_template("index.html", cards = list(cards_list[1:]), info = list(cards_list[0])) 

@app.route("/warPack")
def warPack():

	cards_list = make_war_pack()
	p_name = "warPack"
	p_img = "/static/img/war.jpg"
	return render_template("pullPack.html", cards = list(cards_list[1:]), info = list(cards_list[0]), pack_image = p_img, pack_name = p_name) 

@app.route("/mh1Pack")
def mh1Pack():

	cards_list = make_mh1_pack()
	p_name = "mh1Pack"
	p_img = "/static/img/mh1.jpg"
	return render_template("pullPack.html", cards = list(cards_list[1:]), info = list(cards_list[0]), pack_image = p_img, pack_name = p_name) 

@app.route("/rixPack")
def rixPack():

	cards_list = make_rix_pack()
	p_name = "rixPack"
	p_img = "/static/img/rix.jpg"
	return render_template("pullPack.html", cards = list(cards_list[1:]), info = list(cards_list[0]), pack_image = p_img, pack_name = p_name) 

@app.route("/m19Pack")
def m19Pack():

	cards_list = make_m19_pack()
	p_name = "m19Pack"
	p_img = "/static/img/m19.jpg"
	return render_template("pullPack.html", cards = list(cards_list[1:]), info = list(cards_list[0]), pack_image = p_img, pack_name = p_name) 



@app.route("/pickPack")
def pickPack():

	return render_template("pickPack.html") 
	


if __name__ == "__main__":
	app.run(debug = True)
