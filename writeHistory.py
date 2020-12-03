import mysql.connector as sql
from datetime import datetime
import time

def addUserHistory(username,data):

	now = datetime.now()
	#now.strftime('%Y-%m-%d %H:%M:%S')
	
	conn = sql.connect(
		host='localhost',
		user='gnurgle',
		password='ALR6K66EAA',
		database='mtg_db'
	)

	cur=conn.cursor()
#Set results of pack to user History
#Yeah, it's a lot
	cur.execute('INSERT INTO User_History (User_Id,Booster_Price,Set_Id,\
		Pos1_Id,Pos1_Price,Pos1_Foil,\
		Pos2_Id,Pos2_Price,Pos2_Foil,\
		Pos3_Id,Pos3_Price,Pos3_Foil,\
		Pos4_Id,Pos4_Price,Pos4_Foil,\
		Pos5_Id,Pos5_Price,Pos5_Foil,\
		Pos6_Id,Pos6_Price,Pos6_Foil,\
		Pos7_Id,Pos7_Price,Pos7_Foil,\
		Pos8_Id,Pos8_Price,Pos8_Foil,\
		Pos9_Id,Pos9_Price,Pos9_Foil,\
		Pos10_Id,Pos10_Price,Pos10_Foil,\
		Pos11_Id,Pos11_Price,Pos11_Foil,\
		Pos12_Id,Pos12_Price,Pos12_Foil,\
		Pos13_Id,Pos13_Price,Pos13_Foil,\
		Pos14_Id,Pos14_Price,Pos14_Foil,\
		Pos15_Id,Pos15_Price,Pos15_Foil,\
		DT) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,\
		%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',\
		(username,data[0][3],data[0][4],\
		data[1][0][0],data[1][0][4],cf(data[0][5][0]),\
		data[2][0][0],data[2][0][4],cf(data[0][5][1]),\
		data[3][0][0],data[3][0][4],cf(data[0][5][2]),\
		data[4][0][0],data[4][0][4],cf(data[0][5][3]),\
		data[5][0][0],data[5][0][4],cf(data[0][5][4]),\
		data[6][0][0],data[6][0][4],cf(data[0][5][5]),\
		data[7][0][0],data[7][0][4],cf(data[0][5][6]),\
		data[8][0][0],data[8][0][4],cf(data[0][5][7]),\
		data[9][0][0],data[9][0][4],cf(data[0][5][8]),\
		data[10][0][0],data[10][0][4],cf(data[0][5][9]),\
		data[11][0][0],data[11][0][4],cf(data[0][5][10]),\
		data[12][0][0],data[12][0][4],cf(data[0][5][11]),\
		data[13][0][0],data[13][0][4],cf(data[0][5][12]),\
		data[14][0][0],data[14][0][4],cf(data[0][5][13]),\
		data[15][0][0],data[15][0][4],cf(data[0][5][14]),\
		now.strftime('%Y-%m-%d %H:%M:%S')))

	conn.commit()

	cur.close()
	conn.close()
#Remove History
def removeHistory(username):
	conn = sql.connect(
		host='localhost',
		user='gnurgle',
		password='ALR6K66EAA',
		database='mtg_db'
	)
	print (username)
	cur=conn.cursor()
	cur.execute('DELETE FROM User_History WHERE User_Id = %s',(username,))
	conn.commit()
	cur.close()
	conn.close()

#Check if card was a Foil
def cf(card):
	if card == 'foil':
		return True
	else:
		return False
