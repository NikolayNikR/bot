from logging import ERROR
from sre_constants import error

from settings import *
import telebot
from text import *
from diagrams import safeBar
from diagrams import graph

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Бот работает!")


@bot.message_handler(commands=['message'])
def lox(message):
    bot.send_message(message.chat.id, f"{message}")


@bot.message_handler(commands=['summ'])
def summ(message):
    a = message.text[5:]
    a = a.strip()
    a = a.split(" ")
    bot.send_message(message.chat.id, f"{int(a[0]) + int(a[1])}")


@bot.message_handler(commands=['multi'])
def multi(message):
    a = message.text[6:]
    a = a.strip()
    a = a.split(" ")

    bot.send_message(message.chat.id, f"{int(a[0]) * int(a[1])}")


@bot.message_handler(commands=['division'])
def division(message):
    try:
        a = message.text[9:]
        a = a.strip()
        a = a.split(" ")
        bot.send_message(message.chat.id, f"{int(a[0]) / int(a[1])}")
    except ZeroDivisionError:
        bot.send_message(message.chat.id, f"Делить на 0 нельзя")
    except ValueError:
        bot.send_message(message.chat.id, f"Можно вводить только числа")
    except Exception as e:
        bot.send_message(message.chat.id, f"У бота ошибка{e}")


@bot.message_handler(commands=['subtract'])
def subtract(message):
    a = message.text[9:]
    a = a.strip()
    a = a.split(" ")

    bot.send_message(message.chat.id, f"{int(a[0]) - int(a[1])}")


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, help_text)


@bot.message_handler(commands=['cale'])
def cale(message):
    try:
        text = message.text[5:]
        example = eval(text)
        bot.send_message(message.chat.id, f"{example}")
    except Exception as e:
        bot.send_message(message.chat.id, f"возникла ошибка {e}")


@bot.message_handler(commands=['bars'])
def photo(message):
    try:
        text = message.text[5:]
        lst = text.split(',')

        value = lst[0].strip()
        name = lst[1].strip()

        value = value.split(" ")
        name = name.split(" ")

        value = list(map(int, value))

        safeBar(name, value, 'diagramma.png')
        with open('diagramma.png', 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
    except Exception as e:
        bot.send_message(message.chat.id,
                         f"Я не понимаю твоё сообщение, откройте список команд с помощью команды /help")


@bot.message_handler(commands=['graf'])
def gPhoto(message):
    try:
        text = message.text[5:]
        lst = text.split(',')

        begin = int(lst[0])
        end = int(lst[1])
        step = int(lst[2])
        func = lst[3]

        graph(begin, end, step, func, 'graf.png')
        with open('graf.png', 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
    except Exception as e:
        bot.send_message(message.chat.id,
                         f"ваш ввод был неправельным, он должен выглядеть примерно так"
                         f" /graf (число старта),(число конца),(шаг),x (+-/*) (любое число) "
                         f"за более понятным вводом обращайся /help")



@bot.message_handler(content_types=['text'])
def another_mesange(message):
    bot.send_message(message.chat.id, f"Я не понимаю твоё сообщение, откройте список команд с помощью команды /help")
