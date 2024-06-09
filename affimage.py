import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox

def on_button_click(description):
    messagebox.showinfo("Description", description)

def affimage(image, description, name):
    root = tk.Tk()
    root.title("Image astronomique du jour")

    amoran = Image.open(image)
    photo = ImageTk.PhotoImage(amoran)
    label = tk.Label(root, image=photo)
    label.pack()
    label = tk.Label(root, text=name + "\n")
    label.pack()
    button = tk.Button(root, text="Description", command=lambda: on_button_click(description))
    button.pack()
    root.mainloop()
