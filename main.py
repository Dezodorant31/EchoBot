import telebot
import config


bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(content_types=['text'])
def send_mess(message):
    bot.send_message(message.chat.id, message.text)


# Run bot
bot.polling(none_stop=True)

# t.me/myFEcho_bot
