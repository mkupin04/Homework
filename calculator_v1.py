import tkinter as tk

# Це буде функція для обробки натискання кнопок(поки що вона порожня):

def on_button_click(text):
    if text in "0123456789":
        val = display.get()
        
    pass
    

# Функція для зміни теми:
def set_theme(theme):

    if theme == "light":    

        root.config(bg='white')

        display.config(bg='lightgray', fg='black')

    elif theme == "dark":

        root.config(bg='black')

        display.config(bg='darkgray', fg='white')

    elif theme == "dark_blue":

        root.config(bg="darkblue")

        display.config(bg="darkblue", fg="white")

    elif theme == "green":

        root.config(bg="green")

        display.config(bg="green", fg="black")

    elif theme == "light_blue":

        root.config(bg="lightblue")

        display.config(bg="lightblue", fg="black")

    for button in buttons:
        button.config(bg='lightgray' if theme == "light" else 'darkgray' if theme == "dark" else 'darkblue' if theme == "dark_blue" else "green" if theme == "green" else "lightblue", 
                      fg='black' if theme != "dark" else 'white')


def set_font(fonts):
    display.config(font=(fonts, 18))
    for button in buttons:
        button.config(font=(fonts, 18), width=5, height=2)

# Головне вікно
root = tk.Tk()
root.title("Калькулятор")
root.geometry("400x450")

display = tk.Entry(root, font=('Arial', 24), justify='right', state=tk.DISABLED)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Кнопки калькулятора
buttons = []
button_texts = [

'²√x', 'x²', '<-', 'C',
'7', '8', '9', '/',
'4', '5', '6', '*',
'1', '2', '3', '-',
'.', '0', '=', '+'

]

row_val = 1
col_val = 0

# Створюємо кнопки:
for text in button_texts:
    button = tk.Button(root, text=text, font=('Arial', 18), width=5, height=2, command=lambda text=text: on_button_click(text))
    button.grid(row=row_val, column=col_val)
    buttons.append(button)
    
    col_val += 1
    
    if col_val > 3:
        col_val = 0
        row_val += 1

# МЕНЮ
menubar = tk.Menu(root)
theme_menu = tk.Menu(menubar, tearoff=0)
theme_menu.add_command(label="Світла тема", command=lambda: set_theme("light"))
theme_menu.add_command(label="Темна тема", command=lambda: set_theme("dark"))
theme_menu.add_command(label="Темно-синя тема", command=lambda: set_theme("dark_blue"))
theme_menu.add_command(label="Залена тема", command=lambda: set_theme("green"))
theme_menu.add_command(label="Світло синя тема", command=lambda: set_theme("light_blue"))
menubar.add_cascade(label="Теми", menu=theme_menu)

fonts = tk.Menu(menubar, tearoff=0)
fonts.add_command(label="Шррифт: Arial", command=lambda: set_font("Arial"))
fonts.add_command(label="Шррифт: Bolt", command=lambda: set_font("Bolt"))
fonts.add_command(label="Шррифт: Roboto", command=lambda: set_font("Roboto"))
fonts.add_command(label="Шррифт: Calibri", command=lambda: set_font("Calibri"))
fonts.add_command(label="Шррифт: Impact", command=lambda: set_font("Impact"))
menubar.add_cascade(label='Шрифти', menu=fonts)

root.config(menu=menubar)
root.mainloop()
