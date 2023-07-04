import telebot
from telebot import types
bot = telebot.TeleBot('6253318512:AAEVeEMQqI38RibiTXnurECjX6fZ0yRNtRY')

#bot.send_message(message.from_user.id, "Для начала напиши /start")

name = ''
surname = ''
age = 0

'''
@bot.message_handler(content_types=['text', 'document', 'audio'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
'''


@bot.message_handler(content_types=['text', 'document', 'audio'])
def start(message):
    
    if message.text == '/reg':
        print('reg')
        global name 
        name = ''
        global surname 
        surname = ''
        global age 
        age = 0
        bot.send_message(message.from_user.id, "Как тебя зовут?")
        bot.register_next_step_handler(message, get_name) #следующий шаг – функция get_name
    elif message.text == "/start":
        print('start')
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "Привет":
        print('Hi')
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        print('help')
        bot.send_message(message.from_user.id, "Напиши /reg")
    else:
        print('else help')
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

def get_name(message): #получаем фамилию
    print('name')
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, get_surname)

def get_surname(message):
    print('surname')
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, 'Сколько тебе лет?')
    bot.register_next_step_handler(message, get_age)


def get_age(message):
    print('age')
    global age
    age = int(message.text)
    if age == 0:
                bot.send_message(call.message.chat.id, 'Неккорректный возраст. Попробуй еще раз!')
                print('age incorr')
                bot.send_message(call.message.chat.id, 'Сколько тебе лет?')
                bot.register_next_step_handler(message, get_age)
    while age == 0: #проверяем что возраст изменился
        try:
            age = int(message.text) #проверяем, что возраст введен корректно
            print('age corr')
        except Exception:
             bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
             print('age incorr')
        keyboard = types.InlineKeyboardMarkup() #наша клавиатура
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes') #кнопка «Да»
        keyboard.add(key_yes) #добавляем кнопку в клавиатуру
        key_no= types.InlineKeyboardButton(text='Нет', callback_data='no')
        keyboard.add(key_no)
        question = 'Тебе '+str(age)+' лет, тебя зовут '+name+' '+surname+'?'
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes": #call.data это callback_data, которую мы указали при объявлении кнопки
        bot.send_message(call.message.chat.id, 'Yes') #код сохранения данных, или их обработки
        bot.send_message(call.message.chat.id, 'Запомню : )')
    elif call.data == "no":
        bot.send_message(call.message.chat.id, 'No')
        start('/reg') #переспрашиваем

bot.polling(none_stop=True, interval=0)