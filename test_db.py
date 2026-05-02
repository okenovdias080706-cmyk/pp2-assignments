import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="phonebook",
    user="postgres",
    password="YOUR_PASSWORD",
    port=5432
)

print("CONNECTED SUCCESSFULLY")
conn.close()
