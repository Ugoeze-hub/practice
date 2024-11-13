import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="ugoeze",
  password="Luchiegaezy07+",
  database="myfirstdatabase"
)


mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), fav VARCHAR(255))")
mycursor.execute("CREATE TABLE products (id INT NOT NULL PRIMARY KEY, name VARCHAR(255))")
