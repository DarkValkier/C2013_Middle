import tkinter as tk

BACKGROUND_COLOR = '#000000'
FONT = ("Comic Sans MS", 36)

def onclick():
    label1.config(text=entry1.get())

# Создание окна
window = tk.Tk()
# window.attributes("-fullscreen", True)
window.title('My Tkinter App')
window.iconphoto(False, tk.PhotoImage(file="icon.png"))
window.geometry('800x600')
window.resizable(True, True)
window.minsize(400, 300)
window.maxsize(1200, 900)
window.config(bg=BACKGROUND_COLOR)

label1 = tk.Label(text='Hello world!', font=FONT, fg='#7733f8', bg=BACKGROUND_COLOR)
label1.pack()

entry1 = tk.Entry(font=FONT)
entry1.pack(pady=10)

btn1 = tk.Button(text='Click me!', font=FONT, fg='#ffffff', bg='#7733f8', command=onclick)
btn1.pack()

# Запуск основного цикла окна
window.mainloop()
