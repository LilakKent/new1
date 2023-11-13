import random
import pyautogui as pg
import keyboard as key
from input_audio_ZheBa import listen
from input_en_audio_ZheBa import listen_en
import sqlite3
import pyttsx3




engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)



greeting = ["Привет!", "Здравствуй!", "Приветствую!", "Привет-привет!"]
not_understand = ['Не поняла запрос', 'Перефразируй']

question = {
    "как тебя зовут?": ["Меня зовут ЖэБа", "Я ЖэБа", "Мое имя - ЖэБа"],
    "что ты умеешь?": ["Я могу открывать приложение, если вы это скажете"]
}

with sqlite3.connect('ZheBa.db') as con:
    cur = con.cursor()
    doing = cur.execute('SELECT делать FROM zheba').fetchall()
    doing_2 = [d[0] for d in doing]
    con.commit()
    open_app = [o[0] for o in cur.execute('SELECT open FROM zheba').fetchall()]
    app = [a[0] for a in cur.execute('SELECT app FROM zheba').fetchall()]

def audio_function():
    while True:
        au = listen()
        pl = au.lower()
        listofpl = pl.split(' ')
        if pl == "привет":
            engine.say(random.choice(greeting))
            engine.runAndWait()
        elif pl == 'как тебя зовут':
            engine.say(random.choice(question['как тебя зовут?']))
            engine.runAndWait()
        elif pl == 'что ты умеешь':
            engine.say(random.choice(question['что ты умеешь?']))
            engine.runAndWait()
        elif len(set(listofpl) & set(open_app)) > 0 and len(set(listofpl) & set(app)) > 0 or len(set(listofpl) & set(app)) > 0:
            pg.PAUSE = 0.1
            engine.say('какое приложение?: ')
            engine.runAndWait()
            input_funktion = listen_en()
            if input_funktion:
                pg.hotkey('Win')
                key.write(input_funktion, delay=0.1)
                pg.keyDown('Enter')
                engine.say('что-то ещё?')
                engine.runAndWait()
        elif pl == 'пока':
            exit()
        else:
            print(f'Вы сказали: {listofpl}')
            engine.say(random.choice(not_understand))
            engine.runAndWait()


