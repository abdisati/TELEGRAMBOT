Telegram Joke Bot

A simple Telegram bot built in Python that responds to greetings, provides help commands, and tells random jokes. It supports both English and Oromo greetings.

Features

Responds to /start command with a welcome message.

Responds to /help command with a list of available commands.

Responds to /joke command with a random joke using the pyjokes library.

Replies to greetings in English and Oromo languages.

Handles errors and logs them for debugging purposes.

🛠 Technologies Used

Python 3.x

python-telegram-bot

python-dotenv

pyjokes

📂 Project Structure
.
├── bot.py           # Main bot script
├── .env             # Environment variables (BOT_TOKEN)
└── requirements.txt # Project dependencies

⚡ Setup and Installation

Clone the repository:

git clone https://github.com/your-username/telegram-joke-bot.git
cd telegram-joke-bot


Create a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt


Create a .env file in the project root and add your Telegram bot token:

TOKEN=your-telegram-bot-token


Run the bot:

python bot.py

🤖 Usage

/start – Start the bot and get a welcome message.

/help – List all available commands.

/joke – Get a random joke.

Greetings like hi, hello, akkam – The bot will respond appropriately.

📝 Contributing

Contributions are welcome! Feel free to submit issues or pull requests to improve the bot.
