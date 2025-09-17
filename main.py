import tkinter as tk
import string
import random

from main1 import nadpis, button_password

okno = tk.Tk()
okno.title("Generátor Hesla")
okno.geometry("360x260")

nadpis = tk.Label(okno, text="Vygeneruj Heslo", font=("Arial", 20))
nadpis.pack(pady=10)

def passwordGenerator():
    znaky = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(znaky) for x in range(12))
    passwordDone.config(text=password)

frame_password = tk.Frame(okno)
frame_password.pack(pady=5)

button_password = tk.Button(frame_password, text="Generuj", command=lambda: passwordGenerator())
button_password.pack(side="left", padx=5)

passwordDone = tk.Label(okno, text="")
passwordDone.pack(side="left")

okno.mainloop()