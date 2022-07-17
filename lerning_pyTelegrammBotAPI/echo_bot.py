import telebot
from telebot import types

bot_token = '5309057246:AAHlSg-gPpai544joQP21s2ZW94lpd57-oU'

bot = telebot.TeleBot(bot_token)


@bot.message_handler(commands=['123'])
def echo_ok(message):
    print(message.text)
    bot.reply_to(message, message.text)


@bot.message_handler(commands=['111'])
def show_inline_buttons(message):
    print('ok')
    inline_keyboard = types.InlineKeyboardMarkup(row_width=2)
    inline_button_1 = types.InlineKeyboardButton('inline_button_1', callback_data='inline_button_1')
    inline_button_2 = types.InlineKeyboardButton('inline_button_2', callback_data='inline_button_2')

    inline_keyboard.add(inline_button_1, inline_button_2)

    bot.send_message(message.chat.id, "Hello!", reply_markup=inline_keyboard)


@bot.message_handler()
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
