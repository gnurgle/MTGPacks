import mysql.connector as sql
from datetime import datetime
import time

def pullHistory(username):

	conn = sql.connect(
		host='localhost',
		user='gnurgle',
		password='ALR6K66EAA',
		database='mtg_db'
	)

	cur=conn.cursor()

#Overall Player
#Pull Total Number of Packs
def userTotalPacks(username):
	conn = sql.connect(
		host='localhost',
		user='gnurgle',
		password='ALR6K66EAA',
		database='mtg_db'
	)

	cur=conn.cursor()

	#Total number of packs
	cur.execute('SELECT COUNT(*) FROM User_History WHERE User_Id = %s',(username,))
	rows = cur.fetchone()

	cur.close()
	conn.close()
	
	return  int(rows[0])

#Pull Packs by Day
def userPacksByDay(username):

	conn = sql.connect(
		host='localhost',
		user='gnurgle',
		password='ALR6K66EAA',
		database='mtg_db'
	)

	cur=conn.cursor()

	#Packs by day
	cur.execute('SELECT CAST(DT AS DATE), COUNT(*) FROM User_History WHERE User_Id = %s GROUP BY CAST(DT AS DATE)',(username,))
	rows = cur.fetchall()

	cur.close()
	conn.close()
	
	return rows

#Packs by set
def userPacksBySet(username):

	conn = sql.connect(
		host='localhost',
		user='gnurgle',
		password='ALR6K66EAA',
		database='mtg_db'
	)

	cur=conn.cursor()

	#Packs by set
	cur.execute('SELECT Set_Id, COUNT(*) FROM User_History WHERE User_Id = %s GROUP BY Set_Id',(username,))
	rows = cur.fetchall()
	
	cur.close()
	conn.close()

	return rows

#Packs by Set and Day
def userPacksBySetDay(username,set):

	conn = sql.connect(
		host='localhost',
		user='gnurgle',
		password='ALR6K66EAA',
		database='mtg_db'
	)

	cur=conn.cursor()

	#Packs by set by day
	cur.execute('SELECT CAST(DT AS DATE), COUNT(*) FROM User_History WHERE User_Id = %s AND Set_Id = %s GROUP BY Set_Id, CAST(DT AS DATE)',(username,set))
	rows = cur.fetchall()

	cur.close()
	conn.close()
	
	return rows

#Sets Opened
def userSetsOpened(username):

	conn = sql.connect(
		host='localhost',
		user='gnurgle',
		password='ALR6K66EAA',
		database='mtg_db'
	)

	cur=conn.cursor()


	#Sets Opened
	cur.execute('SELECT Set_Id FROM User_History WHERE User_Id = %s GROUP BY Set_Id',(username,))
	rows = cur.fetchall()

	cur.close()
	conn.close()
	
	return rows

#Sets Opened
def userNumSetsOpened(username):

	conn = sql.connect(
		host='localhost',
		user='gnurgle',
		password='ALR6K66EAA',
		database='mtg_db'
	)

	cur=conn.cursor()


	#Sets Opened
	cur.execute('SELECT Set_Id, COUNT(*) FROM User_History WHERE User_Id = %s GROUP BY Set_Id',(username,))
	rows = cur.fetchall()

	cur.close()
	conn.close()
	
	return rows


#View foils by rarity
def userFoilRarity(username):

	conn = sql.connect(
		host='localhost',
		user='gnurgle',
		password='ALR6K66EAA',
		database='mtg_db'
	)

	cur=conn.cursor()

	#Make views for each position foils
	cur.execute('CREATE OR REPLACE VIEW Foil1 AS SELECT Pos1_Id AS Scryfall_Id FROM User_History WHERE User_Id = %s AND Pos1_Foil = 1',(username,))
	cur.execute('CREATE OR REPLACE VIEW Foil2 AS SELECT Pos2_Id AS Scryfall_Id FROM User_History WHERE User_Id = %s AND Pos2_Foil = 1',(username,))
	cur.execute('CREATE OR REPLACE VIEW Foil3 AS SELECT Pos3_Id AS Scryfall_Id FROM User_History WHERE User_Id = %s AND Pos3_Foil = 1',(username,))
	cur.execute('CREATE OR REPLACE VIEW Foil4 AS SELECT Pos4_Id AS Scryfall_Id FROM User_History WHERE User_Id = %s AND Pos4_Foil = 1',(username,))
	cur.execute('CREATE OR REPLACE VIEW Foil5 AS SELECT Pos5_Id AS Scryfall_Id FROM User_History WHERE User_Id = %s AND Pos5_Foil = 1',(username,))
	cur.execute('CREATE OR REPLACE VIEW Foil6 AS SELECT Pos6_Id AS Scryfall_Id FROM User_History WHERE User_Id = %s AND Pos6_Foil = 1',(username,))
	cur.execute('CREATE OR REPLACE VIEW Foil7 AS SELECT Pos7_Id AS Scryfall_Id FROM User_History WHERE User_Id = %s AND Pos7_Foil = 1',(username,))
	cur.execute('CREATE OR REPLACE VIEW Foil8 AS SELECT Pos8_Id AS Scryfall_Id FROM User_History WHERE User_Id = %s AND Pos8_Foil = 1',(username,))
	cur.execute('CREATE OR REPLACE VIEW Foil9 AS SELECT Pos9_Id AS Scryfall_Id FROM User_History WHERE User_Id = %s AND Pos9_Foil = 1',(username,))
	cur.execute('CREATE OR REPLACE VIEW Foil10 AS SELECT Pos10_Id AS Scryfall_Id FROM User_History WHERE User_Id = %s AND Pos10_Foil = 1',(username,))
	cur.execute('CREATE OR REPLACE VIEW Foil11 AS SELECT Pos11_Id AS Scryfall_Id FROM User_History WHERE User_Id = %s AND Pos11_Foil = 1',(username,))
	cur.execute('CREATE OR REPLACE VIEW Foil12 AS SELECT Pos12_Id AS Scryfall_Id FROM User_History WHERE User_Id = %s AND Pos12_Foil = 1',(username,))
	cur.execute('CREATE OR REPLACE VIEW Foil13 AS SELECT Pos13_Id AS Scryfall_Id FROM User_History WHERE User_Id = %s AND Pos13_Foil = 1',(username,))
	cur.execute('CREATE OR REPLACE VIEW Foil14 AS SELECT Pos14_Id AS Scryfall_Id FROM User_History WHERE User_Id = %s AND Pos14_Foil = 1',(username,))
	cur.execute('CREATE OR REPLACE VIEW Foil15 AS SELECT Pos15_Id AS Scryfall_Id FROM User_History WHERE User_Id = %s AND Pos15_Foil = 1',(username,))



	#Join all views to get a list of all cards  
	cur.execute('CREATE OR REPLACE VIEW User_Foils AS SELECT Scryfall_Id FROM Foil1 \
		UNION ALL SELECT Scryfall_Id FROM Foil2 \
		UNION ALL SELECT Scryfall_Id FROM Foil3 \
		UNION ALL SELECT Scryfall_Id FROM Foil4 \
		UNION ALL SELECT Scryfall_Id FROM Foil5 \
		UNION ALL SELECT Scryfall_Id FROM Foil6 \
		UNION ALL SELECT Scryfall_Id FROM Foil7 \
		UNION ALL SELECT Scryfall_Id FROM Foil8 \
		UNION ALL SELECT Scryfall_Id FROM Foil9 \
		UNION ALL SELECT Scryfall_Id FROM Foil10 \
		UNION ALL SELECT Scryfall_Id FROM Foil11 \
		UNION ALL SELECT Scryfall_Id FROM Foil12 \
		UNION ALL SELECT Scryfall_Id FROM Foil13 \
		UNION ALL SELECT Scryfall_Id FROM Foil14 \
		UNION ALL SELECT Scryfall_Id FROM Foil15')

	cur.execute('SELECT COUNT(*) FROM User_Foils')
	rows = cur.fetchall()


	#Get Rarity Types
	cur.execute('SELECT Card.Rarity, COUNT(*) FROM Card Right JOIN User_Foils ON Card.Scryfall_Id = User_Foils.Scryfall_Id GROUP BY Card.Rarity')

	rows = cur.fetchall()

	cur.close()
	conn.close()

	return rows

#Get all rarity types
def userRarity(username):

	conn = sql.connect(
		host='localhost',
		user='gnurgle',
		password='ALR6K66EAA',
		database='mtg_db'
	)

	cur=conn.cursor()

	#Make views for each position
	cur.execute('CREATE OR REPLACE VIEW AllPos1 AS SELECT Pos1_Id AS Scryfall_Id FROM User_History WHERE User_Id = %s',(username,))
	cur.execute('CREATE OR REPLACE VIEW AllPos2 AS SELECT Pos2_Id AS Scryfall_Id FROM User_History WHERE User_Id = %s',(username,))
	cur.execute('CREATE OR REPLACE VIEW AllPos3 AS SELECT Pos3_Id AS Scryfall_Id FROM User_History WHERE User_Id = %s',(username,))
	cur.execute('CREATE OR REPLACE VIEW AllPos4 AS SELECT Pos4_Id AS Scryfall_Id FROM User_History WHERE User_Id = %s',(username,))
	cur.execute('CREATE OR REPLACE VIEW AllPos5 AS SELECT Pos5_Id AS Scryfall_Id FROM User_History WHERE User_Id = %s',(username,))
	cur.execute('CREATE OR REPLACE VIEW AllPos6 AS SELECT Pos6_Id AS Scryfall_Id FROM User_History WHERE User_Id = %s',(username,))
	cur.execute('CREATE OR REPLACE VIEW AllPos7 AS SELECT Pos7_Id AS Scryfall_Id FROM User_History WHERE User_Id = %s',(username,))
	cur.execute('CREATE OR REPLACE VIEW AllPos8 AS SELECT Pos8_Id AS Scryfall_Id FROM User_History WHERE User_Id = %s',(username,))
	cur.execute('CREATE OR REPLACE VIEW AllPos9 AS SELECT Pos9_Id AS Scryfall_Id FROM User_History WHERE User_Id = %s',(username,))
	cur.execute('CREATE OR REPLACE VIEW AllPos10 AS SELECT Pos10_Id AS Scryfall_Id FROM User_History WHERE User_Id = %s',(username,))
	cur.execute('CREATE OR REPLACE VIEW AllPos11 AS SELECT Pos11_Id AS Scryfall_Id FROM User_History WHERE User_Id = %s',(username,))
	cur.execute('CREATE OR REPLACE VIEW AllPos12 AS SELECT Pos12_Id AS Scryfall_Id FROM User_History WHERE User_Id = %s',(username,))
	cur.execute('CREATE OR REPLACE VIEW AllPos13 AS SELECT Pos13_Id AS Scryfall_Id FROM User_History WHERE User_Id = %s',(username,))
	cur.execute('CREATE OR REPLACE VIEW AllPos14 AS SELECT Pos14_Id AS Scryfall_Id FROM User_History WHERE User_Id = %s',(username,))
	cur.execute('CREATE OR REPLACE VIEW AllPos15 AS SELECT Pos15_Id AS Scryfall_Id FROM User_History WHERE User_Id = %s',(username,))



	#Join all views to get a list of all cards  
	cur.execute('CREATE OR REPLACE VIEW User_AllPos AS SELECT Scryfall_Id FROM AllPos1 \
		UNION ALL SELECT Scryfall_Id FROM AllPos2 \
		UNION ALL SELECT Scryfall_Id FROM AllPos3 \
		UNION ALL SELECT Scryfall_Id FROM AllPos4 \
		UNION ALL SELECT Scryfall_Id FROM AllPos5 \
		UNION ALL SELECT Scryfall_Id FROM AllPos6 \
		UNION ALL SELECT Scryfall_Id FROM AllPos7 \
		UNION ALL SELECT Scryfall_Id FROM AllPos8 \
		UNION ALL SELECT Scryfall_Id FROM AllPos9 \
		UNION ALL SELECT Scryfall_Id FROM AllPos10 \
		UNION ALL SELECT Scryfall_Id FROM AllPos11 \
		UNION ALL SELECT Scryfall_Id FROM AllPos12 \
		UNION ALL SELECT Scryfall_Id FROM AllPos13 \
		UNION ALL SELECT Scryfall_Id FROM AllPos14 \
		UNION ALL SELECT Scryfall_Id FROM AllPos15')

	cur.execute('SELECT COUNT(*) FROM User_AllPos')
	rows = cur.fetchall()


	#Get Rarity Types
	cur.execute('SELECT Card.Rarity, Count(*) FROM Card Right JOIN User_AllPos ON Card.Scryfall_Id = User_AllPos.Scryfall_Id GROUP BY Card.Rarity')

	rows = cur.fetchall()

	cur.close()
	conn.close()

	return rows


#Get profit by time
def userEarning(username):

	conn = sql.connect(
		host='localhost',
		user='gnurgle',
		password='ALR6K66EAA',
		database='mtg_db'
	)

	cur=conn.cursor()

	#Join all views to get a list of all cards  
	cur.execute('CREATE OR REPLACE VIEW User_Prices AS SELECT Pos1_Price AS Price, CAST(DT AS DATE) AS Date FROM User_History WHERE User_Id = (%s) \
		UNION ALL SELECT Pos2_Price AS Price, CAST(DT AS DATE) FROM User_History WHERE User_Id = (%s) \
		UNION ALL SELECT Pos3_Price AS Price, CAST(DT AS DATE) FROM User_History WHERE User_Id = (%s) \
		UNION ALL SELECT Pos4_Price AS Price, CAST(DT AS DATE) FROM User_History WHERE User_Id = (%s) \
		UNION ALL SELECT Pos5_Price AS Price, CAST(DT AS DATE) FROM User_History WHERE User_Id = (%s) \
		UNION ALL SELECT Pos6_Price AS Price, CAST(DT AS DATE) FROM User_History WHERE User_Id = (%s) \
		UNION ALL SELECT Pos7_Price AS Price, CAST(DT AS DATE) FROM User_History WHERE User_Id = (%s) \
		UNION ALL SELECT Pos8_Price AS Price, CAST(DT AS DATE) FROM User_History WHERE User_Id = (%s) \
		UNION ALL SELECT Pos9_Price AS Price, CAST(DT AS DATE) FROM User_History WHERE User_Id = (%s) \
		UNION ALL SELECT Pos10_Price AS Price, CAST(DT AS DATE) FROM User_History WHERE User_Id = (%s) \
		UNION ALL SELECT Pos11_Price AS Price, CAST(DT AS DATE) FROM User_History WHERE User_Id = (%s) \
		UNION ALL SELECT Pos12_Price AS Price, CAST(DT AS DATE) FROM User_History WHERE User_Id = (%s) \
		UNION ALL SELECT Pos13_Price AS Price, CAST(DT AS DATE) FROM User_History WHERE User_Id = (%s) \
		UNION ALL SELECT Pos14_Price AS Price, CAST(DT AS DATE) FROM User_History WHERE User_Id = (%s) \
		UNION ALL SELECT Pos15_Price AS Price, CAST(DT AS DATE) FROM User_History WHERE User_Id = (%s)',\
		(username,username,username,username,username,username,username,username,username,username,\
		username,username,username,username,username))

	#Get Prices Types
	cur.execute('SELECT SUM(Price) FROM User_Prices')
	rows = cur.fetchall()

	cur.close()
	conn.close()
	
	return rows

#Total spent
def userTotalSpent(username):

	conn = sql.connect(
		host='localhost',
		user='gnurgle',
		password='ALR6K66EAA',
		database='mtg_db'
	)

	cur=conn.cursor()

	cur.execute('SELECT SUM(Booster_Price) FROM User_History WHERE User_Id = %s',(username,))
	rows = cur.fetchall()
	cur.close()
	conn.close()
	return rows

#Total earning by day
def userEarningByDate(username):

	conn = sql.connect(
		host='localhost',
		user='gnurgle',
		password='ALR6K66EAA',
		database='mtg_db'
	)

	cur=conn.cursor()

	#Join all views to get a list of all cards  
	cur.execute('CREATE OR REPLACE VIEW User_Prices AS SELECT Pos1_Price AS Price, CAST(DT AS DATE) AS Date FROM User_History WHERE User_Id = (%s) \
		UNION ALL SELECT Pos2_Price AS Price, CAST(DT AS DATE) FROM User_History WHERE User_Id = (%s) \
		UNION ALL SELECT Pos3_Price AS Price, CAST(DT AS DATE) FROM User_History WHERE User_Id = (%s) \
		UNION ALL SELECT Pos4_Price AS Price, CAST(DT AS DATE) FROM User_History WHERE User_Id = (%s) \
		UNION ALL SELECT Pos5_Price AS Price, CAST(DT AS DATE) FROM User_History WHERE User_Id = (%s) \
		UNION ALL SELECT Pos6_Price AS Price, CAST(DT AS DATE) FROM User_History WHERE User_Id = (%s) \
		UNION ALL SELECT Pos7_Price AS Price, CAST(DT AS DATE) FROM User_History WHERE User_Id = (%s) \
		UNION ALL SELECT Pos8_Price AS Price, CAST(DT AS DATE) FROM User_History WHERE User_Id = (%s) \
		UNION ALL SELECT Pos9_Price AS Price, CAST(DT AS DATE) FROM User_History WHERE User_Id = (%s) \
		UNION ALL SELECT Pos10_Price AS Price, CAST(DT AS DATE) FROM User_History WHERE User_Id = (%s) \
		UNION ALL SELECT Pos11_Price AS Price, CAST(DT AS DATE) FROM User_History WHERE User_Id = (%s) \
		UNION ALL SELECT Pos12_Price AS Price, CAST(DT AS DATE) FROM User_History WHERE User_Id = (%s) \
		UNION ALL SELECT Pos13_Price AS Price, CAST(DT AS DATE) FROM User_History WHERE User_Id = (%s) \
		UNION ALL SELECT Pos14_Price AS Price, CAST(DT AS DATE) FROM User_History WHERE User_Id = (%s) \
		UNION ALL SELECT Pos15_Price AS Price, CAST(DT AS DATE) FROM User_History WHERE User_Id = (%s)',\
		(username,username,username,username,username,username,username,username,username,username,\
		username,username,username,username,username))

	cur.execute('SELECT SUM(Price), Date FROM User_Prices GROUP BY Date')
	rows = cur.fetchall()
	cur.close()
	conn.close()
	return rows

#Total spent by Day
def userTotalSpentByDay(username):

	conn = sql.connect(
		host='localhost',
		user='gnurgle',
		password='ALR6K66EAA',
		database='mtg_db'
	)

	cur=conn.cursor()

	cur.execute('SELECT SUM(Booster_Price), CAST(DT AS DATE) FROM User_History WHERE User_Id = %s GROUP BY CAST(DT AS DATE)',(username,))
	rows = cur.fetchall()
	cur.close()
	conn.close()

	return rows



#Per Set Player
#Pull Packs by Day
def userPacksByDaySet(username,set):

	conn = sql.connect(
		host='localhost',
		user='gnurgle',
		password='ALR6K66EAA',
		database='mtg_db'
	)

	cur=conn.cursor()

	#Packs by day
	cur.execute('SELECT CAST(DT AS DATE), COUNT(*) FROM User_History WHERE User_Id = %s AND Set_Id = %s GROUP BY CAST(DT AS DATE)',(username,set))
	rows = cur.fetchall()

	cur.close()
	conn.close()

	return rows


#View foils by rarity
def userFoilRarityBySet(username,set):

	conn = sql.connect(
		host='localhost',
		user='gnurgle',
		password='ALR6K66EAA',
		database='mtg_db'
	)

	cur=conn.cursor()
	cur.execute('CREATE OR REPLACE VIEW User_Set AS SELECT * FROM User_History WHERE User_Id = %s AND Set_Id = %s',(username,set))

	#Make views for each position foils
	cur.execute('CREATE OR REPLACE VIEW Foil1 AS SELECT Pos1_Id AS Scryfall_Id FROM User_Set WHERE User_Id = %s AND Pos1_Foil = 1',(username,))
	cur.execute('CREATE OR REPLACE VIEW Foil2 AS SELECT Pos2_Id AS Scryfall_Id FROM User_Set WHERE User_Id = %s AND Pos2_Foil = 1',(username,))
	cur.execute('CREATE OR REPLACE VIEW Foil3 AS SELECT Pos3_Id AS Scryfall_Id FROM User_Set WHERE User_Id = %s AND Pos3_Foil = 1',(username,))
	cur.execute('CREATE OR REPLACE VIEW Foil4 AS SELECT Pos4_Id AS Scryfall_Id FROM User_Set WHERE User_Id = %s AND Pos4_Foil = 1',(username,))
	cur.execute('CREATE OR REPLACE VIEW Foil5 AS SELECT Pos5_Id AS Scryfall_Id FROM User_Set WHERE User_Id = %s AND Pos5_Foil = 1',(username,))
	cur.execute('CREATE OR REPLACE VIEW Foil6 AS SELECT Pos6_Id AS Scryfall_Id FROM User_Set WHERE User_Id = %s AND Pos6_Foil = 1',(username,))
	cur.execute('CREATE OR REPLACE VIEW Foil7 AS SELECT Pos7_Id AS Scryfall_Id FROM User_Set WHERE User_Id = %s AND Pos7_Foil = 1',(username,))
	cur.execute('CREATE OR REPLACE VIEW Foil8 AS SELECT Pos8_Id AS Scryfall_Id FROM User_Set WHERE User_Id = %s AND Pos8_Foil = 1',(username,))
	cur.execute('CREATE OR REPLACE VIEW Foil9 AS SELECT Pos9_Id AS Scryfall_Id FROM User_Set WHERE User_Id = %s AND Pos9_Foil = 1',(username,))
	cur.execute('CREATE OR REPLACE VIEW Foil10 AS SELECT Pos10_Id AS Scryfall_Id FROM User_Set WHERE User_Id = %s AND Pos10_Foil = 1',(username,))
	cur.execute('CREATE OR REPLACE VIEW Foil11 AS SELECT Pos11_Id AS Scryfall_Id FROM User_Set WHERE User_Id = %s AND Pos11_Foil = 1',(username,))
	cur.execute('CREATE OR REPLACE VIEW Foil12 AS SELECT Pos12_Id AS Scryfall_Id FROM User_Set WHERE User_Id = %s AND Pos12_Foil = 1',(username,))
	cur.execute('CREATE OR REPLACE VIEW Foil13 AS SELECT Pos13_Id AS Scryfall_Id FROM User_Set WHERE User_Id = %s AND Pos13_Foil = 1',(username,))
	cur.execute('CREATE OR REPLACE VIEW Foil14 AS SELECT Pos14_Id AS Scryfall_Id FROM User_Set WHERE User_Id = %s AND Pos14_Foil = 1',(username,))
	cur.execute('CREATE OR REPLACE VIEW Foil15 AS SELECT Pos15_Id AS Scryfall_Id FROM User_Set WHERE User_Id = %s AND Pos15_Foil = 1',(username,))



	#Join all views to get a list of all cards  
	cur.execute('CREATE OR REPLACE VIEW User_Foils AS SELECT Scryfall_Id FROM Foil1 \
		UNION ALL SELECT Scryfall_Id FROM Foil2 \
		UNION ALL SELECT Scryfall_Id FROM Foil3 \
		UNION ALL SELECT Scryfall_Id FROM Foil4 \
		UNION ALL SELECT Scryfall_Id FROM Foil5 \
		UNION ALL SELECT Scryfall_Id FROM Foil6 \
		UNION ALL SELECT Scryfall_Id FROM Foil7 \
		UNION ALL SELECT Scryfall_Id FROM Foil8 \
		UNION ALL SELECT Scryfall_Id FROM Foil9 \
		UNION ALL SELECT Scryfall_Id FROM Foil10 \
		UNION ALL SELECT Scryfall_Id FROM Foil11 \
		UNION ALL SELECT Scryfall_Id FROM Foil12 \
		UNION ALL SELECT Scryfall_Id FROM Foil13 \
		UNION ALL SELECT Scryfall_Id FROM Foil14 \
		UNION ALL SELECT Scryfall_Id FROM Foil15')

	cur.execute('SELECT COUNT(*) FROM User_Foils')
	rows = cur.fetchall()


	#Get Rarity Types
	cur.execute('SELECT Card.Rarity, COUNT(*) FROM Card Right JOIN User_Foils ON Card.Scryfall_Id = User_Foils.Scryfall_Id GROUP BY Card.Rarity')

	rows = cur.fetchall()

	cur.close()
	conn.close()

	return rows

#Get all rarity types
def userRarityBySet(username,set):

	conn = sql.connect(
		host='localhost',
		user='gnurgle',
		password='ALR6K66EAA',
		database='mtg_db'
	)

	cur=conn.cursor()
	cur.execute('CREATE OR REPLACE VIEW User_Set AS SELECT * FROM User_History WHERE User_Id = %s AND Set_Id = %s',(username,set))

	#Make views for each position
	cur.execute('CREATE OR REPLACE VIEW AllPos1 AS SELECT Pos1_Id AS Scryfall_Id FROM User_Set WHERE User_Id = %s',(username,))
	cur.execute('CREATE OR REPLACE VIEW AllPos2 AS SELECT Pos2_Id AS Scryfall_Id FROM User_Set WHERE User_Id = %s',(username,))
	cur.execute('CREATE OR REPLACE VIEW AllPos3 AS SELECT Pos3_Id AS Scryfall_Id FROM User_Set WHERE User_Id = %s',(username,))
	cur.execute('CREATE OR REPLACE VIEW AllPos4 AS SELECT Pos4_Id AS Scryfall_Id FROM User_Set WHERE User_Id = %s',(username,))
	cur.execute('CREATE OR REPLACE VIEW AllPos5 AS SELECT Pos5_Id AS Scryfall_Id FROM User_Set WHERE User_Id = %s',(username,))
	cur.execute('CREATE OR REPLACE VIEW AllPos6 AS SELECT Pos6_Id AS Scryfall_Id FROM User_Set WHERE User_Id = %s',(username,))
	cur.execute('CREATE OR REPLACE VIEW AllPos7 AS SELECT Pos7_Id AS Scryfall_Id FROM User_Set WHERE User_Id = %s',(username,))
	cur.execute('CREATE OR REPLACE VIEW AllPos8 AS SELECT Pos8_Id AS Scryfall_Id FROM User_Set WHERE User_Id = %s',(username,))
	cur.execute('CREATE OR REPLACE VIEW AllPos9 AS SELECT Pos9_Id AS Scryfall_Id FROM User_Set WHERE User_Id = %s',(username,))
	cur.execute('CREATE OR REPLACE VIEW AllPos10 AS SELECT Pos10_Id AS Scryfall_Id FROM User_Set WHERE User_Id = %s',(username,))
	cur.execute('CREATE OR REPLACE VIEW AllPos11 AS SELECT Pos11_Id AS Scryfall_Id FROM User_Set WHERE User_Id = %s',(username,))
	cur.execute('CREATE OR REPLACE VIEW AllPos12 AS SELECT Pos12_Id AS Scryfall_Id FROM User_Set WHERE User_Id = %s',(username,))
	cur.execute('CREATE OR REPLACE VIEW AllPos13 AS SELECT Pos13_Id AS Scryfall_Id FROM User_Set WHERE User_Id = %s',(username,))
	cur.execute('CREATE OR REPLACE VIEW AllPos14 AS SELECT Pos14_Id AS Scryfall_Id FROM User_Set WHERE User_Id = %s',(username,))
	cur.execute('CREATE OR REPLACE VIEW AllPos15 AS SELECT Pos15_Id AS Scryfall_Id FROM User_Set WHERE User_Id = %s',(username,))



	#Join all views to get a list of all cards  
	cur.execute('CREATE OR REPLACE VIEW User_AllPos AS SELECT Scryfall_Id FROM AllPos1 \
		UNION ALL SELECT Scryfall_Id FROM AllPos2 \
		UNION ALL SELECT Scryfall_Id FROM AllPos3 \
		UNION ALL SELECT Scryfall_Id FROM AllPos4 \
		UNION ALL SELECT Scryfall_Id FROM AllPos5 \
		UNION ALL SELECT Scryfall_Id FROM AllPos6 \
		UNION ALL SELECT Scryfall_Id FROM AllPos7 \
		UNION ALL SELECT Scryfall_Id FROM AllPos8 \
		UNION ALL SELECT Scryfall_Id FROM AllPos9 \
		UNION ALL SELECT Scryfall_Id FROM AllPos10 \
		UNION ALL SELECT Scryfall_Id FROM AllPos11 \
		UNION ALL SELECT Scryfall_Id FROM AllPos12 \
		UNION ALL SELECT Scryfall_Id FROM AllPos13 \
		UNION ALL SELECT Scryfall_Id FROM AllPos14 \
		UNION ALL SELECT Scryfall_Id FROM AllPos15')

	cur.execute('SELECT COUNT(*) FROM User_AllPos')
	rows = cur.fetchall()


	#Get Rarity Types
	cur.execute('SELECT Card.Rarity, Count(*) FROM Card Right JOIN User_AllPos ON Card.Scryfall_Id = User_AllPos.Scryfall_Id GROUP BY Card.Rarity')

	rows = cur.fetchall()

	cur.close()
	conn.close()

	return rows


#Total earning by day
def userEarningByDateSet(username,set):

	conn = sql.connect(
		host='localhost',
		user='gnurgle',
		password='ALR6K66EAA',
		database='mtg_db'
	)

	cur=conn.cursor()
	cur.execute('CREATE OR REPLACE VIEW User_Set AS SELECT * FROM User_History WHERE User_Id = %s AND Set_Id = %s',(username,set))

	#Join all views to get a list of all cards  
	cur.execute('CREATE OR REPLACE VIEW User_Prices AS SELECT Pos1_Price AS Price, CAST(DT AS DATE) AS Date FROM User_Set WHERE User_Id = (%s) \
		UNION ALL SELECT Pos2_Price AS Price, CAST(DT AS DATE) FROM User_Set WHERE User_Id = (%s) \
		UNION ALL SELECT Pos3_Price AS Price, CAST(DT AS DATE) FROM User_Set WHERE User_Id = (%s) \
		UNION ALL SELECT Pos4_Price AS Price, CAST(DT AS DATE) FROM User_Set WHERE User_Id = (%s) \
		UNION ALL SELECT Pos5_Price AS Price, CAST(DT AS DATE) FROM User_Set WHERE User_Id = (%s) \
		UNION ALL SELECT Pos6_Price AS Price, CAST(DT AS DATE) FROM User_Set WHERE User_Id = (%s) \
		UNION ALL SELECT Pos7_Price AS Price, CAST(DT AS DATE) FROM User_Set WHERE User_Id = (%s) \
		UNION ALL SELECT Pos8_Price AS Price, CAST(DT AS DATE) FROM User_Set WHERE User_Id = (%s) \
		UNION ALL SELECT Pos9_Price AS Price, CAST(DT AS DATE) FROM User_Set WHERE User_Id = (%s) \
		UNION ALL SELECT Pos10_Price AS Price, CAST(DT AS DATE) FROM User_Set WHERE User_Id = (%s) \
		UNION ALL SELECT Pos11_Price AS Price, CAST(DT AS DATE) FROM User_Set WHERE User_Id = (%s) \
		UNION ALL SELECT Pos12_Price AS Price, CAST(DT AS DATE) FROM User_Set WHERE User_Id = (%s) \
		UNION ALL SELECT Pos13_Price AS Price, CAST(DT AS DATE) FROM User_Set WHERE User_Id = (%s) \
		UNION ALL SELECT Pos14_Price AS Price, CAST(DT AS DATE) FROM User_Set WHERE User_Id = (%s) \
		UNION ALL SELECT Pos15_Price AS Price, CAST(DT AS DATE) FROM User_Set WHERE User_Id = (%s)',\
		(username,username,username,username,username,username,username,username,username,username,\
		username,username,username,username,username))

	cur.execute('SELECT SUM(Price), Date FROM User_Prices GROUP BY Date')
	rows = cur.fetchall()
	cur.close()
	conn.close()
	return rows

#Total spent by Day
def userTotalSpentByDaySet(username,set):

	conn = sql.connect(
		host='localhost',
		user='gnurgle',
		password='ALR6K66EAA',
		database='mtg_db'
	)

	cur=conn.cursor()

	cur.execute('SELECT SUM(Booster_Price), CAST(DT AS DATE) FROM User_History WHERE User_Id = %s AND Set_Id = %s GROUP BY CAST(DT AS DATE)',(username,set))
	rows = cur.fetchall()
	cur.close()
	conn.close()

	return rows

#Total spent by Day
def overallPacks():

	conn = sql.connect(
		host='localhost',
		user='gnurgle',
		password='ALR6K66EAA',
		database='mtg_db'
	)

	cur=conn.cursor()

	cur.execute('SELECT Set_Id, COUNT(*) FROM User_History GROUP BY Set_Id')
	rows = cur.fetchall()
	cur.close()
	conn.close()

	return rows

#Total spent by Day
def overallUserPacks():

	conn = sql.connect(
		host='localhost',
		user='gnurgle',
		password='ALR6K66EAA',
		database='mtg_db'
	)

	cur=conn.cursor()

	cur.execute('SELECT User_Id, COUNT(*) FROM User_History GROUP BY User_Id')
	rows = cur.fetchall()
	cur.close()
	conn.close()

	return rows[0:5]

#Check if card was a Foil
def cf(card):
	if card == 'foil':
		return True
	else:
		return False

if __name__=="__main__":
	pullHistory('Johnny')
