from tkinter import *
from tkinter import messagebox

def convert():
    if celcius_entry.get().isdigit():
        if label_1.cget('text') == " Celcius to Fahrenheit : ":
            celsius = int(celcius_entry.get())
            result = (celsius * 1.8) + 32
            result_entry.delete(0, END)
            result_entry.insert(0, result)
        elif label_1.cget('text') == " Fahrenheit to Celcius : ":
            celcius = int(celcius_entry.get())
            result = (celcius-32)/1.8
            result_entry.delete(0, END)
            result_entry.insert(0, result)
        else:
            pass
    else:
        messagebox.showwarning("Warning..!","Nubers enter chey ra erri malokam..!")

def reset():
    celcius_entry.delete(0,END)
    result_entry.delete(0,END)

def swap():
    label_1.config(text=f' Fahrenheit to Celcius : ')
    swap_button.configure(state="disable")
    unswap_button.configure(state="normal")

def unswap():
    unswap_button.configure(state="disable")
    swap_button.configure(state="normal")
    label_1.config(text=f' Celcius to Fahrenheit : ')

def copy():
    root.clipboard_clear()
    root.clipboard_append(result_entry.get())
    copy_label = Label(root,text="Copied to Clipboard..!",font=("Helvetica",14))
    copy_label.pack(padx=10,pady=10)
    def hide_label():
        copy_label.pack_forget()
    root.after(3000,hide_label)



root = Tk()
root.title("Hari Sirikonda - Tempereature converrter")
root.geometry("500x350")


frame_1 = Frame(root)
frame_1.pack(padx=10,pady=10)
label_1 = LabelFrame(frame_1,text=" Celcius to Fahrenheit : ",font=("Helvetica",10))
label_1.pack(padx=10,pady=10)
celcius_entry = Entry(label_1,font=("Helvetica",18),width=30)
celcius_entry.pack(padx=10,pady=10)

button_frame = Frame(root)
button_frame.pack(padx=10,pady=10)
convert_button = Button(button_frame,text="Convert",font=("Helvetica",10),command=convert)
convert_button.grid(row=0,column=0,padx=10,pady=10)
reset_button = Button(button_frame,text="Reset",font=("Helvetica",10),command=reset)
reset_button.grid(row=0,column=1,padx=10,pady=10)
swap_button = Button(button_frame,text="Swap",font=("Helvetica",10),command=swap)
swap_button.grid(row=0,column=2,padx=10,pady=10)
unswap_button = Button(button_frame,text="Un Swap",font=("Helvetica",10),command=unswap)
unswap_button.grid(row=0,column=3,padx=10,pady=10)
unswap_button.configure(state="disable")

result_frame = LabelFrame(root,text="The Result : ",font=("Helvetica",10))
result_frame.pack(padx=10,pady=10)
result_entry = Entry(result_frame,font=("Helvetica",12),width=30,bd=0,bg="systembuttonface")
result_entry.grid(row=0,column=0,padx=10,pady=10)
copy_button = Button(result_frame,text="Copy",font=("Helvetica",10),command=copy)
copy_button.grid(row=0,column=1,pady=10,padx=10)




root.mainloop()