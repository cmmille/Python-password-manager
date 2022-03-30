from tkinter import *
from tkinter import messagebox
from password_generator import gen_password
import ctypes
import pyperclip
import json

FONT = ('Arial', 16)
EMAIL = "youremail@email.com"

ctypes.windll.shcore.SetProcessDpiAwareness(1)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def set_random_password():
    # Get random password
    random_password = gen_password()

    # Replace password with random password
    pass_input.delete(0, END)
    pass_input.insert(0, random_password)

    # Copy password to clipboard
    pyperclip.copy(random_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    # Get inputs from form
    new_site = web_input.get()
    new_user = email_input.get()
    new_pass = pass_input.get()
    new_data = {
        new_site: {
            "email": new_user,
            "password": new_pass
        }
    }

    # Check for null input
    if len(new_site) == 0 or len(new_user) == 0 or len(new_pass) == 0:
        messagebox.showinfo(title="Error", message="Missing information, please ensure all fields are filled.")
    else:
        try:
            # Read old data
            with open("./passwords.json", "r") as file:
                data = json.load(file)
                # Update data
                data.update(new_data)
        except FileNotFoundError:
            data = new_data
        finally:
            with open("./passwords.json", "w") as file:
                # Write data to file
                json.dump(data, file, indent=4)
                messagebox.showinfo("Success", f"Successfully saved password for {new_site} ")

            # Clear inputs
            web_input.delete(0, END)
            pass_input.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def search_passwords():
    query = web_input.get()

    try:
        with open("./passwords.json", "r") as file:
            data = json.load(file)
            found_email = data[query]["email"]
            found_password = data[query]["password"]
    except FileNotFoundError:
        messagebox.showinfo("Error", "No saved passwords!\nTry adding some passwords first.")
    except KeyError:
        messagebox.showinfo("Error", f"No accounts found for {query}")
    else:
        messagebox.showinfo(query, f"User: {found_email}\nPassword: {found_password}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# --- Canvas --- #
canvas = Canvas(width=300, height=300)
lock_img = PhotoImage(file="./logo.png")
canvas.create_image(150, 150, image=lock_img)
canvas.grid(row=0, column=1)

# --- Labels --- #
web_lbl = Label(text="Website: ", font=FONT)
web_lbl.grid(row=1, column=0, sticky="e")

email_lbl = Label(text="Email/Username: ", font=FONT)
email_lbl.grid(row=2, column=0, sticky="e")

pass_lbl = Label(text="Password: ", font=FONT)
pass_lbl.grid(row=3, column=0, sticky="e")

# ---Inputs --- #
web_input = Entry(width=22, font=FONT)
web_input.grid(row=1, column=1, columnspan=2, sticky="w")
web_input.focus()

email_input = Entry(width=40, font=FONT)
email_input.grid(row=2, column=1, columnspan=2, sticky="w")
email_input.insert(0, EMAIL)

pass_input = Entry(width=22, font=FONT)
pass_input.grid(row=3, column=1, sticky="w")

# --- Buttons --- #
search_btn = Button(text="Search", width=32, command = search_passwords)
search_btn.grid(row=1, column=2, sticky="e")

gen_btn = Button(text="Generate Password", width=32, command=set_random_password)
gen_btn.grid(row=3, column=2, sticky="e")

add_btn = Button(text="Add", width=74, command=save_password)
add_btn.grid(row=4, column=1, columnspan=2, sticky="w")

window.mainloop()
