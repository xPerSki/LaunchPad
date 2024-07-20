import tkinter.messagebox
from settings import *
from playsound import playsound
from time import sleep
import threading

played_notes = []


def check_sequence() -> None:
    for i in range(len(played_notes)):
        if played_notes[i] != random_sequence[i]:
            played_notes.clear()
            break

    if len(played_notes) == len(random_sequence):
        msg = "Sequence has been played perfectly in order! You can try again or generate a new sequence"
        tkinter.messagebox.showinfo("Success", msg)
        played_notes.clear()


def play_sound(n, user=True) -> None:
    threading.Thread(target=playsound, args=(n,), daemon=True).start()
    played_notes.append(n) if user else None
    check_sequence()


def play_sequence() -> None:
    for x in random_sequence:
        play_sound(x, user=False)
        sleep(0.5)


root = tk.Tk("Launch Pad", "LaunchPad")
root.title("Launch Pad")
root.minsize(600, 700)
root.maxsize(600, 700)
root.config(bg="black")
root.attributes("-alpha", 0.95)

generate_random_seq()

pixel = tk.PhotoImage(width=1, height=1)
btn_img = tk.PhotoImage(file="images/button.png")
play_img = tk.PhotoImage(file="images/play.png")
generate_img = tk.PhotoImage(file="images/generate.png")

for row in range(ROWS):
    for col in range(COLUMNS):
        note = notes[(row * COLUMNS) + col]
        button = tk.Button(root, command=lambda n=note: play_sound(n), image=btn_img, relief=STYLE)
        button.config(height=HEIGHT, width=WIDTH, borderwidth=3, highlightthickness=0)
        button.grid(row=row, column=col, padx=PADX, pady=PADY)

sequence_btn = tk.Button(root, command=play_sequence, image=play_img, relief=STYLE)
sequence_btn.config(height=50, width=200)
sequence_btn.place(anchor=tk.S, x=300, y=670)

generate_btn = tk.Button(root, command=generate_random_seq, image=generate_img, relief=STYLE)
generate_btn.config(height=50, width=100)
generate_btn.place(anchor=tk.S, x=500, y=670)

root.mainloop()
