import tkinter as tk
from random import randint, choice


def generate_random_seq() -> None:
    random_sequence.clear()
    for _ in range(randint(2, 6)):
        random_sequence.append(choice(notes))


COLUMNS = 3
ROWS = 4
COLOR = "aqua"
STYLE = tk.FLAT
HEIGHT = 100
WIDTH = 100
PADX = 50 - 3
PADY = 25 - 3

notes = [
    'notes/a3.mp3', 'notes/a4.mp3', 'notes/a5.mp3',
    'notes/b3.mp3', 'notes/b5.mp3', 'notes/c5.mp3',
    'notes/c6.mp3', 'notes/d3.mp3', 'notes/d4.mp3',
    'notes/e3.mp3', 'notes/e4.mp3', 'notes/e5.mp3',
    #'notes/f3.mp3', 'notes/f4.mp3', 'notes/f5.mp3',
    #'notes/g3.mp3', 'notes/g4.mp3', 'notes/g5.mp3',
]

random_sequence = []
