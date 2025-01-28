from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():

    website = website_input.get()
    username = username_input.get()
    password = password_input.get()

    with open("manager_data.txt", "a") as f:
        f.write(f"{website} | {username} | {password}\n")
    website_input.delete(0, END)
    password_input.delete(0, END)

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

website_input = Entry(width=52)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)

username_input = Entry(width=52)
username_input.grid(row=2, column=1, columnspan=2)
username_input.insert(0, "email@email.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_input = Entry(width=34)
password_input.grid(row=3, column=1)

generate_button = Button(text="Generate Password")
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)




window.mainloop()