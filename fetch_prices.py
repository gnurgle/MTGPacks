import json
import requests
import sqlite3 as sql
import time

#Note, this only needs to be runs once a day at the most
def fetch_prices():

	#Set url for fetching card data
	url = "https://api.scryfall.com/cards/"

	#Connect to DB and pull all Scryfall_Id
	conn = sql.connect('mtg_db.db')
	cur = conn.cursor()
	cur.execute("SELECT Scryfall_Id from Card")
	rows = cur.fetchall()

	for i in range(0,len(rows)):
		response = requests.get(url + str(rows[i])[2:38])
		print (url + str(rows[i])[2:38])
		r = json.loads(response.content.decode())
		print (str(r['prices']['usd']))
		print (str(r['prices']['usd_foil']))

		update_query = """UPDATE Card_Images SET Price = ?, Price_foil = ? WHERE Scryfall_Id = ?"""
		price_usd = r['prices']['usd']
		price_foil = r['prices']['usd_foil']

		#Check if null value and set to 0 instead
		if price_usd == None:
			price_usd = 0.00
		if price_foil == None:
			price_foil = 0.00

		data = (price_usd,
		price_foil,
		str(rows[i])[2:38])
		cur.execute(update_query,data)
		conn.commit()

		#Sleep according to api specifications
		time.sleep(.120)

if __name__== '__main__':
	fetch_prices()
