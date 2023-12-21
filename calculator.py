import tkinter as tk

def on_button_click(value):
    current = entry.get()
    if current == "0":
        entry.delete(0, tk.END)
    entry.insert(tk.END, value)

def on_clear_click():
    entry.delete(0, tk.END)
    entry.insert(tk.END, "0")

def on_calc_click():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Калькулятор")

entry = tk.Entry(root, width=16, font=("Arial", 20), justify="right", borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

row, col = 1, 0
for btn in buttons:
    if btn != "=":
        tk.Button(root, text=btn, width=5, font=("Arial", 15), command=lambda b=btn: on_button_click(b)).grid(row=row, column=col)
    else:
        tk.Button(root, text=btn, width=5, font=("Arial", 15), command=on_calc_click).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()