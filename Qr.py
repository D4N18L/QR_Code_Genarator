from tkinter import *

import pyqrcode  # A python module QR generator
from PIL import ImageTk, Image

root = Tk()


def generateQR():
    # Retrieve both link name and link from their Tkinter entries
    weblink_name = n_entry.get()
    weblink = l_entry.get()

    file_name = weblink_name + ".png"
    # pass the link variable to be generated into a QR code by the module (pyqrcode)
    url = pyqrcode.create(weblink)
    url.png(file_name, scale=8)

    # Create the image that will be on the window using the PIL module
    img = ImageTk.PhotoImage(Image.open(file_name))
    img_label = Label(image=img)
    img_label.image = img
    # Add the image to the canvas
    canvas.create_window(200, 410, window=img_label)


# ---------------------Tkinter Design-----------------------------

canvas = Canvas(root, width=400, height=600)
canvas.pack()

label = Label(root, text="QR Code Generator", fg='red', font=("Arial", 30))
canvas.create_window(200, 50, window=label)

n_label = Label(root, text="Link name")
l_label = Label(root, text="Link ")
canvas.create_window(200, 100, window=n_label)
canvas.create_window(200, 150, window=l_label)

n_entry = Entry(root)
l_entry = Entry(root)
canvas.create_window(200, 130, window=n_entry)
canvas.create_window(200, 170, window=l_entry)

button = Button(text="Generate QR Code", command=generateQR)
canvas.create_window(200, 200, window=button)

root.mainloop()
