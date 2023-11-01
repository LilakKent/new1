import random
import speech_recognition
import pyaudio
#list = ['wow', 'pup']
#number = ran.random()
#list1 = ran.choice(list)
#print(list1)

from bs4 import BeautifulSoup
import requests


greetings = {
    "привет": ["Привет!", "Здравствуй!", "Приветствую!", "Привет-привет!"]
}

questions = {
    "как дела?": ["Хорошо, спасибо!", "Отлично!", "Не жалуюсь."],
    "что делаешь?": ["Отвечаю на твои вопросы.", "Разговариваю с тобой.", "Программирую."],
    "как тебя зовут?": ["Меня зовут ЖэБа.", "Я ЖэБа.", "Мое имя - ЖэБа."],
    "что ты умеешь?": ["Я могу отвечать на вопросы и помогать с задачами.", "Могу общаться на разные темы.",
                       "Попробуй спросить меня о чем-нибудь!"]

}


def process_question(question):
    question = question.lower()  # Приводим вопрос к нижнему регистру

    # Поиск ключевого слова в вопросе
    for key in questions:
        if key in question:
            return random.choice(questions[key])

    return "Извини, я не понял вопроса. Можешь перефразировать?"


def search_google(query):
    try:
        # Формируем URL-адрес поискового запроса
        url = f"https://www.google.com/search?q={query}"

        # Отправляем GET-запрос на URL-адрес
        response = requests.get(url)

        # Проверяем успешность запроса
        response.raise_for_status()

        # Создаем объект BeautifulSoup для анализа HTML-страницы
        soup = BeautifulSoup(response.text, "html.parser")

        # Извлекаем результаты поиска из HTML-страницы
        results = soup.select(".yuRUbf")

        # Извлекаем заголовки ссылок из результатов
        titles = [result.find("h3").get_text() for result in results]

        return titles
    except requests.exceptions.RequestException:
        return "Извините, произошла ошибка при выполнении запроса."


# Основной цикл программы
while True:
    user_input = input()  # Получаем ввод пользователя

    if user_input.lower() == "пока":
        print("Пока! Было приятно пообщаться.")
        break

    # Проверяем, является ли вопрос пустым
    if not user_input.endswith("?"):
        print("Извини, это не выглядит как вопрос. Попробуй задать вопрос.")
        continue

    # Генерируем случайное приветствие
    greeting = random.choice(greetings)
    print(greeting)

    # Обрабатываем вопрос и выводим ответ
    response1 = process_question(user_input)
    print(response1)

    # Выполняем поиск в Google и выводим результаты
    response = search_google(user_input)
    if isinstance(response, list):
        for result in response:
            print(result)
    else:
        print(response)

