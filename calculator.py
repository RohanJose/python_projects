from tkinter import *
import customtkinter

root = customtkinter.CTk()
root.title("CALCULATOR")
root.geometry("600x300")
root.resizable(False,False)


def add():
    entry4.delete(0, END)
    x = entry1.get()
    y = entry3.get()
    entry4.insert(0, int(x) + int(y))


def mul():
    entry4.delete(0, END)
    x = entry1.get()
    y = entry3.get()
    entry4.insert(0, int(x) * int(y))


def sub():
    entry4.delete(0, END)
    x = entry1.get()
    y = entry3.get()
    entry4.insert(0, int(x) - int(y))


def div():
    entry4.delete(0, END)
    x = entry1.get()
    y = entry3.get()
    entry4.insert(0, int(x) / int(y))


heading_frame = customtkinter.CTkFrame(master=root,fg_color="transparent")
heading_frame.pack(pady=0)
label = customtkinter.CTkLabel(master=heading_frame, text="CALCULATOR",font=('Sans',30))
label.pack(padx=10,pady=10)

window = customtkinter.CTkFrame(master=root,fg_color="transparent")
window.pack()

label2 = customtkinter.CTkLabel(master=window, text="Value 1:")
label2.grid(row=1, column=0, pady=10)
entry1 = customtkinter.CTkEntry(window)
entry1.grid(row=1, column=1)

label3 = customtkinter.CTkLabel(window, text="Value 2:")
label3.grid(row=2, column=0, pady=10)
entry3 = customtkinter.CTkEntry(window)
entry3.grid(row=2, column=1)

frame = customtkinter.CTkFrame(window)
frame.grid(row=3, column=0, columnspan=2, pady=10)
add_btn = customtkinter.CTkButton(frame, text="+",  command=add)
add_btn.grid(row=0, column=0)

mul_btn = customtkinter.CTkButton(frame, text="x", command=mul)
mul_btn.grid(row=0, column=1)

subt_btn = customtkinter.CTkButton(frame, text="-",  command=sub)
subt_btn.grid(row=0, column=2)

div_btn = customtkinter.CTkButton(frame, text="/", command=div)
div_btn.grid(row=0, column=3)

label4 = customtkinter.CTkLabel(window, text="Result:")
label4.grid(row=4, column=0, pady=10)
entry4 = customtkinter.CTkEntry(window)
entry4.grid(row=4, column=1)

root.mainloop()