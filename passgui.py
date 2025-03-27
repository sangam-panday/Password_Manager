from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json

def search():
    website  =website_entry.get()
    try:
        with open("data.json") as file:
            data = json.load(file)
    except FileNotFoundError:
            messagebox.showinfo(title="Error",message="NO datafile found")
    else:
        if website in data:
            email = data[website]["Email"]
            password = data[website]["Password"]
            messagebox.showinfo(title="Show password",message=f"Email :{email} \n Password :{password}")
        else:
            messagebox.showinfo(title="Error",message="Website Not Found")

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "Email" : email,
            "Password": password
            }
        }
    if len(website_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showinfo(title="Empty Field", message="You have left some field empty")
        return
    else:
        try:
            with open("data.json","r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json","w") as file:
                json.dump(new_data, file, indent= 4)
        else:
            data.update(new_data)
            with open("data.json","w") as file:
                json.dump(new_data, file, indent= 4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

def generate_password():
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_symbols = [choice(symbols) for char in range(randint(2, 4))]
    password_numbers = [choice(numbers) for char in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    password = "".join(password_list)

    print(f"Your password is: {password}") 

    password_entry.insert(0, password)
    pyperclip.copy(password)

window = Tk()
window.config(padx= 20, pady = 20, bg="white")

canvas = Canvas(height= 200, width= 200, bg="white")
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100,image = logo)
canvas.grid(column=1, row= 0)

website_label = Label(text="Website: ",bg = "white", font = ("Courier",11))
website_label.grid(column=0, row=1)

website_entry = Entry(width=27)
website_entry.grid(column=1, row = 1)
website_entry.focus()

search_button = Button(text="Search",width=20,bg = "white", font = ("Courier",11), command=search)
search_button.grid(column=2, row=1)

email_label = Label(text= "Email/Username: ",bg = "white", font = ("Courier",11))
email_label.grid(column=0, row=2)

email_entry = Entry(width=58)
email_entry.grid(column=1, row = 2, columnspan=2)
email_entry.insert(0, "sangampanday09@gmail.com") 

password_label = Label(text = "Password: ",bg = "white", font = ("Courier",11))
password_label.grid(column= 0, row= 3)

password_entry = Entry(width=27)
password_entry.grid(column=1, row=3)

generatepass_button = Button(text="Generate Password",bg = "white", font = ("Courier",11), command=generate_password,width = 20)
generatepass_button.grid(column=2, row=3)

add_button = Button(text="Add",width=43,bg = "white", font = ("Courier",11), command=save)
add_button.grid(column=1, row = 4, columnspan=2)

window.mainloop()