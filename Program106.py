import mysql.connector
from mysql.connector import Error

try:
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = ""
    )

    if mydb.is_connected():
        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE IF NOT EXISTS Ryusui")
        print("Database 'Ryusui' created successfully or already exists")

except Error as e:
    print(f"Error: {e}")
