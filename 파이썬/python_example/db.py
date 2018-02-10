import MySQLdb as mydb
db=mydb.connect("localhost","root","cho123","zabbix")
cur=db.cursor()
cur.execute("select * from users")
while True:
	users=cur.fetchone()
	if not users:
		break
	print users
cur.close()
db.close()
