import os
import requests
import json
import mysql.connector as sql
from flask import Flask, render_template, request, redirect, url_for, jsonify, make_response
from makePack import make_pack_a
from pullCard import fetch_card
from updateSingle import  update_Single
from fetch_prices import fetch_prices
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, validators


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
#app.config['SQLALCHEMY_DATABASE_URI'] = path to mysql database
Bootstrap(app)
db = SQLAlchemy(app)
login_manger = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


#Pack pass throughs
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

@app.route("/thbPack")
def thbPack():

	cards_list = make_pack_a("thb")
	p_name = "thbPack"
	p_img = "/static/img/thb.jpg"
	return render_template("pullPack.html", cards = list(cards_list[1:]), info = list(cards_list[0]), pack_image = p_img, pack_name = p_name) 

@app.route("/eldPack")
def eldPack():

	cards_list = make_pack_a("eld")
	p_name = "eldPack"
	p_img = "/static/img/eld.jpg"
	return render_template("pullPack.html", cards = list(cards_list[1:]), info = list(cards_list[0]), pack_image = p_img, pack_name = p_name) 

@app.route("/m20Pack")
def m20Pack():

	cards_list = make_pack_a("m20")
	p_name = "m20Pack"
	p_img = "/static/img/m20.jpg"
	return render_template("pullPack.html", cards = list(cards_list[1:]), info = list(cards_list[0]), pack_image = p_img, pack_name = p_name) 

@app.route("/a25Pack")
def a25Pack():

	cards_list = make_pack_a("a25")
	p_name = "a25Pack"
	p_img = "/static/img/a25.jpg"
	return render_template("pullPack.html", cards = list(cards_list[1:]), info = list(cards_list[0]), pack_image = p_img, pack_name = p_name) 

@app.route("/imaPack")
def imaPack():

	cards_list = make_pack_a("ima")
	p_name = "imaPack"
	p_img = "/static/img/ima.jpg"
	return render_template("pullPack.html", cards = list(cards_list[1:]), info = list(cards_list[0]), pack_image = p_img, pack_name = p_name) 

@app.route("/mm3Pack")
def mm3Pack():

	cards_list = make_pack_a("mm3")
	p_name = "mm3Pack"
	p_img = "/static/img/mm3.jpg"
	return render_template("pullPack.html", cards = list(cards_list[1:]), info = list(cards_list[0]), pack_image = p_img, pack_name = p_name) 

@app.route("/oriPack")
def oriPack():

	cards_list = make_pack_a("ori")
	p_name = "oriPack"
	p_img = "/static/img/ori.jpg"
	return render_template("pullPack.html", cards = list(cards_list[1:]), info = list(cards_list[0]), pack_image = p_img, pack_name = p_name) 

@app.route("/emaPack")
def emaPack():

	cards_list = make_pack_a("ema")
	p_name = "emaPack"
	p_img = "/static/img/ema.jpg"
	return render_template("pullPack.html", cards = list(cards_list[1:]), info = list(cards_list[0]), pack_image = p_img, pack_name = p_name) 

@app.route("/ogwPack")
def ogwPack():

	cards_list = make_pack_a("ogw")
	p_name = "ogwPack"
	p_img = "/static/img/ogw.jpg"
	return render_template("pullPack.html", cards = list(cards_list[1:]), info = list(cards_list[0]), pack_image = p_img, pack_name = p_name) 

@app.route("/mm2Pack")
def mm2Pack():

	cards_list = make_pack_a("mm2")
	p_name = "mm2Pack"
	p_img = "/static/img/mm2.jpg"
	return render_template("pullPack.html", cards = list(cards_list[1:]), info = list(cards_list[0]), pack_image = p_img, pack_name = p_name) 

@app.route("/dtkPack")
def dtkPack():

	cards_list = make_pack_a("dtk")
	p_name = "dtkPack"
	p_img = "/static/img/dtk.jpg"
	return render_template("pullPack.html", cards = list(cards_list[1:]), info = list(cards_list[0]), pack_image = p_img, pack_name = p_name) 

@app.route("/ktkPack")
def ktkPack():

	cards_list = make_pack_a("ktk")
	p_name = "ktkPack"
	p_img = "/static/img/ktk.jpg"
	return render_template("pullPack.html", cards = list(cards_list[1:]), info = list(cards_list[0]), pack_image = p_img, pack_name = p_name) 

@app.route("/m15Pack")
def m15Pack():

	cards_list = make_pack_a("m15")
	p_name = "m15Pack"
	p_img = "/static/img/m15.jpg"
	return render_template("pullPack.html", cards = list(cards_list[1:]), info = list(cards_list[0]), pack_image = p_img, pack_name = p_name) 

@app.route("/pickPack")
def pickPack():

	return render_template("pickPack.html")

#user class to add users to db
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(80))


@login_manager.user_loader
def load_user(user_id)	
	return User.query.get(int(user_id))


#login routes
@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm

	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user:
			if user.password == from.password.data:
				login_user(user)
				return redirect(url_for('index'))

		return '<h1>Invalid username or password</h1>'
		#return '<h1>' + form.username.data + ' ' + form.password.data + </h1>'
	
	return render_template ('login.html')

@app.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('index')

			
@app.route('/signup', methods=['GET', 'POST'])
	def signup():
		form = SignupForm()

		if from.validate_on_submit():
			new_user = User(username = form.username.data, password=form.password.data)
			db.session.add(new_user)
			db.session.commit()

			return '<h1>New User has been created!</h1>'
			
		return render_template('signUp.html')

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

	cur.execute("SELECT Set_Id, Set_Name FROM Sets")
	rows = cur.fetchall()

	cur.close()
	conn.close()
	#return render_template('addSet.html', choices = list(rows))
	return redirect(url_for('adminSet'))

#Admin page for cards and sets
@app.route('/admin/')
def adminSet():

	form = Form()
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
	return render_template("admin.html", form=form, choices = list(rows)) 

#Set Pull request Form
@app.route("/admin/setPulled/<set_id>")
def setPulled(set_id):
	sets = request.args.get('set_id','')
	fetch_card(set_id)

	return redirect(url_for('adminSet')) 

#Fetch Prices
@app.route("/admin/fetchPrices")
def fetchPrices():

	fetch_prices()
	return redirect(url_for('adminSet')) 

#Fetch Prices
@app.route("/test")
def testingpage():

	return render_template("test.html") 

class Form(FlaskForm):
	#Connect to DB
	conn = sql.connect(
		host="localhost",
		user="gnurgle",
		password="ALR6K66EAA",
		database="mtg_db"
	)
	cur = conn.cursor()
	cur.execute("SELECT Set_Id,Set_Name FROM Sets")
	rows =cur.fetchall()
	rows.insert(0,[" ", "-- Set Name --"])

	sets = SelectField('sets', choices=rows)
	cards = SelectField('cards', choices=[(" ","-- Card Name --")])
	#options = SelectField('options', choices=[(" ","-- Field to Change --")])
	card_change = StringField('New value', [validators.InputRequired()])
	

#Admin page
@app.route("/admin/update", methods=['GET','POST'])
def cardUpdate():

	form = Form()
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

	if request.method =='POST':
		try:
			cur.execute("UPDATE Card SET Scryfall_Id = %s \
				WHERE Scryfall_ID = %s",\
				(form.card_change.data,form.cards.data))
			
			conn.commit()
			cur.close()
			conn.close()
			update_Single(form.card_change.data)
		except:
			print("Update Card Failed")
			conn.rollback()
	return render_template('admin.html', form=form, choices=list(rows))

#Route for card
@app.route('/admin/set/<setsid>')
def cards(setsid):

	#Connect to DB
	conn = sql.connect(
		host="localhost",
		user="gnurgle",
		password="ALR6K66EAA",
		database="mtg_db"
	)
	cur = conn.cursor()
	cur.execute("SELECT Scryfall_Id, Name FROM Card WHERE Set_Id = %s\
				ORDER BY Name,Number",(setsid,))
	rows = cur.fetchall()
	rows.insert(0,[" ", "-- Card Name --"])

	cur.close()
	conn.close()
	return jsonify({'cards' : rows})

#Route for card options
@app.route('/admin/card')
def card_options():

	#Connect to DB
	conn = sql.connect(
		host="localhost",
		user="gnurgle",
		password="ALR6K66EAA",
		database="mtg_db"
	)
	cur = conn.cursor()
	cur.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS \
				WHERE (TABLE_NAME='Card') OR (TABLE_NAME='Card_Images')")
	rows = cur.fetchall()
	#rows.insert(0,[" ", "-- Card Name --"])
	
	return jsonify({'options' : rows})


#Set news page
@app.route('/news')
def new():

	return render_template('news.html')

if __name__ == "__main__":
	app.run(debug = True)
