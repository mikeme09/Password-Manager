from tkinter import *
from tkinter import messagebox
from password_generator_forGUI import generate_random_password


# =================== GENERATING PASSWORD =====================
def gen_pass():
    generate = generate_random_password()
    password_entry.delete(0, END)
    password_entry.insert(0, generate)


# =================== SAVING DATA =============================
def save_data():
    with open("data.txt", "a") as data:
        website = website_entry.get()
        email = email_entry.get()
        password = password_entry.get()

        if not website or not email or not password:
            messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
        else:
            user_satisfy = messagebox.askokcancel(title=website,
                                                  message=f"These are the details entered: \nEmail: {email}"
                                                          f" \nPassword: {password} \n\nAre you okay with this?")
            if user_satisfy:
                data.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)


# ========================= UI ==================================
window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30)

canvas = Canvas(width=210, height=200)
logo_img = PhotoImage(file="logo1.png")
canvas.create_image(110, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry()
website_entry.grid(row=1, column=1, columnspan=2, sticky=EW)
website_entry.focus()

email_entry = Entry()
email_entry.grid(row=2, column=1, columnspan=2, sticky=EW)
# email_entry.insert(END, "michael.arco@gmail.com")  # END is from the tkinter CONSTANT

password_entry = Entry()
password_entry.grid(row=3, column=1, sticky=EW)

# Buttons
generate_password = Button(text="Generate Password", command=gen_pass)
generate_password.grid(row=3, column=2)

add_button = Button(text="Add", command=save_data)
add_button.grid(row=4, column=1, columnspan=2, sticky=EW)

window.mainloop()
