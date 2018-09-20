import telebot
from telebot import types


def main():
    token = '667869143:AAGP9LD_Im7WXUGuxYfHfZ255WMBAdQO7JM'
    bot = telebot.TeleBot(token, threaded=False)
    curr = ['eur', 'usd']
    bot.polling()

    def create_keyboard():
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        buttons = [types.InlineKeyboardButton(text=c, callback_data=c) for c in curr]
        keyboard.add(*buttons)
        return keyboard

    @bot.callback_query_handler(func=lambda x: True)
    def callback_handler(query):
        message = query.message
        text = query.data
        currency, value = check_currency_value(text)
        if currency:
            bot.answer_callback_query(query.id, text=f'{currency} = {value}')
        else:
            bot.send_message(message.chat.id, text='Not found')

    def currency_in_message(message):
        for c in curr:
            if c in message.text.lower():
                return True
        return False

    def check_currency_value(text):
        currency_values = {'eur': 70, 'usd': 60}
        for c, v in currency_values.items():
            if c in text.lower():
                return c, v
        return None, None

    @bot.message_handler(commands=['rate'])
    @bot.message_handler(func=currency_in_message)
    def handle_message(message):
        currency, value = check_currency_value(message.text)
        keyboard = create_keyboard()
        if currency:
            bot.send_message(message.chat.id, text=f'{currency} = {value}', reply_markup=keyboard)
        else:
            bot.send_message(message.chat.id, text='Not found', reply_markup=keyboard)

    @bot.message_handler()
    def handle_message(message):
        print(message)
        bot.send_message(message.chat.id, text='Checking currencies')


if __name__ == '__main__':
    main()
