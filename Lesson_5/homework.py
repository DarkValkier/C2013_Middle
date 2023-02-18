import tkinter as tk

BACKGROUND_COLOR = '#000000'
FONT = ("Comic Sans MS", 36)

def onclick():
    message = 'Привет! '

    age = int(entry1.get())
    message += f'Тебе {age} лет. '

    if age >= 18:
        message += 'Ты совершеннолетний.'
    else:
        message += 'Ты несовершеннолетний.'
    label1.config(text=message)

def change_color():
    label1.config(fg='#ff3333')

# Создание окна
window = tk.Tk()
# window.attributes("-fullscreen", True)
window.title('My Tkinter App')
window.iconphoto(False, tk.PhotoImage(file="icon.png"))
window.geometry('800x600')
window.config(bg=BACKGROUND_COLOR)

label1 = tk.Label(text='Hello world!', font=FONT, fg='#7733f8', bg=BACKGROUND_COLOR)
label1.pack()

entry1 = tk.Entry(font=FONT)
entry1.pack(pady=10)

btn1 = tk.Button(text='Click me!', font=FONT, fg='#ffffff', bg='#7733f8', command=onclick)
btn1.pack()

btn2 = tk.Button(text='Change color', font=FONT, fg='#ffffff', bg='#7733f8', command=change_color)
btn2.pack()

# Запуск основного цикла окна
window.mainloop()
