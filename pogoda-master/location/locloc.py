#pognali nahui
import telebot
from telebot import types
from config import open_weather_token
bot = telebot.TeleBot(API Token)

@bot.message_handler(commands=["start"])
def start (message):
    #Клавиатура с кнопкой запроса локации
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
    keyboard.add(button_geo)
    bot.send_message(message.chat.id, "Поделись местоположением", reply_markup=keyboard)

 #Получаю локацию
@bot.message_handler(content_types=['location'])
def location (message):
    if message.location is not None:
        locloc = message.location
        print(locloc)

bot.polling(none_stop = True)
input()
