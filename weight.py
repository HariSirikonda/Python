from tkinter import *
from tkinter import messagebox

#function for converting the weight
def convert():
    if value_entry.get().isdigit():
        if label_1.cget('text') == " Kilograms to Pounds : ":
            value = int(value_entry.get())
            pounds = value*2.2046
            result_entry.delete(0,END)
            result_entry.insert(0,pounds)
        elif label_1.cget('text') == " Pounds to Kilograms : ":
            value = int(value_entry.get())
            kilograms = value/2.2046
            result_entry.delete(0,END)
            result_entry.insert(0,kilograms)
        else:
            pass
    else:
        reset()
        messagebox.showwarning("Warning","Numbers enter chey ra erri malokam..!")

#fuction for deleting all the entrys in the GUI
def reset():
    value_entry.delete(0,END)
    result_entry.delete(0,END)

#This function swaps the conversion process.
def swap():
    label_1.config(text=f' Pounds to Kilograms : ')
    reset()
    swap_button.configure(state="disable")
    unswap_button.configure(state="normal")

#This function unswaps the conversion process to as it is.
def unswap():
    label_1.config(text=f' Kilograms to Pounds : ')
    reset()
    unswap_button.configure(state="disable")
    swap_button.configure(state="normal")

#copies the result to clipboard
def copy():
    root.clipboard_clear()
    root.clipboard_append(result_entry.get())
    copy_label = Label(root,text=" Copied to clipboard..! ",font=("Helvetica",12))
    copy_label.pack(pady=10,padx=10)
    def hide_label():
        copy_label.pack_forget()
    root.after(3000,hide_label)



root = Tk()
root.title("Hari sirikonda - Weight convertion")
root.geometry("500x350")

frame_1 = Frame(root)
frame_1.pack(padx=10,pady=10)
label_1 = LabelFrame(frame_1,text=" Kilograms to Pounds : ",font=("Helvetica",10))
label_1.pack(padx=10,pady=10)
value_entry = Entry(label_1,font=("Helvetica",14),width=30)
value_entry.pack(padx=10,pady=10)

button_frame = Frame(root)
button_frame.pack(padx=10,pady=10)
convert_button = Button(button_frame,text="Convert",font=("Helvetica",10),command=convert)
convert_button.grid(row=0,column=0,padx=10)
reset_button = Button(button_frame,text="Reset",font=("Helvetica",10),command=reset)
reset_button.grid(row=0,column=1,padx=10)
swap_button = Button(button_frame,text="Swap",font=("Helvetica",10),command=swap)
swap_button.grid(row=0,column=2,padx=10)
unswap_button = Button(button_frame,text="Unswap",font=("Helvetica",10),command=unswap)
unswap_button.grid(row=0,column=3,padx=10)
unswap_button.configure(state="disable")

result_frame = LabelFrame(root,text=" The Result : ")
result_frame.pack(padx=10,pady=10)
result_entry = Entry(result_frame,font=("Helvetica",12),bd=0,bg="systembuttonface",width=30)
result_entry.grid(row=0,column=0,padx=10,pady=10)
copy_button = Button(result_frame,text="Copy",font=("Helvetica",10),command=copy)
copy_button.grid(row=0,column=1,padx=10,pady=10)


root.mainloop()
