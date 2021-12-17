from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re
def get_url(): #Создаем функцию, чтобы получить картинку
    pictures = requests.get('https://aws.random.cat/meow.json').json()
    url = pictures['url'] #Получили url, чтобы иметь возможность отправить изображение
    return url

def get_image_url():
    allowed_extension = ['jpg','jpeg','png'] #Разрешенные форматы
    file_extension = ''
    while file_extension not in allowed_extension: #Будет искать, пока не будет норм формата
        url = get_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url

def bop(bot, update):
    url = get_image_url()
    chat_id = update.message.chat_id #Для получения id получателся
    bot.send_photo(chat_id=chat_id, photo=url) #Бот отправляет изображение

def main(): #Функция для запуска проги
    updater = Updater('5069121340:AAEFDLJLYe2HmXmBSTMhmPaj_aTI-rB0k7c') #надо ввести
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop)) #тут неуверена в bop
    updater.start_polling()
    updater.idle()
    
if __name__ == '__main__':
    main()
