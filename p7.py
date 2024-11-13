import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="ugoeze",
  password="Luchiegaezy07+",
  database="myfirstdatabase"
)

mycursor = mydb.cursor()

# sql = "INSERT INTO users (name, fav) VALUES (%s, %s)"
# val = [
#     ("John", "154"),
#     ("Peter", "154"),
#     ("Amy", "155"),
#     ("Hannah", ""),
#     ("Michael", "")
# ]
# mycursor.executemany(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "record inserted.")

sql = "INSERT INTO products (id, name) VALUES (%s, %s)"
val = [
    ('154', 'Chocolate Heaven'),
    ('155', 'Tasty Lemons'),
    ('156', 'Vanilla Dreams')
]
mycursor.executemany(sql, val)


mydb.commit()

print(mycursor.rowcount, "record inserted.")