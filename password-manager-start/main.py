from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)


    # password = ""
    # for char in password_list:
    #   password += char
    input_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = input_website.get()
    password = input_password.get()
    email = input_email.get()

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo("Error", "Please enter your date")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are details entered: \nWebsite: {website} \nEmail: {email}\nPassword: {password} \n Is it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                input_website.delete(0, END)
                input_password.delete(0, END)
                input_email.delete(0, END)




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column = 1 ,row=0)

#website_label

website_label = Label(text="Website:", font=("Arial", 10))
website_label.grid(column = 0, row=1)

#input_website
input_website = Entry(width=35)
input_website.grid(column=1, row=1, columnspan=2, sticky="EW")
input_website.focus()

#email/username label
email_label = Label(text="Email/Username:", font=("Arial", 10))
email_label.grid(column =0, row = 2)

#input_email
input_email = Entry(width=35)
input_email.grid(column=1, row = 2, columnspan=2, sticky="EW")


#label password
password_label = Label(text="Password:", font=("Arial", 10))
password_label.grid(column = 0, row = 3)

#input password
input_password = Entry(width=35)
input_password.grid(column=1, row = 3, sticky="W")

#button generate password
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row = 3, sticky="EW")

#button add

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column = 1, row = 4, columnspan=2, sticky="EW")


window.mainloop()