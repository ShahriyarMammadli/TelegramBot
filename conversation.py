# Shahriyar Mammadli
# Simple Telegram bot with two functions: 1. return current time if '/time'...
# ...command is used and 2. repeat given input for all other cases
# Import required libraries
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import datetime

# Reply the current time
def time(update, context):
    update.message.reply_text('{:%H:%M:%S}'.format(datetime.datetime.now()))

# Repeat the user message
def repeat(update, context):
    update.message.reply_text(update.message.text)

def main():
    # Initialize the bot
    # User token
    token = ""
    updater = Updater(token, use_context=True)

    dp = updater.dispatcher

    # What to do in different commands
    #dp.add_handler(CommandHandler("repeat", repeat))
    dp.add_handler(CommandHandler("time", time))

    # For a normal message use repeat function
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, repeat))

    # Starting the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()