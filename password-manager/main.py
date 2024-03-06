from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def gen_password():
    """Generated a random password string with letters [ 8 to 10 chars], numbers [2 to 4 chars]
    and symbols [2 to 4 chars]"""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    letter_list = [l_char for l_char in random.choices(letters, k=random.randint(8, 10))]
    symbol_list = [s_char for s_char in random.choices(symbols, k=random.randint(2, 4))]
    number_list = [n_char for n_char in random.choices(numbers, k=random.randint(2, 4))]

    password_list = letter_list + symbol_list + number_list
    random.shuffle(password_list)

    password = "".join(password_list)
    entry_password.insert(END, password)
    pyperclip.copy(password)
    messagebox.showinfo(title="Password Manager", message="Password copied to clipboard.")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_to_file():
    """ Adds entries from the UI to a text file."""
    website = entry_website.get()
    username = entry_username.get()
    password = entry_password.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Password Manager", message="Hey! You have empty fields.")
    else:
        is_ok = messagebox.askokcancel(title="Password Manager", message=f"Data to save : \n\n Website: {website}\n "
                                                                         f"Email/Username: {username}\n Password: {password}\n Ok to save?")
        if is_ok:
            with open("./password_data.txt", mode="a") as data_file:
                data_file.write(f"{website}| "
                                f"{username}| "
                                f"{password}\n")
            clear_fields()


def clear_fields():
    """Clears all the fields after adding the UI details into a .txt file"""

    entry_website.delete(0, END)
    entry_username.delete(0, len(entry_username.get()))
    entry_password.delete(0, len(entry_password.get()))


# ---------------------------- UI SETUP ------------------------------- #
BUTTON_COLOR = "#7f9f80"

window = Tk()
window.title("Password Manager")
window.configure(padx=60, pady=60)

canvas = Canvas(height=300, width=300)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(150, 150, image=lock_img)
canvas.grid(column=1, row=0, sticky="nw")

lbl_website = Label(text="Website: ")
lbl_website.grid(column=0, row=1, sticky="e")

entry_website = Entry(width=50)
entry_website.grid(column=1, row=1, columnspan=2, sticky="w")

lbl_username = Label(text="Email/Username: ")
lbl_username.grid(column=0, row=2, sticky="e")

entry_username = Entry(width=50)
entry_username.grid(column=1, row=2, columnspan=4, sticky="w")

lbl_password = Label(text="Password: ")
lbl_password.grid(column=0, row=3, sticky="e")

entry_password = Entry(width=25)
entry_password.grid(column=1, row=3, sticky="w")

window.grid_rowconfigure(index=3, weight=1, pad=1)
btb_gen_password = Button(text="Generate Password", background=BUTTON_COLOR, command=gen_password)
btb_gen_password.grid(column=1, row=3, sticky="e")

btn_add = Button(text="Add", width=43, background=BUTTON_COLOR, command=save_to_file)
btn_add.grid(column=1, row=5, columnspan=2, sticky="w")

window.mainloop()
