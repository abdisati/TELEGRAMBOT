from dotenv import load_dotenv
import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import pyjokes


load_dotenv()

BOT_TOKEN=os.getenv("TOKEN")


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am your bot. How can I help you?')

# Command handler for the /help command
def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('List of commands:\n/start - Start the bot\n/help - Get help\n/joke - Get a random joke')

# Command handler for the /joke command
def joke(update: Update, context: CallbackContext) -> None:
    joke_text = pyjokes.get_joke()
    update.message.reply_text(joke_text)

def main() -> None:
    # Create the Updater and pass it your bot's token
    updater = Updater(BOT_TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register the command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("joke", joke))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()