import json
from tkinter import TclError

import customtkinter as CTk
from CTkMessagebox import CTkMessagebox as CTkM
import utils

#This file should contains main program logic. Used to start the app and prompt the user for which operation they would like to perform.
#In this file we do not implement the program functionalities, but only the communication with the user.

# In this app we can:

#     See all the contacts
#     Add a contact
#     Delete a contact
#     Search for a contact

# Contacts are stored in a sqlite database.

baseColor = ("#ebebeb", "#242424")
cardContent = ("#dbdbdb", "#2b2b2b")
boxContent = ("#f9f9fa", "#1d1e1e")

utils.setup_db()

def add_contact():
    """
    Add a contact to the contacts list.
    """

    prefix = phonePrefixCombobox.get()
    valid = False
    if nameLabel.get() != "":
        if "(" in prefix and ")" in prefix:
            start = prefix.index("(") + 1
            end = prefix.index(")")
            prefisso = prefix[start:end]
            if validate_phone_number(None):
                #TODO: insert function to add contact to the db
                utils.add_contact(nameLabel.get(), phoneNumberEntry.get(), prefisso)
                valid = True

    all_contact()
    search_contact()

    nameLabel.delete(0, "end")
    phonePrefixCombobox.set("Select Prefix")
    phoneNumberEntry.delete(0, "end")
    validate_phone_number(None)

    if valid:
        CTkM(title="Add Contact", message="Contact added successfully", icon="check")
    else:
        CTkM(title="Add Contact", message="Contact not added", icon="cancel")

def validate_phone_number(event) -> bool:
    """
    Validate the phone number entry.

    :param event - The event that triggered the function
    :return: bool - True if the phone number is valid, False otherwise
    :raises: None
    """

    numero = phoneNumberEntry.get()
    if not numero:
        phoneNumberEntry.configure(border_color="#565b5e")
        return False
    else:
        if not numero.isdigit():
            phoneNumberEntry.delete(0, "end")
            phoneNumberEntry.insert(0, "".join([char for char in numero if char.isdigit()]))
        if len(numero) > 10:
            phoneNumberEntry.delete(10, "end")
        if len(numero) < 9:
            phoneNumberEntry.configure(border_color="#ff0000")
        if len(numero) == 9 or len(numero) == 10:
            phoneNumberEntry.configure(border_color="#00ff00")

        return True

def search_contact():
    """
    Search a contact in the contacts list.
    """

    for widget in contactsList.winfo_children():
        widget.destroy()

    search = searchEntry.get() if searchEntry.get() != "" else ""

    #TODO: insert function to search contact in the db
    contacts = utils.search_contacts(name=f"%{search}%")
    # contacts = [("John", "3913064745", "+39")]

    for contact in contacts:
        contact_button = CTk.CTkButton(contactsList, text=contact[0], command=lambda c=contact: show_contact_details(c))
        contact_button.pack(pady=5)

def all_contact():
    """
    Show all contacts in the contacts list.
    """
    for widget in allContactsList.winfo_children():
        widget.destroy()

    #TODO: insert function to get all contacts from the db
    contacts = utils.get_all_contacts()
    # contacts = [("John", "3913064745", "+39"), ("Mario", "3913064745", "+39"), ("Luigi", "3913064745", "+39")]

    for contact in contacts:
        contact_button = CTk.CTkButton(allContactsList, text=contact[0], command=lambda c=contact: show_contact_details(c))
        contact_button.pack(pady=5)

def schedule_all_contact():
    all_contact()
    search_contact()
    root.after(60000, schedule_all_contact)

def delete_contact(contact, window):
    #TODO: insert function to delete contact from the db
    try:
        utils.delete_contact(name = contact)

        CTkM(title="Delete Contact", message="Contact deleted successfully", icon="check")

        all_contact()
        search_contact()
    except Exception as e:
        print(e)
        CTkM(title="Delete Contact", message="Error deleting contact", icon="cancel")
    finally:
        details_window.attributes("-topmost", False)
        window.destroy()

def show_contact_details(contact):
    global details_window
    details_window = CTk.CTkToplevel(root)
    details_window.title(contact[0])
    details_window.geometry("400x300")
    details_window.attributes("-topmost", True)

    name_label = CTk.CTkLabel(details_window, text=f"Name: {contact[0]}")
    name_label.pack(pady=10)

    phone_prefix = CTk.CTkLabel(details_window, text=f"Phone Prefix: {contact[2]}")
    phone_prefix.pack(pady=10)

    phone_label = CTk.CTkLabel(details_window, text=f"Phone: {contact[1]}")
    phone_label.pack(pady=10)

    delete_button = CTk.CTkButton(details_window, text="Delete Contact", command=lambda: delete_contact(contact[0], details_window))
    delete_button.pack(pady=10)

with open("config/phone_prefixes.json", "r") as file:
    phone_prefixes = json.load(file)

phone_prefix_values = [f"{prefix['name']} ({prefix['dial_code']})" for prefix in phone_prefixes]

root = CTk.CTk()
root.geometry("800x450")
root.title("Python Contacts App")
root.resizable(False, False)
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

contactsTabview = CTk.CTkTabview(root, fg_color=cardContent, width=780, height=440)
contactsTabview.pack()
contactsTabview.place(x=10, y=0)

addC = contactsTabview.add("Add Contact")
searchC = contactsTabview.add("Search Contact")
allC = contactsTabview.add("All Contacts")

# Add Contact Tab
# Contact Name Entry
nameLabel = CTk.CTkEntry(addC, placeholder_text="Mario Rossi", width=750)
nameLabel.pack()
nameLabel.place(x=10, y=10)

# Phone Prefix ComboBox
phonePrefixCombobox = CTk.CTkComboBox(addC, values=phone_prefix_values, width=200, state="readonly")
phonePrefixCombobox.set("Select Prefix")
phonePrefixCombobox.pack()
phonePrefixCombobox.place(x=10, y=80)

# Phone Number Entry
phoneNumberEntry = CTk.CTkEntry(addC, placeholder_text="Phone Number", width=540)
phoneNumberEntry.pack()
phoneNumberEntry.place(x=220, y=80)
phoneNumberEntry.bind("<KeyRelease>", lambda event: validate_phone_number(event))

# Add Contact Button
addCButton = CTk.CTkButton(addC, text="Add Contact", width=200, command=add_contact)
addCButton.pack()
addCButton.place(x=290, y=300)

# Search Contact Tab
# Search Entry
searchEntry = CTk.CTkEntry(searchC, placeholder_text="Search Contact", width=760)
searchEntry.pack()
searchEntry.place(x=4, y=10)
searchEntry.bind("<KeyRelease>", lambda event: search_contact())

# Contacts List
contactsList = CTk.CTkScrollableFrame(searchC, width=738, height=400, fg_color=boxContent)
contactsList.pack()
contactsList.place(x=4, y=50)

# All Contacts Tab
# Contacts List
allContactsList = CTk.CTkScrollableFrame(allC, width=738, height=400, fg_color=boxContent)
allContactsList.pack()
allContactsList.place(x=4, y=4)

schedule_all_contact()

root.mainloop()