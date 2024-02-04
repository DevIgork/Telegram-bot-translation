# Text Translator Bot ReadMe

This Python script implements a simple Telegram bot that translates text messages and voice messages from Ukrainian to various languages. The bot utilizes the Telegram API for communication and integrates with Google Translate for text translation. Additionally, it employs the SpeechRecognition library to convert voice messages to text.

## Requirements
- Python 3.x
- Install required libraries using the following:
  ```bash
  pip install python-telegram-bot googletrans==4.0.0-rc1 pydub SpeechRecognition
  ```

## Getting Started
1. Obtain a Telegram bot token from [@BotFather](https://t.me/BotFather).
2. Replace `"your token"` in the script with the obtained token.

## How to Use
1. Start a chat with the bot.
2. Send a text message to get started. The bot will prompt you to choose the language for translation.
3. Alternatively, you can send a voice message. The bot will convert the voice to text using Google Speech Recognition and prompt you to choose the language for translation.

## Commands
- `/start`: Initiates a conversation with the bot and provides a brief welcome message.
- `/help`: Displays a help message explaining how to use the bot.

## Functionality
- Text Translation:
  - Users can input text messages, and the bot provides translation options in various languages.
  - In case of errors or issues with the translation service, users can press the "Translate" button again until successful.

- Voice Message Translation:
  - Users can send voice messages, and the bot converts the audio to text using Google Speech Recognition.
  - After converting to text, users are prompted to choose the language for translation.

## Supported Languages
- Ukrainian (Source Language)
- English
- Chinese
- Japanese
- French

## Troubleshooting
- If there are issues with the translation service, such as Google API problems, the bot will inform users about the error.

## Note
- This script assumes that the user is communicating in the Ukrainian language.

Feel free to explore and modify the script as needed!
