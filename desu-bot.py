import logging
import re
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

TOKEN = 'placeholder' #Put your bot's token here

def start(update: Update, context: CallbackContext):
    update.message.reply_text('Hello! I am your Desu-bot.')

def process_message(update: Update, context: CallbackContext):

    message = update.message
    regex = r'\b(tbh)\b'
    new_text = re.sub(regex, 'desu', message.text, flags=re.IGNORECASE)
    if new_text != message.text:
        message.reply_text(new_text)

async def error(update: Update, context: CallbackContext):
    print(f'Update {update} caused error {context.error}')

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, process_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
