import random
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
updater = Updater(token='565214317:AAEVUNqiyj1icAX0VUp4Lz4MWzrXTFxh0dA') # Токен API к Telegram
dispatcher = updater.dispatcher
# Обработка команд
def randm():
    msg=random.choice(['Учёный','Больной','Пикачу','Кот','Никто','Террорист','Сантехник','Динозавр','Мама','Менеджер'])
    msg=msg+' приходит '
    msg=msg+random.choice(['в офис','в небытие','в больницу','драться','в лабораторию','на вызов','в парк Юрского периода','на родительское собрание','к кошке','в метро'])
    msg=msg+' и говорит '+'"'
    msg=msg+random.choice(['Какой серьёзный затор.','Возьмите меня есть туристов.','Аллах Акбар!','Я увольняюсь.','Я мама Вовочки.','Давай заведём кота.','У меня болит голова.','Мысленно "Привет, Ничто."','Пика-пика!','Я совершил открытие!'])
    msg=msg+'" '+'A '
    msg=msg+random.choice(['Бульбазавр на это','а начальник ему','а из трубы голос','в ответ слышит','учёное сообщество:','тут по громкоговорителю','доктор ему','Небытие ему в ответ','учительница:','кошка отвечает'])
    msg=msg+' "'
    msg=msg+random.choice(['Ты не Пикачу, ты сантехник.','Я не доктор, я динозавр.','Давай лучше мышат.','Привет, ничтожество.','Следующая станция бесконечная.','Вы не мама, вы папа.','Нам такие не нужны.','Ты же на пенсию вышел.','Ты новый Энштейн!','Ну хочешь шутку расскажу.'])
    msg=msg+' "'
    msg=msg+random.choice([' ))))',' И немедленно выпил.',' С тех пор это закон.',' Так появилась вселенная.',' Вот и сказочке конец.',' И все стали танцевать.',' Держите зачётку.',' Динозавр всё-равно съел туристов.',' И уехали в Казахстан.',' Энтропия нарастала.'])
    msg='История № '+str(random.randint(1,37525)+random.random()) +': '+ msg
    print(msg)
    random.seed()
    return(msg)

def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Привет, хочешь офигительных историй? Их есть у меня!')
def textMessage(bot, update):
    response = randm()
    bot.send_message(chat_id=update.message.chat_id, text=response)
# Хендлеры
start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)
# Добавляем хендлеры в диспетчер
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)
# Начинаем поиск обновлений
updater.start_polling(clean=True)
# Останавливаем бота, если были нажаты Ctrl + C
updater.idle()





