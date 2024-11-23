import mysql.connector
from heslo.py import passwordMySQL

mydb = mysql.connector.connect(
    host="localhost"
    user="root"
    password=passwordMySQL
    database ="saveOceanTest"
)

