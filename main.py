import telebot
from telebot import types

TOKEN = '1641838971:AAE7f1qbLi5S-WU9GCHM3ojtrW7KXyRXqyE'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, 'Привет, Тимур, готов выполнять задания и получать призы?')
    elif message.text == 'Да' or message.text == 'Выполнил':
        keyboard = types.InlineKeyboardMarkup()
        key_ekz = types.InlineKeyboardButton(text='Экзамен, но ты не пугайся) (500 рублей)', callback_data='экзамен')
        keyboard.add(key_ekz)
        key_shash = types.InlineKeyboardButton(text='Шашки, но необычные (2000 рублей)', callback_data='шашки')
        keyboard.add(key_shash)
        key_maf = types.InlineKeyboardButton(text='Мафия (1000 рублей) ', callback_data='мафия')
        keyboard.add(key_maf)
        key_foot = types.InlineKeyboardButton(text='Футбольчик (2000 рублей) ', callback_data='футбол')
        keyboard.add(key_foot)
        key_salat = types.InlineKeyboardButton(text='Айдаман (500 рублей) ', callback_data='айдаман')
        keyboard.add(key_salat)
        bot.send_message(message.from_user.id, text='Тогда выбери одно задание ниже', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'экзамен':
        bot.send_message(call.from_user.id, 'Отличный выбор! Задание: сесть в машину и сдать экзамен по вождению')
    if call.data == 'шашки':
        bot.send_message(call.from_user.id, 'Играем по крупному! Задание: Сыграть в шашки с любым игроком, которого ты выберешь')
    if call.data == 'мафия':
        bot.send_message(call.from_user.id, 'Неплохо, Тимур! Задание: Сыграть в мафию и выиграть)')
    if call.data == 'футбол':
        bot.send_message(call.from_user.id, 'Идем дальше! Задание по адресу: адрес поля возле 6 школы)')
    if call.data == 'айдаман':
        bot.send_message(call.from_user.id, 'Супер! Задание: подготовиться быть вожатым)')


bot.polling(none_stop=True, interval=0)
