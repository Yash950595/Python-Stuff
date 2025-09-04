from tkinter import *
from tkinter import messagebox #used to bring the pop-ups 
import random 
import json
# -----------------m----------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
               'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    symbols = ['!','#','$','%','&','(',')','*','+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)  # clear old password
    password_entry.insert(0, password)  # insert new one
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    web = website_entry.get()
    mail = mail_entry.get()
    passw = password_entry.get()

    new_data = {
        web: {
            "Email": mail,
            "Password": passw,
        }
    }

    if len(web) == 0 or len(passw) == 0:
        messagebox.showinfo(title="OOPS", message="No field can remain empty")
    else:
        try:
            with open(r"Day 29 (Password Manager)\data.json", "r") as data_file:
                # Load old data
                data = json.load(data_file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}

        # Update old data with new entry
        data.update(new_data)

        with open(r"Day 29 (Password Manager)\data.json", "w") as data_file:
            # Save updated data
            json.dump(data, data_file, indent=4)

        website_entry.delete(0, END)
        password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
windows=Tk()
windows.config(padx=50,pady=50)
windows.title("Password Manager")

canvas=Canvas(width=200,height=200)

img=PhotoImage(file="Day 29 (Password Manager)\logo.png") 
#just the file name didn't work.Had to use relative address instead

canvas.create_image(100,100,image=img)
canvas.grid(row=0,column=1)


website=Label(text="Website:")
website.grid(row=1,column=0)

website_entry=Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus() #makes the cursor to be always in webite_entry first then to the rest

mail_id=Label(text="Email/Username: ")
mail_id.grid(row=2,column=0)

mail_entry=Entry(width= 35)
mail_entry.grid(row=2,column=1,columnspan=2)
mail_entry.insert(0,"yashpatil0710@gmail.com")


password=Label(text="Password: ")
password.grid(row=3,column=0)

password_entry=Entry(width=35)
password_entry.grid(row=3,column=1,columnspan=2)


generate_button=Button(text="Generate Password",command=generate_password)
generate_button.grid(row=3,column=2)

add_button=Button(text="Add",width=36, command=save)
add_button.grid(row=4,column=1,columnspan=2)


windows.mainloop()

