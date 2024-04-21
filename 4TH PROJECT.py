import tkinter as tk

def button_click(symbol):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + symbol)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, 'Error')

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2),
    ('+', 1, 3), ('-', 2, 3), ('*', 3, 3), ('/', 4, 3),
    ('C', 5, 0)
]

for (text, row, column) in buttons:
    button = tk.Button(root, text=text, padx=20, pady=10, command=lambda symbol=text: button_click(symbol))
    button.grid(row=row, column=column)

clear_button = tk.Button(root, text="Clear", padx=20, pady=10, command=clear)
clear_button.grid(row=5, column=1, columnspan=2)

equal_button = tk.Button(root, text="=", padx=20, pady=10, command=calculate)
equal_button.grid(row=5, column=0)

root.mainloop()
