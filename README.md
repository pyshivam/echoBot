# EchoBot - Telegram Bot

Simple Bot to reply to Telegram messages and print Channel messages.

This Bot uses the Updater class to handle the bot.

First, a few handler functions are defined after that those functions are passed to the dispatcher and registered at their respective places.

Bot will be started and runs until we press Ctrl-C on the command line.


## Installation

    pip3 install -r requirement.txt

It will install `python-telegram-bot` This library provides a pure Python interface for the Telegram Bot API. 


## Usage

### Edit echoBot.py

    TOKEN = "your token"

### Start bot

    python3 echoBot.py

Basic Echobot example, repeats messages and prints Channel messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
