#This file should contain the source code necessary for the operation of the application.

import sqlite3
conn: sqlite3.Connection = None

#Database setup
def setup_db() -> int:
    """
    Sets up the database.
    Creates a new database if it does not exist.
    Creates a new contacts table if it does not exist.
    
    Overrides global variable conn to provide access to other functions without passing the connection object.
    
    return: 0 if the database is successfully set up
            1 if there is an error setting up the database (also prints exception to stdout)

    """
    global conn

    try: 
        conn = sqlite3.connect('contacts.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS contacts( 
                    name TEXT UNIQUE NOT NULL, 
                    phone VARCHAR(10) NOT NULL UNIQUE,
                    phone_prefix VARCHAR(10) NOT NULL
                    )
                ''')
        conn.commit()
    except sqlite3.Error as ex:
        print("Error setting up database: ", ex)
        return 1

    return 0

def close_connection() -> int:
    """
    Closes the connection to the database.
    Should be called after all database operations are done.

    return: 0 if the connection is successfully closed
            1 if there is an error closing the connection (also prints exception to stdout)
    """

    try:
        conn.close()
    except sqlite3.Error as ex:
        print("Error closing connection: ", ex)
        return 1

# Common database queries 
def add_contact(name: str, phone: str, phone_prefix:str ) -> int:
    """
    Adds new contact to the database. 
    name: str - contact name
    phone: str - contact phone number
    phone_prefix: str - contact phone number prefix should start with +

    return: 0 if the contact is successfully added to the database
            1 if there is an error adding the contact (also prints exception to stdout)
    """

    try:
        c = conn.cursor()
        c.execute("INSERT INTO contacts (name, phone, phone_prefix) VALUES (?, ?, ?)", (name, phone, phone_prefix))
        conn.commit()
    except sqlite3.Error as ex:
        print("Error adding contact: ", ex)
        return 1

def delete_contact(phone_number:str) -> int:
    """
    Deletes contact from the database.
    phone_number: str - contact phone number

    return: 0 if the contact is successfully deleted from the database
            1 if there is an error deleting the contact (also prints exception to stdout)
    """

    try:
        c = conn.cursor()
        c.execute("DELETE FROM contacts WHERE phone=?", (phone_number,))
        conn.commit()
    except sqlite3.Error as ex:
        print("Error deleting contact: ", ex)
        return 1    

def search_contacts(name='', phone=''):
    """
    Searches for contacts in the database.
    name: str - contact name
    phone: str - contact phone number

    return: list - list of contacts that match the search criteria
            int - 1 if there is an error searching for contacts (also prints exception to stdout)
    """

    try:
        c = conn.cursor()
        c.execute("SELECT * FROM contacts WHERE name LIKE ? OR phone LIKE ?", (name, phone))
        results = c.fetchall()
        return results
    except sqlite3.Error as ex:
        print("Error searching for contacts: ", ex)
        return 1

def get_all_contacts():
    """
    Retrieves all contacts from the database.
    
    return: list - list of all contacts in the database
            int - 1 if there is an error retrieving contacts (also prints exception to stdout)
    """

    try:
        c = conn.cursor()
        c.execute("SELECT * FROM contacts")
        results = c.fetchall()
        return results
    except sqlite3.Error as ex:
        print("Error retrieving contacts: ", ex)
        return 1