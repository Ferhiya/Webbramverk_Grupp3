import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="shop20220128"
)

print("✅ Anslutning lyckades!")
conn.close()
