from tkinter import *
from tkinter import messagebox
from random import choice,shuffle,randint
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SEARCH FUNCTION ------------------------------- #
def find_password():
    website = website_entry.get()
    #Check if the user entry matches an item
    try:
        with open('data.json','r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No data file found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(f"{website}", f"email: {email}\npassword {password}")
        else:
            messagebox.showinfo(title="Error",message="Website not found")

# ---------------------------- SAVE PASSWORD ------------------------------- #

def adding_pasword():
    # passwords:
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website:    {
                    "email":email,
                    "password": password
                    }
                }
    if len(password) == 0 or len(website) == 0 :
        messagebox.showinfo("Field empty", "You have an empty field left")
    else:

        try:
            with open('data.json','r') as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open(file="data.json", mode="w") as file:
                #Saving updated data
                json.dump(data,file, indent= 4)
        else:
            data.update(new_data)

            with open('data.json','w') as data_file:
                json.dump(data,data_file,indent=4)
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200,height=200)
bg_image = PhotoImage(file="logo.png")
canvas.create_image(100,100,image = bg_image )
canvas.grid(row=0,column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1,column=0,sticky="E")
email_label = Label(text="Email/Username: ")
email_label.grid(row=2,column=0,sticky="E")
password_label = Label(text="Password: ")
password_label.grid(row=3,column=0,sticky="E")

#Entries
website_entry = Entry(width=34)
website_entry.grid(row=1,column=1,columnspan=2,sticky="W")
website_entry.focus()

email_entry = Entry(width=34)
email_entry.grid(row=2,column=1,columnspan=2,sticky="W")
email_entry.insert(0,string="email@google.com")
password_entry = Entry(width=34)
password_entry.grid(row=3,column=1,sticky="W")


#buttons
button_generate = Button(text="Generate Password",width=15,command=generate_password)
button_generate.grid(row=3,column=2,sticky="E")
search_button = Button(text="Search",width=15,command=find_password)
search_button.grid(row=1,column=2,sticky="E")
add_button = Button(text="Add",width=45,command=adding_pasword)
add_button.grid(row=4,column=1,columnspan=2,sticky="W")



window.mainloop()
