import telebot
from telebot import types

TOKEN = '1641838971:AAE7f1qbLi5S-WU9GCHM3ojtrW7KXyRXqyE'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, 'Привет, начнем!')
    if message.text == 'Выполнил' or message.text == 'Да':
        service = telebot.types.ReplyKeyboardMarkup(True, True)
        service.row('Экзамен')
        service.row('Шашки')
        service.row('Мафия')
        service.row('Задание по адресу')
        bot.send_message(message.from_user.id, 'Выбери задание)', reply_markup=service)
    if message.text == "Экзамен":
        a = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, 'Идём дальше?', reply_markup=a)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "Экзамен":
        a = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, 'Дальше', reply_markup=a)
    if message.text == "Шашки":
        a = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, 'Дальше', reply_markup=a)
    if message.text == "Мафия":
        a = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, 'Дальше', reply_markup=a)
    if message.text == "Задание по адресу":
        a = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, 'Дальше', reply_markup=a)


bot.polling(none_stop=True, interval=0)
