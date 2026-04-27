import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.configure(bg="#222")

def click(val):
    entry.insert(tk.END, val)

def clear():
    entry.delete(0, tk.END)

def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

entry = tk.Entry(root, font=("Arial", 20), bd=5, relief="ridge")
entry.pack(fill="both", ipadx=8, pady=10)

buttons = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','.','=','+'
]

frame = tk.Frame(root, bg="#222")
frame.pack()

row = 0
col = 0

for b in buttons:
    action = lambda x=b: click(x) if x != "=" else equal()
    tk.Button(frame, text=b, width=5, height=2,
              command=action, bg="#444", fg="white").grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

tk.Button(root, text="Clear", command=clear, bg="red", fg="white").pack(fill="both")

root.mainloop()