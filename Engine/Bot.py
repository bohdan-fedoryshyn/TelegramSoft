import telebot


bot = telebot.TeleBot("1143333191:AAG8JA8OB6kuZDomwllT9ztKp-_IM7KKi1g", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN


@bot.message_handler(commands=['start'])
def send_welcome(message):
    print(message.chat.id)
    bot.send_message(message.chat.id, "Howdy, how are you doing?")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)


bot.infinity_polling()