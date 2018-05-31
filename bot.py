#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Simple Bot to reply to roll dice.
A must have for RPG Fans.

"""

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from Roll import Roll, WodRoll
import os
import arquetipo as arq


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Oi! Ainda não corrijo erros. Digite /roll NdF, ex. 3d10"')


def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help! Please, help!!!')


def echo(bot, update):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def error(bot, update):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)

def arquetipo(bot, update, args):
    "Print arquetype information"
    query = arq.get_info(args)
    bot.send_message (chat_id=update.message.chat_id, text=query)

def xp(bot, update):
    bot.send_photo (chat_id=update.message.chat_id, photo=open ('img/xp.png', 'rb'))


def roll(bot, update, args):
    args = args[0]
    roll = Roll(args)

    bot.send_message (chat_id=update.message.chat_id, text="Rolling {} : {}".format(args, roll.roll_dice()))


def wod_roll(bot, update, args):
    """"
    World of Destruction Rolls
    """
    args = ' '.join(args).upper()

    roll = WodRoll(args)
    n, d, result, message = roll.roll_dice()

    bot.send_message (chat_id=update.message.chat_id, text="Rolling {}d10 : Dificuldade {} \n"
                                                           "Result: {} => {}".format(n,d,result, message ))


def unknown(bot, update):
    bot.send_message (chat_id=update.message.chat_id, text="Desculpas. Não entendi esse comando.")


def main():
    token = os.environ['TELEGRAM_TOKEN']
    """Start the bot."""

    print ('Running bot... ')
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(token)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler (CommandHandler("xp", xp))
    dp.add_handler(CommandHandler("roll", roll, pass_args=True))
    dp.add_handler(CommandHandler("wod", wod_roll, pass_args=True))
    dp.add_handler (CommandHandler("arquetipo", arquetipo, pass_args=True))


    dp.add_handler(MessageHandler(Filters.command, unknown))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == "__main__":
    main()
