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
Front_Image CHAR(102),\
Back_Image CHAR(102),\
PRIMARY KEY(Scryfall_ID),\
FOREIGN KEY(Scryfall_ID) REFERENCES Card(Scryfall_ID) ON UPDATE CASCADE)') 

cur.execute('CREATE TABLE Users (User_Id CHAR(30),\
Email CHAR(30),\
Password CHAR(30),\
PRIMARY KEY(User_Id))')

cur.execute('CREATE TABLE User_History (User_Id CHAR(30),\
Booster_Price DECIMAL(8,2),\
Set_Id CHAR(5),\
Pos1_Id CHAR(70),\
Pos1_Price DECIMAL(8,2),\
Pos1_Foil BIT,\
Pos2_Id CHAR(70),\
Pos2_Price DECIMAL(8,2),\
Pos2_Foil BIT,\
Pos3_Id CHAR(70),\
Pos3_Price DECIMAL(8,2),\
Pos3_Foil BIT,\
Pos4_Id CHAR(70),\
Pos4_Price DECIMAL(8,2),\
Pos4_Foil BIT,\
Pos5_Id CHAR(70),\
Pos5_Price DECIMAL(8,2),\
Pos5_Foil BIT,\
Pos6_Id CHAR(70),\
Pos6_Price DECIMAL(8,2),\
Pos6_Foil BIT,\
Pos7_Id CHAR(70),\
Pos7_Price DECIMAL(8,2),\
Pos7_Foil BIT,\
Pos8_Id CHAR(70),\
Pos8_Price DECIMAL(8,2),\
Pos8_Foil BIT,\
Pos9_Id CHAR(70),\
Pos9_Price DECIMAL(8,2),\
Pos9_Foil BIT,\
Pos10_Id CHAR(70),\
Pos10_Price DECIMAL(8,2),\
Pos10_Foil BIT,\
Pos11_Id CHAR(70),\
Pos11_Price DECIMAL(8,2),\
Pos11_Foil BIT,\
Pos12_Id CHAR(70),\
Pos12_Price DECIMAL(8,2),\
Pos12_Foil BIT,\
Pos13_Id CHAR(70),\
Pos13_Price DECIMAL(8,2),\
Pos13_Foil BIT,\
Pos14_Id CHAR(70),\
Pos14_Price DECIMAL(8,2),\
Pos14_Foil BIT,\
Pos15_Id CHAR(70),\
Pos15_Price DECIMAL(8,2),\
Pos15_Foil BIT,\
DT DATETIME,\
PRIMARY KEY (User_ID, DT),\
FOREIGN KEY (Pos1_ID) REFERENCES Card(Scryfall_Id) ON UPDATE CASCADE,\
FOREIGN KEY (Pos2_ID) REFERENCES Card(Scryfall_Id) ON UPDATE CASCADE,\
FOREIGN KEY (Pos3_ID) REFERENCES Card(Scryfall_Id) ON UPDATE CASCADE,\
FOREIGN KEY (Pos4_ID) REFERENCES Card(Scryfall_Id) ON UPDATE CASCADE,\
FOREIGN KEY (Pos5_ID) REFERENCES Card(Scryfall_Id) ON UPDATE CASCADE,\
FOREIGN KEY (Pos6_ID) REFERENCES Card(Scryfall_Id) ON UPDATE CASCADE,\
FOREIGN KEY (Pos7_ID) REFERENCES Card(Scryfall_Id) ON UPDATE CASCADE,\
FOREIGN KEY (Pos8_ID) REFERENCES Card(Scryfall_Id) ON UPDATE CASCADE,\
FOREIGN KEY (Pos9_ID) REFERENCES Card(Scryfall_Id) ON UPDATE CASCADE,\
FOREIGN KEY (Pos10_ID) REFERENCES Card(Scryfall_Id) ON UPDATE CASCADE,\
FOREIGN KEY (Pos11_ID) REFERENCES Card(Scryfall_Id) ON UPDATE CASCADE,\
FOREIGN KEY (Pos12_ID) REFERENCES Card(Scryfall_Id) ON UPDATE CASCADE,\
FOREIGN KEY (Pos13_ID) REFERENCES Card(Scryfall_Id) ON UPDATE CASCADE,\
FOREIGN KEY (Pos14_ID) REFERENCES Card(Scryfall_Id) ON UPDATE CASCADE,\
FOREIGN KEY (Pos15_ID) REFERENCES Card(Scryfall_Id) ON UPDATE CASCADE)')

cur.close()
conn.close()


