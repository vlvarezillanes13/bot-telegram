from unicodedata import name

from django.urls import clear_script_prefix
from config import * #config
import telebot #api de bot
#Instancia del bot
bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=["start","ayuda","help"])
def cmd_start(message):
    """Bienvenida"""
    bot.reply_to(message, "Me has llamado?")

@bot.message_handler(content_types=["text"])
def bot_mensajes_texto(message):
    bot.send_message( message.chat.id,"Escribiste algo")



### MAIN ###
if __name__ == '__main__':
    print('INICIADO  BOT')
    bot.infinity_polling()