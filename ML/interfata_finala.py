import tkinter as tk
from PIL import Image, ImageTk
import tkinter.filedialog as fd
from tkinter import Message

root = tk.Tk() #inceputul interfetei

root.configure(bg = "white")
root.title("Notes Translator")
canvas = tk.Canvas(root, width = 800, height = 600) #setam dimensiunile feresteri root
canvas.grid(columnspan = 3, rowspan = 3)

#logo
logo = Image.open('logo3.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image = logo, bg="white")
logo_label.image = logo
logo_label.grid(column=1, row=0)

#instructiuni
instructiuni = tk.Label(root, text="Selectati un fisier .wav pentru a detecta notele muzicale.", font="Raleway", fg = '#545454')
instructiuni.grid(columnspan=3, column=0, row=1)

def open_file():
    alege_audio.set("Se incarca...")
    file = fd.askopenfile(parent=root, mode = 'r', title="Alege un fisier", filetype = [("Fisiere Wav", ".wav")])
    if file:
        print("Fisierul a fost incarcat cu succes")
        tk.messagebox.showinfo(title="Fisier audio incarcat", message="Fisierul a fost incarcat cu succes")
    
alege_audio = tk.StringVar()
alege_buton = tk.Button(root, textvariable=alege_audio, command = lambda:open_file(), font='Raleway', fg = 'white', bg='#FF1616', height = 2, width = 15)
alege_audio.set("Alege")
alege_buton.grid(column=1,row=2)

root.mainloop() #sfarsitul interfetei