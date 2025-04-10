import telebot
from telebot import types
import random

bot = telebot.TeleBot('7714652343:AAGiBjQLeXZ_jIJRWEukA4zbbvuml7k8eSI')


user_game_data = {}


horoscopes = {
    'овен': "Сегодня вы будете полны энергии и готовы к новым свершениям. Хотите сыграть в игру 'Угадай число'? Напишите /guess.",
    'телец': "Сегодня вам стоит обратить внимание на финансовые вопросы. Хотите сыграть в игру 'Угадай число'? Напишите /guess.",
    'близнецы': "Сегодня отличный день для общения и новых знакомств. Хотите сыграть в игру 'Угадай число'? Напишите /guess.",
    'рак': "Постарайтесь уделить время семье и близким. Хотите сыграть в игру 'Угадай число'? Напишите /guess.",
    'лев': "Ваши лидерские качества помогут вам в решении задач. Хотите сыграть в игру 'Угадай число'? Напишите /guess.",
    'дева': "Обратите внимание на детали, они могут быть важны. Хотите сыграть в игру 'Угадай число'? Напишите /guess.",
    'весы': "Сегодня вам будет легко находить общий язык с окружающими. Хотите сыграть в игру 'Угадай число'? Напишите /guess.",
    'скорпион': "Следует избегать конфликтов и напряженных ситуаций. Хотите сыграть в игру 'Угадай число'? Напишите /guess.",
    'стрелец': "Сегодня удачный день для путешествий и новых впечатлений. Хотите сыграть в игру 'Угадай число'? Напишите /guess.",
    'козерог': "Работа потребует от вас максимальной концентрации. Хотите сыграть в игру 'Угадай число'? Напишите /guess.",
    'водолей': "Ваша креативность поможет решить сложные задачи. Хотите сыграть в игру 'Угадай число'? Напишите /guess.",
    'рыбы': "Не забывайте о своих мечтах и желаниях. Хотите сыграть в игру 'Угадай число'? Напишите /guess. "
}


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я бот, который может рассказать тебе гороскоп или предложить сыграть в игру 'Угадай число'. Как ты себя чувствуешь?")


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    user_response = message.text.lower()

    if user_response in ["привет", "здравствуй", "салам"]:
        bot.send_message(message.from_user.id, "")
    elif user_response in ["хорошо","нормально","супер","замечательно","неплохо","прекрасно","шикарно","норм","ок","чудесно","лучше всех","привет норм","привет ок","привет чудесно","привет лучше всех","привет хорошо","привет нормально","привет супер","привет замечательно","привет прекрасно","привет шикарно","привет, хорошо" ,"привет, нормально","привет, супер","привет, замечательно","привет, прекрасно","привет, шикарно","привет, норм","привет, ок","привет, чудесно","привет, лучше всех","привет, неплохо","привет неплохо"]:
        bot.send_message(message.from_user.id, "Отлично! Показать гороскоп на сегодня?")
    elif user_response in ["плохо", "ужасно", "не очень", "привет плохо","привет ужасно","привет не очень", "привет, плохо","привет, ужасно","привет, не очень"]:
        bot.send_message(message.from_user.id, "Ну блииин! Показать гороскоп на сегодня?")
    elif user_response in ["да","давай","ну да","ну давай","ок","вперёд","вперед","согласна","хочу","ага","конечно","ладно"]:
        bot.send_message(message.from_user.id, "Я расскажу тебе гороскоп на сегодня.")
        keyboard = types.InlineKeyboardMarkup()
        for sign in horoscopes:
            keyboard.add(types.InlineKeyboardButton(text=sign.capitalize(), callback_data=sign))
        bot.send_message(message.chat.id, text='Выбери свой знак зодиака', reply_markup=keyboard)
    elif user_response in ["нет","не хочу","не надо","не","неа"]:
        bot.send_message(message.chat.id, "Хорошо, хотите сыграть в игру 'Угадай число'? Напишите /guess.")
    elif user_response == "/guess":
        start_guess_game(message)
    else:
        bot.send_message(message.chat.id, "Я тебя не понимаю.")


@bot.message_handler(commands=['guess'])
def start_guess_game(message):
    n = random.randint(1, 100)
    bot.send_message(message.chat.id, 'Я загадал число от 1 до 100. Попробуй угадать!')
    bot.register_next_step_handler(message, number_guess, n)


def number_guess(message, n):
    number = message.text


    if not number.isdigit():
        bot.send_message(message.chat.id, 'Это не число. Попробуйте снова.')
        bot.register_next_step_handler(message, number_guess, n)
        return


    number = int(number)

    if number > n:
        bot.send_message(message.chat.id, "Слишком большое число.")
        bot.register_next_step_handler(message, number_guess, n)
    elif number < n:
        bot.send_message(message.chat.id, "Слишком маленькое число.")
        bot.register_next_step_handler(message, number_guess, n)
    else:
        bot.send_message(message.chat.id, "Угадал! Напиши /guess, чтобы сыграть снова.")



@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data in horoscopes:
        horoscope = horoscopes[call.data]
        bot.send_message(call.message.chat.id, horoscope)


if __name__ == '__main__':
    bot.polling(none_stop=True)