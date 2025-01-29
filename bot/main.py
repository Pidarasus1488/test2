import os
import random
import telebot

texts = [
    "Есть три основных способа переработки пластика: механический, химический и термический. Механическая переработка – способ, при котором пластик сортируют, моют, дробят и делают гранулу. При механическом методе полимерную цепочку пластика не разрушают, а очищают, измельчают и плавят подготовленный материал.",
    "В контейнеры для раздельного сбора можно сдавать: алюминий; ПЭТ — обычные пластиковые бутылки, в которых продают напитки, масла и др. Отмечены маркировкой «01»/PET. бутылки/канистры/флаконы, например из-под косметических средств, с маркировкой «02», HDPE, «ПНД».",
    "Самый опасный вид пластика — ПВХ (PVC). При сжигании он выделяет в воздух очень токсичные диоксины. Содержащиеся в нем пластификаторы могут вызывать поражение печени и почек, бесплодие, рак. При возможности ограничьте использование изделий из ПВХ."
]

bot = telebot.TeleBot('8029708237:AAHOEJwjyjMLVSVxnMWmNmc4TCUcNIdrCAY');

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Доброго времени суток, человек! Введи /sovet ")

@bot.message_handler(commands=['sovet_photo'])
def send_mem(message):
    img_name = random.choice(os.listdir('cache'))
    with open(f'cache/{img_name}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)  

# Обработчик команды /random
@bot.message_handler(commands=['sovet_text'])
def send_random_text(message):
    random_text = random.choice(texts)  # Выбор случайного текста
    bot.send_message(message.chat.id, random_text)  # Отправка сообщения

@bot.message_handler(commands=['sovet'])
def send_welcome(message):
    bot.reply_to(message, "/sovet_text или /sovet_photo")


@bot.message_handler(content_types=['animation', 'audio', 'contact', 'dice', 'document', 'location', 'photo', 'poll', 'sticker', 'text', 'venue', 'video', 'video_note', 'voice'])
@bot.message_handler(commands=['sovet_text'])
def send_welcome(message):
    bot.reply_to(message, 'Пон')

bot.polling()