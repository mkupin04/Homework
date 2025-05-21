import tkinter as tk
import random

root = tk.Tk()

root.title("Вітальне вікно")
root.geometry("300x300")

label1 = tk.Label(root, text="Введіть ім'я")
entry = tk.Entry(root)

def name():
    name = entry.get()
    name = name.capitalize()
    hi = f"Привіт, {name}!"
    label2.config(text=hi)

button = tk.Button(root, text="привітатись", command=name)
label2 = tk.Label(root, text="")

def bg():
    dick_with_colors = ["blue", "red", "yellow", "green"]
    color = random.choice(dick_with_colors)
    root.config(bg=color)
label3 = tk.Label(root, text="натисни кнопку щоб змінти колір фону")
button2 = tk.Button(root, text="Змінити колір", command=bg)

label1.pack()
entry.pack()
button.pack()
label2.pack()
label3.pack()
button2.pack()

root.mainloop()
