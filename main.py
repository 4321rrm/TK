# from tkinter import ttk
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import Label

root=tk.Tk()
root.title("Пример списков")
root.geometry("500x500")

def button_click1():
    l1=Label(root,text="нажата кнопка1")
    label.pack()

def button_click2():
    l2=Label(root,text="нажата кнопка2")
    label.pack()

button1 = tk.Button(
root,
text="Кнопка1",
command=button_click1,
bg="lightblue",  # Background color
fg="darkblue",  # Foreground (text) color
font=("Arial", 14, "bold"),  # Font style and size
padx=20,  # Horizontal padding
pady=10
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
pady=10
)
button2.pack()


root.mainloop()
