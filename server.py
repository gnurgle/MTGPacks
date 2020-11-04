import os
from flask import Flask, render_template
from makePack import make_pack_a
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)
#notes for future improvements:
#change so that set name is passes by make_x_pack()
#make the p_name and p_img on the fly in the appropriate files 


@app.route("/")
def index():

	cards_list = make_pack_a("m19")
	return render_template("index.html", cards = list(cards_list[1:]), info = list(cards_list[0])) 

@app.route("/warPack")
def warPack():

	cards_list = make_pack_a("war")
	p_name = "warPack"
	p_img = "/static/img/war.jpg"
	return render_template("pullPack.html", cards = list(cards_list[1:]), info = list(cards_list[0]), pack_image = p_img, pack_name = p_name) 

@app.route("/mh1Pack")
def mh1Pack():

	cards_list = make_pack_a("mh1")
	p_name = "mh1Pack"
	p_img = "/static/img/mh1.jpg"
	return render_template("pullPack.html", cards = list(cards_list[1:]), info = list(cards_list[0]), pack_image = p_img, pack_name = p_name) 

@app.route("/rixPack")
def rixPack():

	cards_list = make_pack_a("rix")
	p_name = "rixPack"
	p_img = "/static/img/rix.jpg"
	return render_template("pullPack.html", cards = list(cards_list[1:]), info = list(cards_list[0]), pack_image = p_img, pack_name = p_name) 

@app.route("/m19Pack")
def m19Pack():

	cards_list = make_pack_a("m19")
	p_name = "m19Pack"
	p_img = "/static/img/m19.jpg"
	return render_template("pullPack.html", cards = list(cards_list[1:]), info = list(cards_list[0]), pack_image = p_img, pack_name = p_name) 

@app.route("/aerPack")
def aerPack():

	cards_list = make_pack_a("aer")
	p_name = "aerPack"
	p_img = "/static/img/aer.jpg"
	return render_template("pullPack.html", cards = list(cards_list[1:]), info = list(cards_list[0]), pack_image = p_img, pack_name = p_name) 

@app.route("/domPack")
def domPack():

	cards_list = make_pack_a("dom")
	p_name = "domPack"
	p_img = "/static/img/dom.jpg"
	return render_template("pullPack.html", cards = list(cards_list[1:]), info = list(cards_list[0]), pack_image = p_img, pack_name = p_name) 

@app.route("/xlnPack")
def xlnPack():

	cards_list = make_pack_a("xln")
	p_name = "xlnPack"
	p_img = "/static/img/xln.jpg"
	return render_template("pullPack.html", cards = list(cards_list[1:]), info = list(cards_list[0]), pack_image = p_img, pack_name = p_name) 



@app.route("/pickPack")
def pickPack():

	return render_template("pickPack.html") 
	


if __name__ == "__main__":
	app.run(debug = True)
