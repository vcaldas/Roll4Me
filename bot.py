TOKEN = '548521253:AAEA6jgci6DR2IrgoF9TTIc5pmf86o3UJKM'
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Simple Bot to reply to roll dice.
A must have for RPG Fans.

"""

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import random


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
    update.message.reply_text('Help!')


def echo(bot, update):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def get_dice_params(args):
    """

    :param args: Argument containing the number of dice and the faces, ex. d10, d20, 2D10, 4D6
    :return: n number of dice to roll
             f number of faces in the dice
    """
    args = ' '.join (args).upper ()
    # Format can be DN or XDN

    parts = args.split("D")

    if parts[0] == "":
        parts[0] == 1

    return parts[0], parts[1]


def roll_dice(n,f):
    """

    :param n: Number of dices to roll
    :param f: Number of faces in the dice
    :return: List of results
    """
    n = int(n)
    f = int(f)

    rolls = []

    for j in range (n):
        rolls.append (random.randint (1, f))

    return rolls


def roll(bot, update, args):

    n, f = get_dice_params(args)


    rolls = roll_dice(n,f)
    #bot.send_message (chat_id=update.message.chat_id, text=text_caps)
   # update.message.reply_text (text_caps)
    update.message.reply_text("Rolling {} : {}".format(args, rolls) )


def main():
    """Start the bot."""
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("roll", roll, pass_args=True))

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


if __name__ == '__main__':
    main()