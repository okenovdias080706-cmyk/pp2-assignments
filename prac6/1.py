import sqlite3
import csv

# Database connection
conn = sqlite3.connect("phonebook.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS phonebook (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    phone TEXT UNIQUE
)
""")

conn.commit()


#1. Insert from console
def insert_from_console():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone = input("Enter phone: ")

    try:
        cursor.execute("INSERT INTO phonebook (first_name, last_name, phone) VALUES (?, ?, ?)",
                       (first_name, last_name, phone))
        conn.commit()
        print("✅ Added successfully")
    except:
        print("❌ Error (maybe duplicate phone)")


#2. Insert from CSV
def insert_from_csv():
    file_name = input("Enter CSV file name: ")

    try:
        with open(file_name, newline='') as file:
            reader = csv.reader(file)
            next(reader)  # skip header

            for row in reader:
                cursor.execute("INSERT OR IGNORE INTO phonebook (first_name, last_name, phone) VALUES (?, ?, ?)", row)

        conn.commit()
        print("✅ CSV uploaded")
    except:
        print("❌ Error reading file")


#3 Update data
def update_data():
    print("1. Change name")
    print("2. Change phone")
    choice = input("Choose: ")

    if choice == "1":
        phone = input("Enter phone: ")
        new_name = input("Enter new first name: ")

        cursor.execute("UPDATE phonebook SET first_name=? WHERE phone=?", (new_name, phone))
        conn.commit()
        print("✅ Updated")

    elif choice == "2":
        name = input("Enter first name: ")
        new_phone = input("Enter new phone: ")

        cursor.execute("UPDATE phonebook SET phone=? WHERE first_name=?", (new_phone, name))
        conn.commit()
        print("✅ Updated")


#4 Query data
def query_data():
    print("1. Show all")
    print("2. Search by name")
    print("3. Search by phone")

    choice = input("Choose: ")

    if choice == "1":
        cursor.execute("SELECT * FROM phonebook")
    elif choice == "2":
        name = input("Enter name: ")
        cursor.execute("SELECT * FROM phonebook WHERE first_name LIKE ?", ('%' + name + '%',))
    elif choice == "3":
        phone = input("Enter phone: ")
        cursor.execute("SELECT * FROM phonebook WHERE phone=?", (phone,))

    rows = cursor.fetchall()
    for row in rows:
        print(row)


#5 Delete data
def delete_data():
    print("1. Delete by name")
    print("2. Delete by phone")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Enter name: ")
        cursor.execute("DELETE FROM phonebook WHERE first_name=?", (name,))
    elif choice == "2":
        phone = input("Enter phone: ")
        cursor.execute("DELETE FROM phonebook WHERE phone=?", (phone,))

    conn.commit()
    print("✅ Deleted")


#6 Menu
def menu():
    while True:
        print("\n PHONEBOOK MENU")
        print("1. Insert from console")
        print("2. Insert from CSV")
        print("3. Update")
        print("4. Query")
        print("5. Delete")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            insert_from_console()
        elif choice == "2":
            insert_from_csv()
        elif choice == "3":
            update_data()
        elif choice == "4":
            query_data()
        elif choice == "5":
            delete_data()
        elif choice == "0":
            break
        else:
            print("❌ Wrong choice")


#7 Run program
menu()

conn.close()