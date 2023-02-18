import tkinter as tk

time = 0
bomb = 100
is_game_running = False

FONT = ('Comic Sans MS', 32)
FONT_BOLD = ('Comic Sans MS', 42, 'bold')

def tick():
    global time, bomb, is_game_running
    time += 0.1
    bomb = max(bomb - (time ** 0.5) / 4, 0)

    time_label.config(text=round(time, 1))
    bomb_label.config(text=round(bomb))

    if bomb > 0:
        root.after(100, tick)
    else:
        is_game_running = False
        btn.config(state=tk.DISABLED)
        root.after(2000, lambda: btn.config(state=tk.NORMAL))

def onclick():
    global time, bomb, is_game_running
    if not is_game_running:
        time = 0
        bomb = 100
        tick()
        is_game_running = True
    else:
        bomb += 0.3

def create_window():
    window = tk.Tk()
    window.title('Bomb')
    window.geometry('300x400')

    return window

root = create_window()

time_label = tk.Label(text='0.0', font=FONT, width=40, bg='#000000', fg='#ffffff')
time_label.pack()

bomb_label = tk.Label(text='100', font=FONT_BOLD)
bomb_label.pack(pady=20)

btn = tk.Button(text='Click me!', font=FONT, height=2, bg='#000000', fg='#ffffff', activebackground='#777777',
                command=onclick)
btn.pack()

root.mainloop()