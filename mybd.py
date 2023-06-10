import mysql.connector
#  to create a data base
dataBase = mysql.connector.connect(
    
    host = 'localhost',
    user = 'root',
    passwd = 'pass123',

)


# preper a cursor
crusorobject = dataBase.cursor()

# create a database
crusorobject.execute("CREATE DATABASE d_crm")

print("Created database")
