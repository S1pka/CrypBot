import telebot
from config import keys, token
from extensions import CryptoConverter, APIExeption




bot = telebot.TeleBot(token)




@bot.message_handler(commands=['start', 'help'])
def action(message: telebot.types.MessageID):
     text = ("Hi my Dier Friend! Чтобы начать работу ведите команду боту в следующей формате:   <Имя валюты>"
             "<В какую валюту перевести>"
             "<Количество>\n"
             "Чтобы уиведеть доступные валюты наберите команду </values>"
            )
     bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(messages: telebot.types.Message):
    text = 'Value: '
    for key in keys.keys():
       text = '\n'.join((text,key, ))
    bot.reply_to(messages,text)



@bot.message_handler()
def convereter(message: telebot.types.Message):
    try:
         values =  message.text.split(' ')
         if len(values) != 3:
             raise APIExeption('СЛИШКОМ МНОГО ПАРАМЕТРОВ.')
         quote, base, amount = values
         total_base = CryptoConverter.convert(quote, base, amount)
    except APIExeption as e:
        bot.reply_to(message, f"Ошибка пользователя.\n {e}")

    except Exception as e:
        bot.reply_to(message,f'Не удалсь обработать команду \n {e}')
    else:
          text = f'Цена {amount} {quote} в {base} - {total_base} '
          bot.send_message(message.chat.id, text)

bot.polling()