import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="schedule"
)

cursor = db.cursor()
sql="CREATE TABLE IF NOT EXISTS activities (number INT(4) AUTO_INCREMENT, category VARCHAR(255),name VARCHAR(255),duration INT(4), PRIMARY KEY (number))"

cursor.execute(sql)

db.close()
cursor.close()