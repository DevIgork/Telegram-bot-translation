import logging
import speech_recognition as sr
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler
from googletrans import Translator, LANGUAGES
from pydub import AudioSegment



TOKEN = "6020719509:AAEziDsJjyqDtz9ZcC0Pj7WumjdxKh9pc3o"

logging.basicConfig(level=logging.INFO)

translator = Translator()

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        'Вітаю! Я бот, що перекладає текст. Напишіть текст для перекладу в разі виникниння помилки напишіть /help:'
    )

def help_command(update: Update, context: CallbackContext):
    update.message.reply_text(
        'Вітаю! Я бот, що перекладає текст. Для початку перекладу, напишіть текст і виберіть з доступних мов переклад в разі виникнення помилки нажміть на кнопку знов поки не перекладе це связано з проблемами в google api. '
    )

def translate(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    data = query.data.split(';')
    text = data[1]
    dest_lang = data[2]

    translation = None
    while translation is None:
        translation = Translator().translate(text, dest=dest_lang).text

    query.edit_message_text(translation)



def voice_message(update: Update, context: CallbackContext):
    file_id = update.message.voice.file_id
    file = context.bot.get_file(file_id)
    file.download('voice.ogg')

    # Convert OGG to WAV
    ogg_file = AudioSegment.from_ogg('voice.ogg')
    ogg_file.export('voice.wav', format='wav')

    recognizer = sr.Recognizer()
    with sr.AudioFile('voice.wav') as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio, language='uk-UA')
        update.message.text = text
        choose_language(update, context)
    except sr.UnknownValueError:
        update.message.reply_text("Вибачте, я не зміг розпізнати ваше голосове повідомлення.")
    except sr.RequestError as e:
        update.message.reply_text(f"Помилка сервісу розпізнавання мови; {e}")

def choose_language(update: Update, context: CallbackContext):
    text = update.message.text
    print(f"Користувач вводить: {text}")

    languages = {
        'uk': 'Українська',
        'en': 'Англійська',
        'zh-CN': 'Китайська',
        'ja': 'Японська',
        'fr': 'Французька',
    }

    buttons = [
        InlineKeyboardButton(languages[lang_code], callback_data=f"translate;{text};{lang_code}")
        for lang_code in languages
    ]

    update.message.reply_text(
        'Оберіть мову перекладу:',
        reply_markup=InlineKeyboardMarkup.from_column(buttons)
    )

def main():
    try:
        updater = Updater(TOKEN)

        dispatcher = updater.dispatcher
        dispatcher.add_handler(CommandHandler("start", start))
        dispatcher.add_handler(CommandHandler("help", help_command))
        dispatcher.add_handler(MessageHandler(Filters.voice, voice_message))
        dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, choose_language))
        dispatcher.add_handler(CallbackQueryHandler(translate))

        updater.start_polling()
        updater.idle()
    except Exception as e:
        logging.error(str(e))

if __name__ == '__main__':
    main()