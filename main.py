import tkinter as tk
import string
import random

from main1 import nadpis

okno = tk.Tk()
okno.title("Generátor Hesla")
okno.geometry("360x260")

nadpis = tk.Label(okno, text="Vygeneruj Heslo", font=("Arial", 20))
nadpis.pack(pady=10)
