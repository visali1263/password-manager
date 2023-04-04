#!/usr/bin/python3
from tkinter import *
from tkinter import messagebox
import random
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)
    passw = ''.join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, passw)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if not website or not email or not password:
        messagebox.showinfo(title="Oops", message="Don't leave any fields empty")

    else:
        with open("data.json", "r") as file:
            # file.write(f"{website} | {email} | {password}\n")
            try:
                data = json.load(file)
                data.update(new_data)
            except:
                pass

            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
    
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)


def find_password():
    search_website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

        if search_website in data:
            email = data[search_website]['email']
            password = data[search_website]['password']
            messagebox.showinfo(title="Credentials",
                                message=f"Website: {search_website}\nEmail: {email}\npassword: {password}")
    except:
        messagebox.showinfo(message="Data file not found")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="~/Documents/PycharmProjects/password-manager-start/logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)

website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(row=1, column=2)

email_label = Label(text="Email/Username: ")
email_label.grid(row=2, column=0)

email_entry = Entry(width=38)
email_entry.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=37, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)
window.mainloop()
