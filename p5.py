import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="ugoeze",
  password="Luchiegaezy07+",
  database="myfirstdatabase"
)

#this is if the table doesn't exist
# mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
# mycursor = mydb.cursor()



mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)