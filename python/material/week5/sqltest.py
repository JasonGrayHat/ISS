import pymysql

host = "ictceweb.ict.sait.ca"
username = "instructors"
password = "con Ed"
databaseName = "cprg104"

db = pymysql.connect(host,username,password,databaseName)
cursor = db.cursor()

db.close()


#####################CREATE
#sql = 'INSERT INTO `student`(`first_name`,`last_name`,`phone`) VALUES("{}","{}","{}")'.format("Robert","Doerksen","1-587-971-7142")
#cursor.execute(sql)
#db.commit()


#####################READ
#sql = 'SELECT * FROM `student`'
#cursor.execute(sql)
#results = cursor.fetchall()
#for row in results:
#	for cell in row:
#		print(cell, end = '\t')
#	print()

##################UPDATE
#sql = 'UPDATE `student` SET `first_name` = "{}" WHERE `id` = {}'.format("Bob")
#cursor.execute(sql)
#db.commit()


####################DELETE
#sql = 'DELETE FROM `student` WHERE `id` = {}'.format(1)
#cursor.execute(sql)
#db.commit()

######################VERSION
#cursor.execute("SELECT VERSION()")
#data = cursor.fetchone()#

#print("Database Version :",data)