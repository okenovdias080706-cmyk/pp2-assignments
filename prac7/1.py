import psycopg2

# ---------------- CONNECTION ----------------
try:
    conn = psycopg2.connect(
        dbname="mydb",        # өз базаң
        user="postgres",
        password="1234",      # өз паролің
        host="localhost",
        port="5432"
    )

    cursor = conn.cursor()
    print("✅ Connected to PostgreSQL")

    # ---------------- CREATE TABLE ----------------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            age INT,
            email VARCHAR(100)
        )
    """)
    conn.commit()
    print("✅ Table created")

    # ---------------- INSERT ----------------
    cursor.execute(
        "INSERT INTO users (name, age, email) VALUES (%s, %s, %s)",
        ("Dias", 18, "dias@mail.com")
    )
    conn.commit()
    print("✅ Data inserted")

    # ---------------- BATCH INSERT ----------------
    data = [
        ("Ali", 20, "ali@mail.com"),
        ("Aruzhan", 19, "aru@mail.com")
    ]

    cursor.executemany(
        "INSERT INTO users (name, age, email) VALUES (%s, %s, %s)",
        data
    )
    conn.commit()
    print("✅ Batch inserted")

    # ---------------- SELECT ----------------
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    print("\n📊 Users:")
    for row in rows:
        print(row)

    # ---------------- UPDATE ----------------
    cursor.execute(
        "UPDATE users SET age = %s WHERE name = %s",
        (25, "Ali")
    )
    conn.commit()
    print("✅ Updated")

    # ---------------- DELETE ----------------
    cursor.execute(
        "DELETE FROM users WHERE name = %s",
        ("Aruzhan",)
    )
    conn.commit()
    print("✅ Deleted")

    # ---------------- FINAL SELECT ----------------
    cursor.execute("SELECT * FROM users")
    print("\n📊 Final data:")
    print(cursor.fetchall())

# ---------------- ERROR HANDLING ----------------
except Exception as e:
    print("❌ Error:", e)
    conn.rollback()

# ---------------- CLOSE ----------------
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
    print("🔒 Connection closed")