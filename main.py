from telegram.ext import CallbackContext, Updater, MessageHandler, Filters, CommandHandler
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup

import os 

TOKEN = os.environ['TOKEN']

def start(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id
    bot = context.bot
    # like emoji unicode: U+1F44D
    # dislike emoji unicode: U+1F44E
    like = KeyboardButton(text = '\U0001F44D')
    dislike = KeyboardButton(text = '\U0001F44E')

    keyboard = ReplyKeyboardMarkup([
        [like, dislike]
    ], resize_keyboard=True)

    bot.sendMessage(chat_id=chat_id, text="Click like or dislike", reply_markup=keyboard)

def text(update: Update, context: CallbackContext):

    bot = context.bot
    message = update.message.text
    chat_id = update.message.chat.id

    bot.sendMessage(chat_id=chat_id, text=message)

updater = Updater(token=TOKEN)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, text))

updater.start_polling()