import telebot


# todo:                                  ..:: Key Words ::..


key_words1 = ["математик", "дослідження операцій", "статистик", "економік", "фізик", "ймовірності", "тімс",
              "матаналіз", "курсов", "дипломн", "реферат", "презентаці", "статистиці", "філософі", "алгебр",
              "економетри" , "економіці", "курсач", "численні методи", "численним методам"]

key_words2 = ["допомога", "допоможе", "зробити", "виконати", "допомогти", "помогти", "помощь", "потрібен"]

res_msg = ["Звертайтесь до @kakadesa", "Увага ! Дуже багато шахраїв ! Перевіряйте виконавців, які відгукнуться "
           "( відгуки, гарантії, бот @ugodabot, робота наперед )"]


# todo:                                  ..:: Code ::..


bot = telebot.TeleBot("5480236027:AAFVSKP_ujUosykr0YlRCkmT1Hj4-HGSNmA", parse_mode='html')


def for_in(array, message):
    for item in array:
        if item.lower() in message.lower():
            return True


@bot.message_handler()
def botTelegramRandomMessage(message):
    result = for_in(key_words1, message.text)
    if result:
        print(message)
        return bot.send_message(message.chat.id, res_msg[0])
    result2 = for_in(key_words2, message.text)
    if result2 and not for_in(key_words1, message.text):
        return bot.send_message(message.chat.id, res_msg[1])


if __name__ == '__main__':
    bot.infinity_polling(timeout=10, long_polling_timeout=5)


# todo:                                  ..:: Devs ::..
# pip install pyTelegramBotAPI
