from telegram.ext import CallbackContext, Updater, MessageHandler, Filters, CommandHandler
from telegram import Update

import os 

TOKEN = os.environ['TOKEN']

def start(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id
    bot = context.bot

    bot.sendMessage(chat_id, "Bizning botga hush kelibsiz!")

def text(update: Update, context: CallbackContext):
    bot = context.bot
    message = update.message.text
    chat_id = update.message.chat.id
    like = 0
    dislike = 0
    text = f"LIKE: {like}\nDISLIKE: {dislike}"
    bot.sendMessage(chat_id=chat_id, text=text)

updater = Updater(token=TOKEN)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, text))

updater.start_polling()