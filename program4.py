import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="rkce",

)
c=mydb.cursor()
c.execute("update employee set city='hyderavad' where eid=101")
mydb.commit()