import random
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

question_of_permission = input('Даёте ли вы своё разрешение на использование пуска? Ответьте да или нет: \n').lower()
if question_of_permission == 'да':
    print('Вы хотите вводить текст вручную или голосом? Ответьте вручную или голосом: ')
    question_of_input = input().lower()
    if question_of_input == 'вручную':
        import interface
        interface.send_message()


    elif question_of_input == 'голосом':
        engine.say(random.choice(greeting) + ' ' + 'Чем могу помочь?')
        engine.runAndWait()
        from audio_input_output import audio_function
        audio_function()


elif question_of_permission == 'нет':
    engine.say('Извините, но без разрешения, я не смогу выполнять важные функции(')
    engine.runAndWait()
else:
    engine.say('Вы ответили не да и не нет!)')
    engine.runAndWait()
