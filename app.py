import customtkinter as CTk
from CTkMessagebox import CTkMessagebox as CTkM

baseColor = ("#ebebeb", "#242424")
cardContent = ("#dbdbdb", "#2b2b2b")
boxContent = ("#f9f9fa", "#1d1e1e")

def add_contact():
    CTkM(title="Add Contact", message="Contact added successfully", icon="check")

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

# Add Contact
nameLabel = CTk.CTkEntry(addC, placeholder_text="Mario Rossi", width=750)
nameLabel.pack()
nameLabel.place(x=10, y=10)

addCButton = CTk.CTkButton(addC, text="Add Contact", width=200, command=add_contact)
addCButton.pack()
addCButton.place(x=290, y=300)

root.mainloop()