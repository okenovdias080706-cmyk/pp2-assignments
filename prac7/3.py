import psycopg2

conn = psycopg2.connect(
    dbname="test",
    user="postgres",
    password="1234",
    host="localhost"
)

cur = conn.cursor()
cur.execute("SELECT * FROM users")
rows = cur.fetchall()

for row in rows:
    print(row)