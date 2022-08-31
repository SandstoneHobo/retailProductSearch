import sqlite3 as sql

def connect(path):
    connection = sql.connect(path)
    return connection

def executeQuery(connection, query):
  cursor = connection.cursor()
  cursor.execute(query)
  connection.commit()

def executeReadQuery(connection, query):
  cursor = connection.cursor()
  result = None

  cursor.execute(query)
  result = cursor.fetchall()
  return result

path = "C:/Users/Merven Thomas/Desktop/PriceComparer/Database/database.sql"
db = connect(path)
