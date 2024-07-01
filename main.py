from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
WHITE = "#ffffff"
BLACK = "#000000"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    new_password = "".join(password_list)
    password_input.insert(0, new_password)
    pyperclip.copy(new_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_user_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
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
            # Saving updated data
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_input.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #


def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword:{password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #
# Window Setup
window = Tk()
window.title("Password Manager")
window.config(bg=WHITE, padx=50, pady=50)
window.resizable(False, False)

# Canvas and Image Setup
canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
lock = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock)
canvas.grid(column=1, row=0)

# Labels Setup
website_label = Label(text="Website:", borderwidth=0, bg=WHITE, fg=BLACK)
website_label.grid(column=0, row=1, sticky="EW")
email_username_label = Label(text="Email/Username:", borderwidth=0, bg=WHITE, fg=BLACK)
email_username_label.grid(column=0, row=2, sticky="EW")
password_label = Label(text="Password:", borderwidth=0, bg=WHITE, fg=BLACK)
password_label.grid(column=0, row=3, sticky="EW")

# Button Setup
add_button = Button(text="Add", bg=WHITE, fg=BLACK, highlightbackground=WHITE, width=36, command=save)
add_button.grid(column=1, row=4, sticky="EW")
generate_password_button = Button(text="Generate Password", bg=WHITE, fg=BLACK, highlightbackground=WHITE,
                                  command=generate_password)
generate_password_button.grid(column=2, row=3, sticky="EW")
search_button = Button(text="Search", bg=WHITE, fg=BLACK, highlightbackground=WHITE, width=15, command=find_password)
search_button.grid(row=1, column=2)

# Entry Setup
website_entry = Entry(width=21, bg=WHITE, highlightthickness=0, fg=BLACK)
website_entry.grid(column=1, row=1, sticky="EW")
website_entry.focus()
website_entry.config(insertbackground=BLACK)
email_user_input = Entry(width=35, bg=WHITE, highlightthickness=0, fg=BLACK)
email_user_input.grid(column=1, row=2, columnspan=2, sticky="EW")
email_user_input.insert(0, "tweedy5646@yahoo.com", )
email_user_input.config(insertbackground=BLACK)
password_input = Entry(width=21, bg=WHITE, highlightthickness=0, fg=BLACK)
password_input.grid(column=1, row=3, sticky="EW")
password_input.config(insertbackground=BLACK)

window.mainloop()
