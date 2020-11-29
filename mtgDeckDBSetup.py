import mysql.connector as sql

#Create initial DB
conn = sql.connect(
	host="localhost",
	user="gnurgle",
	password="ALR6K66EAA"
)

cur = conn.cursor()
cur.execute("CREATE DATABASE mtg_db")

#Create Tables
conn = sql.connect(
	host="localhost",
	user="gnurgle",
	password="ALR6K66EAA",
	database="mtg_db"
)

cur = conn.cursor()

cur.execute('CREATE TABLE Sets (Set_Id CHAR(5),\
Set_Name CHAR(40),\
Year INT,\
Num_Cards INT,\
Booster_Price DECIMAL(8,2),\
Pack_Size INT,\
Land INT,\
Common INT,\
Uncommon INT,\
Rare_Mythic INT,\
Rare_Chance INT,\
Mythic_chance INT,\
Foil_Chance INT,\
Foil_Common INT,\
Foil_Uncommon INT,\
Foil_Rare INT,\
Foil_Mythic INT,\
Foil_Land INT,\
PRIMARY KEY(Set_Id))')

cur.execute('CREATE TABLE Card (Number INT,\
Name CHAR(30),\
Set_Id CHAR(5),\
Rarity Char(10),\
Color CHAR(15),\
Layout CHAR(15),\
Booster BIT,\
Scryfall_Id CHAR(70),\
Has_Foil BIT,\
Has_NonFoil BIT,\
Is_Promo BIT,\
Is_Land BIT,\
PRIMARY KEY(Scryfall_Id),\
FOREIGN KEY(Set_Id) REFERENCES Sets(Set_Id) ON UPDATE CASCADE)')

cur.execute('CREATE TABLE Card_Images (Scryfall_Id CHAR(70),\
Num_sides INT,\
Price DECIMAL(8,2),\
Price_Foil DECIMAL(8,2),\
Front_Image CHAR(80),\
Back_Image CHAR(80),\
PRIMARY KEY(Scryfall_ID),\
FOREIGN KEY(Scryfall_ID) REFERENCES Card(Scryfall_ID) ON UPDATE CASCADE)') 

cur.execute('CREATE TABLE Users(User_Id CHAR(30),\
Username CHAR(20),\
Password CHAR(80),\
PRIMARY KEY(User_Id))')

cur.close()
conn.close()


