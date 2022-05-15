from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # List comprehension, get a random item for i in range(n), 'i.e' number of times to get it
    password_letters = [random.choice(letters) for _ in range(nr_letters)]  # _ if you won't use it
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    # we can join all
    password = "".join(password_list)  # the password list will have been shuffled!
    password_entry.insert(0, password)  # populate the password entry
    pyperclip.copy(password)  # This will automatically copy the password!


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()  # this gets the data on the web entry
    email = email_entry.get()
    password = password_entry.get()
    new_data = {  # We create a dictionary for json data
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='empty entry', message='Fill in empty field')
    else:
        try:  # when file is not found!
            with open('data.json', 'r') as datafile:
                # Reading old data
                data = json.load(datafile)
        except FileNotFoundError:  # create it and write to it
            with open('data.json', 'w') as datafile:
                json.dump(new_data, datafile, indent=4)

        else:  # if error is rectified do this
            # updating old data with new data
            data.update(new_data)
            # Then save
            with open('data.json', 'w') as datafile:  # This writes the updated data to the json
                # saving data to json
                json.dump(data, datafile, indent=4)
        finally:
            website_entry.delete(0, END)  # This clears it out!
            password_entry.delete(0, END)


# ------------------------------ Find Password --------------------
def search_password():
    website = website_entry.get()  # get anything that is in the website entry
    try:
        with open('data.json') as datafile:
            data = json.load(datafile)  # this is a dictionary

    except FileNotFoundError:
        messagebox.showinfo(title='Error', message='Data not found')

    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f'email: {email}\nPassword: {password}')
        else:
            messagebox.showinfo(title='Error', message='Data not found')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg='black', width=500, height=500)

# Canvas
canvas = Canvas(width=200, height=200, bg='black', highlightthickness=0)  # hlt=0 makes padding line not to show
logo_image = PhotoImage(file="logo.png")  # reading the image !
canvas.create_image(100, 100, image=logo_image)  # (x_pos, y_pos, image) to show where it will be displayed
canvas.grid(row=0, column=1, padx=5, pady=5)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, padx=5, pady=5)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, padx=5, pady=5)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0, padx=5, pady=5)

# Entry

website_entry = Entry(width=21)  # width should be here!
website_entry.grid(row=1, column=1, padx=5, pady=5)
website_entry.focus()  # This will focus the cursor on the entry

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, padx=5, pady=5)
email_entry.insert(0, 'aladesaea@gmail.com')  # allows it to be there!

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, padx=5, pady=5)

# Buttons
add_button = Button(text="Add")
add_button.config(width=36, bg='black', command=save)
add_button.grid(row=4, column=1, columnspan=2, padx=5, pady=5)

gen_button = Button(text="Generate Password", command=password_generator)
gen_button.grid(row=3, column=2, padx=5, pady=5)

search_button = Button(text='Search', width=13, command=search_password)
search_button.grid(row=1, column=2, padx=5, pady=5)

window.mainloop()
