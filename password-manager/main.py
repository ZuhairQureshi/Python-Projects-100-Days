# Import necessary modules
import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# All possible characters for use in password generation
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def make_password():

    # Specify the number of each type of character to use in the password
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # Choose the assortment of characters for the password
    letters_used = [random.choice(letters) for i in range(nr_letters)]
    symbols_used = [random.choice(symbols) for i in range(nr_symbols)]
    numbers_used = [random.choice(numbers) for i in range(nr_numbers)]

    # Generate the password in array form
    password_chars = letters_used + symbols_used + numbers_used
    random.shuffle(password_chars)

    # Finalize the password as a string
    generated_password = "".join(password_chars)

    # Display the password in the entry field and copy to clipboard
    password_entry.delete(0, END)
    password_entry.insert(0, generated_password)
    pyperclip.copy(generated_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


# Saving information to .txt file
def write_to_file():

    # Collect text-field input
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # Dictionary of info to add to JSON file
    new_data = {
        website: {
            "Email": email,
            "Password": password,
        }
    }

    # Ensure that no text field is left empty
    if not (website == "" or email == "" or password == ""):
        # Display a confirmation message to the user
        confirm = messagebox.askokcancel(title=website, message=f"Please click 'OK' to confirm the following "
                                                                            f"information: \n\nWebsite: {website} \n"
                                                                            f"Email: {email} "
                                                                            f"\nPassword: {password}")

        if confirm:
            # Save information to JSON File
            try:
                # Check if the file already exists
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)

            except FileNotFoundError:
                # Create new file otherwise and dump the new data into it
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                # If the file already exists, dump the updated data into it
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)

            finally:
                # Clear website and password fields
                website_entry.delete(0, END)
                password_entry.delete(0, END)

    else:
        # If any textfield is empty, notify the user and force them to fill all fields
        messagebox.showwarning(title="WARNING", message="Please fill in all the fields!")

# ---------------------------- SEARCH & RETRIVE INFO ------------------------------- #


def retrieve_info():
    website = website_entry.get()

    try:
        # Check if the file exists and try to load it into a dict variable
        with open("data.json", "r") as data_file:
            data_dict = json.load(data_file)

    except FileNotFoundError:
        # If not found, tell the user
        messagebox.showwarning(title="WARNING", message="Nothing exists yet in your password database.")

    else:
        # If the file does exist
        try:
            # Check if the corresponding website entry exists
            website_info = data_dict[website]

        except KeyError:
            # If not, tell the user
            messagebox.showwarning(title="WARNING", message="No such entry exists.")

        else:
            # Otherwise, retrieve and display the info
            messagebox.showinfo(title=website, message=f"EMAIL: {website_info['Email']}\n"
                                                       f"PASSWORD: {website_info['Password']}")

# ---------------------------- UI SETUP ------------------------------- #

# Set up window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Set up canvas
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")  # generate image
canvas.create_image(100, 100, image=logo)  # display image
canvas.grid(column=1, row=0)

# Set up website entry
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)

# Set up search button with retrieval-function specified
search_button = Button(text="Search", command=retrieve_info)
search_button.grid(column=2, row=1)

# Set up email entry
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "zuhair.q01@gmail.com")

# Set up password entry
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_entry = Entry(width=25)
password_entry.grid(column=1, row=3, columnspan=2)

# Set up random password generator with password-generating function specified
password_generator = Button(text="Generate Password", command=make_password)
password_generator.grid(column=2, row=3)

# Set up save button with info-saving function specified
add_button = Button(text="Add", width=35, command=write_to_file)
add_button.grid(column=1, row=4, columnspan=2)

# Keep window open
window.mainloop()
