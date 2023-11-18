import tkinter
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

binary_to_octal_dictionary = {
    "0"  : 0,
    "00" : 0,
    "000": 0,
    "1"  : 1,
    "01" : 1,
    "001": 1,
    "10" : 2,
    "010": 2,
    "11" : 3,
    "011": 3,
    "100": 4,
    "101": 5,
    "110": 6,
    "111": 7
}

binary_to_hexa_dictionary = {
    "0"    : 0,
    "00"   : 0,
    "000"  : 0,
    "0000" : 0,
    "1"    : 1,
    "01"   : 1,
    "001"  : 1,
    "0001" : 1,
    "10"   : 2,
    "010"  : 2,
    "0010" : 2,
    "11"   : 3,
    "011"  : 3,
    "0011" : 3,
    "100"  : 4,
    "0100" : 4,
    "101"  : 5,
    "0101" : 5,
    "110"  : 6,
    "0110" : 6,
    "111"  : 7,
    "0111" : 7,
    "1000" : 8,
    "1001" : 9,
    "1010" : "A",
    "1011" : "B",
    "1100" : "C",
    "1101" : "D",
    "1110" : "E",
    "1111": "F"
}



def Decimal_to_Binary(number):
    Binary_list = []
    while number!=0:
        remainder=number%2
        Binary_list.append(remainder)
        number=number//2
    Result_entry.delete(0,END)
    #by the time it prints in the result entry.. the numbers will be in reverse order no need to reverse the list
    for elements in Binary_list:
        Result_entry.insert(0,elements)


def Decimal_to_Octal(number):
    Octal_list = []
    while number != 0:
        remainder = number % 8
        Octal_list.append(remainder)
        number = number // 8
    Result_entry.delete(0, END)
    for elements in Octal_list:
        Result_entry.insert(0,elements)

def Decimal_to_Hexa(number):
    Hexa_list = []
    while number!=0:
        remainder = number % 16
        Hexa_list.append(remainder)
        number = number // 16
    Result_entry.delete(0, END)
    for elements in Hexa_list:
        Result_entry.insert(0,elements)

def Binary_to_Decimal(number):
    Temporary_list = []
    digits = len(str(number))
    print("The digits = ",digits)
    for n in range(digits):
        remainder = number%10
        if remainder == 0 or remainder == 1:
            pass
        else:
            messagebox.showwarning("Warning...!","Enter a BINARY Number")
            return
        value = remainder*(2**n)
        Temporary_list.append(value)
        number = number//10
    result = 0
    for i in range(digits):
        result = result + Temporary_list[i]
    Result_entry.delete(0,END)
    Result_entry.insert(0,result)

def Octal_to_Decimal(number):
    octal_list = []
    digits = len(str(number))
    for n in range(digits):
        remainder = number%10
        value = remainder*(8**n)
        octal_list.append(value)
        number = number//10
    result = 0
    for i in range(digits):
        result = result+octal_list[i]
    Result_entry.delete(0,END)
    Result_entry.insert(0,result)

def Hexa_to_Decimal(number):
    hexa_list = []
    digits = len(str(number))
    for n in range(digits):
        remainder = number%10
        value = remainder * (16**n)
        hexa_list.append(value)
        number= number//10
    result = 0
    for i in range(digits):
        result = result+hexa_list[i]
    Result_entry.delete(0,END)
    Result_entry.insert(0,result)

def binary_to_octal(number):
    octals = []
    number = int(number)
    while number!=0:
        remainder = number%1000
        str_remainder = str(remainder)
        octal = binary_to_octal_dictionary[str_remainder]
        octals.append(octal)
        number = number//1000
        Result_entry.delete(0, END)
    for elements in octals:
        Result_entry.insert(0,elements)

def binary_to_hexa(number):
    hexa_list = []
    number = int(number)
    while number !=0:
        remainder = number%10000
        remainder = str(remainder)
        hexa_number = binary_to_hexa_dictionary[remainder]
        hexa_list.append(hexa_number)
        number = number//10000
    Result_entry.delete(0,END)
    for elements in hexa_list:
        Result_entry.insert(0,elements)



def lock():
    drop_down_1.config(state='disable')
    drop_down_2.config(state='disable')
    frame_3.config(text=f' Enter the {From.get()} Number ')
    frame_4.config(text=f' The {To.get()} Equivalent : ')

def unlock():
    drop_down_1.config(state='normal')
    drop_down_2.config(state='normal')

def Convert():
    if not value.get():
        messagebox.showwarning("Warning !","Fill the Number Field...")
    elif From.get() == To.get():
        result = int(value.get())
        Result_entry.delete(0,END)
        Result_entry.insert(0,result)
    elif From.get() == "Decimal" and To.get()=="Binary":
        final_value = int(value.get())
        Decimal_to_Binary(final_value)
    elif From.get() == "Decimal" and To.get() == "Octal":
        final_value = int(value.get())
        Decimal_to_Octal(final_value)
    elif From.get()=="Decimal" and To.get()=="Hexa Decimal":
        final_value = int(value.get())
        Decimal_to_Hexa(final_value)
    elif From.get() == "Binary" and To.get()=="Decimal":
        final_value = int(value.get())
        Binary_to_Decimal(final_value)
    elif From.get() == "Octal" and To.get() == "Decimal":
        final_value = int(value.get())
        Octal_to_Decimal(final_value)
    elif From.get() == "Hexa Decimal" and To.get() == "Decimal":
        final_value = int(value.get())
        Hexa_to_Decimal(final_value)
    elif From.get() == "Binary" and To.get() == "Octal":
        final_value = int(value.get())
        binary_to_octal(final_value)
    elif From.get() == "Binary" and To.get() == "Hexa Decimal":
        final_value = int(value.get())
        binary_to_hexa(final_value)
    else:
        pass


def reset():
    Result_entry.delete(0,END)
    value.delete(0,END)

def copy():
    root.clipboard_clear()
    root.clipboard_append(Result_entry.get())
    info = Label(root,text="Copied to Clipboard..!",font=("HElvetica",12))
    info.pack(pady=10,padx=10)

root = Tk()
root.title("Hari Sirikonda_Number Conversions")
root.geometry("500x450")

From = StringVar()
From.set("From")
To = StringVar()
To.set("To")

#Frame 1 and it's Elements
Frame_1 = LabelFrame(root,text="Select the conversion : ",font=("Helvetica",10))
Frame_1.pack(pady=10,padx=20,fill=BOTH)
drop_down_1 = OptionMenu(Frame_1, From,"Decimal","Binary","Octal","Hexa Decimal")
drop_down_1.grid(row=0,column=0,padx=100,pady=10)
drop_down_2 = OptionMenu(Frame_1, To,"Decimal","Binary","Octal","Hexa Decimal")
drop_down_2.grid(row=0,column=1,padx=0,pady=10)

#Frame 2 and it's Elements
lock_frame = Frame(root)
lock_frame.pack(pady=10,padx=10)
Lock_Button = Button(lock_frame,text="Lock",font=("Helvetica",10),command=lock)
Lock_Button.grid(row=0,column=0,pady=10,padx=10)
unlock_button = Button(lock_frame,text="Unlock",font=("Helvetica",10),command=unlock)
unlock_button.grid(row=0,column=1,padx=10,pady=10)

#Frame 3 and it's Elements
frame_3 = LabelFrame(root,text=" Enter The Number : ",font=("Helvetica",10))
frame_3.pack(pady=10,padx=20)
value = Entry(frame_3,font=("Helvetica",18))
value.pack(padx=10,pady=10)

#Frame 4 and it's Elements
frame_4 = LabelFrame(root,text=" The Result Equivalent : ",font=("Helvetica",10))
frame_4.pack(pady=10,padx=10)
Result_entry = Entry(frame_4,font=("Helvetica",18),bd=0,bg="systembuttonface")
Result_entry.grid(row=0,column=0,padx=10,pady=10)
copy_button = Button(frame_4,text="Copy",font=("Helvetica",10),command=copy)
copy_button.grid(row=0,column=1,padx=10,pady=10)

#Frame 4 and it's Elements
button_frame = Frame(root)
button_frame.pack(padx=10,pady=10)
convert_button = Button(button_frame,text="Convert",font=("Helvetica",10),command=Convert)
convert_button.grid(row=0,column=0,padx=10)
reset_button = Button(button_frame,text="RESET",font=("Helvetica",10),command=reset)
reset_button.grid(row=0,column=1,padx=10)


root.mainloop()

