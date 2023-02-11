import tkinter as tk
import random

BACKGROUND_COLOR = '#222222'
FONT = ("Comic Sans MS", 36)
numbers_list = [2, 2]

def generate_numbers():
    global numbers_list

    numbers_list = [
        random.randint(1, 99),
        random.randint(1, 99)
    ]

def show_task():
    label1.config(text=f'{numbers_list[0]} + {numbers_list[1]}')

def onclick():
    answer = int(entry1.get())
    entry1.delete(0, tk.END)
    if sum(numbers_list) == answer:
        generate_numbers()
        show_task()

# Создание окна
window = tk.Tk()
# window.attributes("-fullscreen", True)
window.title('Math Trainer')
window.geometry('300x400')
window.resizable(False, False)
window.config(bg=BACKGROUND_COLOR)

label1 = tk.Label(text='2 + 2', font=FONT, fg='#7733f8', bg=BACKGROUND_COLOR)
label1.pack()

entry1 = tk.Entry(font=FONT)
entry1.pack(pady=10)

btn1 = tk.Button(text='Answer', font=FONT, fg='#ffffff', bg='#7733f8', command=onclick)
btn1.pack()

# Запуск основного цикла окна
window.mainloop()
