#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Simple Bot to reply to Telegram messages and print Channel messages.
This Bot uses the Updater class to handle the bot.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages and prints Channel messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""
from telegram import Bot, Update
from telegram.ext import Updater, MessageHandler, CommandHandler
from telegram.ext.filters import Filters
import logging


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.

chat_id_of_channel = -1001169150122
TOKEN = '577029885:AAGHJElNz3nm8zc9zzpWS1G843f2AZqG2zA'


def start(bot: Bot, update: Update):
    """Send a message when the command /start is issued."""
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text="hi there, welcome to my channel")


# Print messages received from channel.
def channel_message(bot: Bot, update: Update):
    msg = update.effective_message
    print("Message received from channel: %s" % str(msg['text']))


# Reply user with uppercase messages of user.
def reply_upper(bot: Bot, update: Update):
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=update.message.text.upper())



# Main Function of bot, here we are defining all handlers we require.
def main():
    updater = Updater(TOKEN)
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(MessageHandler(Filters.chat(chat_id=chat_id_of_channel), channel_message))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, reply_upper))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
