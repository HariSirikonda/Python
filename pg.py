import tkinter
from tkinter import *
from tkinter import ttk
from random import randint
from tkinter import messagebox
import datetime
import re



today = datetime.date.today()
formatted_date = today.strftime('%d/%m/%Y')



def check_password_strength(password):
    # Define the criteria for a strong password
    length_regex = re.compile(r'.{8,}')
    uppercase_regex = re.compile(r'[A-Z]')
    lowercase_regex = re.compile(r'[a-z]')
    digit_regex = re.compile(r'\d')
    symbol_regex = re.compile(r'[!@#$%^&*()_+=\[{\]}\|\\:;\"\'<,>\.?/`~]')

    # Check if the password meets the criteria
    length_check = length_regex.search(password)
    uppercase_check = uppercase_regex.search(password)
    lowercase_check = lowercase_regex.search(password)
    digit_check = digit_regex.search(password)
    symbol_check = symbol_regex.search(password)

    # Calculate the strength score based on the criteria met
    strength_score = 0
    if length_check:
        strength_score += 1
    if uppercase_check:
        strength_score += 1
    if lowercase_check:
        strength_score += 1
    if digit_check:
        strength_score += 1
    if symbol_check:
        strength_score += 1

    # Return the strength score
    return strength_score



def generate_password():
    number = EntryBox_2.get()
    if number.isdigit():
        result_entry.delete(0, END)
        password_length = int(EntryBox_2.get())
        Generated_password = ''
        for x in range(password_length):
            Generated_password += chr(randint(33, 126))
        result_entry.insert(0, Generated_password)
    else:
        messagebox.showwarning("PASSWORD GENERATOR","please entera valid number..!")
    # Check the strength of the password
    strength_score = check_password_strength(Generated_password)

    # Update the strength label
    if strength_score <= 2:
        strength_label.config(text="Weak", fg="red")
    elif strength_score <= 4:
        strength_label.config(text="Moderate", fg="orange")
    else:
        strength_label.config(text="Strong", fg="green")


def clipper():
    app.clipboard_clear()
    app.clipboard_append(result_entry.get())
    save_info.delete(0, END)
    save_info.insert(0, "Copied To Clipboard..!")

def save_password():
    # Open a file in write mode ('w')
    with open('My_Passwords.txt', 'a') as file:
        # Write some text to the file
        file.write("\n")
        file.write("\n")
        file.write("\n")
        file.write("\n")
        file.write("DATE : \t")
        file.write(formatted_date)
        file.write("\n")
        file.write('NAME : \t')
        file.write(EntryBox_1.get())
        file.write("\n")
        file.write("CHARACTERS : \t")
        file.write(EntryBox_2.get())
        file.write("\n")
        file.write('PASSWORD : \t')
        file.write(result_entry.get())
        text = strength_label.cget("text")
        file.write("\n")
        file.write('STRENGTH : \t')
        file.write(text)


    save_info.delete(0, END)
    save_info.insert(0,"Password Saved..!")


app = tkinter.Tk()
app.title("PASSWORD GENERATOR")
app.geometry("600x400")


LabelFrame = ttk.LabelFrame(app,text="Name the Password : ")
LabelFrame.pack(pady=10)

EntryBox_1 = tkinter.Entry(LabelFrame,font=("Helvetica",18))
EntryBox_1.pack(pady=10,padx=10)

LabelFrame = ttk.LabelFrame(app,text="How many charecters do you want : ")
LabelFrame.pack(pady=10)

EntryBox_2 = tkinter.Entry(LabelFrame,font=("Helvetica",18))
EntryBox_2.pack(pady=10,padx=10)


result_frame = ttk.LabelFrame(app,text="The Password :")
result_frame.pack(pady=10,padx=10)

result_entry = tkinter.Entry(result_frame,font=("Helvetica",18),bd=0,bg="systembuttonface")
result_entry.grid(row=0,column=0,padx=10,pady=10)

strength_label = tkinter.Label(result_frame,text="Strength")
strength_label.grid(row=0,column=1,padx=10,pady=10)

Buttonframe = ttk.LabelFrame(app,text="Functions")
Buttonframe.pack(pady=10)

Button_1 = tkinter.Button(Buttonframe,text="Generate strong password",font=("Helvetica",8),bg="white",fg="black",command=generate_password)
Button_1.grid(row=0,column=0,padx=30,pady=10)


Button_2 = tkinter.Button(Buttonframe,text="Copy To Clipboard",font=("Helvetica",8),bg="white",fg="black",command=clipper)
Button_2.grid(row=0,column=1,padx=30,pady=10)


Button_3 = tkinter.Button(Buttonframe,text="Save Password",font=("Helvetica",8),bg="white",fg="black",command=save_password)
Button_3.grid(row=0,column=2,padx=30,pady=10)

save_info = tkinter.Entry(app,font=("Helvetica",18),bg="systembuttonface",bd=0)
save_info.pack(pady=5)

app.mainloop()







