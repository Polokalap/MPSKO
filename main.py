import tkinter as tk
from tkinter import *
from datetime import datetime
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
import argparse

# @ meow
# Utálom a windowst
# - Polokalap

print("###############################################################")
print("###################         poLOG        ######################")
print("###############################################################")

print("A program elindult")

entries = {}
boxlist = {}

def add_label(text, row, col):
    label = tk.Label(root, text=text, background="#161616", fg="#fff")
    label.grid(row=row, column=col, padx=1, pady=1)
    logger(f'Hozzáadva: {text}, {row}, {col}')

def add_entry(row, col, ID):
    entry = tk.Entry(root, background="#161616", fg="#fff")
    entry.grid(row=row, column=col, padx=1, pady=1)
    entries[ID] = entry
    logger(f'Hozzáadva: {ID} (entry), {row}, {col}')

def add_button(text, row, col, cmd):
    button = tk.Button(root, text=text, background="#161616", fg="#fff", command=cmd)
    button.grid(row=row, column=col, padx=1, pady=1, )
    logger(f'Hozzáadva: {text}, {row}, {col}')

def add_checkbox(row, col, ID):
    checkbox = tk.Checkbutton(root, background="#161616")
    checkbox.grid(row=row, column=col, padx=1, pady=1)
    boxlist[ID] = checkbox
    logger(f'Hozzáadva: {ID} (checkbox), {row}, {col}')

def logger(text):
    print(f'[{datetime.now().strftime("%H:%M:%S")}] @ {text}')

root = tk.Tk()

def check():
    reference = entries[1].get()
    image = entries[2].get()
    logger(f'{reference} {image}')

    img1 = cv2.imread(reference)
    img2 = cv2.imread(image)

    if img1.shape != img2.shape:
        img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    score = ssim(gray1, gray2, full=True)[0]
    logger(f"{score:.4f}")
    scoref = float.__round__(score * 100)

    if score >= 0.8 and boxlist[1] == 1:
        add_label(f'A kép valószínűleg hasonlít. {scoref}%', 4, 2)
    elif score >= 0.7:
        add_label(f'A kép valószínűleg hasonlít. {scoref}%', 4, 2)
    else:
        add_label(f'A kép nem hasonlít. {scoref}%', 4, 2)

root.title("Kép összehasonlító")
root.config(background="#161616")
root.geometry("600x400")
root.resizable(False, False)

add_label("Kép összehasonlító", 1, 1)

add_label("Referencia kép: ", 2, 1)
add_entry(2, 2, 1)

add_label("Ellenőrzendő kép: ", 3, 1)
add_entry(3, 2, 2)

add_button("Ellenőrzés", 4, 1, check)

add_label("Nagyon pontos ", 2, 4)
add_checkbox(2, 5, 1)

root.mainloop()
