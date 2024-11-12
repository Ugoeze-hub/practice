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

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Michelle", "Blue Village")
mycursor.execute(sql, val)

mydb.commit()

print("1 record inserted, ID:", mycursor.lastrowid)