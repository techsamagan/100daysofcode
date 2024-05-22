from tkinter import *
from tkinter import messagebox
from password_generator import generator
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_gen():
    password_entry.delete(0, END)
    password = generator()
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if website == "" or email == "" or password == "":
        messagebox.showinfo(title="Oops", message="You have to fill all blanks!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}\nPasword: {password}\n Are you gonna save this?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                new_data = f"{website} | {email} | {password}\n"
                data_file.write(new_data)
                website_entry.delete(0, END)
                password_entry.delete(0, END)




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height = 200, width=200)
logo_img = PhotoImage(file="logo.png")

canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels 
website_label = Label(text="Website")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0)
passwors_label = Label(text="Password")
passwors_label.grid(row=3, column=0)

#EnTries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=29)
password_entry.grid(row=3, column=1, columnspan=2)

#Buttons
generate_password_button = Button(text="Generate Password", command=password_gen)
generate_password_button.grid(row=3, column=2, columnspan=1)

add_button = Button(text="Add", width=30, command=save)
add_button.grid(row=4, column=1, columnspan=2)



window.mainloop()