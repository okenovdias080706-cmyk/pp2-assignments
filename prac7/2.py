import psycopg2

conn = psycopg2.connect(
    dbname="phonebook_db",
    user="postgres",
    password="YOUR_PASSWORD",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()
print("Connected to PostgreSQL!")

#Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS contacts (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    phone VARCHAR(20) UNIQUE
)
""")
conn.commit()

#Inserting Rows
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
phone = input("Enter phone number: ")

cursor.execute(
    "INSERT INTO contacts (first_name, last_name, phone) VALUES (%s, %s, %s)",
    (first_name, last_name, phone)
)
conn.commit()
print("Contact added")

#Querying Data
cursor.execute("SELECT * FROM contacts")
for contact in cursor.fetchall():
    print(contact)

#Updating Existing Rows
old_phone = input("Enter phone number to update: ")
new_first_name = input("New first name (leave empty if no change): ")
new_phone = input("New phone number (leave empty if no change): ")

if new_first_name:
    cursor.execute("UPDATE contacts SET first_name = %s WHERE phone = %s",
                   (new_first_name, old_phone))
if new_phone:
    cursor.execute("UPDATE contacts SET phone = %s WHERE phone = %s",
                   (new_phone, old_phone))
conn.commit()
print("Contact updated")

#Deleting Rows
delete_choice = input("Delete by (1) Name or (2) Phone? ")

if delete_choice == "1":
    name = input("Enter first name to delete: ")
    cursor.execute("DELETE FROM contacts WHERE first_name = %s", (name,))
elif delete_choice == "2":
    phone = input("Enter phone to delete: ")
    cursor.execute("DELETE FROM contacts WHERE phone = %s", (phone,))
conn.commit()
print("Contact deleted")

#Handling Transactions and Error Recovery
try:
    cursor.execute("INSERT INTO contacts (first_name, last_name, phone) VALUES (%s,%s,%s)",
                   ("Test", "User", "123456789"))
    conn.commit()
except Exception as e:
    print("Error:", e)
    conn.rollback()