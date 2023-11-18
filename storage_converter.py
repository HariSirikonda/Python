from tkinter import *
from tkinter import messagebox


def lock():
    frame_3.config(text=f' Enter the {From.get()} : ')
    frame_4.config(text=f' The {To.get()} Equivalent : ')
    drop_down_1.config(state="disable")
    drop_down_2.config(state="disable")
    lock_button.config(state="disable")
    unlock_button.config(state="normal")
    reset()


def unlock():
    drop_down_1.config(state="normal")
    drop_down_2.config(state="normal")
    lock_button.config(state="normal")
    unlock_button.config(state="disable")


def Exit():
    root.destroy()


def reset():
    entry_1.delete(0, END)
    result_entry.delete(0, END)


def copy():
    root.clipboard_clear()
    root.clipboard_append(result_entry.get())
    copy_label = Label(root, text="Copied to clipboard...!", font=("Helvetica", 12))
    copy_label.pack(padx=10, pady=10)
    def hide_label():
        copy_label.pack_forget()
    root.after(3000,hide_label)


def same_to_same():
    value = entry_1.get()
    result_entry.delete(0, END)
    result_entry.insert(0, value)


def bytes_to_kilobytes():
    kilobytes = int(entry_1.get()) / 1024
    value = kilobytes
    result_entry.delete(0, END)
    result_entry.insert(0, value)


def bytes_to_megabytes():
    megabytes = int(entry_1.get()) / 2048
    value = megabytes
    result_entry.delete(0, END)
    result_entry.insert(0, value)


def bytes_to_gigabytes():
    gigabytes = int(entry_1.get()) / 3072
    value = gigabytes
    result_entry.delete(0, END)
    result_entry.insert(0, value)


def bytes_to_terabytes():
    terabytes = int(entry_1.get()) / 4096
    value = terabytes
    result_entry.delete(0, END)
    result_entry.insert(0, value)


def kilobytes_to_bytes():
    bytes = int(entry_1.get()) * 1024
    value = bytes
    result_entry.delete(0, END)
    result_entry.insert(0, value)


def kilobytes_to_megabytes():
    megabytes = int(entry_1.get()) / 1024
    value = megabytes
    result_entry.delete(0, END)
    result_entry.insert(0, value)


def kilobytes_to_gigabytes():
    gigabytes = int(entry_1.get()) / 2048
    value = gigabytes
    result_entry.delete(0, END)
    result_entry.insert(0, value)


def kilobytes_to_terabytes():
    terabytes = int(entry_1.get()) / 3072
    value = terabytes
    result_entry.delete(0, END)
    result_entry.insert(0, value)


def megabytes_to_bytes():
    bytes = int(entry_1.get()) * 2048
    value = bytes
    result_entry.delete(0, END)
    result_entry.insert(0, value)


def megabytes_to_kilobytes():
    kilobytes = int(entry_1.get()) * 1024
    value = kilobytes
    result_entry.delete(0, END)
    result_entry.insert(0, value)


def megabytes_to_gigabytes():
    gigabytes = int(entry_1.get()) / 1024
    value = gigabytes
    result_entry.delete(0, END)
    result_entry.insert(0, value)


def megabytes_to_terabytes():
    terabytes = int(entry_1.get()) / 2048
    value = terabytes
    result_entry.delete(0, END)
    result_entry.insert(0, value)


def gigabytes_to_bytes():
    bytes = int(entry_1.get()) * 3072
    value = bytes
    result_entry.delete(0, END)
    result_entry.insert(0, value)


def gigabytes_to_kilobytes():
    kilobytes = int(entry_1.get()) * 2048
    value = kilobytes
    result_entry.delete(0, END)
    result_entry.insert(0, value)


def gigabytes_to_megabytes():
    megabytes = int(entry_1.get()) * 1024
    value = megabytes
    result_entry.delete(0, END)
    result_entry.insert(0, value)


def gigabytes_to_terabytes():
    terabytes = int(entry_1.get()) / 1024
    value = terabytes
    result_entry.delete(0, END)
    result_entry.insert(0, value)


def terabytes_to_bytes():
    bytes = int(entry_1.get()) * 4096
    value = bytes
    result_entry.delete(0, END)
    result_entry.insert(0, value)


def terabytes_to_kilobytes():
    kilobytes = int(entry_1.get()) * 3072
    value = kilobytes
    result_entry.delete(0, END)
    result_entry.insert(0, value)


def terabytes_to_megabytes():
    megabytes = int(entry_1.get()) * 2048
    value = megabytes
    result_entry.delete(0, END)
    result_entry.insert(0, value)


def terabytes_to_gigabytes():
    gigabytes = int(entry_1.get()) * 1024
    value = gigabytes
    result_entry.delete(0, END)
    result_entry.insert(0, value)


def convert():
    if entry_1.get().isdigit():
        if From.get() == To.get():
            same_to_same()
        elif From.get() == "Bytes" and To.get() == "Kilo Bytes":
            bytes_to_kilobytes()
        elif From.get() == "Bytes" and To.get() == "Mega Bytes":
            bytes_to_megabytes()
        elif From.get() == "Bytes" and To.get() == "Giga Bytes":
            bytes_to_gigabytes()
        elif From.get() == "Bytes" and To.get() == "Tera Bytes":
            bytes_to_terabytes()
        elif From.get() == "Kilo Bytes" and To.get() == "Bytes":
            kilobytes_to_bytes()
        elif From.get() == "Kilo Bytes" and To.get() == "Mega Bytes":
            kilobytes_to_megabytes()
        elif From.get() == "Kilo Bytes" and To.get() == "Giga Bytes":
            kilobytes_to_gigabytes()
        elif From.get() == "Kilo Bytes" and To.get() == "Tera Bytes":
            kilobytes_to_terabytes()
        elif From.get() == "Mega Bytes" and To.get() == "Bytes":
            megabytes_to_bytes()
        elif From.get() == "Mega Bytes" and To.get() == "Kilo Bytes":
            megabytes_to_kilobytes()
        elif From.get() == "Mega Bytes" and To.get() == "Giga Bytes":
            megabytes_to_gigabytes()
        elif From.get() == "Mega Bytes" and To.get() == "Tera Bytes":
            megabytes_to_terabytes()
        elif From.get() == "Giga Bytes" and To.get() == "Bytes":
            gigabytes_to_bytes()
        elif From.get() == "Giga Bytes" and To.get() == "Kilo Bytes":
            gigabytes_to_kilobytes()
        elif From.get() == "Giga Bytes" and To.get() == "Mega Bytes":
            gigabytes_to_megabytes()
        elif From.get() == "Giga Bytes" and To.get() == "Tera Bytes":
            gigabytes_to_terabytes()
        elif From.get() == "Tera Bytes" and To.get() == "Bytes":
            terabytes_to_bytes()
        elif From.get() == "Tera Bytes" and To.get() == "Kilo Bytes":
            terabytes_to_kilobytes()
        elif From.get() == "Tera Bytes" and To.get() == "Mega Bytes":
            terabytes_to_megabytes()
        elif From.get() == "Tera Bytes" and To.get() == "Giga Bytes":
            terabytes_to_gigabytes()
    else:
        messagebox.showwarning("Warning..!", "Numbers enter chey ra ERRI MALOKAM..!")


root = Tk()
root.title("Hari Sirikonda - Storage_Converter")
root.geometry("500x500")

From = StringVar()
From.set("From")
To = StringVar()
To.set("To")

frame_1 = LabelFrame(root, text=" Type of convertion : ", font=("Helvetica", 10))
frame_1.pack(padx=10, pady=10)
drop_down_1 = OptionMenu(frame_1, From, "Bytes", "Kilo Bytes", "Mega Bytes", "Giga Bytes", "Tera Bytes")
drop_down_1.grid(row=0, column=0, padx=50, pady=10)
drop_down_2 = OptionMenu(frame_1, To, "Bytes", "Kilo Bytes", "Mega Bytes", "Giga Bytes", "Tera Bytes")
drop_down_2.grid(row=0, column=1, padx=50, pady=10)

frame_2 = Frame(root)
frame_2.pack(padx=10, pady=10)
lock_button = Button(frame_2, text="Lock", font=("Helvetica", 10), command=lock)
lock_button.grid(row=0, column=0, padx=10, pady=10)
unlock_button = Button(frame_2, text="UnLock", font=("helvetica", 10), command=unlock)
unlock_button.grid(row=0, column=1, padx=10, pady=10)
unlock_button.config(state="disable")

frame_3 = LabelFrame(root, text=" Enter the Value Here : ", font=("Helvetica", 10))
frame_3.pack(padx=10, pady=10)
entry_1 = Entry(frame_3, font=("Helvetica", 14), width=25)
entry_1.pack(padx=10, pady=10)

frame_4 = LabelFrame(root, text=" Resultant : ")
frame_4.pack(padx=10, pady=10)
result_entry = Entry(frame_4, font=("Helvetica", 16), bd=0, bg="systembuttonface")
result_entry.grid(row=0, column=0, padx=10, pady=10)
copy_button = Button(frame_4, text="Copy", font=("helvetica", 10), command=copy)
copy_button.grid(row=0, column=1, padx=10, pady=10)

frame_5 = Frame(root)
frame_5.pack(padx=10, pady=10)
convert_button = Button(frame_5, text="Convert", font=("helvetica", 10), command=convert)
convert_button.grid(row=0, column=0, padx=10, pady=10)
reset_button = Button(frame_5, text="Reset", font=("helvetica", 10), command=reset)
reset_button.grid(row=0, column=1, padx=10, pady=10)
exit_button = Button(frame_5, text="Exit", font=("helvetica", 10), command=Exit)
exit_button.grid(row=0, column=2, padx=10, pady=10)

root.mainloop()
