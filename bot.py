import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot import types

admin = 1068856695
TOKEN = '6641948174:AAE3KUJSfwmnAEIgQaSthv4YLXkme7QYLO0'
bot = telebot.TeleBot(TOKEN, parse_mode="Markdown")


@bot.chat_join_request_handler()
def okay(message: telebot.types.ChatJoinRequest):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    one = InlineKeyboardButton("🤷‍♂️Я человек")
    markup.add(one)
    bot.send_message(message.from_user.id, f"{message.from_user.first_name}, спасибо за подписку на канал.\nЯ анти-спам бот.\nДля подтверждения, того что вы живой человек, нажмите кнопку\n«*Я человек*»\nили напишите мне", reply_markup=markup)
    bot.send_message(admin, f"Пользователь {message.from_user.first_name} отправил заявку📩")

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    one = InlineKeyboardButton("🤷‍♂️Я человек")
    markup.add(one)
    bot.send_message(message.from_user.id, f"{message.from_user.first_name}, спасибо за подписку на канал.\nЯ анти-спам бот.\nДля подтверждения, того что вы живой человек, нажмите кнопку\n«*Я человек*»\nили напишите мне", reply_markup=markup)
    bot.send_message(admin, f"Пользователь {message.from_user.first_name} отправил заявку📩")

@bot.message_handler(content_types=['text'])
def func(message, res=False):
    if(message.text == "🤷‍♂️Я человек"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        one = InlineKeyboardButton("📨Связь с админом")
        two = InlineKeyboardButton("🎲Бросить кубик")
        markup.add(one)
        markup.add(two)
        menu = telebot.types.InlineKeyboardMarkup()
        menu.add(telebot.types.InlineKeyboardButton(text = 'Кинуть заявку ✅', url = 'https://t.me/+lXuLL1TgGMg2ODcy'))
        bot.send_message(message.chat.id, text="Спасибо, вы подтвердили, что вы не робот.", reply_markup=markup)
        bot.send_message(message.chat.id, text="Нажмите на кнопку ниже, чтобы кинуть заявку, модераторы примут её в ближайшее время.", reply_markup=menu)
        bot.send_message(admin, f"Пользователь {message.from_user.first_name} подтвержден✅")
    elif (message.text == "📨Связь с админом"):
        bot.send_message(message.chat.id, "👨‍💻Связь с админом: @moderatorglp555")
    elif (message.text == "🎲Бросить кубик"):
        bot.send_dice(message.chat.id)


bot.infinity_polling(allowed_updates = telebot.util.update_types)

