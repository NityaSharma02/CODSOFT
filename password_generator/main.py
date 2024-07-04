from tkinter import *
from tkinter import ttk, messagebox
import string, random, pyperclip, os

def generatePassword():
    length = int(scale.get())
    if length == 0:
        password = ''.join(random.choices(string.ascii_lowercase, k = length))
        strength = "*Invalid length"

    elif length < 6 and length >= 1:
        password = ''.join(random.choices(string.ascii_lowercase, k = length))
        strength = "*Very Weak"
    
    elif length < 8:
        password = ''.join(random.choices(string.ascii_letters, k = length))
        strength = "*Weak"
    
    elif length < 10:
        password = ''.join(random.choices(string.ascii_letters + string.digits, k = length))
        strength = "*Normal"

    elif length < 12:
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k = length))
        strength = "*Strong"
    
    else:
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k = length))
        strength = "*Very Strong"
    
    password_generate_entry.delete(0, END)
    password_generate_entry.insert(0, password)
    strength_label.config(text=f"{strength}")

def update_value(value):
    value = round(float(value))
    value_label.config(text=f"{value}")

def copy_clipboard():
    password = password_generate_entry.get()
    pyperclip.copy(password)

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title = "Opps", message="Please make sure you haven't left any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=F"These are the details entered: \nEmail: {email}"
                                       f"\nPassword: {password} \nIs it ok to save?")
        
        if is_ok:
            scrpit_dir = os.path.dirname(__file__)
            file_path = os.path.join(scrpit_dir, "data.txt")


            with open(file_path, "a") as file:
                file.write(f"{website} | {email} | {password}")
            
            messagebox.showinfo(title="Saved", message="Your details have been saved.")
            website_entry.delete(0, END)
            password_entry.delete(0, END)

#  -------------------- UI SetUP ------------------------------

window = Tk()
window.title("Password Manager")

canvas = Canvas(height=600, width=500, bg= "white", highlightthickness= 40, highlightbackground= "#1679AB")
canvas.grid(row=0, column=1)

logo_img = PhotoImage(file = "password_generator/image.png")
pwd_image = logo_img.subsample(3, 3)

canvas_width = 750
image_width = pwd_image.width()
image_height = pwd_image.height()
x = (canvas_width - image_width) // 2
canvas.create_image(x, 70, anchor=N, image = pwd_image)

# Entry
password_generate_entry = Entry(width=29, font=("Arial", 16))
password_generate_entry.place(relx= 0.2, rely = 0.5, anchor = "w")

website_entry = Entry(width = 25, font=("Arial", 10))
website_entry.place(relx= 0.5, rely= 0.62)

email_entry = Entry(width = 25, font=("Arial", 10))
email_entry.place(relx= 0.5, rely= 0.66)
email_entry.insert(0, "www.example.com")

password_entry = Entry(width=25, font=("Arial", 10))
password_entry.place(relx= 0.5, rely = 0.7)

# Labels
pwd_label = Label(canvas, text="Password Generator", font=("Arial", 14, "bold"), bg="white", fg="black")
pwd_label.place(relx = 0.5, rely = 0.38, anchor= CENTER)

pass_label = Label(canvas, text="Your digital security starts here - generate strong passwords effortlessly.", font=("Arial", 10, "bold"), bg="white", fg="black")
pass_label.place(relx = 0.5, rely = 0.41, anchor= CENTER)

pwd_length = Label(canvas, text="Password Length-", font=("Arial", 10, "bold"), bg="white", fg="black")
pwd_length.place(relx= 0.2, rely = 0.59, anchor = "w")

website_label = Label(canvas, text="Website    :", font=("Arial", 10, "bold"), bg = "white", fg="black")
website_label.place(relx=0.2, rely= 0.62)

email_label = Label(canvas, text="Email       :", font=("Arial", 10, "bold"), bg = "white", fg="black")
email_label.place(relx=0.2, rely= 0.66)

password_label = Label(canvas, text="Password :", font=("Arial", 10, "bold"), bg = "white", fg="black")
password_label.place(relx=0.2, rely = 0.7)

scale = ttk.Scale(canvas, from_=0, to=50, length=180, orient=HORIZONTAL, command=update_value)
scale.place(relx=0.65, rely=0.59, anchor="center")

value_label = Label(canvas, text="0", font=("Arial", 10, "bold"), bg="white", fg="black")
value_label.place(relx=0.4, rely=0.591, anchor="w")

strength_label = Label(canvas, text="", font=("Arial", 8, "bold"), bg="white", fg="#FF1E1E")
strength_label.place(relx=0.2, rely=0.53, anchor="w")

# Buttons
generate_password_button = Button(canvas, text = "Generate Password", font=("Arial", 10, "bold"), command = generatePassword, width = 19)
generate_password_button.place(relx = 0.2, rely = 0.75)

copy_password = Button(canvas, text="Copy", width= 21, font=("Arial", 10, "bold"), command = copy_clipboard)
copy_password.place(relx=0.5, rely=0.75)

save_button = Button(text="Save", width=43, font=("Arial", 10, "bold"), command=save)
save_button.place(relx = 0.2, rely = 0.8)

window.mainloop()