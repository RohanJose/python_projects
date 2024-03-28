from tkinter import *
import customtkinter

root = customtkinter.CTk()
root.title("To Do Application")
root.geometry("500x500")
root.resizable(False,False)

heading_frame = customtkinter.CTkFrame(master=root,fg_color="transparent")
heading_frame.pack(pady=0)
label = customtkinter.CTkLabel(master=heading_frame, text="TO DO LIST",font=('Sans',30))
label.pack(padx=10,pady=10)


input_entry = customtkinter.CTkEntry(master=root, placeholder_text="Enter a task..",width=480)
input_entry.pack(pady=20)


def button_event():

    val = input_entry.get().strip()
    if val == "":
        pass
    else:
        task_entry.insert(END,val,)
        task_entry.insert(END, "\n")






button = customtkinter.CTkButton(master=root, text="ADD", command=button_event)
button.pack()


task_entry = customtkinter.CTkTextbox(master=root,height=480,width=480)
task_entry.pack(pady=10)





root.mainloop()