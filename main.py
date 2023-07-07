from telegram.ext import CallbackContext, Updater, MessageHandler, Filters
from telegram import Update

import os 

TOKEN = os.environ['TOKEN']


def text(update: Update, context: CallbackContext):
    message = update.message.text
    chat_id = update.message.chat.id
    print(message, chat_id)

updater = Updater(token=TOKEN)

updater.dispatcher.add_handler(MessageHandler(Filters.text, text))

updater.start_polling()