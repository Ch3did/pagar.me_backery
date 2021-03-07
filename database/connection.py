import mysql.connector

def get_connection(config):
  mydb = mysql.connector.connect(
    host=config["host"],
    user=config["user"],
    password=config["password"],
    database=config["database"]
  )
  return mydb
    