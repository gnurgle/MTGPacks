import mysql.connector as sql

def input_data(id,name,yr,num,p,sz,l,c,u,r,rc,mc,f_c,fc,fu,fr,fm,fl):

	conn = sql.connect(
		host="localhost"
		user="gnurgle"
		password="ALR6K66EAA"
	)

	cur = conn.cursor()
	cur.execute("INSERT IGNORE INTO Sets VALUES \
		(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",\
		(id,name,yr,num,p,sz,l,c,u,r,rc,mc,f_c,fc,fu,fr,fm,fl)

	conn.commit()

	curr.close()
	conn.close()

if __name__='__main__':
	input_data(id,name,yr,num,p,sz,l,c,u,r,rc,mc,f_c,fc,fu,fr,fm,fl)
	
