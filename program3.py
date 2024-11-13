import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="rkce",

)
c=mydb.cursor()
c.execute("delete from employee where eid=102")
mydb.commit()