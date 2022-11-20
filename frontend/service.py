import tkinter
import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="qwerty67",
    database="kin"


)
cur=mydb.cursor()
sql="CREATE TABLE KIN (ID not null, firstname varchat(20))"
cur.execute(sql)




