
import telebot
from telebot import types
import time
import os
import sqlite3

database = 'db.db'
con = sqlite3.connect(database, check_same_thread=False)
cursor = con.cursor()

admin = 1068856695
admins = '1068856695'
admin2 = 6512545545
admins2 = '6512545545'

bot = telebot.TeleBot('6763281103:AAHAY1libC_5b0O3VDKwXArwtINSgsiJ3gA')
@bot.message_handler(commands=['start'])
def start(message):
    
    try:
        cursor.execute(f'SELECT id FROM banned WHERE id = "{message.chat.id}";')
        con.commit()
        cursor.execute(f"SELECT reason FROM banned WHERE id = '{message.chat.id}'")
        result = cursor.fetchone()
        con.commit()
        x1 = f"{result[0]}"
        bot.send_message(message.chat.id, f'Вы заблокированы\nПричина блокировки: {x1}')
        return
    except TypeError or sqlite3.OperationalError:
        pass
    try:
        cursor.execute(f'INSERT INTO users (balance,id) VALUES ("0","{message.chat.id}");')
        con.commit()

        user_id = message.from_user.id

        if " " in message.text:
            referrer_candidate = message.text.split()[1]

            try:
                referrer_candidate = int(referrer_candidate)
                try:
                    cursor.execute(f'SELECT id FROM banned WHERE id = "{referrer_candidate}";')
                    con.commit()
                    cursor.execute(f"SELECT reason FROM banned WHERE id = '{referrer_candidate}'")
                    result = cursor.fetchone()
                    con.commit()
                    x1 = f"{result[0]}"
                    bot.send_message(message.chat.id, f'Пользователь который вас пригласил заблокирован')
                    pass
                except TypeError or sqlite3.OperationalError:
                    try:
                        cursor.execute(f'SELECT id FROM users WHERE id = "{referrer_candidate}";')
                        cursor.execute(f"SELECT balance FROM users WHERE id = '{referrer_candidate}'")
                        result = cursor.fetchone()
                        x1 = int(result[0])
                        x3 = x1 + 5
                        cursor.execute(f"UPDATE users SET balance = '{x3}' WHERE id = '{referrer_candidate}';")
                        con.commit()
                        bot.send_message(referrer_candidate, f'на ваш баланс зачислено 5 рублей за реферала, текущий баланс {x3}')
                        bot.send_message(admins, f'Пользователь {referrer_candidate} пригласил {message.from_user.id}')
                        bot.send_message(admins2, f'Пользователь {referrer_candidate} пригласил {message.from_user.id}')
                    except sqlite3.OperationalError:
                        pass


            except ValueError:
                pass

    except sqlite3.IntegrityError:
        print()


    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Товары 💎")
    item2 = types.KeyboardButton("Мой профиль 🧑‍💻")
    item3 = types.KeyboardButton("Тех. Поддержка 🆘")
    item4 = types.KeyboardButton("Правила 📃")

    markup.add(item1, item2)
    markup.add(item3, item4)

    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}".format(message.from_user), reply_markup=markup)

@bot.message_handler(commands=['admin'])
def admin(message):
    if str(message.chat.id) == admins or str(message.chat.id) == admins2:
        buttons = types.InlineKeyboardMarkup()
        key2 = types.InlineKeyboardButton(text='Управление балансом', callback_data='key2')
        key3 = types.InlineKeyboardButton(text='Рассылка всем пользователям', callback_data='key3')
        key4 = types.InlineKeyboardButton(text='Отправить сообщение пользователю', callback_data='key4')
        key5 = types.InlineKeyboardButton(text='Вывести данные с базы', callback_data='key5')
        key6 = types.InlineKeyboardButton(text='Проверить баланс пользователя', callback_data='key6')
        key7 = types.InlineKeyboardButton(text='Управление блокировками', callback_data='key7')
        key8 = types.InlineKeyboardButton(text='Управление подпиской Fatality', callback_data='key8')
        buttons.add(key2)
        buttons.add(key3)
        buttons.add(key4)
        buttons.add(key5)
        buttons.add(key6)
        buttons.add(key7)
        cursor.execute("select count(*) from users")
        row_count = cursor.fetchone()
        con.commit()
        stat2 = row_count[0]
        bot.send_message(message.chat.id, f'Панель инструментов открыта\n\nВсего пользователей: {stat2} ', reply_markup=buttons)




@bot.message_handler(content_types=['text'])
def bot_message(message):
    try:
        cursor.execute(f'SELECT id FROM banned WHERE id = "{message.chat.id}";')
        con.commit()
        cursor.execute(f"SELECT reason FROM banned WHERE id = '{message.chat.id}'")
        result = cursor.fetchone()
        con.commit()
        x1 = result[0]
        bot.send_message(message.chat.id, f'Вы заблокированы\nПричина блокировки: {x1}')
        return
    except TypeError or sqlite3.OperationalError:
        pass
    if message.chat.type == 'private':
        if message.text == 'Товары 💎':
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("Пробив 🌎", callback_data = "btn1")
            button2 = types.InlineKeyboardButton("Кошельки 💰", callback_data = "btn2")
            button3 = types.InlineKeyboardButton("VPN 🥷", callback_data = "btn3")
            button4 = types.InlineKeyboardButton("Sim 🪪", callback_data = "btn4")
            button5 = types.InlineKeyboardButton("Особое 🔥", callback_data = "btn5")
            button6 = types.InlineKeyboardButton("Софты 💿", callback_data = "btn6")
            button7 = types.InlineKeyboardButton("Мануалы 📃", callback_data = "btn7")
            button8 = types.InlineKeyboardButton("Абузы💰", callback_data = "btn8")
            markup.add(button1, button2)
            markup.add(button3, button4)
            markup.add(button6, button7)
            markup.add(button8)
            markup.add(button5)
            bot.send_message(message.chat.id, "Выберите категорию:", reply_markup=markup)

        elif message.text == 'Мой профиль 🧑‍💻':
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("Пополнить 💵", callback_data = "balance")
            button2 = types.InlineKeyboardButton("Вывести 💶", callback_data = "vivesti")
            button3 = types.InlineKeyboardButton("Рефералка 🤝", callback_data = "refferal")
            markup.add(button1)
            markup.add(button2)
            markup.add(button3)
            cursor.execute(f"SELECT balance FROM users WHERE id = '{message.chat.id}'")
            result = cursor.fetchone()
            con.commit()
            x1 = int(result[0])
            bot.send_message(message.chat.id, f"Ваш профиль 🧑‍💻\n\n💻 Айди: {message.chat.id}\n💰 Баланс: {x1}₽", reply_markup=markup)

        elif message.text == 'Тех. Поддержка 🆘':

            def helpBot(message):
                bot.send_message(help_user_id, 'Сообщение отправлено')
                bot.forward_message(admins, help_user_id, message.message_id)
                markup = types.InlineKeyboardMarkup()
                button1 = types.InlineKeyboardButton(text='Не отвечать', callback_data='ignore')
                markup.add(button1)
                msg = bot.send_message(admins, f"напишите ответ пользователю {help_user_id}", reply_markup=markup)
                bot.register_next_step_handler(msg, next_update)

            def next_update(message):
                    reply = message.text
                    markup = types.InlineKeyboardMarkup()
                    button1 = types.InlineKeyboardButton(text='Закрыть диалог', callback_data='cancel_dialog')
                    markup.add(button1)
                    msg = bot.send_message(help_user_id, f"Вам пришло сообщение от администрации, ответьте на него или нажмите на кнопку для отмены\n\nСообщение: {reply}", reply_markup=markup)
                    bot.register_next_step_handler(msg, helpBot)

            help_user_id = message.from_user.id
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton(text='Отмена', callback_data='cancel')
            markup.add(button1)
            msg = bot.send_message(message.chat.id, 'Задайте вопрос прямо сюда. Вам ответят как можно быстрее.', reply_markup=markup)
            bot.register_next_step_handler(msg, helpBot)

        elif message.text == 'Правила 📃':
            bot.send_message(message.chat.id, "1. По вопросам рекламы: @katerinasurprise\n\n2. Замена невалидных товаров производится в течении часа после покупки и предоставлении скриншотов, доказывающие невалидность товара.\n\n3. Замена по гарантии 24 часа. Возврат по гарантии осуществляется, если приобретенный товар не соответствует описанию указанному при продаже.\n\n4. Любые попытки обмана магазина или введения администрации в заблуждение, наказывается баном.\n\n5. Администрация не несет ответственность за любые противозаконные действия совершаемые покупателем с помощью товаров приобретенных в магазине.\n\n6. За привлечение ботов и пустышек по рефералке вы будете заблокированы в боте навсегда.")

        elif message.text == 'Рынок⚖':
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("Зайти", callback_data = "inside")
            markup.add(button1)


            bot.send_message(message.chat.id, "Рынок - место, где участники нашего бота могут продавать и покупать друг у друга различные товары. Заработанные с рынка деньги можно выводить себе на карту.\n\nНажмите кнопку ниже, чтобы попасть на рынок!", reply_markup=markup)

@bot.message_handler(commands=['start'])
def get_photo(message):
    try:
        cursor.execute(f'SELECT id FROM banned WHERE id = "{message.chat.id}";')
        con.commit()
        cursor.execute(f"SELECT reason FROM banned WHERE id = '{message.chat.id}'")
        result = cursor.fetchone()
        con.commit()
        x1 = result[0]
        bot.send_message(message.chat.id, f'Вы заблокированы\nПричина блокировки: {x1}')
        return
    except TypeError or sqlite3.OperationalError:
        pass
    photo = message.photo[-1]
    file_info = bot.get_file(photo.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    save_path = 'photo.jpg'
    with open(save_path, 'wb') as new_file:
        new_file.write(downloaded_file)
    new_file.close()
    bot.reply_to(message, 'Ожидайте проверки')
    photo = open('photo.jpg', 'rb')
    bot.send_photo(admins, photo)
    bot.send_message(admins, f'пользователь {message.chat.id}')
    os.remove('photo.jpg')

@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback_data(callback):
    bot.answer_callback_query(callback_query_id=callback.id)
    try:
        cursor.execute(f'SELECT id FROM banned WHERE id = "{callback.message.chat.id}";')
        con.commit()
        cursor.execute(f"SELECT reason FROM banned WHERE id = '{callback.message.chat.id}'")
        result = cursor.fetchone()
        con.commit()
        x1 = result[0]
        bot.send_message(callback.message.chat.id, f'Вы заблокированы\nПричина блокировки: {x1}')
        return
    except TypeError or sqlite3.OperationalError:
        pass

    if callback.data == 'check':

        def id_ban(message):
            try:
                cursor.execute(f'SELECT id, reason FROM banned WHERE id = {message.text};')
                bot.send_message(callback.message.chat.id, 'Пользователь заблокирован')
            except:
                bot.send_message(callback.message.chat.id, 'Пользователь не заблокирован')

        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(text='Отмена ❌', callback_data='cancel_un')
        markup.add(button1)
        msg = bot.send_message(callback.message.chat.id, f"напишите айди пользователя", reply_markup=markup)
        bot.register_next_step_handler(msg, id_ban)

        
    if callback.data == 'up':
        def reason(message):
            cursor1.execute(f'INSERT INTO login (id, hwid) VALUES ("{gett}", "{message.text}")')
            bot.send_message(callback.message.chat.id, 'Пользователь добавлен в базу')
            con1.commit()


        def id_get(message):
            global gett
            gett = message.text
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton(text='Отмена ❌', callback_data='cancel_un')
            markup.add(button1)
            msg = bot.send_message(callback.message.chat.id, f"напишите hwid пользователя", reply_markup=markup)
            bot.register_next_step_handler(msg, reason)

        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(text='Отмена ❌', callback_data='cancel_un')
        markup.add(button1)
        msg = bot.send_message(callback.message.chat.id, f"напишите айди пользователя", reply_markup=markup)
        bot.register_next_step_handler(msg, id_get)

    if callback.data == 'down':
        def reason(message):

            cursor1.execute(f'DELETE FROM login WHERE id = "{message.text}";')
            bot.send_message(callback.message.chat.id, 'Пользователь удален из базы')
            con1.commit()

        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(text='Отмена ❌', callback_data='cancel_un')
        markup.add(button1)
        msg = bot.send_message(callback.message.chat.id, f"напишите айди пользователя", reply_markup=markup)
        bot.register_next_step_handler(msg, reason)

    if callback.data == 'check_FT':
        def id_ban(message):
            try:
                cursor1.execute(f'SELECT id, hwid FROM login WHERE id = {message.text};')
                bot.send_message(callback.message.chat.id, 'Пользователь есть в базе')
                cursor1.close()
                con1.close()
            except:
                bot.send_message(callback.message.chat.id, 'Пользователя нет в базе')

        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(text='Отмена ❌', callback_data='cancel_un')
        markup.add(button1)
        msg = bot.send_message(callback.message.chat.id, f"напишите айди пользователя", reply_markup=markup)
        bot.register_next_step_handler(msg, id_ban)
    
    
    if callback.data == 'key8':
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(text='Добавить в базу', callback_data='up')
        button2 = types.InlineKeyboardButton(text='Убрать с базы', callback_data='down')
        button3 = types.InlineKeyboardButton(text='Проверить наличие в базе', callback_data='check_FT')
        markup.add(button1)
        markup.add(button2)
        markup.add(button3)
        bot.send_message(callback.message.chat.id, 'Открыта панель управления системой Fatality', reply_markup=markup)
        
    if callback.data == 'ban':
        def reason(message):
            try:
                cursor.execute(f'INSERT INTO banned (reason,id) VALUES ("{message.text}","{banned}");')
                bot.send_message(callback.message.chat.id, 'Пользователь заблокирован')
            except sqlite3.IntegrityError:
                bot.send_message(callback.message.chat.id, 'Пользователь уже занесен с список банов')
            con.commit()


        def id_ban(message):
            global banned
            banned = message.text
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton(text='Отмена ❌', callback_data='cancel_un')
            markup.add(button1)
            msg = bot.send_message(callback.message.chat.id, f"укажите причину бана", reply_markup=markup)
            bot.register_next_step_handler(msg, reason)

        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(text='Отмена ❌', callback_data='cancel_un')
        markup.add(button1)
        msg = bot.send_message(callback.message.chat.id, f"напишите айди пользователя", reply_markup=markup)
        bot.register_next_step_handler(msg, id_ban)

    if callback.data == 'unban':
        def unban(message):
            cursor.execute(f'DELETE FROM banned WHERE id = "{message.text}";')
            con.commit()
            bot.send_message(callback.message.chat.id, 'Блокировка снята')

        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(text='Отмена ❌', callback_data='cancel_un')
        markup.add(button1)
        msg = bot.send_message(callback.message.chat.id, f"напишите айди пользователя", reply_markup=markup)
        bot.register_next_step_handler(msg, unban)

    if callback.data == 'key7':
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(text='Заблокировать пользователя', callback_data='ban')
        button2 = types.InlineKeyboardButton(text='Разблокировать пользователя', callback_data='unban')
        button3 = types.InlineKeyboardButton(text='Проверить наличие блокировки', callback_data='check')
        markup.add(button1)
        markup.add(button2)
        markup.add(button3)
        bot.send_message(callback.message.chat.id, 'Открыта панель управления блокировками', reply_markup=markup)



    if callback.data == 'key6':
        def id_get1(message):
            id_user = message.text
            cursor.execute(f"SELECT balance FROM users WHERE id = '{id_user}'")
            result = cursor.fetchone()
            con.commit()
            x1 = int(result[0])
            bot.send_message(callback.message.chat.id, f'Пользователь: {id_user}\nБаланс: {x1}')

        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(text='Отмена ❌', callback_data='cancel_un')
        markup.add(button1)
        msg = bot.send_message(callback.message.chat.id, f"напишите айди пользователя",
                               reply_markup=markup)
        bot.register_next_step_handler(msg, id_get1)


    if callback.data == 'key5':
        records = []
        cursor.execute('SELECT * FROM users')
        rows = cursor.fetchall()
        for row in rows:
            records.append({'id': str(row[0]), 'balance': str(row[1])})
        bot.send_message(callback.message.chat.id, f'{records}')
        con.commit()

    if callback.data == 'refferal':
        bot.send_message(callback.message.chat.id, f'Ваша реферальная ссылка:\nhttps://t.me/Glpshopbot?start={callback.message.chat.id}\n\nЗа приглашённого пользователя вы получаете:\n\n5₽ на баланс\n10% от его пополнений', disable_web_page_preview=True)
    
    if callback.data == 'cancel_dialog':
        bot.clear_step_handler_by_chat_id(chat_id=callback.message.chat.id)
        bot.send_message(callback.message.chat.id, 'Диалог закрыт')
    
    if callback.data == 'cancel':
        bot.clear_step_handler_by_chat_id(chat_id=callback.message.chat.id)
        bot.send_message(callback.message.chat.id, 'Отменено')
    
    if callback.data == 'cancel_un':
        bot.clear_step_handler_by_chat_id(chat_id=callback.message.chat.id)
        bot.send_message(callback.message.chat.id, 'Команда выполнена')

    if callback.data == 'key4':
        
                       
        def helpBot(message):
            bot.send_message(id_user, 'Сообщение отправлено')
            bot.forward_message(admins, id_user, message.message_id)
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton(text='Не отвечать', callback_data='ignore')
            markup.add(button1)
            msg = bot.send_message(admins, f"напишите ответ пользователю {id_user}", reply_markup=markup)
            bot.register_next_step_handler(msg, next_update)
        
        def next_update(message):
            reply = message.text
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton(text='Закрыть диалог', callback_data='cancel_dialog')
            markup.add(button1)
            msg = bot.send_message(id_user, f"Вам пришло сообщение от администрации, ответьте на него или нажмите на кнопку для отмены\n\nСообщение: {reply}", reply_markup=markup)
            bot.register_next_step_handler(msg, helpBot)
            
        def message_text(message):
            reply = message.text
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton(text='Закрыть диалог', callback_data='cancel_dialog')
            markup.add(button1)
            msg = bot.send_message(id_user, f"Вам пришло сообщение от администрации, ответьте на него или нажмите на кнопку для отмены\n\nСообщение: {reply}", reply_markup=markup)
            bot.register_next_step_handler(msg, helpBot)
    

            

        def id_get(message):
            global id_user
            id_user = message.text
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton(text='Отмена ❌', callback_data='cancel_un')
            markup.add(button1)
            msg = bot.send_message(callback.message.chat.id, f"напишите сообщение для пользователя {id_user}",
                                   reply_markup=markup)
            bot.register_next_step_handler(msg, message_text)

        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(text='Отмена ❌', callback_data='cancel_un')
        markup.add(button1)
        msg = bot.send_message(callback.message.chat.id, f"напишите айди пользователя",
                               reply_markup=markup)
        bot.register_next_step_handler(msg, id_get)





    if callback.data == 'key2':
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Пополнить баланс", callback_data="add")
        button2 = types.InlineKeyboardButton("Вычесть с баланса", callback_data="unadd")
        markup.add(button1)
        markup.add(button2)
        bot.send_message(callback.message.chat.id, "Выберите тип операции", reply_markup=markup)

    if callback.data == 'key3':
        def send_3(message):
            cursor.execute('SELECT id FROM users')
            result = cursor.fetchall()
            msg = message.text
            time.sleep(1)
            for x in result:
                try:
                    bot.send_message(x[0], str(msg))
                except telebot.apihelper.ApiTelegramException:
                    pass
            bot.send_message(callback.message.chat.id, 'успешно!')

        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(text='Отмена ❌', callback_data='cancel_un')
        markup.add(button1)
        msg = bot.send_message(callback.message.chat.id, f"напишите cообщение для всех пользователей",
                               reply_markup=markup)
        bot.register_next_step_handler(msg, send_3)


    elif callback.data == 'add':
        def unbal3(message):
            count = message.text
            cursor.execute(f"SELECT balance FROM users WHERE id = {id_uner}")
            result = cursor.fetchone()
            x1 = int(result[0])
            x2 = int(count)
            x3 = x1 + x2
            cursor.execute(f"UPDATE users SET balance = '{x3}' WHERE id = '{id_uner}';")
            con.commit()
            bot.send_message(id_uner, f'Вам выдали {x2} рублей\nтекущий баланс: {x3}')
            bot.send_message(callback.message.chat.id, 'успешно!')

        def unbal2(message):
            global id_uner
            id_uner = message.text
            cursor.execute(f"SELECT balance FROM users WHERE id = {id_uner}")
            result = cursor.fetchone()
            x1 = int(result[0])
            con.commit()
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton(text='Отмена ❌', callback_data='cancel')
            markup.add(button1)
            msg = bot.send_message(callback.message.chat.id,
                                   f"сколько начислить пользователю?\n\nБаланс пользователя: {x1}",
                                   reply_markup=markup)
            bot.register_next_step_handler(msg, unbal3)

        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(text='Отмена ❌', callback_data='cancel')
        markup.add(button1)
        msg = bot.send_message(callback.message.chat.id, f"напишите id пользователя", reply_markup=markup)
        bot.register_next_step_handler(msg, unbal2)

    elif callback.data == 'unadd':
        def unbal3(message):
            count = message.text
            cursor.execute(f"SELECT balance FROM users WHERE id = {id_uner}")
            result = cursor.fetchone()
            x1 = int(result[0])
            x2 = int(count)
            x3 = x1 - x2
            cursor.execute(f"UPDATE users SET balance = '{x3}' WHERE id = '{id_uner}';")
            con.commit()
            bot.send_message(id_uner, f'У вас забрали {x2} рублей\nтекущий баланс: {x3}')
            bot.send_message(callback.message.chat.id, 'успешно!')

        def unbal2(message):
            global id_uner
            id_uner = message.text
            cursor.execute(f"SELECT balance FROM users WHERE id = {id_uner}")
            result = cursor.fetchone()
            x1 = int(result[0])
            con.commit()
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton(text='Отмена ❌', callback_data='cancel')
            markup.add(button1)
            msg = bot.send_message(callback.message.chat.id,
                                   f"сколько забрать у пользователя?\n\nБаланс пользователя: {x1}",
                                   reply_markup=markup)
            bot.register_next_step_handler(msg, unbal3)

        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(text='Отмена ❌', callback_data='cancel')
        markup.add(button1)
        msg = bot.send_message(callback.message.chat.id, f"напишите id пользователя", reply_markup=markup)
        bot.register_next_step_handler(msg, unbal2)

    if callback.data == "inside":
        time.sleep(0.5)
        bot.send_message(callback.message.chat.id, "Для входа необходим ранг ТЕМЩИК⛔️\n\nотследить свой ранг можно в разделе Мой профиль")

    if callback.data == "vivesti":
        def helpBot(message):
            bot.send_message(help_user_id, 'Заявка на вывод создана.\n\nЕсли у вас к моменту одобрения заявки не будет указанной суммы на балансе, то выплата не произведётся.')
            bot.send_message(admins, f"📋 Новая заявка на вывод:]\n\nID: {help_user_id}")
            bot.forward_message(admins, help_user_id, message.message_id)
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton(text='Не отвечать', callback_data='ignore')
            markup.add(button1)
            msg = bot.send_message(admins, f"напишите ответ пользователю {help_user_id}", reply_markup=markup)
            bot.register_next_step_handler(msg, next_update)

        def next_update(message):
            reply = message.text
            bot.send_message(help_user_id, f'{reply}')

        help_user_id = callback.message.chat.id
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(text='Отмена', callback_data='cancel')
        markup.add(button1)
        msg = bot.send_message(callback.message.chat.id, 'Укажите вашу карту и сумму которую желаете вывести\n\nОбратите внимание, что минимальная сумма вывода 100₽!',
                               reply_markup=markup)
        bot.register_next_step_handler(msg, helpBot)



    if callback.data == 'ignore':
        bot.clear_step_handler_by_chat_id(chat_id=callback.message.chat.id)
        bot.send_message(callback.message.chat.id, 'Команда выполнена')


    if callback.data == "balance":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("СБП 🟢️️", callback_data = "btn0-1")
        button2 = types.InlineKeyboardButton("Криптовалюта ⚫️", callback_data = "btn0-2")
        markup.add(button1)
        markup.add(button2)

        bot.send_message(callback.message.chat.id, "Пополнение баланса 💵", reply_markup=markup)

    elif callback.data == "btn1":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Пробив но номеру - 215₽", callback_data = "btn1-1")
        button2 = types.InlineKeyboardButton("Пробив соцсети - 275₽", callback_data = "btn1-2")
        button3 = types.InlineKeyboardButton("Бесплатный пробив", callback_data = "btn1-3")
        markup.add(button1, button2)
        markup.add(button3)

        bot.send_message(callback.message.chat.id, "Вас обманули мошенники или вы просто хотите вычислить информацию о плохом человеке? Мы вам поможем 🔎", reply_markup=markup)

    elif callback.data == "btn2":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("🥝 QIWI основной 🥝", callback_data = "btn2-1")
        button2 = types.InlineKeyboardButton("🥝 QIWI профессиональный 🥝", callback_data = "btn2-2")
        button3 = types.InlineKeyboardButton("⚛️ ЮMoney именной ⚛️", callback_data = "btn2-3")
        button4 = types.InlineKeyboardButton("🅿 ️Payeer идентифицированный 🅿", callback_data = "btn2-4")
        markup.add(button1)
        markup.add(button2)
        markup.add(button3)
        markup.add(button4)

        bot.send_message(callback.message.chat.id, "Вам необходим левый кошелёк для принятия грязных денег, либо вы хотите скрыть свои данные от получателя? Принимайте деньги на фейковые кошельки!", reply_markup=markup)

    elif callback.data == "btn3":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Windscribe PRO до 2025г - 250₽", callback_data = "btn3-1")
        button2 = types.InlineKeyboardButton("Exspress VPN | 12 мес - 300₽", callback_data = "btn3-2")
        markup.add(button1)
        markup.add(button2)

        bot.send_message(callback.message.chat.id, "Хотите быть анонимным в интернете? Используете бесплатный VPN в надежде что вас не поймают? Купите VPN у нас, и ваш IP-адрес не вычислят даже государственные спец.службы!", reply_markup=markup)

    elif callback.data == "btn4":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Билайн 🟡",callback_data = "btn4-1")
        button2 = types.InlineKeyboardButton("Мегафон 🟢", callback_data = "btn4-2")
        button3 = types.InlineKeyboardButton("МТС 🔴", callback_data = "btn4-3")
        markup.add(button1)
        markup.add(button2)
        markup.add(button3)

        bot.send_message(callback.message.chat.id, "Вам нужна левая симка для сохранения анонимности или регистрации в сервисах? Арендуйте у нас виртуальную sim на определенный срок, принимайте на нее смс и регистрируйтесь где угодно!", reply_markup=markup)

    elif callback.data == "btn5":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Вспышка 📡", callback_data = "btn5-1")
        button2 = types.InlineKeyboardButton("Защита ваших данных 🛡", callback_data = "btn5-2")
        button3 = types.InlineKeyboardButton("APK вирус ☠", callback_data = "btn5-3")
        button4 = types.InlineKeyboardButton("Блокировка карты 🚫", callback_data = "btn5-4")
        button6 = types.InlineKeyboardButton("Атака пиццей 🍕", callback_data = "btn5-6")
        button5 = types.InlineKeyboardButton("Разработка бота 🤖", callback_data = "btn5-5")
        markup.add(button1)
        markup.add(button2)
        markup.add(button3)
        markup.add(button4)
        markup.add(button6)
        markup.add(button5)

        bot.send_message(callback.message.chat.id, "В этом разделе мы вам предложим услуги, которые могут быть очень полезными для вас! 🔥", reply_markup=markup)

    elif callback.data == "btn6":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Билдер майнера 🪙", callback_data = "btn6-1")
        button2 = types.InlineKeyboardButton("Деанонимизация анон чата 🎭", callback_data = "btn6-2")
        button3 = types.InlineKeyboardButton("Фаталити 🔪", callback_data = "btn6-3")

        markup.add(button1)
        markup.add(button2)
        markup.add(button3)
        
        bot.send_message(callback.message.chat.id, "В этом разделе собраны интересные программы, которые могут вам пригодиться!", reply_markup=markup)

    elif callback.data == "btn7":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Анонимность в интернете 🥷", callback_data = "btn7-1")
        button2 = types.InlineKeyboardButton("Деанон любого 🕵️", callback_data = "btn7-2")
        markup.add(button1)
        markup.add(button2)

        bot.send_message(callback.message.chat.id, "Мы делимся с вами нашим опытом в самых важных для любого пользователя интернета сферах!", reply_markup=markup)

    elif callback.data == "btn8":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Такси за 0₽ 🚕", callback_data = "btn8-1")
        button2 = types.InlineKeyboardButton("Абуз СберМегаМаркета 🛍", callback_data = "btn8-2")
        button3 = types.InlineKeyboardButton("ТГ премиум бесплатно ⭐", callback_data = "btn8-3")
        button4 = types.InlineKeyboardButton("Голоса Вк за лоупрайс ⚡", callback_data = "btn8-4")
        button5 = types.InlineKeyboardButton("Абуз бонусов СберСпасибо 🟢", callback_data = "btn8-5")
        markup.add(button1)
        markup.add(button2)
        markup.add(button3)
        markup.add(button4)
        markup.add(button5)
        bot.send_message(callback.message.chat.id, "Абуз - злоупотребление дырами в системе для получения выгоды. Благодаря данным ниже абузам вы сможете сэкономить свои кровные 💵", reply_markup=markup)

    elif callback.data == "btn0-1":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("100₽", callback_data = "oplata100")
        button2 = types.InlineKeyboardButton("200₽", callback_data = "oplata200")
        button3 = types.InlineKeyboardButton("300₽", callback_data = "oplata300")
        button4 = types.InlineKeyboardButton("400₽", callback_data = "oplata400")
        button5 = types.InlineKeyboardButton("500₽", callback_data = "oplata500")
        button6 = types.InlineKeyboardButton("600₽", callback_data = "oplata600")
        button7 = types.InlineKeyboardButton("700₽", callback_data = "oplata700")
        button8 = types.InlineKeyboardButton("800₽", callback_data = "oplata800")
        button9 = types.InlineKeyboardButton("900₽", callback_data = "oplata900")
        markup.add(button1, button2, button3)
        markup.add(button4, button5, button6)
        markup.add(button7, button8, button9)
        global message_del
        message_del = bot.send_message(callback.message.chat.id, "Выберите сумму пополнения", reply_markup=markup)

    elif callback.data == "oplata100":
        bot.delete_message(callback.message.chat.id, message_del.message_id)
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("ПОПОЛНИТЬ", url = 'https://payok.io/payment_link/9j2uw-018zt-3kxpc')
        markup.add(button1)
        time.sleep(1)
        bot.send_message(callback.message.chat.id, "Счет на оплату сформирован.", reply_markup=markup)

    elif callback.data == "oplata200":
        bot.delete_message(callback.message.chat.id, message_del.message_id)
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("ПОПОЛНИТЬ", url = 'https://payok.io/payment_link/iy4s4-51m2g-zx1ai')
        markup.add(button1)
        time.sleep(1)
        bot.send_message(callback.message.chat.id, "Счет на оплату сформирован.", reply_markup=markup)

    elif callback.data == "oplata300":
        bot.delete_message(callback.message.chat.id, message_del.message_id)
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("ПОПОЛНИТЬ", url = 'https://payok.io/payment_link/81549-3r666-8x9g9')
        markup.add(button1)
        time.sleep(1)
        bot.send_message(callback.message.chat.id, "Счет на оплату сформирован.", reply_markup=markup)

    elif callback.data == "oplata400":
        bot.delete_message(callback.message.chat.id, message_del.message_id)
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("ПОПОЛНИТЬ", url = 'https://payok.io/payment_link/65396-e7471-2pad5')
        markup.add(button1)
        time.sleep(1)
        bot.send_message(callback.message.chat.id, "Счет на оплату сформирован.", reply_markup=markup)

    elif callback.data == "oplata500":
        bot.delete_message(callback.message.chat.id, message_del.message_id)
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("ПОПОЛНИТЬ", url = 'https://payok.io/payment_link/q387o-a1hdo-940qq')
        markup.add(button1)
        time.sleep(1)
        bot.send_message(callback.message.chat.id, "Счет на оплату сформирован.", reply_markup=markup)

    elif callback.data == "oplata600":
        bot.delete_message(callback.message.chat.id, message_del.message_id)
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("ПОПОЛНИТЬ", url = 'https://payok.io/payment_link/h2l0q-5q4g2-yg469')
        markup.add(button1)
        time.sleep(1)
        bot.send_message(callback.message.chat.id, "Счет на оплату сформирован.", reply_markup=markup)

    elif callback.data == "oplata700":
        bot.delete_message(callback.message.chat.id, message_del.message_id)
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("ПОПОЛНИТЬ", url = 'https://payok.io/payment_link/a417k-34j6q-u7qiv')
        markup.add(button1)
        time.sleep(1)
        bot.send_message(callback.message.chat.id, "Счет на оплату сформирован.", reply_markup=markup)

    elif callback.data == "oplata800":
        bot.delete_message(callback.message.chat.id, message_del.message_id)
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("ПОПОЛНИТЬ", url = 'https://payok.io/payment_link/dyp8k-0877x-38xd1')
        markup.add(button1)
        time.sleep(1)
        bot.send_message(callback.message.chat.id, "Счет на оплату сформирован.", reply_markup=markup)

    elif callback.data == "oplata900":
        bot.delete_message(callback.message.chat.id, message_del.message_id)
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("ПОПОЛНИТЬ", url = 'https://payok.io/payment_link/kk70m-1978z-q8ws5')
        markup.add(button1)
        time.sleep(1)
        bot.send_message(callback.message.chat.id, "Счет на оплату сформирован.", reply_markup=markup)

    elif callback.data == "btn0-2":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("ПОПОЛНИТЬ", url='t.me/send?start=IVu55ebwYGJh')
        markup.add(button1)

        bot.send_message(callback.message.chat.id, "Пополнение криптовалютой.\n\nДля пополнения криптой нажмите ПОПОЛНИТЬ, выберите соответствующую монету и переведите желаемую сумму, средства зачислятся в течение минуты\n\nКонвертация криптовалюты к рублю происходит по сегодняшнему курсу!", reply_markup=markup)

    elif callback.data == "btn0-3":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("ПОПОЛНИТЬ", url = 'https://yoomoney.ru/to/4100118564878883')
        button2 = types.InlineKeyboardButton("Я ОПЛАТИЛ", callback_data = "next")
        markup.add(button1)
        markup.add(button2)
        bot.send_message(callback.message.chat.id, "Пополнение Юмани.\n\nНажмите на кнопку ПОПОЛНИТЬ и переведите желаемую сумму, затем сделайте скриншот успешного перевода.\n\nДалее нажмите Я ОПЛАТИЛ", reply_markup=markup)

    elif callback.data == "next":
        msg = bot.send_message(callback.message.chat.id, "Отправьте скриншот успешного перевода, после проверки модератором средства будут начислены вам")
        bot.register_next_step_handler(msg, get_photo)

    elif callback.data == "btn1-1":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("КУПИТЬ 💸", callback_data = "oplata")
        markup.add(button1)

        bot.send_message(callback.message.chat.id, "Пробив по номеру\nСтоимость услуги: 215₽\n\nПроисходит пробив номера, который\nвы даёте.\n\nНаходим вам с вероятностью 99,9%:\n– ФИО\n– Год рождения\n– Паспорт, СНИЛС, ИНН\n– Адрес\n– Авто\n– Соцсети\n\nНа поиск уходит 1 час.", reply_markup=markup)
    elif callback.data == "btn1-2":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("КУПИТЬ 💸", callback_data = "oplata")
        markup.add(button1)

        bot.send_message(callback.message.chat.id, "Пробив соцсети\nСтоимость услуги: 275₽\n\nПроисходит пробив соцсети, который\nвы даёте.\n\nНаходим вам с вероятностью 99,9%:\n– Номер\n– ФИО\n– Год рождения\n– Паспорт, СНИЛС, ИНН\n– Адрес\n– Авто\n– Другие соцсети\n\nНа поиск уходит 1 час.", reply_markup=markup)

    elif callback.data == "btn1-3":
        markup = types.InlineKeyboardMarkup()
        bot.send_message(callback.message.chat.id, "Бесплатный пробив\n\nБесплатно пробьем для вас педофила или живодера. Для этого напишите нам в ТП со всеми доказательствами!", reply_markup=markup)

    elif callback.data == "btn2-1":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("КУПИТЬ 💸", callback_data = "oplata")
        markup.add(button1)

        bot.send_message(callback.message.chat.id, "🥝QIWI основной🥝\nСтоимость: 150₽\n\nПолучаете Qiwi на RU номер с основным статусом верификации.\n\nВыдаём:\nЛогин(номер)\nПароль\nAPI Токен", reply_markup=markup)
    elif callback.data == "btn2-2":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("КУПИТЬ 💸", callback_data = "oplata")
        markup.add(button1)

        bot.send_message(callback.message.chat.id, "🥝QIWI профессиональный🥝\nСтоимость: 450₽\n\nПолучаете Qiwi на RU номер с профессиональным статусом верификации.\n\nВыдаём:\nЛогин(номер)\nПароль\nAPI Токен", reply_markup=markup)
    elif callback.data == "btn2-3":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("КУПИТЬ 💸", callback_data = "oplata")
        markup.add(button1)

        bot.send_message(callback.message.chat.id, "⚛️ЮMoney именной⚛️\nСтоимость: 275₽\n\nПолучаете ЮMoney со статусом именной.\n\nВыдаём:\nЛогин(номер)\nПароль", reply_markup=markup)

    elif callback.data == "btn2-4":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("КУПИТЬ 💸", callback_data = "oplata")
        markup.add(button1)

        bot.send_message(callback.message.chat.id, "🅿️ Payeer идентифицированный 🅿️\nСтоимость: 150₽\n\nПолучаете Payeer со статусом идентифицированный.\n\nВыдаём:\nЛогин\nПароль\nСекретный код", reply_markup=markup)


    elif callback.data == "btn3-1":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("КУПИТЬ 💸", callback_data = "oplata")
        markup.add(button1)

        bot.send_message(callback.message.chat.id, "Windscribe PRO - 250₽\n\nБрут аккаунты.\n\nЕсли вход в аккаунт успешный, но по какой-то причине вы не можете пользоваться данным VPN (пример: блокировка данного VPN по вашему месту проживания), предоставляется замена.", reply_markup=markup)
    elif callback.data == "btn3-2":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("КУПИТЬ 💸", callback_data = "oplata")
        markup.add(button1)

        bot.send_message(callback.message.chat.id, "ExpressVPN | 12 месяцев\n\n– Подписка на 12 месяцев!\n– Gmail почта при регистрации!\n– Защищенный доступ в любом уголке Земли.\n– Надежное соединение из любой точки мира.\n\n– Можно использовать на всех устройствах\n– Вы получите удобные приложения для всех возможных устройств, включая телефон, планшет, компьютер, роутер и другие девайсы.", reply_markup=markup)


    elif callback.data == "btn4-1":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("КУПИТЬ 💸", callback_data = "oplata")
        markup.add(button1)

        bot.send_message(callback.message.chat.id, "Симка Билайн\nЦена: 225₽ за 7д\n\nМы выдадим вам номер, на который можно принимать смс в течение 7 дней, а так же страницу с панелью, куда приходят смс.\n\nИдеальный вариант для регистрации во всех соц.сетях!", reply_markup=markup)
    elif callback.data == "btn4-2":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("КУПИТЬ 💸", callback_data = "oplata")
        markup.add(button1)

        bot.send_message(callback.message.chat.id, "Симка Мегафон\nЦена: 275₽ за 7д\n\nМы выдадим вам номер, на который можно принимать смс в течение 7 дней, а так же страницу с панелью, куда приходят смс.\n\nИдеальный вариант для регистрации во всех соц.сетях!", reply_markup=markup)
    elif callback.data == "btn4-3":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("КУПИТЬ 💸", callback_data = "oplata")
        markup.add(button1)

        bot.send_message(callback.message.chat.id, "Симка МТС\nЦена: 350₽ за 7д\n\nМы выдадим вам номер, на который можно принимать смс в течение 7 дней, а так же страницу с панелью, куда приходят смс.\n\nИдеальный вариант для регистрации во всех соц.сетях!", reply_markup=markup)


    elif callback.data == "btn5-1":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("КУПИТЬ 💸", callback_data = "oplata")
        markup.add(button1)

        bot.send_message(callback.message.chat.id, "Вспышка 📡\nСтоимость услуги: 1000₽\n\nОпределяем местоположение человека на данный момент по его номеру телефона 🔎\n\nНа выполнение услуги уходит около 30 минут.\nРаботает только с RU номерами!\nВ случае неудачи (5%) делаем вам манибэк, оставляя себе 75₽", reply_markup=markup)
    elif callback.data == "btn5-2":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("КУПИТЬ 💸", callback_data = "oplata")
        markup.add(button1)

        bot.send_message(callback.message.chat.id, "Защита ваших данных 🛡\nСтоимость услуги: 200₽\n\nПолностью удаляем ваши данные со всех интернет-сервисов по пробиву и слитых баз данных.\n\nВаши враги и злоумышленники ничего не смогут найти о вас, если захотят это сделать. Ваша анонимность в интернете поднимется на 99% ⚡", reply_markup=markup)
    elif callback.data == "btn5-3":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("КУПИТЬ 💸", callback_data = "oplata")
        markup.add(button1)

        bot.send_message(callback.message.chat.id, "APK вирус ☠\nСтоимость услуги: 300₽\n\nПолучаете файл APK (для андроид), когда вы кинете его своей жертве и она установит его себе на телефон, то мобила сразу умирает. Хороший способ проучить обидчика.", reply_markup=markup)
    elif callback.data == "btn5-4":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("КУПИТЬ 💸", callback_data = "oplata")
        markup.add(button1)

        bot.send_message(callback.message.chat.id, "Блокировка карты 🚫\nСтоимость услуги: 200₽\n\nБлокируем карту СБЕР. Соблюдая анонимность, мы звоним в отделение сбербанка и говорим что нашли на улице карту, и диктуем ту, которую вы нам укажете. Ее блокируют через 5 минут. Ответственность берем на себя. Хороший способ проучить мошенников, если вы знаете их карту. Работает ТОЛЬКО со сбером!", reply_markup=markup)
    elif callback.data == "btn5-6":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("КУПИТЬ 💸", callback_data = "oplata")
        markup.add(button1)

        bot.send_message(callback.message.chat.id, "Атака пиццей 🍕\nСтоимость услуги: 125₽\n\nВы даете нам адрес жертвы, например вашего обидчика, и мы, благодаря вирт.номеру и прокси, заказываем на него 30пицц (10 пицц с одной пиццерии) с оплатой на месте курьеру. Итог: ваша жертва будет страдать. Всё делаем анонимно и ответственность берем на себя!", reply_markup=markup)
    elif callback.data == "btn5-5":
        bot.send_message(callback.message.chat.id, "Разработка бота 🤖\nСтоимость услуги: от 500₽\n\nСоздадим вам любого бота на заказ, всё обговаривается в личных сообщениях. @katerinasurprise")


    elif callback.data == "btn6-1":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("КУПИТЬ 💸", callback_data = "oplata")
        markup.add(button1)

        bot.send_message(callback.message.chat.id, "Билдер майнера 🪙\nСтоимость: 175₽\n\nБилдер майнера - это программа, которая позволит вам сделать и настроить свой майнер за 2-3 минуты. После создания вам будет выдан файл, который вы должны кинуть жертве под любым предлогом. После того как она его установит, программа начнет добывать биткоин, медленно убивая телефон или компьютер вашей жертвы. Удаление не поможет. Файл можно кинуть хоть 100 людям. Идеальный вариант заработка!", reply_markup=markup)

    elif callback.data == "btn6-2":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("КУПИТЬ 💸", callback_data = "oplata")
        markup.add(button1)

        bot.send_message(callback.message.chat.id, "Софт для деанонимизации анонимного чата 🎭\nСтоимость услуги: 350₽\n\nМы создали скрипт, который позволяет узнать вашего собеседника в @AnonRuBot , вам выдает аккаунт того, с кем вы общаетесь!\n\nДемонстрация - @softforanonchat", reply_markup=markup)
    
    elif callback.data == "btn6-3":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("КУПИТЬ 💸", url = "https://t.me/FatalityProject")
        markup.add(button1)

        bot.send_message(callback.message.chat.id, "Fatality - Софт для для спама звонками, флуда в телеграмме, массового репортинга, чат парсинга и тд.\n\nСтоимость услуги: 400₽\n\nМы создали данный скрипт который позволяет выполнять разные действия автоматически. Например оставлять заявки на сайте или флудить в тг чате.\n\nПриобрести- @FatalityProject", reply_markup=markup)
    
    
    
    elif callback.data == "btn7-1":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("КУПИТЬ 💸", callback_data = "oplata")
        markup.add(button1)

        bot.send_message(callback.message.chat.id, "Гайд по анонимности в сети 🥷\nСтоимость: 250₽\n\nДанный мануал обучит вас оставаться полностью анонимным в интернете, даже совершая что-то не очень хорошее.😉\nГайд состоит из 5 разделов, общее количество страниц - 45!", reply_markup=markup)

    elif callback.data == "btn7-2":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("КУПИТЬ 💸", callback_data = "oplata")
        markup.add(button1)

        bot.send_message(callback.message.chat.id, "Деанон любого 🕵️\nСтоимость: 575₽\n\nМы подготовили для вас гайд по деанону любого пользователя в сети. В нем содержится 50% наших умений, которых мы набирались долгие годы. Гайд содержит в себе десятки страниц. К примеру, в нём есть 3 способа вычислить IP любого телеграм пользователя, или cпособ как найти паспорт по любому номеру телефона. Бонусом мы добавили в гайд пару нюансов соц.инженерии и базу данных в 10.000 строк!", reply_markup=markup)

    elif callback.data == "btn8-1":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("КУПИТЬ 💸", callback_data = "oplata")
        markup.add(button1)
        
        bot.send_message(callback.message.chat.id, "Такси за 0₽ 🚕\nСтоимость: 350₽\n\nПокупая данную позицию, вы получаете способ бесплатно кататься на Яндекс Такси! Абуз заключается в рефаунде (возврат средств), особых умений не требуется. Способ не сливали, поэтому он долговечен. Условием является то, что поездка должна быть менее 20-25км!", reply_markup=markup)

    elif callback.data == "btn8-2":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("КУПИТЬ 💸", callback_data = "oplata")
        markup.add(button1)
        
        bot.send_message(callback.message.chat.id, "Абуз СберМегаМаркета 🛍️\nСтоимость: 400₽\n\nДанный гайд(+промокоды) поможет вам совершать покупки за полцены на СберМегаМаркете. В услугу входит наша личная видеоинструкция.", reply_markup=markup)

    elif callback.data == "btn8-3":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("КУПИТЬ 💸", callback_data = "oplata")
        markup.add(button1)
        
        bot.send_message(callback.message.chat.id, "ТГ премиум бесплатно ⭐\nСтоимость: 400₽\n\nНедавно наши коллеги придумали способ  рефаунда(возврата средств) за покупку ТГ премиума. Способ очень прост, главное покупать ТГ премиум через Сбербанк или Тинькофф!", reply_markup=markup)

    elif callback.data == "btn8-4":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("КУПИТЬ 💸", callback_data = "oplata")
        markup.add(button1)
        
        bot.send_message(callback.message.chat.id, "Голоса Вк за лоупрайс ⚡\nСтоимость: 250₽\n\nДешево сливаем для вас способ одного белорусского гения по покупке голосов Вк за лоупрайс. Курс голосов по данному способу составляет 1 голос = 3₽ (вместо 7). Не знаем сколько проживет данный способ. Если кнопка купить работает, то способ еще живой.", reply_markup=markup)

    elif callback.data == "btn8-5":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("КУПИТЬ 💸", callback_data = "oplata")
        markup.add(button1)
     
        bot.send_message(callback.message.chat.id, "Абуз бонусов СберСпасибо 🟢\nСтоимость: 375₽\n\nЭто способ, придуманный лично нашей командой! Он позволяет бесплатно получать бонусы СберСпасибо. А в наше время это полезная вещь, ведь ей можно расплачиваться в некоторых местах, например Бургер Кинг, и тд! ", reply_markup=markup)

    elif callback.data == "podarok":
        time.sleep(0.5)
        bot.send_message(callback.message.chat.id, "Вы получите +10% к первому пополнению ✅")


    elif callback.data == "oplata":
        time.sleep(1)
        bot.send_message(callback.message.chat.id, "Недостаточно средств на балансе 🚫")


bot.infinity_polling()
