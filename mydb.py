import mysql.connector

database = mysql.connector.connect(
    host = "db",
    user = 'root',
    passwd = 'Jack1998'
)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE ojijoco")
print("All done")