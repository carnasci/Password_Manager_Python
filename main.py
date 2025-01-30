from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #



#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list = [choice(letters) for _ in range(randint(8, 10))]
    symbols_list = [choice(symbols) for _ in range(randint(2, 4))]
    numbers_list = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = letters_list + symbols_list + numbers_list
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():

    website = website_input.get()
    username = username_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "username": username,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Ooops", message="Please don't leave any fields empty.")
    else:
        try:
            with open("manager.data.json", "r") as f:
                # Read previous data
                data = json.load(f)
        except FileNotFoundError:
            with open("manager_data.json", "w") as f:
                json.dump(new_data, f, indent=4)
        else:
            # Update previous data
            data.update(new_data)

            with open("manager_data.json", "w") as f:
                # Saves updated data
                json.dump(new_data, f, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = website_input.get()

    with open("manager_data.json", "r") as f:
        data = json.load(f)
        try:
            password = data[website]["password"]
        except KeyError:
            messagebox.showinfo(title="Password Search", message="Website not found.")
        else:
            messagebox.showinfo(title="Password", message=f"{password}")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_input = Entry(width=33)
website_input.grid(row=1, column=1)
website_input.focus()

search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(row=1, column=2)

username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)

username_input = Entry(width=52)
username_input.grid(row=2, column=1, columnspan=2)
username_input.insert(0, "email@email.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_input = Entry(width=33)
password_input.grid(row=3, column=1)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)




window.mainloop()