import tkinter as tk
from tkinter import scrolledtext
import random
import pyautogui as pg
import keyboard as key



bye = ['пока-пока', 'пока', 'до встречи!']
greeting = ["Привет!", "Здравствуй!", "Приветствую!", "Привет-привет!"]
not_understand = ['Не поняла запрос', 'Перефразируй']

question = {
    "как тебя зовут?": ["Меня зовут ЖэБа", "Я ЖэБа", "Мое имя - ЖэБа"],
    "что ты умеешь?": ["Я могу открывать приложение, если вы это скажете"]
}


def send_message(*args):
    user_input = entry.get()


    if user_input:
        display_message(f"Вы: {user_input}")
        entry.delete(0, tk.END)
        pl = user_input.lower()
        listofpl = pl.split(' ')
        if pl == "привет":
            display_message(random.choice(greeting))
        elif pl == 'как тебя зовут' or pl == 'как тебя зовут?':
            display_message(random.choice(question['как тебя зовут?']))
        elif pl == 'что ты умеешь' or pl == 'что ты умеешь?':
            display_message(random.choice(question['что ты умеешь?']))
        elif 'открой' in listofpl and 'приложение' in listofpl and len(listofpl) > 2:
            pg.PAUSE = 0.5
            pg.hotkey('Win')
            key.write(' '. join(listofpl[2:]), delay=0.1)
            pg.keyDown('Enter')
            display_message('что-то ещё?')
        elif pl == 'пока':
            exit()

        else:
            display_message(random.choice(not_understand))



def display_message(message):
    chat_history.config(state=tk.NORMAL)
    chat_history.insert(tk.END, message + "\n")
    chat_history.yview(tk.END)
    chat_history.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Чат-бот")
root.resizable(width=False, height=False)
root.geometry('+1400+150')


chat_history = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=20, state=tk.DISABLED)
chat_history.pack(padx=10, pady=10)


entry = tk.Entry(root, width=30)
entry.pack(pady=10)


entry.bind("<Return>", send_message)


send_button = tk.Button(root, text="Отправить", command=send_message)
send_button.pack()


display_message(random.choice(greeting) + ' ' + 'Чем могу помочь?')

root.mainloop()

