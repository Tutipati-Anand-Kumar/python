import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="RKCE",

)
c=mydb.cursor()
c.execute("create table student (sid int, sname varchar(30),marks int, city varchar(30))")