from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    [password_list.append(choice(letters)) for char in range(randint(8, 10))]

    [password_list.append(choice(symbols)) for char in range(randint(2, 4))]

    [password_list.append(choice(numbers)) for char in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)

# ---------------------------- SEARCH FUNCTION ------------------------------- #

def find_password():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
            messagebox.showerror(title="Error", message="No Data File Found")
    web = website_entry.get()
    for name in data:
        if web in data:
            password = data[web]["password"]
            email = data[web]["email"]
            messagebox.showinfo(title=web, message=f"Website: {web}\nEmail: {email}\nPassword: {password}")
            break
        elif not web in data:
            messagebox.showinfo(title="Error", message=f"No details for {web} exists")
            break

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    web = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data =  {
        web: {
            "email": username,
            "password": password,
        }
    }

    if len(web) == 0 or len(password) == 0:
        messagebox.showerror(title="Unfilled fields", message="Please fill all the fields")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
canvas.create_image(100, 100, image=logo)
canvas.grid(row=1, column=1)

website_label = Label(text="Website:", bg="white")
website_label.grid(row=2, column=0)

website_entry = Entry(width=52)
website_entry.grid(row=2, column=1, columnspan=2, sticky=EW)
website_entry.focus()

username_label = Label(text="Email/Username:", bg="white")
username_label.grid(row=3, column=0)

username_entry = Entry(width= 52)
username_entry.grid(row=3, column=1, columnspan=2, sticky=EW)
username_entry.insert(0, "example@email.com")

password_label = Label(text="Password:", bg="white")
password_label.grid(row=4, column=0)

password_entry = Entry(width=33)
password_entry.grid(row=4, column=1, columnspan=1, sticky=EW)

generate_password_btn = Button(text="Generate Password", bg="white", command=generate_password)
generate_password_btn.grid(row=4, column=2, sticky=EW)

add_button = Button(text="Add", bg="white", width=50, command=save)
add_button.grid(row=5, column=1, columnspan=2, sticky=EW)

search_button = Button(text="Search", bg="white", command=find_password)
search_button.grid(row=2, column=2, sticky=EW)

window.mainloop()