from tkinter import *

# Initializing the main window
root = Tk()
root.geometry('400x400')
root.config(bg='SlateGray3')
root.resizable(0, 0)
root.title('DataFlair-AddressBook')

# Sample contact list
contactlist = [
    ['Parv Maheswari', '0176738493'],
    ['David Sharma', '2684430000'],
    ['Mandish Kabra', '4338354432'],
    ['Prisha Modi', '6834552341'],
    ['Rahul kaushik', '1234852689'],
    ['Johena Shaa', '2119876543'],
]

# Variables to store input from Entry widgets
Name = StringVar()
Number = StringVar()

# Frame and Scrollbar setup for displaying contacts
frame = Frame(root)
frame.pack(side=RIGHT)

scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, height=12)

scroll.config(command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT, fill=BOTH, expand=1)

# Function to return the index of selected contact in the Listbox
def Selected():
    return int(select.curselection()[0])

# Function to add a new contact to the list
def AddContact():
    contactlist.append([Name.get(), Number.get()])
    Select_set()

# Function to edit an existing contact in the list
def EDIT():
    contactlist[Selected()] = [Name.get(), Number.get()]
    Select_set()

# Function to delete a selected contact from the list
def DELETE():
    del contactlist[Selected()]
    Select_set()

# Function to view details of a selected contact
def VIEW():
    NAME, PHONE = contactlist[Selected()]
    Name.set(NAME)
    Number.set(PHONE)

# Function to exit the application
def EXIT():
    root.destroy()

# Function to reset the Name and Number Entry widgets
def RESET():
    Name.set('')
    Number.set('')

# Function to update the Listbox with current contact list
def Select_set():
    contactlist.sort()
    select.delete(0, END)
    for name, phone in contactlist:
        select.insert(END, name)

# Initial call to populate the Listbox with sample contacts
Select_set()

# Labels and Entry widgets for Name and Number inputs
Label(root, text='NAME', font='arial 12 bold', bg='SlateGray3').place(x=30, y=20)
Entry(root, textvariable=Name).place(x=100, y=20)

Label(root, text='PHONE NO.', font='arial 12 bold', bg='SlateGray3').place(x=30, y=70)
Entry(root, textvariable=Number).place(x=130, y=70)

# Buttons for various actions
Button(root, text=" ADD", font='arial 12 bold', bg='SlateGray4', command=AddContact).place(x=50, y=110)
Button(root, text="EDIT", font='arial 12 bold', bg='SlateGray4', command=EDIT).place(x=50, y=260)
Button(root, text="DELETE", font='arial 12 bold', bg='SlateGray4', command=DELETE).place(x=50, y=210)
Button(root, text="VIEW", font='arial 12 bold', bg='SlateGray4', command=VIEW).place(x=50, y=160)
Button(root, text="EXIT", font='arial 12 bold', bg='tomato', command=EXIT).place(x=300, y=320)
Button(root, text="RESET", font='arial 12 bold', bg='SlateGray4', command=RESET).place(x=50, y=310)

# Start the Tkinter main loop
root.mainloop()
