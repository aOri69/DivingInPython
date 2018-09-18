import telebot


def main():
    token = '667869143:AAGP9LD_Im7WXUGuxYfHfZ255WMBAdQO7JM'
    bot = telebot.TeleBot(token, threaded=False)

    bot.polling()

    @bot.message_handler()
    def handle_message(message):
        print(message.text)


if __name__ == '__main__':
    main()
