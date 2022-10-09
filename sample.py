import tkinter
from tkinter import *
from PIL import Image, ImageTk

root = Tk()

# Create a photoimage object of the image in the path
image1 = Image.open(
    "D://vscode//Exposys data//blog_application//bg-texture.jpg")
test = ImageTk.PhotoImage(image1)

label1 = tkinter.Label(image=test)
label1.image = test

# Position image
label1.place(x=100, y=50)
root.mainloop()
