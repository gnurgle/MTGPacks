import mysql.connector as sql
import random

#---List of Pack names and types
#make_pack_a = Core M19 Style Pack

#Core m19 Style Pack
def make_pack_a(setN):

	#Set Set Name
	setName=setN
	#Connect to DB
	#conn = sql.connect('mtg_db.db')
	conn = sql.connect(
		host="localhost",
		user="gnurgle",
		password="ALR6K66EAA",
		database="mtg_db"
	)

	cur = conn.cursor()

	#Get Set information
	cur.execute("SELECT Pack_size, Land, Common, Uncommon, Rare_Mythic, Rare_Chance, Mythic_chance, Foil_Chance, Foil_Common, Foil_Uncommon, Foil_Rare, Foil_Mythic, Foil_Land FROM Sets WHERE Set_Id = %s",(setName,))
	rows = cur.fetchall()

	#Pack properties
	pack_size = rows[0][0]
	land_count = rows[0][1]
	common_count = rows[0][2]
	uncommon_count = rows[0][3]
	r_mr_count = rows[0][4]
	foil_count = 0
	rare_chance = rows[0][5]
	mythic_chance = rows[0][6]
	#Foil breakdown
	foil_chance = rows[0][7]
	foil_common = rows[0][8]
	foil_uncommon = rows[0][9]
	foil_rare = rows[0][10]
	foil_mythic = rows[0][11]
	foil_land = rows[0][12]
	foil_type = ""

	if check_foil(foil_chance):
		common_count = common_count - 1
		foil_count = 1
		foil_type = (foil_rarity(foil_common, foil_uncommon, foil_rare, foil_mythic, foil_land))

	#Make lists of rarity types
	#Mythic Rare
	cur.execute("SELECT Name, Scryfall_ID FROM Card WHERE Set_Id = %s AND Booster = 1 AND Rarity = 'mythic'",(setName,))
	mythic_rows = cur.fetchall()
	#Rare
	cur.execute("SELECT Name, Scryfall_ID FROM Card WHERE Set_Id = %s AND Booster = 1 AND Rarity = 'rare'",(setName,))
	rare_rows = cur.fetchall()
	#Uncommon
	cur.execute("SELECT Name, Scryfall_ID FROM Card WHERE Set_Id = %s AND Booster = 1 AND Rarity = 'uncommon' AND Is_Land = 0",(setName,))
	uncommon_rows = cur.fetchall()
	#Common
	cur.execute("SELECT Name, Scryfall_ID FROM Card WHERE Set_Id = %s AND Booster = 1 AND Rarity = 'common' AND Is_Land = 0",(setName,))
	common_rows = tuple(cur.fetchall())
	#Land
	cur.execute("SELECT Name, Scryfall_ID FROM Card WHERE Set_Id = %s AND Booster = 1 AND Is_Land = 1 AND Rarity = 'common'",(setName,))
	land_rows = cur.fetchall()
	booster_pack = []

	#Shuffle rows, prevents duplicates vs random.choice
	common_shuffled = random.sample(common_rows, len(common_rows))
	uncommon_shuffled = random.sample(uncommon_rows, len(uncommon_rows))
	booster_pack.append(common_shuffled[:common_count])
	booster_pack.append(uncommon_shuffled[:uncommon_count])

	#random.choice okay for single cards

	#Define type layout for passing information
	layout = []
	for i in range(0,common_count):
		layout.append("common")
	for i in range(0,uncommon_count):
		layout.append("uncommon")



	#Add Rare or Mythic
	for i in range(0,r_mr_count):
		if check_rare_mythic(rare_chance, mythic_chance) == "rare":
			booster_pack.append(random.choice(rare_rows))
			layout.append("rare")
		else:
			booster_pack.append(random.choice(mythic_rows))
			layout.append("mythic")

	#Add foil
	if foil_count == 1 and foil_type != "land":
		cur.execute("SELECT Name, Scryfall_ID FROM Card WHERE Set_Id = %s AND Booster = 1 AND Rarity = %s AND Has_Foil = 1",(setName,foil_type))
		foil_rows = tuple(cur.fetchall())
		booster_pack.append(random.choice(foil_rows))
		layout.append("foil")
	elif foil_count == 1 and foil_type == "land":
		cur.execute("SELECT Name, Scryfall_ID FROM Card WHERE Set_Id = %s AND Booster = 1 AND Is_Land = 1",(setName,))
		foil_rows = cur.fetchall()
		booster_pack.append(random.choice(foil_rows))
		layout.append("foil")

	for i in range(0,land_count):
		booster_pack.append(random.choice(land_rows))
		layout.append("land")
		
	cur.close()
	conn.close()
	#Strip internal lists out of booster list
	output_pack = []
	for i in range(0,len(booster_pack)):
		if len(booster_pack[i]) > 2:
			for j in range(0,len(booster_pack[i])):
				output_pack.append(booster_pack[i][j])
		else:
			output_pack.append(booster_pack[i])

	#Send to process final output
	out_pack = output_pack_info(pack_size, foil_count, output_pack, setName,layout)
	return (out_pack)

#Determine whether rare or mythic
def check_rare_mythic(r_c, m_c):
	#total chance possibility
	total_chance = r_c+m_c

	rm_value = random.randint(1,total_chance)
	if rm_value in range(1,r_c+1):
		return "rare"
	else:
		return "mythic"
#Foil Check
def check_foil(fchance):

	if random.randint(1,100) > fchance:
		return False
	else: 
		return True
#Determine foil rarity
def foil_rarity(c_c, u_c, r_c, m_c, l_c):
	
	#Total Chance possibility
	total_chance = c_c + u_c + r_c + m_c + l_c
	
	foil_value = random.randint(1,total_chance)
	if foil_value in range(1,c_c+1):
		return "common"
	elif foil_value in range(c_c+1, c_c+u_c+1):
		return "uncommon"
	elif foil_value in range(c_c+u_c+1, c_c+u_c+r_c+1):
		return "rare"
	elif foil_value in range(c_c+u_c+r_c+1, c_c+u_c+r_c+l_c+1):
		return "land"
	else:
		return "mythic"

#This is for single foil packs
def output_pack_info(num_c, f_c, pack, setID, lay):

	#Last entry is num of cards, position of foil if one, total_price, setprice, empty
	#Rest of entry is scryfall, num of sides, front, back or empty, price
	layout = lay
	output_info = []
	info_entry = []
	subtotal = 0
	#Open DB to fetch and attach card Images
	conn = sql.connect(
		host="localhost",
		user="gnurgle",
		password="ALR6K66EAA",
		database="mtg_db"
	)


	cur = conn.cursor()

	

	for i in range(0,num_c):
		#Mythic Rare
		if layout[i] == "foil":
			cur.execute("SELECT Card_Images.Scryfall_ID, \
						Card_Images.Num_Sides, \
						Card_Images.Front_Image, \
						Card_Images.Back_Image, \
						Card_Images.Price_Foil, \
						Card.Rarity \
						FROM Card_Images \
						INNER JOIN Card\
						ON Card_Images.Scryfall_Id = Card.Scryfall_Id \
						WHERE Card_Images.Scryfall_Id = %s", (pack[i][1],))
		else:
			#cur.execute("SELECT Scryfall_ID, Num_Sides, Front_Image, Back_Image, Price FROM Card_Images WHERE Scryfall_Id = %s", (pack[i][1],))
			cur.execute("SELECT Card_Images.Scryfall_ID, \
						Card_Images.Num_Sides, \
						Card_Images.Front_Image, \
						Card_Images.Back_Image, \
						Card_Images.Price, \
						Card.Rarity \
						FROM Card_Images \
						INNER JOIN Card\
						ON Card_Images.Scryfall_Id = Card.Scryfall_Id \
						WHERE Card_Images.Scryfall_Id = %s", (pack[i][1],))

		info_entry = cur.fetchall()
		output_info.append(info_entry)
		subtotal = subtotal + info_entry[0][4]

	#Clear info_entry
	info_entry = []
	#Create first entry
	info_entry.append(num_c)
	if f_c > 0:
		info_entry.append(num_c-1)
	else:
		info_entry.append(0)
	#Add two empty slots	
	info_entry.append(subtotal)
	#Grab price of Pack and add
	cur.execute("SELECT Booster_Price FROM Sets WHERE Set_ID = %s",(setID,))
	setPrice = cur.fetchall()
	info_entry.append(setPrice[0][0])
	info_entry.append(setID)
	#Add layout for foil usage
	info_entry.append(layout)
	#Add info_entry to output_info
	output_info.insert(0,info_entry) 
	
	cur.close()
	conn.close()
	
	return output_info
	

if __name__ == '__main__':
	make_pack_a("m19")

