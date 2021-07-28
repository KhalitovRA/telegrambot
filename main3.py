import telebot
from telebot import types

TOKEN = '1641838971:AAE7f1qbLi5S-WU9GCHM3ojtrW7KXyRXqyE'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, 'Привет, Тимур, готов выполнять задания и получать призы?')
    elif message.text == 'Да':
        bot.send_message(message.from_user.id, 'Тогда погнали, первое задание! Вычисли мафию и получи приз и следующую подсказку!!!')
    elif message.text == 'Kill':
        bot.send_message(message.from_user.id, 'Круто! Второе задание - экзамен!)')
    elif message.text == 'Rich':
        bot.send_message(message.from_user.id, 'Супер! Задание по адресу: Напольная 2  ')
    elif message.text == 'Drink':
        bot.send_message(message.from_user.id, 'Задание: Попробуй выжить! Сыграй в шашки, но необычные')
    elif message.text == 'Sniper':
        bot.send_message(message.from_user.id, 'Задание: Не промахнись!')
    elif message.text == 'Done':
        bot.send_message(message.from_user.id, 'Молодец! справился со всеми заданиями! С Днем Рождения, наш Мудачок❤')
bot.polling(none_stop=True, interval=0)
