import random
import pyautogui as pg
import keyboard as key
from PyQt5.QtWidgets import *
import sys
#import speech_recognition
#import pyaudio
#list = ['wow', 'pup']
#number = ran.random()
#list1 = ran.choice(list)
#print(list1)

from bs4 import BeautifulSoup
import requests




greeting = ["Привет!", "Здравствуй!", "Приветствую!", "Привет-привет!"]
not_understand = ['Не поняла запрос', 'Перефразируй']


question = {
    "как дела?": ["Хорошо, спасибо!", "Отлично!", "Не жалуюсь."],
    "что делаешь?": ["Отвечаю на твои вопросы.", "Разговариваю с тобой.", "Программирую."],
    "как тебя зовут?": ["Меня зовут ЖэБа.", "Я ЖэБа.", "Мое имя - ЖэБа."],
    "что ты умеешь?": ["Я могу отвечать на вопросы и помогать с задачами.", #"Могу общаться на разные темы.",
                       "Попробуй спросить меня о чём-нибудь!"]

}
def function():
    print(random.choice(greeting) + ' Чем могу помочь?')
    while True:
        
        cmd = input()
        pl = cmd.lower()
        listofpl = pl.split(' ')
        if pl == "привет":
            print(random.choice(greeting))
        elif pl == 'что делаешь' or pl == 'что делаешь?':
            print(random.choice(question['что делаешь?']))
        elif pl == 'как тебя зовут' or pl == 'как тебя зовут?':
            print(random.choice(question['как тебя зовут?']))
        elif pl == 'что ты умеешь' or pl == 'что ты умеешь?':
            print(random.choice(question['что ты умеешь?']))
        elif pl == 'как дела' or pl == 'как дела?':
            print(random.choice(question['как дела?']))
        elif pl == 'открой гугл':
            pg.PAUSE = 1
            pg.hotkey('Win')
            key.write('Chrome', delay=0.1)
            pg.keyDown('Enter')
            print('что-то ещё?')
        elif 'найди' in listofpl and 'файл' in listofpl:
            pg.PAUSE = 0.5
            pg.hotkey('Win')
            key.write(listofpl[2], delay=0.1)
        elif 'найди' in listofpl and 'в' in listofpl and 'проводнике' in listofpl:
            pg.PAUSE = 0.5
            pg.hotkey('Win')
            key.write('Проводник', delay=0.1)
        elif pl == 'пока':
            exit()
        else:
            print(random.choice(not_understand))


function()