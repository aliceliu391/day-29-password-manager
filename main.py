from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_clicked():
    website = website_entry.get()
    user = user_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(user) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered:\nUsername/Email: {user}\nPassword: "
                                               f"{password}\n Is it OK to save?")

        if is_ok:
            with open("data.txt", mode="a") as file:
                file.write(f"{website.title()} | {user} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
user_label = Label(text="Email/Username:")
user_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=36)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)
user_entry = Entry(width=36)
user_entry.grid(column=1, row=2, columnspan=2)
user_entry.insert(END, "your_email@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Buttons
password_button = Button(text="Generate Password", width=11, command=generate_password)
password_button.grid(column=2, row=3)
add_button = Button(text="Add", width=34, command=add_clicked)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
