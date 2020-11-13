import json
import requests
import mysql.connector as sql

#update single scryfall ID
def update_Single(input):

	#Connect to DB
	conn = sql.connect(
		host="localhost",
		user="gnurgle",
		password="ALR6K66EAA",
		database = "mtg_db"
	)

	cur = conn.cursor()
	#Set URL for card
	url = "https://api.scryfall.com/cards/" + str(input)

	#Fetch Url
	response = requests.get(url)
	r = json.loads(response.content.decode())

	#Check if land and set flag
	if r['type_line'][:4] == "Land":
		is_land = True
	elif r['type_line'][:5] == "Basic":
		is_land = True
	else:
		is_land = False

	#Set card information
	cur.execute("UPDATE Card " +
		"SET Number = %s, Name= %s, Rarity= %s, Booster= %s, " +
		"Has_Foil= %s, Has_NonFoil= %s, Is_Promo= %s, Is_Land= %s "+
		"WHERE Scryfall_Id = %s",\
		(r['collector_number'], r['name'], r['rarity'], int(r['booster']), \
		int(r['foil']), int(r['nonfoil']), int(r['promo']), int(is_land), \
		str(input)))

	conn.commit()
	
	#Fetch card information based on needed 
	url = 'https://api.scryfall.com/cards/' + str(input) + '?format=image&version=border_crop'
	url2 = url + '&face=back'
	response = requests.get(url2)

	#Check if back side image
	if response.status_code == 200:
		num_sides = 2
		back_image = url2
	else:
		num_sides = 1
		back_image = None

	#Initialize prices
	price_usd = r['prices']['usd']
	price_foil = r['prices']['usd_foil']

	#Check if null value and set to 0 instead
	if price_usd == None:
		price_usd = 0.00
	if price_foil == None:
		price_foil = 0.00

	#Set images and prices
	cur.execute("UPDATE Card_Images " +
	"SET Front_Image = %s, Back_Image = %s, Price = %s, Price_Foil = %s " +
	"WHERE Scryfall_Id = %s", (str(url),back_image,price_usd,price_foil, str(input)))
	conn.commit()

	#Close connection
	cur.close()
	conn.close()
	
if __name__ == "__main__":
	update_Single("1bdb0b15-d651-4730-8be9-d0e01145311b")
