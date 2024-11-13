import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="anand",

)
c=mydb.cursor()
c.execute("insert into student values(102, 'anand kumar', 96, 'vijayawada' )")
mydb.commit()