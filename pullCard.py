import json
import requests
import time
import mysql.connector as sql


def fetch_card(setName):
	
	#Fetch M19 Set and pull data from it
	url = "https://api.scryfall.com/sets/" + setName

	#Fetch Set name, printed_size, tcgplayer_id, printed_size, code, released_at
	response = requests.get(url)

	r = json.loads(response.content.decode())
	print ("Set Name = " + r['name'])
	print ("Card number = " + str(r['card_count']))
	print ("TCGPlayerID = " + str(r['tcgplayer_id']))
	print ("Short code = " + r['code'])
	print ("Release Date = " + str(r['released_at']))
 
	setSize = r['card_count']

	#Fetch Card 13 from set
	url = "https://api.scryfall.com/cards/collection"
	
	fetchDict = {
		"identifiers": [
		{
		'collector_number': str("1"),
		'set': setName
		}
		]
	}

	#Connect to DB
	conn = sql.connect(
		host="localhost",
		user="gnurgle",
		password="ALR6K66EAA",
		database = "mtg_db"
	)
	#Override setSizes for specific sets with issues
	if setName == "war":
		setSize = 275
		
	for i in range(1,setSize):

		fetchDict['identifiers'][0]['collector_number'] = str(i)

		response = requests.post(url, json=fetchDict)

		r = json.loads(response.content.decode())

		#Check if land and set flag
		if r['data'][0]['type_line'][:4] == "Land":
			is_land = True
		elif r['data'][0]['type_line'][:5] == "Basic":
			is_land = True
		else:
			is_land = False
		
		#Fetch relevant card Data
		#name, set, numer, rarity, color_identity, tcgplayer_id, layout, booster, uri, prices, foil
		print("Collector Number = " + r['data'][0]['collector_number'])
		print("Name = " + r['data'][0]['name'])
		#print("Set =" + r['data'][0]['set'])
		#print("Rarity = " + r['data'][0]['rarity'])
		#print("Color Identity = " + str(r['data'][0]['color_identity']))
		#print("TCGPlayer ID = " + str(r['data'][0]['tcgplayer_id']))
		#print("Layout = " + r['data'][0]['layout'])
		#print("Booster = " + str(r['data'][0]['booster']))
		print("UniqueID = " + str(r['data'][0]['uri'][31:]))
		#print("Prices = " + str(r['data'][0]['prices']['usd']))
		#print("Prices Foil= " #+ str(r['data'][0]['prices']['usd_foil']))
		#print("Has foil? = " + str(r['data'][0]['foil']))
		#print("Has nonfoil? = " + str(r['data'][0]['nonfoil']))
		#print("Is promo? = " + str(r['data'][0]['promo']))
		#Write to DB---------------------------------------------------
		cur = conn.cursor()

		cur.execute("INSERT IGNORE INTO Card \
		(Number, Name, Set_Id, Rarity, Color, Layout, Booster, Scryfall_Id, Has_Foil, Has_NonFoil, Is_Promo, Is_Land) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",\
		(r['data'][0]['collector_number'], r['data'][0]['name'], r['data'][0]['set'], \
		r['data'][0]['rarity'], str(r['data'][0]['color_identity']), \
		r['data'][0]['layout'], int(r['data'][0]['booster']), \
		r['data'][0]['uri'][31:], int(r['data'][0]['foil']), int(r['data'][0]['nonfoil']), \
		int(r['data'][0]['promo']), int(is_land)))

		conn.commit()

		#Wait per API specifications
		time.sleep(.120)

	cur.close()
	conn.close()

	pull_card_images(setName)

def pull_card_images(setName):

	#Connect to DB to fetch cards images to be added/refreshed
	conn = sql.connect(
		host="localhost",
		user="gnurgle",
		password="ALR6K66EAA",
		database = "mtg_db"
	)


	#conn.row_factory = sql.Row
	cur = conn.cursor()

	#Select ScryfallIDs And layout of cards in set
	cur.execute("SELECT Scryfall_Id from Card WHERE Set_Id = %s",(setName,))
	rows = cur.fetchall()

	#conn.close()

	#conn = sql.connect('mtg_db.db')
	#cur = conn.cursor()

	
	for i in range (0,len(rows)):
		#Fetch card information based on needed 
		url = "https://api.scryfall.com/cards/" + str(rows[i][0]) + "?format=image&version=border_crop"
		url2 = url + "&face=back"
		response = requests.get(url2)

		if response.status_code == 200:
			num_sides = 2
			back_image = url2
		else:
			num_sides = 1
			back_image = None

		cur.execute("INSERT IGNORE INTO Card_Images (Scryfall_ID, Num_Sides, Front_Image, Back_Image) VALUES (%s,%s,%s,%s)", (str(rows[i][0]),num_sides,url,back_image))

		conn.commit()

		print (str(i+1) + " of " + str(len(rows)) + " images processed ...")
		#Wait per API specifications
		time.sleep(.120) 

	cur.close()
	conn.close()
if __name__== '__main__':
	fetch_card("dom")
