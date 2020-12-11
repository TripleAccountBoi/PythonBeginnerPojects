import sqlite3
# Create and connect to database
database = sqlite3.connect('phone_book.db')
# Create database cursor
cursor = database.cursor()
# Create table 'contacts' with the necessary columns
cursor.execute("""CREATE TABLE IF NOT EXISTS contacts(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        address TEXT,
        phone_number TEXT NOT NULL,
        email_address TEXT
    )""")

database.commit()


# Add functionality
def new():
    name_input = input("Add a name: ")
    number_input = input("Add a number: ")
    address_input = input("Add an address (optional): ")
    email_input = input("Add an email (optional): ")

    try:
        cursor.execute(f"INSERT INTO contacts(name, address, phone_number, email_address) VALUES(?, ?, ?, ?)",
                       (name_input or None, address_input or None, number_input or None, email_input or None))
        database.commit()
        print("New contact successfully created!")
    except sqlite3.IntegrityError:
        print("Error: Name and number input value cannot be null. New contact not created.")


def update():
    contact_input = input("Which contact would you like to update? (name) ")
    field_update_input = input("What field would you like to update? (name, number, address, email) ").lower()
    updated_input = input("What would you like the new value to be? ")
    if field_update_input == 'name':
        cursor.execute(f"UPDATE contacts SET name = '{updated_input}' WHERE name LIKE '%{contact_input}%'")
        database.commit()
    elif field_update_input == 'number':
        cursor.execute(f"UPDATE contacts SET phone_number = '{updated_input}' WHERE name LIKE '%{contact_input}%'")
        database.commit()
    elif field_update_input == 'address':
        cursor.execute(f"UPDATE contacts SET address = '{updated_input}' WHERE name LIKE '%{contact_input}%'")
        database.commit()
    elif field_update_input == 'email':
        cursor.execute(f"UPDATE contacts SET email_address = '{updated_input}' WHERE name LIKE '%{contact_input}%'")
        database.commit()
    else:
        print("Error: Faulty command.")


def delete(name):
    cursor.execute(f"DELETE FROM contacts WHERE name LIKE '%{name.lower()}%'")
    database.commit()


def show():
    cursor.execute("SELECT name, phone_number, address, email_address FROM contacts")
    for index, x in enumerate(cursor.fetchall()):
        print(f"{index+1}) Name: {x[0]}, Number: {x[1]}, Address: {x[2]}, Email: {x[3]}")


# Contacts app loop
while True:
    user_input = input("What would you like to do? (new/update/delete/show/quit) ")
    if user_input == 'quit':
        break
    elif user_input == 'new':
        print("Creating a new contact...")
        new()
    elif user_input == 'update':
        update()
    elif user_input == 'delete':
        delete_input = input("What contact would you like to delete? (Type name) ")
        delete(delete_input.lower())
    elif user_input == 'show':
        show()
    else:
        print("I'm not sure what that means. Try again.")
