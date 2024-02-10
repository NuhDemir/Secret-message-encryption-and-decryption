from tkinter import *
from tkinter import messagebox
import base64
import os

def decrypt():
    password = code.get()

    if password == "1234":  # Use double equals (==) for comparison
        screen2 = Toplevel(screen)
        screen2.title("deryption")
        screen2.geometry("800x400")
        screen2.configure(bg="#fdac07")

        message = text_1.get(1.0, END)
        decode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(decode_message)
        decrypt = base64_bytes.encode("ascii")

        Label(screen2, text="DECRYPT", font="Montserrat", fg="white", bg="black").place(x=50, y=0)
        text_2 = Text(screen2, font="Roboto 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text_2.place(x=20, y=90, width=760, height=300)

        text_2.insert(END, decrypt)

    elif password == "":
        messagebox.showerror("encryption", "ınput password")

    elif password != "1234":
        messagebox.showerror("encryption", "ınvalid password")

def encrypt():
    password = code.get()

    if password == "1234":  # Use double equals (==) for comparison
        screen1 = Toplevel(screen)
        screen1.title("encryption")
        screen1.geometry("800x400")
        screen1.configure(bg="#03161d")

        message = text_1.get(1.0, END)
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypt = base64_bytes.decode("ascii")

        Label(screen1, text="ENCRYPT", font="Montserrat", fg="white", bg="#ef6101").place(x=50, y=0)
        text_2= Text(screen1,font="Roboto 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
        text_2.place(x=20,y=90,width=760,height=300)

        text_2.insert(END,encrypt)

    elif password=="":
        messagebox.showerror("encryption","ınput password")

    elif password !="1234":
        messagebox.showerror("encryption", "ınvalid password")

def main_screen():
    global screen
    global code
    global text_1

    screen = Tk()
    screen.geometry("750x796")
    # icon
    image_icon = PhotoImage(file="logo.png")
    screen.iconphoto(False, image_icon)
    screen.title("DecRip")

    def reset():
        code.set("")
        text_1.delete(1.0, END)

    Label(text="Enter text for encyrption and decryption", fg="black", font=("Montsterrat", 16)).place(x=162.5, y=37.5)
    text_1 = Text(font="Montserrat 16", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text_1.place(x=20, y=90, width=710, height=200)
    Label(text="Enter secret key for encryption and decryption", fg="black", font=("Montserrat", 16)).place(x=112.5,y=300)
    code = StringVar()
    Entry(textvariable=code, width=39, bd=0, font=("Montserrat", 25), show="*").place(x=21, y=340)
    Button(text="ENCRYPT", height="2", width=23, bg="#045658", fg="white", bd=0, command=encrypt).place(x=21, y=400)
    Button(text="DECRYPT", height="2", width=23, bg="#ef6101", fg="white", bd=0, command=decrypt).place(x=558, y=400)
    Button(text="RESET", height="2", width=100, bg="#03161d", fg="white", bd=0,command=reset).place(x=21, y=450)

    screen.mainloop()
main_screen()
