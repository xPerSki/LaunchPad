import tkinter as tk
from playsound import playsound

root = tk.Tk("Launch Pad", "LaunchPad")
root.title("Launch Pad")
root.minsize(600, 600)
root.maxsize(600, 600)


def create_buttons() -> None:
    COLOR = "aqua"
    STYLE = tk.SOLID
    HEIGHT = 100
    WIDTH = 100
    PADX = 50 - 3
    PADY = 50 - 3

    pixel = tk.PhotoImage(width=1, height=1)

    def first_row():
        button1 = tk.Button(root, command='playsound("notes/a3.mp3")', image=pixel, relief=STYLE)
        button1.config(height=HEIGHT, width=WIDTH, bg=COLOR)
        button1.grid(row=0, column=0, padx=PADX, pady=PADY)

        button2 = tk.Button(root, command=root.destroy, image=pixel, relief=STYLE)
        button2.config(height=HEIGHT, width=WIDTH, bg=COLOR)
        button2.grid(row=0, column=1, padx=PADX, pady=PADY)

        button3 = tk.Button(root, command=root.destroy, image=pixel, relief=STYLE)
        button3.config(height=HEIGHT, width=WIDTH, bg=COLOR)
        button3.grid(row=0, column=2, padx=PADX, pady=PADY)

    def second_row():
        button4 = tk.Button(root, command=root.destroy, image=pixel, relief=STYLE)
        button4.config(height=HEIGHT, width=WIDTH, bg=COLOR)
        button4.grid(row=1, column=0, padx=PADX, pady=PADY)

        button5 = tk.Button(root, command=root.destroy, image=pixel, relief=STYLE)
        button5.config(height=HEIGHT, width=WIDTH, bg=COLOR)
        button5.grid(row=1, column=1, padx=PADX, pady=PADY)

        button6 = tk.Button(root, command=root.destroy, image=pixel, relief=STYLE)
        button6.config(height=HEIGHT, width=WIDTH, bg=COLOR)
        button6.grid(row=1, column=2, padx=PADX, pady=PADY)

    def third_row():
        button7 = tk.Button(root, command=root.destroy, image=pixel, relief=STYLE)
        button7.config(height=HEIGHT, width=WIDTH, bg=COLOR)
        button7.grid(row=2, column=0, padx=PADX, pady=PADY)

        button8 = tk.Button(root, command=root.destroy, image=pixel, relief=STYLE)
        button8.config(height=HEIGHT, width=WIDTH, bg=COLOR)
        button8.grid(row=2, column=1, padx=PADX, pady=PADY)

        button9 = tk.Button(root, command=root.destroy, image=pixel, relief=STYLE)
        button9.config(height=HEIGHT, width=WIDTH, bg=COLOR)
        button9.grid(row=2, column=2, padx=PADX, pady=PADY)

    first_row()
    second_row()
    third_row()


create_buttons()

root.mainloop()
