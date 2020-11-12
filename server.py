import os
import requests
import json
import mysql.connector as sql
from flask import Flask, render_template, request, redirect, url_for
from makePack import make_pack_a
from pullCard import fetch_card
from fetch_prices import fetch_prices
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
@app.route("/grnPack")
def grnPack():

	cards_list = make_pack_a("grn")
	p_name = "grnPack"
	p_img = "/static/img/grn.jpg"
	return render_template("pullPack.html", cards = list(cards_list[1:]), info = list(cards_list[0]), pack_image = p_img, pack_name = p_name) 

@app.route("/rnaPack")
def rnaPack():

	cards_list = make_pack_a("rna")
	p_name = "rnaPack"
	p_img = "/static/img/rna.jpg"
	return render_template("pullPack.html", cards = list(cards_list[1:]), info = list(cards_list[0]), pack_image = p_img, pack_name = p_name) 

@app.route("/bbdPack")
def bbdPack():

	cards_list = make_pack_a("bbd")
	p_name = "bbdPack"
	p_img = "/static/img/bbd.jpg"
	return render_template("pullPack.html", cards = list(cards_list[1:]), info = list(cards_list[0]), pack_image = p_img, pack_name = p_name) 

@app.route("/umaPack")
def umaPack():

	cards_list = make_pack_a("uma")
	p_name = "umaPack"
	p_img = "/static/img/uma.jpg"
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

#Add a Set
@app.route('/admin/addSet')
def new_set():
	return render_template('addSet.html')

#Set add request Form
@app.route("/admin/setAdded", methods = ['POST','GET'])
def addSet():

	#Check for POST
	if request.method == 'POST':

		#Pull data from form
		set_id = request.form["Set_Id"]
		price = request.form["Booster_Price"]
		size = request.form["Pack_Size"]
		land = request.form["Land"]
		cmn = request.form["Common"]
		unc = request.form["Uncommon"]
		ra_my = request.form["Rare_Mythic"]
		r_cnc = request.form["Rare_Chance"]
		m_cnc = request.form["Mythic_Chance"]
		f_cnc = request.form["Foil_Chance"]
		f_cmn = request.form["Foil_Common"]
		f_unc = request.form["Foil_Uncommon"]
		f_rar = request.form["Foil_Rare"]
		f_my = request.form["Foil_Mythic"]
		f_land = request.form["Foil_Land"]

	#Fetch Set and pull misc data from it
	url = "https://api.scryfall.com/sets/" + set_id

	response = requests.get(url)

	r = json.loads(response.content.decode())
	set_name =  r['name']
	year = str(r['released_at'])[:4]
	num_cards = r['card_count']
 
	setSize = r['card_count']
	#Connect to DB
	conn = sql.connect(
		host="localhost",
		user="gnurgle",
		password="ALR6K66EAA",
		database="mtg_db"
		)
	cur = conn.cursor()

	#Insert data from forms into appropriate places
	cur.execute("INSERT IGNORE INTO Sets VALUES \
		(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"\
		,(set_id,set_name,year,num_cards,price,size,land,cmn,unc,ra_my,r_cnc,m_cnc,f_cnc,f_cmn,f_unc,f_rar,f_my,f_land))
	#Commit to DB
	conn.commit()
	cur.close()
	conn.close()
	return render_template('addSet.html')

#Pull a Set
@app.route('/admin/pullSet')
def pull_set():

	#Connect to DB
	conn = sql.connect(
		host="localhost",
		user="gnurgle",
		password="ALR6K66EAA",
		database="mtg_db"
	)
	cur = conn.cursor()

	#Select Set information
	cur.execute("SELECT Set_Id, Set_Name FROM Sets")
	rows = cur.fetchall()

	cur.close()
	conn.close()
	return render_template("pullSet.html", choices = list(rows)) 

#Set Pull request Form
@app.route("/admin/setPulled/<set_id>")
def setPulled(set_id):
	sets = request.args.get('set_id','')
	fetch_card(set_id)

	return redirect("/admin/pullSet") 

#Fetch Prices
@app.route("/admin/fetchPrices")
def fetchPrices():

	fetch_prices()
	return redirect("/admin/pullSet") 

#Fetch Prices
@app.route("/test")
def testingpage():

	return render_template("test.html") 

if __name__ == "__main__":
	app.run(debug = True)
