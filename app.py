import speech_recognition as sr
import os
import sys
import webbrowser


def talk(words):
    print(words)
    os.system("say " + words)


talk("Привет, Я Владислава Масленникова, вы можете спросить меня о чем либо")


def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Говорите...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)

        audio = r.listen(source)

    try:
        task = r.recognize_google(audio).lower()
        # task = r.recognize_google(audio, language="ru-RU").lower()
        print("Вы сказали: " + task)
    except sr.UnknownValueError:
        talk("Я вас не понимаю")
        task = command()

    return task


def do_something(task):
    if 'open website' in task:
        talk("Уже открываю")
        url = "https://google.com"
        webbrowser.open(url)
    elif 'what do you do' in task:
        talk("Сейчас я общаюсь с тобой, а вообще я люблю спорт и активный отдых")
    elif 'your favorite colour' in task:
        talk("Мой любимый цвет черный")
    elif 'where do you study' in task:
        talk("Я учусь в Николаевском Черноморском университете Петра Могилы")
    elif 'how old are you' in task:
        talk("Мне 27 лет")
    elif 'stop' in task:
        talk("Конечно, досвидания")
        sys.exit()


while True:
    do_something(command())
