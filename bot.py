from dotenv import load_dotenv
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import pyjokes
import logging

# Load environment variables from .env file
load_dotenv()

# Get the bot token from environment variable
BOT_TOKEN = os.getenv("TOKEN")

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Command handler for the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Hello! I am your bot. How can I help you?')

# Command handler for the /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('List of commands:\n/start - Start the bot\n/help - Get help\n/joke - Get a random joke')

# Command handler for the /joke command
async def joke(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    joke_text = pyjokes.get_joke()
    await update.message.reply_text(joke_text)

# Handler for greeting messages
async def greet(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    greetings = ['hi', 'hello', 'hey', 'good morning', 'good afternoon', 'good evening']
    oromos=['akkam','nagumaa','jirtaa']
    user_message = update.message.text.lower()

    if any(greeting in user_message for greeting in greetings):
        await update.message.reply_text('Hello! How can I assist you today?')
    elif any(oromo in user_message for oromo in oromos):
        await update.message.reply_text('Akkam jirtuu! maal issin gargaaruu?')

# Error handler
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.warning(f'Update {update} caused error {context.error}')

def main() -> None:
    # Create the Application and pass it your bot's token
    application = Application.builder().token(BOT_TOKEN).build()

    # Register the command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("joke", joke))

    # Register the greeting handler
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), greet))

    # Register the error handler
    application.add_error_handler(error)

    # Start the Bot
    application.run_polling()

if __name__ == '__main__':
    main()
