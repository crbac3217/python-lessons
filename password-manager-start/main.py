from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    web = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    with open("data.txt", "a") as data:
        data.write(f"{web} : {email} / {password}\n")
        web_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("pasManager")
window.config(padx = 50, pady = 20)

canvas = Canvas(height=200, width= 200)
logo_img = PhotoImage(file="logo.png")

canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

web_label = Label(text="website")
web_label.grid(row=1, column=0)
email_label = Label(text="email")
email_label .grid(row=2, column=0)
password_label = Label(text="password")
password_label.grid(row=3, column=0)

web_entry = Entry(width=35)
web_entry.grid(row=1, column=1, columnspan=2)
web_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "crbac3217@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

password_button = Button(text = "Generate")
password_button.grid(row=3, column=2)

add_button = Button(text = "Add", width=35, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()