# -*- coding: utf-8 -*-

import telebot
from telebot import types

bot = telebot.TeleBot("529659050:AAHurAaKFXlywJK4EBQ4J0x0EwsezX-rt8o")

print("Test")

keyboard = types.InlineKeyboardMarkup(row_width=2)
url_button = types.InlineKeyboardButton(text="URL", url="https://ya.ru")
callback_button = types.InlineKeyboardButton(text="Callback", callback_data="test")
switch_button = types.InlineKeyboardButton(text="Switch", switch_inline_query="Telegram")
keyboard.add(url_button, callback_button, switch_button)
bot.send_message(message.chat.id, "Я – сообщение из обычного режима", reply_markup=keyboard)




if __name__ == '__main__':
    bot.polling(none_stop=True)
