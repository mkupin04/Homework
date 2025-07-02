import telebot
import random
import os
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = "7185174306:AAHowuwl7KR0LWBwdttLCX8nrfpvyBKcGcA"
bot = telebot.TeleBot(TOKEN)

UPLOAD_FOLDER = "C:/Users/Максим/OneDrive/Dokumenty/python/Create bot API/Меми/"

memes = os.listdir(UPLOAD_FOLDER)

def meme_choise(message):
    meme = random.choice(memes)
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button_like = KeyboardButton("👍")
    button_dislike = KeyboardButton("👎")
    button_info = KeyboardButton("Інфо")
    keyboard.row(button_like, button_dislike)
    keyboard.row(button_info)

    with open(UPLOAD_FOLDER + meme, "rb") as photo:
        bot.send_photo(message.chat.id, photo)

    bot.send_message(message.chat.id, "Тобі сподобався мем?", reply_markup=keyboard)


@bot.message_handler(content_types=["photo"])
def recive_meme(message):
    file_info = bot.get_file(message.photo[-1].file_id)

    dowloaded_file = bot.download_file(file_info.file_path)

    file_name = str(len(memes) + 1) + ".jpg"
    with open(UPLOAD_FOLDER + file_name, "wb") as new_file:
        new_file.write(dowloaded_file)
    
    memes.append(file_name)
    
    bot.reply_to(message, "мем отримано")

@bot.message_handler(commands=["start"])
def start(message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button_start = KeyboardButton("Почати")
    keyboard.add(button_start)
    bot.send_message(message.chat.id, "Привіт, тут ти зможеж подивитись різні меми та додати свої!", reply_markup=keyboard)
 
@bot.message_handler(commands=["count"])
def count(message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton("Продовжити")
    keyboard.add(button)
    count = len(memes)
    bot.send_message(message.chat.id, f"Наразі в мене є {count} мемів", reply_markup=keyboard)
    
@bot.message_handler(commands=["meme"])
def send_random_meme(message):
    if memes:
        meme_choise(message)
    else:
        bot.reply_to(message, "Мемів поки немає :(")

@bot.message_handler(func=lambda message: True)
def handle_callback(message):
    if message.text == "Почати":
        meme_choise(message)
    
    elif message.text == '👍':
        bot.send_message(message.chat.id, "Радий що тобі сподобалось!")
        meme_choise(message)

    elif message.text == '👎':
        bot.send_message(message.chat.id, "Жаль, попробую підібрати щось інше")
        meme_choise(message)

    elif message.text == 'Інфо':
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        button = KeyboardButton("Продовжити")
        keyboard.add(button)
        bot.send_message(message.chat.id, "щоб додати свій мем просто скинь його боту. Ти можеж використовувати такі комінди: /start, /meme, /count", reply_markup=keyboard)

    elif message.text == "Продовжити":
        meme_choise(message)

    
    pass


bot.polling()
