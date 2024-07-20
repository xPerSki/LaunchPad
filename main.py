import tkinter as tk
from settings import *
from playsound import playsound
import threading


def play_sound(n):
    threading.Thread(target=playsound, args=(n,), daemon=True).start()


root = tk.Tk("Launch Pad", "LaunchPad")
root.title("Launch Pad")
root.minsize(600, 700)
root.maxsize(600, 700)

pixel = tk.PhotoImage(width=1, height=1)

for row in range(ROWS):
    for col in range(COLUMNS):
        note = notes[(row * COLUMNS) + col]
        button = tk.Button(root, command=lambda n=note: play_sound(n), image=pixel, relief=STYLE)
        button.config(height=HEIGHT, width=WIDTH, bg=COLOR)
        button.grid(row=row, column=col, padx=PADX, pady=PADY)

root.mainloop()
