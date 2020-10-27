import sqlite3 as sql
import random

def make_m19_pack():

	#Pack properties
	pack_size = 15
	land_count = 1
	common_count = 10
	uncommon_count = 3
	r_mr_count = 1
	foil_count = 0
	rare_chance = 7
	mythic_chance = 1
	#Foil breakdown
	foil_chance = 24
	foil_common = 88
	foil_uncommon = 24
	foil_rare = 7
	foil_mythic = 1
	foil_land = 8
	foil_type = ""

	if check_foil(foil_chance):
		common_count = common_count - 1
		foil_count = 1
		print ("This pack has a foil")
		foil_type = (foil_rarity(foil_common, foil_uncommon, foil_rare, foil_mythic, foil_land))
		print (foil_type)
	else:
		print ("This pack has no foil :(")

	#Make lists of rarity types
	conn = sql.connect('mtg_db.db')
	#conn.row_factory = sql.Row
	cur = conn.cursor()

	#Note here, booster needs to be updated when changed to Bit for all
	#Mythic Rare
	cur.execute("SELECT Name, Scryfall_ID FROM Card WHERE Set_Id = 'm19' AND Booster = '1' AND Rarity = 'mythic'")
	mythic_rows = cur.fetchall()
	#Rare
	cur.execute("SELECT Name, Scryfall_ID FROM Card WHERE Set_Id = 'm19' AND Booster = '1' AND Rarity = 'rare'")
	rare_rows = cur.fetchall()
	#Uncommon
	cur.execute("SELECT Name, Scryfall_ID FROM Card WHERE Set_Id = 'm19' AND Booster = '1' AND Rarity = 'uncommon'")
	uncommon_rows = cur.fetchall()
	#Common - Needs to be updated once land is a Bit column
	cur.execute("SELECT Name, Scryfall_ID FROM Card WHERE Set_Id = 'm19' AND Booster = '1' AND Rarity = 'common'")
	common_rows = tuple(cur.fetchall())
	#Land - Needs to be updated once land is a Bit column
	cur.execute("SELECT Name, Scryfall_ID FROM Card WHERE Set_Id = 'm19' AND Booster = '1' AND (Name = 'Plains' OR Name = 'Island' OR Name = 'Mountain' OR Name = 'Swamp' OR Name = 'Forest')")
	land_rows = cur.fetchall()
	#print (tuple(land_rows[1:4][1]))
	booster_pack = []

	booster_pack.append(random.choices(common_rows, k=common_count))
	booster_pack.append(random.choices(uncommon_rows, k=uncommon_count))
	if check_rare_mythic(rare_chance, mythic_chance) == "rare":
		booster_pack.append(random.choice(rare_rows))
	else:
		booster_pack.append(random.choice(mythic_rows))

	if foil_count == 1 and foil_type != "land":
		cur.execute("SELECT Name, Scryfall_ID FROM Card WHERE Set_Id = 'm19' AND Booster = '1' AND Rarity = ? AND Has_Foil = 1",(foil_type,))
		foil_rows = tuple(cur.fetchall())
		booster_pack.append(random.choice(foil_rows))
	elif foil_count == 1 and foil_type == "land":
		cur.execute("SELECT Name, Scryfall_ID FROM Card WHERE Set_Id = 'm19' AND Booster = '1' AND (Name = 'Plains' OR Name = 'Island' OR Name = 'Mountain' OR Name = 'Swamp' OR Name = 'Forest')")
		foil_rows = cur.fetchall()
		booster_pack.append(random.choice(foil_rows))

	booster_pack.append(random.choice(land_rows))

	#Strip internal lists out of booster list
	output_pack = []
	for i in range(0,len(booster_pack)):
		if len(booster_pack[i]) > 2:
			for j in range(0,len(booster_pack[i])):
				output_pack.append(booster_pack[i][j])
		else:
			output_pack.append(booster_pack[i])

	return (output_pack)

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
	print (str(total_chance) + " : " + str(foil_value)) 
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
 
if __name__ == '__main__':
	make_m19_pack()

