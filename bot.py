import os
import telebot
from io import BytesIO
import cv2
from sentinal import senal
BOT_TOKEN = "6547348303:AAEnlJLjYn7Nb43ACyQXuy3Q2_Nrl0nqk1E"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'check'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(content_types=['photo'])
def photo(message):
    print ('message.photo =', message.photo)
    fileID = message.photo[-1].file_id
    print ('fileID =', fileID)
    file_info = bot.get_file(fileID)
    print(file_info)
    print ('file.file_path =', file_info.file_path)
    downloaded_file = bot.download_file(file_info.file_path)
    with open("images/image.jpg", 'wb') as new_file:
        new_file.write(downloaded_file)
    emo = senal();
    st = ''
    for x in emo.keys():
        st+=f'{x} : {emo[x]} \n'
    # st = 'jello'
    bot.reply_to(message,st)

bot.infinity_polling()