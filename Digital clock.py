import tkinter as tk
import time

root = tk.Tk()
root.title("Clock")
root.configure(bg="black")

def update():
    current = time.strftime("%H:%M:%S")
    label.config(text=current)
    root.after(1000, update)

label = tk.Label(root, font=("Arial", 40), fg="cyan", bg="black")
label.pack()

update()
root.mainloop()