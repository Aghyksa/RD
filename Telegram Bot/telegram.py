import telebot

bot = telebot.TeleBot("6421673458:AAFl1ZMC17dj-v1DvJOJIm6NerEGv_f8U4c")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()