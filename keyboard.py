import telegram
from telegram import ReplyKeyboardMarkup, KeyboardButton
import os 

TOKEN = os.environ["TOKEN"]

bot = telegram.Bot(TOKEN)

button1 = KeyboardButton(text='Button1', request_contact=True)
button2 = KeyboardButton(text='Button2')

buttons = [
    [button1, button2]
]
keyboard = ReplyKeyboardMarkup(buttons, resize_keyboard=True)

update = bot.getUpdates()[-1]
chat_id = update.message.chat.id

msg = bot.sendMessage(chat_id, "Keyboard", reply_markup = keyboard)

print(msg)