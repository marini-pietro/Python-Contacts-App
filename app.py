import utils

#This file should contains main program logic. Used to start the app and prompt the user for which operation they would like to perform.
#In this file we do not implement the program functionalities, but only the communication with the user.

# In this app we can:

#     See all the contacts
#     Add a contact
#     Delete a contact
#     Search for a contact

# Contacts are stored in a sqlite database.
 
utils.setup_db()
utils.add_contact("John", "3246362611", "+39")

print(utils.search_contacts(name="John"))