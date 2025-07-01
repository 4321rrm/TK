# from tkinter import ttk
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import Label

root=tk.Tk()
root.title("Пример списков")
root.geometry("500x500")

def button_click1():
    label=Label(root,text="нажата кнопка1")
    label.pack()
    win1= tk.Tk()
    win1.title("Нажата кнопка1")
    win1.geometry("200x200")
    lbl = Label(win1, text="кнопка1")
    lbl.grid(column=0, row=0)  
    txt = Entry(win1,width=10)  
    txt.grid(column=1, row=0)  
    win1.mainloop
def button_click2():
    #label=Label(root,text="нажата кнопка2")
    #label.pack()
    win2=tk.Tk()
    win2.title=("Нажата кнопка2")
    win2.geometry("200x200")
    lbl= Label(win2, text="кнопка2")
    lbl.pack
    lbl.grid(column=0, row=0)
    txt = Entry(win2,width=10)  
    txt.grid(column=1, row=0)  
    win2.mainloop

button1 = tk.Button(
root,
text="Кнопка1",
command=button_click1,
bg="lightblue",  # Background color
fg="darkblue",  # Foreground (text) color
font=("Arial", 14, "bold"),  # Font style and size
padx=20,  # Horizontal padding
pady=20
)
button1.pack()

button2 = tk.Button(
root,
text="кнопка2",
command=button_click2,
bg="lightblue",  # Background color
fg="darkblue",  # Foreground (text) color
font=("Arial", 14, "bold"),  # Font style and size
padx=20,  # Horizontal padding
pady=20
)
button2.pack()


root.mainloop()
