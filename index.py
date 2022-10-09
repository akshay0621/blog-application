from cProfile import label
from cgitb import text
from tkinter import *
from tkinter import ttk
from tokenize import String
"""
def register():
    global screen1
    screen1 = Toplevel()
    screen1.title("Register")
    screen1.geometry("500x500")

    global username
    global password

    global username_entry
    global password_entry

    username = StringVar()
    password = StringVar()

    Label(screen1, text="Enter the required details below").pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Username * ").pack()
    username_entry = Entry(screen1, textvariable="username").pack()
    Label(screen1, text="Password * ").pack()
    password_entry = Entry(screen1, textvariable="password").pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Sign Up", width="20", height="2",
           command=register_user).pack()


def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info+".txt", "w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text="Registered Successfully!!", fg="green").pack()


def login():
    print(screen, "Login session started!!")

"""


def main_screen():
    global screen
    screen = Tk()
    screen.geometry("900x700")
    screen.title("Blog Application")
    screen.configure(background="green")
    btn1 = Button(screen, text="Login", width="22", height="2")
    btn1.place(x=700, y=20)
    btn2 = Button(screen, text="Sign Up", width="22", height="2")
    btn2.place(x=500, y=20)
    image = PhotoImage(file="D://vscode//Exposys data//bg-texture.jpg")
    screen.create_image(0, 0, anchor=NW, image=image)
    #img = ImageTk.PhotoImage(Image.open("bg-texture.jpg"))
    #image1 = Image.open("bg-texture.jpg")
    #image1 = Image.resize((50, 50), Image.ANTIALIAS)
    screen.mainloop()


main_screen()
