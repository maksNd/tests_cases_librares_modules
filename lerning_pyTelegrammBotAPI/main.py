import telebot
from telebot import types

bot_token = '5502806240:AAGM7kRYiAIr6s5yTGl5NRXW_IPGn8wLS34'

bot = telebot.TeleBot(bot_token)


@bot.message_handler(commands=['buttons'])  # обработать сообщение /buttons как комманду
def show_ordinary_buttons(message):
    # bot.reply_to(message, "Howdy, how are you doing?")

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Создаем клавиатуру
    button_1 = types.KeyboardButton('Button_1')  # Создаем кнопку для клавиатуры
    button_2 = types.KeyboardButton('Button_2')  # Создаем кнопку для клавиатуры
    keyboard.add(button_1, button_2)

    bot.send_message(message.chat.id, "Hello!", reply_markup=keyboard)


@bot.message_handler()
def pressed_ordinary_buttons(message):  # Обработка нажатий на кнопки
    if message.text == 'Button_1':
        bot.send_message(message.chat.id, message.text, reply_markup=None)
    elif message.text == 'Button_2':
        bot.send_message(message.chat.id, message.text, reply_markup=None)


@bot.message_handler(commands=['inline'])
def show_inline_buttons(message):
    print('ok')
    inline_keyboard = types.InlineKeyboardMarkup(row_width=2)
    inline_button_1 = types.InlineKeyboardButton('inline_button_1', callback_data='inline_button_1')
    inline_button_2 = types.InlineKeyboardButton('inline_button_2', callback_data='inline_button_2')

    inline_keyboard.add(inline_button_1, inline_button_2)

    bot.send_message(message.chat.id, "Hello!", reply_markup=inline_keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == 'inline_button_1':
            bot.send_message(call.message.chat.id, 'Вот и отличненько 😊')
        elif call.data == 'inline_button_2':
            bot.send_message(call.message.chat.id, 'Бывает 😢')

        # # remove inline buttons
        # bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😊 Как дела?",
        #                       reply_markup=None)
        #
        # # show alert
        # bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
        #                           text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!!11")


# @bot.callback_query_handlers(func=lambda call: True)
# def pressed_inline_buttons(call):  # Обработка нажатий на кнопки
#     if call.data == 'inline_button_1':
#         bot.send_message(call.message.chat.id, "inline_button_1")
#     elif call.data == 'inline_button_2':
#         bot.send_message(call.message.chat.id, "inline_button_2")


bot.infinity_polling()
