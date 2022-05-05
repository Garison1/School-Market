# -*- coding: utf-8 -*- 
import sys
sys.path
sys.path.append('D:\\Дима\\Програмирование\\Python\\BOT')
import mysql.connector
import telebot
import random
import logging
import base64
import datetime
from datetime import timedelta
from telebot import types

users = {}
buy_users = {}
counters = {}
ww = {}

count_er = 0
io = ''
    
db = mysql.connector.connect(host="localhost", user="garison", password="drowssap", database="test")
cursor = db.cursor()

qw = "SELECT distinct `user id` FROM `users` "
cursor.execute(qw)
result = cursor.fetchall()
for i in result:
    chat_id = int(i[0])
    qw = "SELECT distinct `nickname` FROM `users` WHERE `user id` = %s and `nickname` <> ''" %(chat_id)
    cursor.execute(qw)
    r = cursor.fetchall()
    for a in r:
        users[chat_id] = {'chat': 0, 'free': 0, 'ban': 0, 'subject_r': '', 'class_r':'', 'c.data': 0, 'nickname': a[0], 'nicou': 0, 'subject': '', 'class': '', 'date': '', 'note': '', 'file': [], 'price': 0, 'noname': ''}
        buy_users[chat_id] = {'buy_subject': '', 'buy_class': '', 'buy_data': '', 'buynum': '', 'buy_file': []}
        counters[chat_id] = {'count_3': 0, 'cou': 0, 'count_2': 0, 'count': 0, 'call': '', 'ids': '', 'idz': '', 'csc': 0, 'bd': 0, 'buy_data': 0, 'uou': 0, 'uqu': 0, 'f': 0, 'zwz': 0, 'coc': 0, 'cec': 0,'cac': 0, 'czc': 0, 'cjc': 0}
        ww[chat_id] = {'result': '', 'row': '', 'b': 0, 'assessment': '', 'cou': 1, 'N': 0, 'rating': 0.0}
    
token = '639065045:AAG1TpgP3I0ssDpj2me9_GVNWZn3Nm5z55w'
bot = telebot.TeleBot(token, threaded=False)

def code(s):
    s = base64.b64encode(bytes(s, 'utf-8'))
    s = s.decode('utf-8')
    return(s)

def txt(s):
    s = base64.b64decode(str(s).encode())
    s = s.decode()
    return(s)

def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

@bot.message_handler(commands=['rating'])
def trusted(message):
    MESSAGE = '\nP.S. объявления стоимостью меньше 2🍆 не оцениваются.'
    num = 1
    qw = "SELECT `nickname` FROM `personal` WHERE `nickname` <> '' and `stars` <> 0 ORDER BY `stars`, `N`"
    cursor.execute(qw)
    result = cursor.fetchall()
    result.reverse()
    if not result:
        bot.send_message(message.chat.id,'Рейтинг пуст.')
    else:
        for a in result:
            qw = "SELECT distinct `rating` FROM `personal` WHERE `nickname` = '%s'" %(a[0])
            cursor.execute(qw)
            resul = cursor.fetchall()
            qw = "SELECT distinct `N` FROM `personal` WHERE `nickname` = '%s'" %(a[0])
            cursor.execute(qw)
            res = cursor.fetchall()
            if res[0][0] != 0:
                if str((resul[0][0]/res[0][0])-int(resul[0][0]/res[0][0]))[1:] == '.0':
                    if num == 1:
                        MESSAGE = '👑' + txt(str(a[0])) + '  -  рейтинг:  ' + str(int(resul[0][0]/res[0][0])) + '⭐️,   оценок:  ' + str(int(res[0][0])) + '\n' + MESSAGE
                    else:
                        MESSAGE = str(num) + ') ' + txt(str(a[0])) + '  -  рейтинг:  ' + str(int(resul[0][0]/res[0][0])) + '⭐️,   оценок:  ' + str(int(res[0][0])) + '\n' + MESSAGE
                else:
                    if num == 1:
                        MESSAGE = '👑' + txt(str(a[0])) + '  -  рейтинг:  ' + str(round(resul[0][0]/res[0][0], 2)) + '⭐️,   оценок:  ' + str(int(res[0][0])) + '\n' + MESSAGE
                    else:
                        MESSAGE = str(num) + ') ' + txt(str(a[0])) + '  -  рейтинг:  ' + str(round(resul[0][0]/res[0][0], 2)) + '⭐️,   оценок:  ' + str(int(res[0][0])) + '\n' + MESSAGE
            num += 1
    bot.reply_to(message, MESSAGE)
    num = 1
    
@bot.message_handler(commands=['reliable'])
def trusted(message):
    num = 0
    qw = "SELECT `nickname` FROM `personal` WHERE `super` = 1"
    cursor.execute(qw)
    result = cursor.fetchall()
    if len(result) != 0:
        MESSAGE = 'На 99,9% надежные продавцы:\n'
        for i in result:
            num += 1
            MESSAGE = MESSAGE + '\n' + str(num) + ') ' + str(txt(i[0]))
        bot.send_message(message.chat.id, MESSAGE + ' \n\nP.S. Все кто в этом списке имеют неограниченный доступ к объявлениям. Если вы хотите попасть в этот список, напишите мне —> @RL_support_Bot')

@bot.message_handler(commands=['donate'])
def send_wel(message):
    bot.reply_to(message, "Донат от 5 грн у человека, который описан в пополнении счета.")
    
@bot.message_handler(commands=['act'])
def send_welcom(message):
    if message.chat.id == 562050144 or message.chat.id == 653376416:
        if message.chat.id == 653376416:
            key = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            key.row("овощи", "рассылка", "гривны")
            key.row("доверие", "бан", "воля", 'недоверие')
            key.row("начать чат", "все", "переименовать")
            key.row("отмена")
            if message.chat.id == 562050144:
                bot.send_message(message.chat.id, "Егор, это пункт управления ботом, пользуйся с умом!",reply_markup=key)
            if message.chat.id == 653376416:
                bot.send_message(message.chat.id, "Да здравствует повелитель!",reply_markup=key)
        else:
            key = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            key.row("овощи", "гривны")
            key.row("бан", "воля")
            key.row("переименовать", 'все')
            key.row("отмена")
            if message.chat.id == 562050144:
                bot.send_message(message.chat.id, "Вы попали в пункт управления ботом, пользуйтесь с умом!",reply_markup=key)
            if message.chat.id == 653376416:
                bot.send_message(message.chat.id, "Да здравствует повелитель!",reply_markup=key)
    else:
        bot.send_message(message.chat.id, "Вы не администратор😜")
            
@bot.message_handler(commands=['help'])
def send_welcom(message):
    bot.reply_to(message, "Все вопросы на —> @Rl_support_Bot\n\nP.S. Бот находится в стадии BETA тестирования, воши отзывы могут помочь в дальнейшем развитии.")

@bot.message_handler(commands=["start"])
def keyboard(message):
    qw = "SELECT distinct `nickname` FROM `users` WHERE `user id` = %s" %(str(message.chat.id))
    cursor.execute(qw)
    result = cursor.fetchall()
    if len(result) == 0:
        if message.chat.id not in users.keys():
            
            users[message.chat.id] = {'chat': 0, 'free': 0, 'ban': 0, 'subject_r': '', 'class_r':'', 'c.data': 0, 'nicou': 0, 'subject': '', 'class': '', 'date': '', 'note': '', 'file': [], 'price': 0, 'noname': ''}
            buy_users[message.chat.id] = {'buy_subject': '', 'buy_class': '', 'buy_data': '', 'buynum': '', 'buy_file': []}
        
        if message.chat.id in users.keys():
            users[message.chat.id] = {'chat': 0, 'free': 0, 'ban': 0, 'subject_r': '', 'class_r':'', 'c.data': 0, 'nicou': 0, 'subject': '', 'class': '', 'date': '', 'note': '', 'file': [], 'price': 0, 'noname': ''}
            buy_users[message.chat.id] = {'buy_subject': '', 'buy_class': '', 'buy_data': '', 'buynum': '', 'buy_file': []}
            
            cur = datetime.datetime.now()
            a = datetime.timedelta(hours=6)
            cur += a
            qw = """INSERT INTO `test`.`users` (`id`, `user id`, `subject`, `class`, `date`, `note`, `file_path`, `price`, `balance`, `nickname`) VALUES( NULL, '%s', '%s',' %s', '%s', '%s', '%s', %d, %d, '%s')""" %(message.chat.id,users[message.chat.id]['subject'],users[message.chat.id]['class'], cur.strftime('%Y-%m-%d-%H-%M'),users[message.chat.id]['note'],'',users[message.chat.id]['price'],0,'')
            cursor.execute(qw)
            db.commit()
            
            counters[message.chat.id] = {'count_3': 0, 'cou': 0, 'count_2': 0, 'count': 0, 'call': '', 'ids': '', 'idz': '', 'csc': 0, 'bd': 0, 'buy_data': 0, 'uou': 0, 'uqu': 0, 'f': 0, 'zwz': 0, 'coc': 0, 'cec': 0,'cac': 0, 'czc': 0, 'cjc': 0}
            ww[message.chat.id] = {'result': '', 'row': '', 'b': 0, 'assessment': '', 'cou': 1, 'N': 0, 'rating': 0.0}
            counters[message.chat.id]['call'] = ''
            counters[message.chat.id]['ids'] = ''
            counters[message.chat.id]['idz'] = ''
            counters[message.chat.id]['csc'] = 0
            counters[message.chat.id]['bd'] = 0
            counters[message.chat.id]['buy_data'] = 0
            counters[message.chat.id]['uou'] = 0
            counters[message.chat.id]['uqu'] = 0
            counters[message.chat.id]['f'] = 0
            counters[message.chat.id]['zwz'] = 0
            counters[message.chat.id]['coc'] = 0
            counters[message.chat.id]['cec'] = 0
            counters[message.chat.id]['cac'] = 0
            counters[message.chat.id]['czc'] = 0
            counters[message.chat.id]['cjc'] = 0
            
            bot.send_document(message.chat.id, 'https://i.pinimg.com/originals/7d/9b/1d/7d9b1d662b28cd365b33a01a3d0288e1.gif')
            users[message.chat.id] = {'chat': 0, 'free': 0, 'ban': 0, 'subject_r': '', 'class_r':'', 'c.data': 0, 'nicou': 0, 'subject': '', 'class': '', 'date': '', 'note': '', 'file': [], 'price': 0, 'nickname': '', 'noname': ''}
            buy_users[message.chat.id] = {'buy_subject': '', 'buy_class': '', 'buy_data': '', 'buynum': '', 'buy_file': []}

        if message.chat.id in users.keys():
            users[message.chat.id] = {'chat': 0, 'free': 0, 'ban': 0, 'subject_r': '', 'class_r':'', 'c.data': 0, 'nicou': 0, 'subject': '', 'class': '', 'date': '', 'note': '','file': [], 'price': 0, 'nickname': '', 'noname': ''}
            buy_users[message.chat.id] = {'buy_subject': '', 'buy_class': '', 'buy_data': '', 'buynum': '', 'buy_file': []}
            ww[message.chat.id] = {'result': '', 'row': '', 'b': 0, 'assessment': '', 'cou': 1, 'N': 0, 'rating': 0.0}
            users[message.chat.id]['nickname'] = result
            key = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            key.row("продать", "купить")
            key.row("пополнить счет", "регистрация", "баланс")
            bot.send_message(message.chat.id, "Управляйте ботом с помощью кнопок",reply_markup=key)

    else:
        users[message.chat.id] = {'chat': 0, 'free': 0, 'ban': 0, 'subject_r': '', 'class_r':'', 'c.data': 0, 'nicou': 0, 'subject': '', 'class': '', 'date': '', 'note': '', 'file': [], 'price': 0, 'noname': ''}
        buy_users[message.chat.id] = {'buy_subject': '', 'buy_class': '', 'buy_data': '', 'buynum': '', 'buy_file': []}
        ww[message.chat.id] = {'result': '', 'row': '', 'b': 0, 'assessment': '', 'cou': 1, 'N': 0, 'rating': 0.0}
        users[message.chat.id]['nickname'] = result[0]
        key = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        key.row("продать", "купить")
        key.row("пополнить счет", "баланс")
        bot.send_message(message.chat.id, "Управляйте ботом с помощью кнопок",reply_markup=key)
        
@bot.message_handler(func=lambda c:True, content_types=['text'])
def info_message(message):
    msg = message.text.lower() 
    nores = 0
    global count_er
    if message.chat.id not in users.keys() or message.chat.id not in buy_users.keys() or message.chat.id not in ww.keys() or message.chat.id not in counters.keys():
        
        qw = "SELECT distinct `nickname` FROM `users` WHERE `user id` = %s and `nickname` <> ''" %(message.chat.id)
        cursor.execute(qw)
        result = cursor.fetchall()
        result = txt(result)
        
        if len(result) != 0:
            users[message.chat.id] = {'chat': 0, 'free': 0, 'ban': 0, 'subject_r': '', 'class_r':'', 'c.data': 0, 'nickname': result[0], 'nicou': 0, 'subject': '', 'class': '', 'date': '', 'note': '', 'file': [], 'price': 0, 'noname': ''}
            buy_users[message.chat.id] = {'buy_subject': '', 'buy_class': '', 'buy_data': '', 'buynum': '', 'buy_file': []}
            counters[message.chat.id] = {'count_3': 0, 'cou': 0, 'count_2': 0, 'count': 0, 'call': '', 'ids': '', 'idz': '', 'csc': 0, 'bd': 0, 'buy_data': 0, 'uou': 0, 'uqu': 0, 'f': 0, 'zwz': 0, 'coc': 0, 'cec': 0,'cac': 0, 'czc': 0, 'cjc': 0}
            ww[message.chat.id] = {'result': '', 'row': '', 'b': 0, 'assessment': '', 'cou': 1, 'N': 0, 'rating': 0.0}
        else:
            users[message.chat.id] = {'chat': 0, 'free': 0, 'ban': 0, 'subject_r': '', 'class_r':'', 'c.data': 0, 'nickname': '', 'nicou': 0, 'subject': '', 'class': '', 'date': '', 'note': '', 'file': [], 'price': 0, 'noname': ''}
            buy_users[message.chat.id] = {'buy_subject': '', 'buy_class': '', 'buy_data': '', 'buynum': '', 'buy_file': []}
            counters[message.chat.id] = {'count_3': 0, 'cou': 0, 'count_2': 0, 'count': 0, 'call': '', 'ids': '', 'idz': '', 'csc': 0, 'bd': 0, 'buy_data': 0, 'uou': 0, 'uqu': 0, 'f': 0, 'zwz': 0, 'coc': 0, 'cec': 0,'cac': 0, 'czc': 0, 'cjc': 0}
            ww[message.chat.id] = {'result': '', 'row': '', 'b': 0, 'assessment': '', 'cou': 1, 'N': 0, 'rating': 0.0}
   

    qw = "SELECT `ban` FROM `personal` WHERE `user id` = %s" %(str(message.chat.id)) 
    cursor.execute(qw)
    result = cursor.fetchall()
    if len(result) == 0:
        nores = 1
    if nores == 1 or nores == 0 and result[0][0] == 0:
        
        qw = "SELECT distinct `nickname` FROM `users` WHERE `user id` = %s and nickname <> ''" %(str(message.chat.id))
        cursor.execute(qw)
        ww[message.chat.id]['result'] = cursor.fetchall()
        if len(ww[message.chat.id]['result']) == 0:
            users[message.chat.id]['noname'] = 1
        else:
            users[message.chat.id]['noname'] = 0

        if msg == msg:
            counters[message.chat.id]['buy_data'] = 0

        if msg == 'завершить чат':
            if users[message.chat.id]['chat'] != 0:
                
                key = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                key.row("продать", "купить")
                key.row("пополнить счет", "баланс")
                bot.send_message(message.chat.id, 'Чат завершен.',reply_markup=key)
                
                key = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                key.row("продать", "купить")
                key.row("пополнить счет", "баланс")
                bot.send_message(users[message.chat.id]['chat'], 'Чат завершен.' ,reply_markup=key)

                users[users[message.chat.id]['chat']]['chat'] = 0
                users[message.chat.id]['chat'] = 0
        
        
        if msg == 'отмена':
            
            count_er = 0
            counters[message.chat.id]['cjc'] = 0
            counters[message.chat.id]['count'] = 0
            counters[message.chat.id]['ids'] = ''
            counters[message.chat.id]['idz'] = ''
            counters[message.chat.id]['uou'] = 0
            counters[message.chat.id]['uqu'] = 0
            counters[message.chat.id]['coc'] = 0
            counters[message.chat.id]['cec'] = 0
            counters[message.chat.id]['cac'] = 0
            counters[message.chat.id]['czc'] = 0
            users[message.chat.id]['nicou'] = 0
            counters[message.chat.id]['count_3'] = 0

            buy_users[message.chat.id] = {'buy_subject': '', 'buy_class': '', 'buy_data': '', 'buynum': '', 'buy_file': []}

            if users[message.chat.id]['noname'] == 1:
                users[message.chat.id] = {'chat': 0, 'free': 0, 'ban': 0, 'subject_r': '', 'class_r':'', 'c.data': 0, 'nicou': 0, 'subject': '', 'class': '', 'date': '', 'note': '', 'file': [], 'price': 0, 'nickname': users[message.chat.id]['nickname'], 'noname': 1}
                key = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                key.row("продать", "купить")
                key.row("пополнить счет", "регистрация", "баланс")
                bot.send_message(message.chat.id, 'Успешно отменено!',reply_markup=key) 

            if users[message.chat.id]['noname'] == 0:
                users[message.chat.id] = {'chat': 0, 'free': 0, 'ban': 0, 'subject_r': '', 'class_r':'', 'c.data': 0, 'nicou': 0, 'subject': '', 'class': '', 'date': '', 'note': '', 'file': [], 'price': 0, 'nickname': users[message.chat.id]['nickname'], 'noname': 0}
                key = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                key.row("продать", "купить")
                key.row("пополнить счет", "баланс")
                bot.send_message(message.chat.id, 'Успешно отменено!',reply_markup=key) 

        if users[message.chat.id]['nicou'] == 1:
            users[message.chat.id]['nickname'] = message.text
            qw = "SELECT distinct `nickname` FROM `users` WHERE `nickname` <> ''"
            cursor.execute(qw)
            ww[message.chat.id]['result'] = cursor.fetchall()
            for i in ww[message.chat.id]['result']:
                srt = txt(i[0])
                if users[message.chat.id]['nickname'].lower() == srt.lower():
                    ww[message.chat.id]['b'] = 1
                    bot.send_message(message.chat.id, "Такой ник уже занят! Введите другой:")  
                else:
                    ww[message.chat.id]['b'] = 0

            if len(users[message.chat.id]['nickname']) < 3:
                if len(users[message.chat.id]['nickname']) > 20:
                    bot.send_message(message.chat.id, 'Nickname слишком длинный, повторите ввод:')
                if len(users[message.chat.id]['nickname']) < 3:
                    bot.send_message(message.chat.id, 'Nickname слишком короткий, повторите ввод:')

            if len(users[message.chat.id]['nickname']) <= 20 and len(users[message.chat.id]['nickname']) >= 3 and ww[message.chat.id]['b'] == 0:
                qw = """UPDATE `users` SET `nickname` = "%s" WHERE `user id` = '%s' """ %(code(users[message.chat.id]['nickname']), message.chat.id)
                cursor.execute(qw)
                db.commit()

                qw = """INSERT INTO `test`.`personal` (`user id`, `nickname`, `rating`, `N`, `ban`) VALUES('%s', '%s', %d, %d, %d)""" %(message.chat.id,code(users[message.chat.id]['nickname']),0,0,0)
                cursor.execute(qw)
                db.commit()

                key = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                key.row("продать", "купить")
                key.row("пополнить счет", "баланс")
                bot.send_message(message.chat.id, 'Nickname  "' + str(users[message.chat.id]['nickname']) + '"  успешно добавлен! Если вы хотите его изменить, напишите мне —> @Rl_support_Bot',reply_markup=key) 
                users[message.chat.id]['nicou'] = 0
                
                
                
                
        if users[message.chat.id]['ban'] == 1 and message.chat.id == 653376416 and msg != 'отмена' or users[message.chat.id]['ban'] == 1 and message.chat.id == 684759645 and msg != 'отмена':
            qw = "SELECT `nickname` FROM `personal` WHERE `user id` = '%s'" %(str(message.text)) 
            cursor.execute(qw)
            result = cursor.fetchall()
            if len(result) != 0:
                qw = """UPDATE `personal` SET `ban` = %d WHERE `user id` = '%s' """ %(1, str(message.text))
                cursor.execute(qw)
                db.commit()
                bot.send_message(message.chat.id, 'Пользователь успешно забанен!')
                users[message.chat.id]['ban'] = 0
            else:
                bot.send_message(message.chat.id, 'Такого пользователя не существует! Повторите ввод:')

        if message.text == 'бан' and message.chat.id == 653376416 or message.text == 'бан' and message.chat.id == 684759645:
            bot.send_message(message.chat.id, 'Кого забанить? (id)')
            users[message.chat.id]['ban'] = 1

        if users[message.chat.id]['free'] == 1 and message.chat.id == 653376416 or users[message.chat.id]['free'] == 1 and message.chat.id == 684759645:

            qw = "SELECT `nickname` FROM `personal` WHERE `user id` = '%s'" %(str(message.text)) 
            cursor.execute(qw)
            result = cursor.fetchall()
            if len(result) != 0:
                qw = """UPDATE `personal` SET `ban` = %d WHERE `user id` = '%s' """ %(0, str(message.text))
                cursor.execute(qw)
                db.commit()
                bot.send_message(message.chat.id, 'Пользователь свободен!')
                bot.send_document(message.text, 'https://i.pinimg.com/originals/7d/9b/1d/7d9b1d662b28cd365b33a01a3d0288e1.gif')
                bot.send_message(message.text, 'Вы разбанены!!!')
                users[message.chat.id]['free'] = 0
            else:
                bot.send_message(message.chat.id, 'Такого пользователя не существует! Повторите ввод:')

        if message.text == 'воля' and message.chat.id == 653376416 or message.text == 'воля' and message.chat.id == 684759645:
            bot.send_message(message.chat.id, 'Кого освободить? (id)')
            users[message.chat.id]['free'] = 1

                
                
                

        if counters[message.chat.id]['count_3'] == 3:
            qw = "SELECT `nickname` FROM `personal` WHERE `user id` = '%s'" %(str(message.text)) 
            cursor.execute(qw)
            ww[message.chat.id]['result'] = cursor.fetchall()
            if len(ww[message.chat.id]['result']) != 0:
                qw = """UPDATE `personal` SET `super` = 0 WHERE `user id` = '%s' """ %(message.text)
                cursor.execute(qw)
                db.commit()
                bot.send_message(message.chat.id, 'Пользователь ' + txt(ww[message.chat.id]['result']) + ' удален из списка reliable!')
                bot.send_message(message.text, 'Вы удалены из списка reliable.')
                counters[message.chat.id]['count_3'] = 0
            else:
                bot.send_message(message.chat.id, 'Такого юзера не существует! Повторите ввод:')
                
        if counters[message.chat.id]['count_3'] == 1:
            qw = "SELECT `nickname` FROM `personal` WHERE `user id` = '%s'" %(str(message.text)) 
            cursor.execute(qw)
            ww[message.chat.id]['result'] = cursor.fetchall()
            if len(ww[message.chat.id]['result']) != 0:
                qw = """UPDATE `personal` SET `super` = 1 WHERE `user id` = '%s' """ %(message.text)
                cursor.execute(qw)
                db.commit()
                bot.send_message(message.chat.id, 'Пользователь ' + txt(ww[message.chat.id]['result']) + ' добавлен в список reliable!')
                bot.send_message(message.text, 'Поздравляем! Вы стали доверенным пользователем и теперь у вас безлимитрый доступ ко всем объявлениям! Но с этого момента вы должны продавать только качественный товар, в противном случае будете лишены данного статуса!')
                counters[message.chat.id]['count_3'] = 0
            else:
                bot.send_message(message.chat.id, 'Такого юзера не существует! Повторите ввод:')
        
        global io
        if count_er == 1:
            nkb = 0
            qw = "SELECT `user id` FROM `personal` WHERE `nickname` = '%s'" %(io)
            cursor.execute(qw)
            resultat = cursor.fetchall()
            if len(ww[message.chat.id]['result']) != 0:
                users[message.chat.id]['nickname'] = message.text
                qw = "SELECT distinct `nickname` FROM `users` WHERE `nickname` <> ''"
                cursor.execute(qw)
                ww[message.chat.id]['result'] = cursor.fetchall()
                for i in ww[message.chat.id]['result']:
                    srt = txt(i[0])
                    if users[message.chat.id]['nickname'].lower() == srt.lower():
                        ww[message.chat.id]['b'] = 1
                        bot.send_message(message.chat.id, "Такой ник уже занят! Введите другой:")
                        nkb = 0
                        break
                    else:
                        nkb = 1
                if nkb == 1:        
                    qw = """UPDATE `users` SET `nickname` = '%s' WHERE `user id` = '%s' """ %(code(message.text), resultat[0][0])
                    cursor.execute(qw)
                    db.commit()

                    qw = """UPDATE `personal` SET `nickname` = '%s' WHERE `user id` = '%s' """ %(code(message.text), resultat[0][0])
                    cursor.execute(qw)
                    db.commit()

                    bot.send_message(message.chat.id, 'Ник успешно изменен!')
                    bot.send_message(resultat[0][0], 'Ваш ник изменен на "' + str(message.text) + '"')
                    count_er = 0
                    nkb = 0
            else:
                bot.send_message(message.chat.id, 'Такого юзера не существует, повторите ввод:')
        
        if msg == 'переименовать' and message.chat.id == 653376416:
                
            qw = "SELECT `nickname` FROM `personal`" 
            cursor.execute(qw)
            ww[message.chat.id]['result'] = cursor.fetchall()
            buttons = []
            key = types.InlineKeyboardMarkup()
            for i in ww[message.chat.id]['result']:
                buttons.append(types.InlineKeyboardButton(text = txt(i[0]), callback_data = '!' + i[0]))
                key.add(buttons[-1])
            bot.send_message(message.chat.id, 'Переименовать:', reply_markup = key) 
        
        if msg == 'доверие' and message.chat.id == 653376416:
            bot.send_message(message.chat.id, 'Доверенный пользователь получит неограниченный доступ к домашним заданиям!\n\nКому дать доверенность(id):')
            counters[message.chat.id]['count_3'] = 1
            
        if msg == 'недоверие' and message.chat.id == 653376416:
            bot.send_message(message.chat.id, 'У кого забрать доверие(id):')
            counters[message.chat.id]['count_3'] = 3
            
        if msg == 'регистрация' and users[message.chat.id]['nicou'] == 0:  
            if users[message.chat.id]['noname'] == 1:
                key = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                key.row("отмена")
                bot.send_message(message.chat.id, 'Введите nickname:',reply_markup=key)
                users[message.chat.id]['nicou'] = 1
            if users[message.chat.id]['noname'] == 0:
                bot.send_message(message.chat.id, 'Вы уже зарегистрированы!')

        if counters[message.chat.id]['csc'] == 1:   
            note = message.text
            if len(note) < 3:
                bot.send_message(message.chat.id, 'Коментарий слишком короткий, повторите ввод:')
            if len(note) > 100:
                bot.send_message(message.chat.id, 'Коментарий слишком длинный, повторите ввод:')
            if len(note) <= 100 and len(note) >= 3:
                note = message.text
                users[message.chat.id]['note'] = str(note)
                key = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                key.row('готово', 'отмена')
                bot.send_message(message.chat.id, 'Отлично! Назначьте цену🍆:',reply_markup=key) 
                counters[message.chat.id]['zwz'] = 1
                counters[message.chat.id]['csc'] = 0
        # Вывод средств
        if msg == 'гривны' and message.chat.id == 653376416 or msg == 'гривны' and message.chat.id == 684759645 or msg == 'гривны' and message.chat.id == 562050144:
            counters[message.chat.id]['uqu'] = 1
        if message.chat.id == 653376416 and counters[message.chat.id]['uqu'] == 1 or message.chat.id == 684759645 and counters[message.chat.id]['uqu'] == 1:

            if counters[message.chat.id]['cjc'] == 1:
                gr = message.text
                if gr.isdigit() == False:
                    bot.send_message(message.chat.id, 'Сумма введена не корректно, повторите ввод:')
                if gr.isdigit() == True:   
                    qw = "SELECT distinct `balance` FROM `users` WHERE `user id` = %s" %(str(counters[message.chat.id]['idz'])) 
                    cursor.execute(qw)
                    ww[message.chat.id]['result'] = cursor.fetchall()
                    if len(ww[message.chat.id]['result']) != 0:
                        old0bal = ww[message.chat.id]['result'][0][0]
                        owo = int(gr)
                        vivod = owo / 5
                        if old0bal >= owo:
                            owo = old0bal - owo  
                            qw = """UPDATE `users` SET `balance` = %s WHERE `user id` = %s """ %(owo, str(counters[message.chat.id]['idz']))   
                            cursor.execute(qw)
                            db.commit()
                            bot.send_message(message.chat.id, 'Вы вывели ' + str(vivod) + ' грн!') 
                            owo = 0
                            vivod = 0
                            counters[message.chat.id]['cjc'] = 0
                            old0bal = 0
                            gr = 0
                            counters[message.chat.id]['uqu'] = 0
                        if old0bal < owo:
                            bot.send_message(message.chat.id, 'Сумма вывода > баланса, повторите ввод:')
                    else:
                        bot.send_message(message.chat.id, 'Такого юзера не существует!')

            m = message.text
            if counters[message.chat.id]['cac'] == 1:   
                if len(m) != 9:
                    bot.send_message(message.chat.id, 'Не корректный id, повторите ввод:')
                if len(m) == 9:
                    if m.isdigit() == False:
                        bot.send_message(message.chat.id, 'id введен не корректно, повторите ввод:')
                    if m.isdigit() == True:
                        counters[message.chat.id]['idz'] = message.text
                        qw = "SELECT distinct `balance` FROM `users` WHERE `user id` = %s" %(str(counters[message.chat.id]['idz'])) 
                        cursor.execute(qw)
                        ww[message.chat.id]['result'] = cursor.fetchall()
                        if len(ww[message.chat.id]['result']) != 0:
                            bot.send_message(message.chat.id, 'Отлично! Введите сумму вывода в 🍆:')
                            counters[message.chat.id]['cac'] = 0
                            counters[message.chat.id]['cjc'] = 1
                        else:
                            bot.send_message(message.chat.id, 'Такого юзера не существует!')

            if message.text == 'гривны' and counters[message.chat.id]['cac'] == 0:  
                bot.send_message(message.chat.id, 'id пользователя:') 
                counters[message.chat.id]['cac'] = 1
              
        if msg == 'начать чат' and message.chat.id == 653376416:
            
            message_to_users = message.text
            qw = "SELECT `nickname` FROM `personal`" 
            cursor.execute(qw)
            ww[message.chat.id]['result'] = cursor.fetchall()
            
            buttons = []
            
            key = types.InlineKeyboardMarkup()
            for i in ww[message.chat.id]['result']:
                buttons.append(types.InlineKeyboardButton(text = txt(i[0]), callback_data = i[0]))
                key.add(buttons[-1])
            bot.send_message(message.chat.id, 'Начать чат с:', reply_markup = key) 
            
        if users[message.chat.id]['chat'] != 0:
            bot.send_message(int(users[message.chat.id]['chat']), message.text)
              
        if counters[message.chat.id]['count'] == 1 and msg != 'отмена':
            message_to_users = message.text
            qw = "SELECT distinct `user id` FROM `users`" 
            cursor.execute(qw)
            ww[message.chat.id]['result'] = cursor.fetchall()
            for i in ww[message.chat.id]['result']:
                bot.send_message(i[0], message_to_users)
            bot.reply_to(message, 'Сообщение безвозвратно отправлено!')
            counters[message.chat.id]['count'] = 0

                
        if msg == 'рассылка' and message.chat.id == 653376416 or msg == 'рассылка' and message.chat.id == 684759645:
            bot.send_message(message.chat.id, "Введите сообщение которое будет отправленно всем пользователям бота:")
            counters[message.chat.id]['count'] = 1

        # пополнить счет🍆
        if msg == 'овощи' and message.chat.id == 653376416 or msg == 'овощи' and message.chat.id == 684759645 or msg == 'овощи' and message.chat.id == 562050144:
            counters[message.chat.id]['uou'] = 1
        if message.chat.id == 653376416 and counters[message.chat.id]['uou'] == 1 or message.chat.id == 684759645 and counters[message.chat.id]['uou'] == 1:

            if counters[message.chat.id]['czc'] == 1:
                grn = message.text
                if grn.isdigit() == False:
                    bot.send_message(message.chat.id, 'Сумма введена не корректно, повторите ввод:')
                if grn.isdigit() == True:
                    qw = "SELECT distinct `balance` FROM `users` WHERE `user id` = %s" %(counters[message.chat.id]['ids']) 
                    cursor.execute(qw)
                    ww[message.chat.id]['result'] = cursor.fetchall()
                    oldbal = ww[message.chat.id]['result'][0][0]
                    ovo = int(grn) * 5
                    wow = ovo
                    ovo = ovo + oldbal
                    if len(ww[message.chat.id]['result']) != 0:        
                        qw = """UPDATE `users` SET `balance` = %s WHERE `user id` = %s """ %(ovo, str(counters[message.chat.id]['ids']))   
                        cursor.execute(qw)
                        db.commit()
                        bot.send_message(message.chat.id, 'Счет пополнен на ' + str(wow) + '🍆!')
                        if message.chat.id != 65337641 or message.chat.id != 684759645:
                            bot.send_message(counters[message.chat.id]['ids'], 'Ваш счет пополнен на ' + str(wow) + '🍆, спасибо что вы с нами!')
                        oldbal = 0
                        ovo = 0
                        wow = 0
                        counters[message.chat.id]['czc'] = 0
                        counters[message.chat.id]['uou'] = 0
                        grn = 0
                    else:
                        bot.send_message(message.chat.id, 'Такого юзера не существует!')

            ms = message.text
            if counters[message.chat.id]['cec'] == 1:   
                if len(ms) != 9:
                    bot.send_message(message.chat.id, 'Не корректный id, повторите ввод:')
                if len(ms) == 9:
                    if ms.isdigit() == False:
                        bot.send_message(message.chat.id, 'id введен не корректно, повторите ввод:')
                    if ms.isdigit() == True:
                        counters[message.chat.id]['ids'] = message.text
                        qw = "SELECT distinct `balance` FROM `users` WHERE `user id` = %s" %(str(counters[message.chat.id]['ids'])) 
                        cursor.execute(qw)
                        ww[message.chat.id]['result'] = cursor.fetchall()
                        if len(ww[message.chat.id]['result']) != 0:
                            bot.send_message(message.chat.id, 'Отлично! Введите сумму пополнения в грн:')
                            counters[message.chat.id]['cec'] = 0
                            counters[message.chat.id]['czc'] = 1
                        else:
                            bot.send_message(message.chat.id, 'Такого юзера не существует!')


            if message.text == 'овощи' and counters[message.chat.id]['cec'] == 0:  
                bot.send_message(message.chat.id, 'id пользователя:') 
                counters[message.chat.id]['cec'] = 1

        if counters[message.chat.id]['f'] == 0 and users[message.chat.id]['subject'] in ["r", "z", "a", "g", "an", "f", "b", "y", "yk", "h", "ge", "v", "i", "fi", "in", "o", "p"]:

            price = message.text
            if counters[message.chat.id]['coc'] == 1:   
                price = message.text
                if len(str(price)) >= 5:
                    bot.send_message(message.chat.id, 'Я конечно все понимаю, но это уже перебор...')
                if price.isdigit() == False:
                    bot.send_message(message.chat.id, 'Цена введена не корректно, повторите ввод:')
                if price.isdigit() == True and len(str(price)) < 5 and int(price) >= 0:
                    price = message.text
                    users[message.chat.id]['price'] = str(price)
                    counters[message.chat.id]['coc'] = 0
                    counters[message.chat.id]['f'] = 1

            if counters[message.chat.id]['zwz'] == 1 and counters[message.chat.id]['coc'] == 0:  
                counters[message.chat.id]['zwz'] = 0
                counters[message.chat.id]['coc'] = 1

            if msg == 'готово' and users[message.chat.id]['class'] != '' and users[message.chat.id]['subject'] != '':
                key = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                key.row('отмена')
                bot.send_message(message.chat.id, "Отлично! Назначьте цену🍆:",reply_markup=key) 
                counters[message.chat.id]['coc'] = 1

        if msg == 'get id':
            bot.send_message(message.chat.id, message.chat.id)

    #    if msg == 'пополнить счет':
    #        bot.send_message(message.chat.id, "Для покупки овощей🍆 подходите в будни на большой перемене в 8 кабинет ( лично к Егору Котеневу ), |текущий курс: покупка - 0,55 ||| продажа - 0,5грн|, продажа от 10🍆!")

        if counters[message.chat.id]['csc'] == 0 and msg == 'добавить коментарий' and users[message.chat.id]['subject'] in ["r", "z", "a", "g", "an", "f", "b", "y", "yk", "h", "ge", "v", "i", "fi", "in", "o", "p"]: 
            key = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            key.row('готово', 'отмена')
            bot.send_message(message.chat.id, 'Следующее сообщение станет коментарием:',reply_markup=key) 
            counters[message.chat.id]['csc'] = 1

        if message.chat.id == 562050144 and msg == 'все' or message.chat.id == 684759645 and msg == 'все' or message.chat.id == 653376416 and msg == 'все':
            MESSAGE = '🔼все пользователи🔼'
            num = 1
            qw = "SELECT `nickname` FROM `personal` WHERE `nickname` <> '' ORDER BY `stars`, `N`"
            cursor.execute(qw)
            result = cursor.fetchall()
            result.reverse()
            for a in result:
                qw = "SELECT distinct `user id` FROM `personal` WHERE `nickname` = '%s'" %(a[0])
                cursor.execute(qw)
                resu = cursor.fetchall()
                qw = "SELECT distinct `balance` FROM `users` WHERE `nickname` = '%s'" %(a[0])
                cursor.execute(qw)
                re = cursor.fetchall()
                qw = "SELECT distinct `stars` FROM `personal` WHERE `nickname` = '%s'" %(a[0])
                cursor.execute(qw)
                r = cursor.fetchall()
                qw = "SELECT distinct `ban` FROM `personal` WHERE `nickname` = '%s'" %(a[0])
                cursor.execute(qw)
                resulttus = cursor.fetchall()
                qw = "SELECT distinct `rating` FROM `personal` WHERE `nickname` = '%s'" %(a[0])
                cursor.execute(qw)
                resul = cursor.fetchall()
                qw = "SELECT distinct `N` FROM `personal` WHERE `nickname` = '%s'" %(a[0])
                cursor.execute(qw)
                res = cursor.fetchall()
                if resulttus[0][0] == 1:
                    truefalse = '🚫'
                else:
                    truefalse = 'Волен'
                if res[0][0] != 0:
                    if str((resul[0][0]/res[0][0])-int(resul[0][0]/res[0][0]))[1:] == '.0':
                        MESSAGE = str(num) + ') ' + txt(str(a[0])) + ' (' + str(resu[0][0]) + ')' + '  -  баланс: ' + str(re[0][0]) + ' рейтинг:  ' + str(int(r[0][0])) + '⭐️,   оценок:  ' + str(int(res[0][0])) + ' Статус: ' + truefalse + '\n\n' + MESSAGE
                    else:
                        MESSAGE = str(num) + ') ' + txt(str(a[0])) + ' (' + str(resu[0][0]) + ')' + '  -  баланс: ' + str(re[0][0]) + ' рейтинг:  ' + str(round(r[0][0], 2)) + '⭐️,   оценок:  ' + str(int(res[0][0])) + ' Статус: ' + truefalse + '\n\n' + MESSAGE
                else:
                    MESSAGE = str(num) + ') ' + txt(str(a[0])) + ' (' + str(resu[0][0]) + ')' + '  -  баланс: ' + str(re[0][0]) + ' рейтинг:  ' + str(int(r[0][0])) + '⭐️,   оценок:  ' + str(int(res[0][0])) + ' Статус: ' + truefalse + '\n\n' + MESSAGE
                num += 1
            bot.reply_to(message, MESSAGE)
            num = 1

        if message.chat.id == 562050144 and msg == 'я':
            bot.send_message(message.chat.id, 'Егор Котенев, доверенное лицо, ответственный за покупку/продажу овощей.')
        if message.chat.id == 653376416 and msg == 'я':
            bot.send_message(message.chat.id, 'Дмитрий Сидюк, создатель.')
        if message.chat.id != 653376416 and message.chat.id != 562050144 and msg == 'я':
            qw = "SELECT `nickname` FROM `personal` WHERE `user id` = '%s'" %(str(message.chat.id))
            cursor.execute(qw)
            ww[message.chat.id]['result'] = cursor.fetchall() 
            if len(ww[message.chat.id]['result']) != 0:
                bot.send_message(message.chat.id, txt(ww[message.chat.id]['result'][0][0]) + ', мой id:\n' + str(message.chat.id))
            else:
                bot.send_message(message.chat.id, 'Зарегистрируйтесь!')

        if msg == 'пополнить счет':
            bot.send_message(message.chat.id, "Для покупки овощей🍆/гривен подойди в будни на большой перемене в 8 кабинет к Егору Котеневу, у него ты сможешь купить 🍆/грн. Все просто! Удачи!\n\nP.S. В скором будущем будет введен более удобный способ пополнения счета и купли/продажи в целом!")

        if msg == 'баланс':
            qw = "SELECT `balance` FROM `users` WHERE `user id` = '%s'" %(message.chat.id)
            cursor.execute(qw)
            ww[message.chat.id]['result'] = cursor.fetchall()  
            if ww[message.chat.id]['result'][0][0] == 0:
                bot.send_message(message.chat.id, 'У тебя 0🍆')
            else:
                bot.send_message(message.chat.id, "На вашем счету " + str(ww[message.chat.id]['result'][0][0]) + '🍆' )

        if counters[message.chat.id]['f'] == 1:
            key = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            key.row('опубликовать', 'отмена')
            bot.send_message(message.chat.id, "Вот ваше сообщение. Опубликовать?",reply_markup=key) 

            if users[message.chat.id]['class'] == "1":
                users[message.chat.id]['class_r'] = '7-Ф'
            if users[message.chat.id]['class'] == "2":
                users[message.chat.id]['class_r'] = "7-М"
            if users[message.chat.id]['class'] == "3":
                users[message.chat.id]['class_r'] = "7-ХБ"
            if users[message.chat.id]['class'] == "4":
                users[message.chat.id]['class_r'] = "8-Ф"
            if users[message.chat.id]['class'] == "5":
                users[message.chat.id]['class_r'] = "8-М"
            if users[message.chat.id]['class'] == "6":
                users[message.chat.id]['class_r'] = "8-ХБ"
            if users[message.chat.id]['class'] == "7":
                users[message.chat.id]['class_r'] = "9-Ф"
            if users[message.chat.id]['class'] == "8":
                users[message.chat.id]['class_r'] = "9-М"   
            if users[message.chat.id]['class'] == "9":
                users[message.chat.id]['class_r'] = "9-ХБ"  
            if users[message.chat.id]['class'] == "10":
                users[message.chat.id]['class_r'] = "10-Ф"
            if users[message.chat.id]['class'] == "11":
                users[message.chat.id]['class_r']= "10-М"
            if users[message.chat.id]['class'] == "12":
                users[message.chat.id]['class_r'] = "10-ХБ"
            if users[message.chat.id]['class'] == "13":
                users[message.chat.id]['class_r'] = "11-Ф"
            if users[message.chat.id]['class'] == "14":
                users[message.chat.id]['class_r'] = "11-М"
            if users[message.chat.id]['class'] == "15":
                users[message.chat.id]['class_r'] = "11-ХБ"


            if users[message.chat.id]['subject'] == "r":
                users[message.chat.id]['subject_r'] = 'Русский'
            if users[message.chat.id]['subject'] == "z":
                users[message.chat.id]['subject_r'] = "Зарубежка"
            if users[message.chat.id]['subject'] == "a":
                users[message.chat.id]['subject_r'] = "Алгебра"
            if users[message.chat.id]['subject'] == "g":
                users[message.chat.id]['subject_r'] = "Геометрия"
            if users[message.chat.id]['subject'] == "an":
                users[message.chat.id]['subject_r'] = "Английский"
            if users[message.chat.id]['subject'] == "f":
                users[message.chat.id]['subject_r'] = "Физика"
            if users[message.chat.id]['subject'] == "b":
                users[message.chat.id]['subject_r'] = "Биология"
            if users[message.chat.id]['subject'] == "y":
                users[message.chat.id]['subject_r'] = "Укр.яз"   
            if users[message.chat.id]['subject'] == "yk":
                users[message.chat.id]['subject_r'] = "Укр.лит"  
            if users[message.chat.id]['subject'] == "h":
                users[message.chat.id]['subject_r'] = "Химия"
            if users[message.chat.id]['subject'] == "ge":
                users[message.chat.id]['subject_r'] = "География"
            if users[message.chat.id]['subject'] == "v":
                users[message.chat.id]['subject_r'] = "Всемирная история"
            if users[message.chat.id]['subject'] == "i":
                users[message.chat.id]['subject_r'] = "История Украины"
            if users[message.chat.id]['subject'] == "fi":
                users[message.chat.id]['subject_r'] = "Физкультура"
            if users[message.chat.id]['subject'] == "in":
                users[message.chat.id]['subject_r'] = "Информатика"
            if users[message.chat.id]['subject'] == "o":
                users[message.chat.id]['subject_r'] = "Основы здоровья"
            if users[message.chat.id]['subject'] == "p":
                users[message.chat.id]['subject_r'] = "Полезная инфа"

            num = len(users[message.chat.id]['file'])

            if num%10 == 1:
                pic = 'картинка.'
            if num%10 in [2,3,4] :
                pic = 'картинки.'
            if num%10 in [5,6,7,8,9,0] :
                pic = 'картинок.'

            if users[message.chat.id]['note'] == '':
                bot.send_message(message.chat.id, "🔑Цена:   " + users[message.chat.id]['price'] +
                                 '🍆' + "\n🔥Предмет:   " + users[message.chat.id]['subject_r'] + 
                                 "\n🔝Класс:   " + users[message.chat.id]['class_r'] + 
                                 '\n📅Дата:  ' + users[message.chat.id]['date'].strftime('%Y-%m-%d')+ 
                                 '\n🕑Время:   ' + users[message.chat.id]['date'].strftime('%H : %M')+ 
                                 '\n+ ' + str(len(users[message.chat.id]['file'])) + ' ' + pic)
                counters[message.chat.id]['f'] = 0
            else:
                bot.send_message(message.chat.id, "🔑Цена:   " + users[message.chat.id]['price'] + 
                                 '🍆' + "\n🔥Предмет:   " + users[message.chat.id]['subject_r'] + 
                                 "\n🔝Класс:   " + users[message.chat.id]['class_r'] + 
                                 '\n📅Дата:  ' + users[message.chat.id]['date'].strftime('%Y-%m-%d')+ 
                                 '\n🕑Время:   ' + users[message.chat.id]['date'].strftime('%H : %M')+ 
                                 '\n+ ' + str(len(users[message.chat.id]['file'])) + ' ' + pic +
                                 '\nP.S. ' + users[message.chat.id]['note']) 
                counters[message.chat.id]['f'] = 0



        if msg == 'опубликовать' and users[message.chat.id]['class'] != '' and users[message.chat.id]['subject'] != '' and users[message.chat.id]['file'] != '':
            qw = """INSERT INTO `test`.`users` (`id`, `user id`, `subject`, `class`, `date`, `note`, `file_path`, `balance`, `price`, `nickname`) VALUES( NULL, '%s', '%s', '%s', '%s', '%s', '%s', %d, '%s', '%s')"""%(message.chat.id,  users[message.chat.id]['subject'],users[message.chat.id]['class'], users[message.chat.id]['date'].strftime('%Y-%m-%d-%H-%M'),code(users[message.chat.id]['note']),"\n".join(users[message.chat.id]['file']),0,users[message.chat.id]['price'], '')
            cursor.execute(qw)
            db.commit()
            counters[message.chat.id]['bd'] = 1
            qw = "SELECT `balance` FROM `users` WHERE `user id` = %s" %(message.chat.id) 
            cursor.execute(qw)
            ww[message.chat.id]['result'] = cursor.fetchall()
            ol = ww[message.chat.id]['result'][0][0]
            qw = """UPDATE `users` SET `balance` = %s WHERE `user id` = %s """ %(str(ol), message.chat.id)   
            cursor.execute(qw)
            db.commit()

            users[message.chat.id] = {'chat': 0, 'free': 0, 'ban': 0, 'subject_r': '', 'class_r':'', 'c.data': 0, 'nicou': 0, 'subject': '', 'class': '', 'date': '', 'note': '', 'file': [], 'price': '', 'nickname': users[message.chat.id]['nickname'], 'noname': 0}

            if users[message.chat.id]['noname'] == 1:
                key = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                key.row("продать", "купить")
                key.row("пополнить счет", "регистрация", "баланс")
                bot.send_message(message.chat.id, 'Отлично! Объявление подано!',reply_markup=key)
            if users[message.chat.id]['noname'] == 0:
                key = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                key.row("продать", "купить")
                key.row("пополнить счет", "баланс")
                bot.send_message(message.chat.id, 'Отлично! Объявление подано!',reply_markup=key)
            counters[message.chat.id]['f'] = 0

        #if msg == 'иилрмлРПАНЕАОПМ732еу6авыпфмрПМНЕФНП876е634н5467**/*4646466РРПЯЫПливрп874н3ащлывсъ\ылсыотсцшыычkjvndksbvdbosajaaskjag7678343284230-89=@$#!#@#%&%*&^(*)_+)_*(&^%$#%^&*()_OKJHBVCFR^T&U':

        #    global pin

        if msg == 'купить':

            qw = "SELECT distinct `user id` FROM `users` "
            cursor.execute(qw)
            result = cursor.fetchall()
            for i in result:
                chat_id = int(i[0])
                qw = "SELECT distinct `nickname` FROM `users` WHERE `user id` = %s and `nickname` <> ''" %(chat_id)
                cursor.execute(qw)
                r = cursor.fetchall()
                for a in r:
                    users[chat_id] = {'chat': 0, 'free': 0, 'ban': 0, 'subject_r': '', 'class_r':'', 'c.data': 0, 'nickname': a[0], 'nicou': 0, 'subject': '', 'class': '', 'date': '', 'note': '', 'file': [], 'price': 0, 'noname': ''}
                    buy_users[chat_id] = {'buy_subject': '', 'buy_class': '', 'buy_data': '', 'buynum': '', 'buy_file': []}
                    counters[chat_id] = {'count_3': 0, 'cou': 0, 'count_2': 0, 'count': 0, 'call': '', 'ids': '', 'idz': '', 'csc': 0, 'bd': 0, 'buy_data': 0, 'uou': 0, 'uqu': 0, 'f': 0, 'zwz': 0, 'coc': 0, 'cec': 0,'cac': 0, 'czc': 0, 'cjc': 0}
                    ww[chat_id] = {'result': '', 'row': '', 'b': 0, 'assessment': '', 'cou': 1, 'N': 0, 'rating': 0.0}

            qw = "SELECT distinct `nickname` FROM `users` WHERE `user id` = %s and `nickname` <> ''" %(message.chat.id)
            cursor.execute(qw)
            result = cursor.fetchall()
            result = txt(result)

            if len(result) != 0:
                users[message.chat.id] = {'chat': 0, 'free': 0, 'ban': 0, 'subject_r': '', 'class_r':'', 'c.data': 0, 'nickname': result[0], 'nicou': 0, 'subject': '', 'class': '', 'date': '', 'note': '', 'file': [], 'price': 0, 'noname': ''}
                buy_users[message.chat.id] = {'buy_subject': '', 'buy_class': '', 'buy_data': '', 'buynum': '', 'buy_file': []}
                counters[message.chat.id] = {'count_3': 0, 'cou': 0, 'count_2': 0, 'count': 0, 'call': '', 'ids': '', 'idz': '', 'csc': 0, 'bd': 0, 'buy_data': 0, 'uou': 0, 'uqu': 0, 'f': 0, 'zwz': 0, 'coc': 0, 'cec': 0,'cac': 0, 'czc': 0, 'cjc': 0}
                ww[message.chat.id] = {'result': '', 'row': '', 'b': 0, 'assessment': '', 'cou': 1, 'N': 0, 'rating': 0.0}
            else:
                users[message.chat.id] = {'chat': 0, 'free': 0, 'ban': 0, 'subject_r': '', 'class_r':'', 'c.data': 0, 'nickname': '', 'nicou': 0, 'subject': '', 'class': '', 'date': '', 'note': '', 'file': [], 'price': 0, 'noname': ''}
                buy_users[message.chat.id] = {'buy_subject': '', 'buy_class': '', 'buy_data': '', 'buynum': '', 'buy_file': []}
                counters[message.chat.id] = {'count_3': 0, 'cou': 0, 'count_2': 0, 'count': 0, 'call': '', 'ids': '', 'idz': '', 'csc': 0, 'bd': 0, 'buy_data': 0, 'uou': 0, 'uqu': 0, 'f': 0, 'zwz': 0, 'coc': 0, 'cec': 0,'cac': 0, 'czc': 0, 'cjc': 0}
                ww[message.chat.id] = {'result': '', 'row': '', 'b': 0, 'assessment': '', 'cou': 1, 'N': 0, 'rating': 0.0}

            ky = types.InlineKeyboardMarkup()
            bt_1 = types.InlineKeyboardButton(text="7-Ф",callback_data="16")
            bt_2 = types.InlineKeyboardButton(text="7-М",callback_data="17")
            bt_3 = types.InlineKeyboardButton(text="7-ХБ",callback_data="18")
            bt_4 = types.InlineKeyboardButton(text="8-Ф",callback_data="19")
            bt_5 = types.InlineKeyboardButton(text="8-М",callback_data="20")
            bt_6 = types.InlineKeyboardButton(text="8-ХБ",callback_data="21")
            bt_7 = types.InlineKeyboardButton(text="9-Ф",callback_data="22")
            bt_8 = types.InlineKeyboardButton(text="9-М",callback_data="23")
            bt_9 = types.InlineKeyboardButton(text="9-ХБ",callback_data="24")
            bt_10 = types.InlineKeyboardButton(text="10-Ф",callback_data="25")
            bt_11 = types.InlineKeyboardButton(text="10-М",callback_data="26")
            bt_12 = types.InlineKeyboardButton(text="10-ХБ",callback_data="27")
            bt_13 = types.InlineKeyboardButton(text="11-Ф",callback_data="28")
            bt_14 = types.InlineKeyboardButton(text="11-М",callback_data="29")
            bt_15 = types.InlineKeyboardButton(text="11-ХБ",callback_data="30")
            ky.add(bt_1, bt_2, bt_3, bt_4, bt_5, bt_6, bt_7, bt_8, bt_9, bt_10, bt_11, bt_12, bt_13, bt_14, bt_15)
            bot.send_message(message.chat.id, "Выберите ваш класс:", reply_markup=ky) 

            key = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            key.row('отмена') 
            bot.send_message(message.chat.id, "Вы всегда можете отменить действие.",reply_markup=key)
        if msg == 'продать':
            azaza = 0
            if type(users[message.chat.id]['nickname']) != tuple:
                if len(users[message.chat.id]['nickname']) != 0:
                    azaza = 1
            if type(users[message.chat.id]['nickname']) == tuple:
                if len(users[message.chat.id]['nickname'][0]) != 0:
                    azaza = 1

            if azaza == 1:
                counters[message.chat.id]['buy_data'] = 0
                ky = types.InlineKeyboardMarkup()
                bt_1 = types.InlineKeyboardButton(text="7-Ф",callback_data="1")
                bt_2 = types.InlineKeyboardButton(text="7-М",callback_data="2")
                bt_3 = types.InlineKeyboardButton(text="7-ХБ",callback_data="3")
                bt_4 = types.InlineKeyboardButton(text="8-Ф",callback_data="4")
                bt_5 = types.InlineKeyboardButton(text="8-М",callback_data="5")
                bt_6 = types.InlineKeyboardButton(text="8-ХБ",callback_data="6")
                bt_7 = types.InlineKeyboardButton(text="9-Ф",callback_data="7")
                bt_8 = types.InlineKeyboardButton(text="9-М",callback_data="8")
                bt_9 = types.InlineKeyboardButton(text="9-ХБ",callback_data="9")
                bt_10 = types.InlineKeyboardButton(text="10-Ф",callback_data="10")
                bt_11 = types.InlineKeyboardButton(text="10-М",callback_data="11")
                bt_12 = types.InlineKeyboardButton(text="10-ХБ",callback_data="12")
                bt_13 = types.InlineKeyboardButton(text="11-Ф",callback_data="13")
                bt_14 = types.InlineKeyboardButton(text="11-М",callback_data="14")
                bt_15 = types.InlineKeyboardButton(text="11-ХБ",callback_data="15")
                ky.add(bt_1, bt_2, bt_3, bt_4, bt_5, bt_6, bt_7, bt_8, bt_9, bt_10, bt_11, bt_12, bt_13, bt_14, bt_15)
                bot.send_message(message.chat.id, "Выберите ваш класс:", reply_markup=ky) 

                key = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                key.row('отмена')
                bot.send_message(message.chat.id, "Вы всегда можете отменить действие.",reply_markup=key)
            if azaza == 0:
                key = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                key.row("продать", "купить")
                key.row("пополнить счет", "регистрация", "баланс")
                bot.send_message(message.chat.id, 'Чтобы продавать нужно зарегистрироваться!',reply_markup=key)
    else:
        bot.send_photo(message.chat.id, open('D:\Дима\Програмирование\Python\BOT\Фото\Angrybot.jpg', 'rb'))
        bot.send_message(message.chat.id, 'Вы забанены! По всем вопросам —> @RL_support_Bot')
        
@bot.callback_query_handler(func=lambda c:True)
def inline(c):
    global count_er
    global io
    if c.message.chat.id not in users.keys() or c.message.chat.id not in buy_users.keys() or c.message.chat.id not in ww.keys() or c.message.chat.id not in counters.keys():
        
        qw = "SELECT distinct `nickname` FROM `users` WHERE `user id` = %s and `nickname` <> ''" %(c.message.chat.id)
        cursor.execute(qw)
        result = cursor.fetchall()
        result = txt(result)
        
        if len(result) != 0:
            users[c.message.chat.id] = {'chat': 0, 'free': 0, 'ban': 0, 'subject_r': '', 'class_r':'', 'c.data': 0, 'nickname': result[0], 'nicou': 0, 'subject': '', 'class': '', 'date': '', 'note': '', 'file': [], 'price': 0, 'noname': ''}
            buy_users[c.message.chat.id] = {'buy_class_r': '', 'buy_subject': '', 'buy_class': '', 'buy_data': '', 'buynum': '', 'buy_file': []}
            counters[c.message.chat.id] = {'count_3': 0, 'cou': 0, 'count_2': 0, 'count': 0, 'call': '', 'ids': '', 'idz': '', 'csc': 0, 'bd': 0, 'buy_data': 0, 'uou': 0, 'uqu': 0, 'f': 0, 'zwz': 0, 'coc': 0, 'cec': 0,'cac': 0, 'czc': 0, 'cjc': 0}
            ww[c.message.chat.id] = {'result': '', 'row': '', 'b': 0, 'assessment': '', 'cou': 1, 'N': 0, 'rating': 0.0}
        else:
            users[c.message.chat.id] = {'chat': 0, 'free': 0, 'ban': 0, 'subject_r': '', 'class_r': '','c.data': 0, 'nickname': '', 'nicou': 0, 'subject': '', 'class': '', 'date': '', 'note': '', 'file': [], 'price': 0, 'noname': ''}
            buy_users[c.message.chat.id] = {'buy_class_r': '','buy_subject': '', 'buy_class': '', 'buy_data': '', 'buynum': '', 'buy_file': []}
            counters[c.message.chat.id] = {'count_3': 0, 'cou': 0, 'count_2': 0, 'count': 0, 'call': '', 'ids': '', 'idz': '', 'csc': 0, 'bd': 0, 'buy_data': 0, 'uou': 0, 'uqu': 0, 'f': 0, 'zwz': 0, 'coc': 0, 'cec': 0,'cac': 0, 'czc': 0, 'cjc': 0}
            ww[c.message.chat.id] = {'result': '', 'row': '', 'b': 0, 'assessment': '', 'cou': 1, 'N': 0, 'rating': 0.0}
    users[c.message.chat.id]['c.data'] = c.data
    
    qw = "SELECT `ban` FROM `personal` WHERE `user id` = %s" %(str(c.message.chat.id)) 
    cursor.execute(qw)
    result = cursor.fetchall()
    nore = 0
    if len(result) == 0:
        nore = 1
    if nore == 0 and result[0][0] == 0 or nore == 1:
    
        qw = "SELECT distinct `user id` FROM `personal`"
        cursor.execute(qw)
        ww[c.message.chat.id]['assessment'] = cursor.fetchall()
        for i in ww[c.message.chat.id]['assessment']:
            if i[0] in users[c.message.chat.id]['c.data']:
                if ww[c.message.chat.id]['cou'] == 0:
                    if users[c.message.chat.id]['c.data'] == '1⭐️' + i[0]:
                        ww[c.message.chat.id]['rating'] = 1.0
                        qw = "SELECT distinct `rating` FROM `personal` WHERE `user id` = %s" %(i[0])
                        cursor.execute(qw)
                        rat = cursor.fetchall()

                        qw = """UPDATE `personal` SET `rating` = %d  WHERE `user id` = %s """ %(ww[c.message.chat.id]['rating'] + rat[0][0], i[0])
                        cursor.execute(qw)
                        db.commit()

                        qw = """UPDATE `personal` SET `N` = `N` + 1 WHERE `user id` = %s """ %(i[0])
                        cursor.execute(qw)
                        db.commit()
                        bot.send_message(c.message.chat.id, "Спасибо, учтено.")
                        ww[c.message.chat.id]['cou'] = 1

                        qw = "SELECT distinct `N` FROM `personal` WHERE `user id` = %s" %(i[0])
                        cursor.execute(qw)
                        ww[c.message.chat.id]['N'] = cursor.fetchall()

                        qw = """UPDATE `personal` SET `stars` = %s WHERE `user id` = %s """ %((ww[c.message.chat.id]['rating'] + rat[0][0])/ww[c.message.chat.id]['N'][0][0], i[0])
                        cursor.execute(qw)
                        db.commit()

                    if users[c.message.chat.id]['c.data'] == '2⭐️' + i[0]:
                        ww[c.message.chat.id]['rating'] = 2.0
                        qw = "SELECT distinct `rating` FROM `personal` WHERE `user id` = %s" %(i[0])
                        cursor.execute(qw)
                        rat = cursor.fetchall()

                        qw = """UPDATE `personal` SET `rating` = %d  WHERE `user id` = %s """ %(ww[c.message.chat.id]['rating'] + rat[0][0], i[0])
                        cursor.execute(qw)
                        db.commit()

                        qw = """UPDATE `personal` SET `N` = `N` + 1 WHERE `user id` = %s """ %(i[0])
                        cursor.execute(qw)
                        db.commit()
                        bot.send_message(c.message.chat.id, "Спасибо, учтено.")
                        ww[c.message.chat.id]['cou'] = 1

                        qw = "SELECT distinct `N` FROM `personal` WHERE `user id` = %s" %(i[0])
                        cursor.execute(qw)
                        ww[c.message.chat.id]['N'] = cursor.fetchall()

                        qw = """UPDATE `personal` SET `stars` = %s WHERE `user id` = %s """ %((ww[c.message.chat.id]['rating'] + rat[0][0])/ww[c.message.chat.id]['N'][0][0], i[0])
                        cursor.execute(qw)
                        db.commit()

                    if users[c.message.chat.id]['c.data'] == '3⭐️' + i[0]:
                        ww[c.message.chat.id]['rating'] = 3.0
                        qw = "SELECT distinct `rating` FROM `personal` WHERE `user id` = %s" %(i[0])
                        cursor.execute(qw)
                        rat = cursor.fetchall()

                        qw = """UPDATE `personal` SET `rating` = %d  WHERE `user id` = %s """ %(ww[c.message.chat.id]['rating'] + rat[0][0], i[0])
                        cursor.execute(qw)
                        db.commit()

                        qw = """UPDATE `personal` SET `N` = `N` + 1 WHERE `user id` = %s """ %(i[0])
                        cursor.execute(qw)
                        db.commit()
                        bot.send_message(c.message.chat.id, "Спасибо, учтено.")
                        ww[c.message.chat.id]['cou'] = 1

                        qw = "SELECT distinct `N` FROM `personal` WHERE `user id` = %s" %(i[0])
                        cursor.execute(qw)
                        ww[c.message.chat.id]['N'] = cursor.fetchall()

                        qw = """UPDATE `personal` SET `stars` = %s WHERE `user id` = %s """ %((ww[c.message.chat.id]['rating'] + rat[0][0])/ww[c.message.chat.id]['N'][0][0], i[0])
                        cursor.execute(qw)
                        db.commit()

                    if users[c.message.chat.id]['c.data'] == '4⭐️' + i[0]:
                        ww[c.message.chat.id]['rating'] = 4.0

                        qw = "SELECT distinct `rating` FROM `personal` WHERE `user id` = %s" %(i[0])
                        cursor.execute(qw)
                        rat = cursor.fetchall()

                        qw = """UPDATE `personal` SET `rating` = %d  WHERE `user id` = %s """ %(ww[c.message.chat.id]['rating'] + rat[0][0], i[0])
                        cursor.execute(qw)
                        db.commit()

                        qw = """UPDATE `personal` SET `N` = `N` + 1 WHERE `user id` = %s """ %(i[0])
                        cursor.execute(qw)
                        db.commit()
                        bot.send_message(c.message.chat.id, "Спасибо, учтено.")
                        ww[c.message.chat.id]['cou'] = 1

                        qw = "SELECT distinct `N` FROM `personal` WHERE `user id` = %s" %(i[0])
                        cursor.execute(qw)
                        ww[c.message.chat.id]['N'] = cursor.fetchall()  

                        qw = """UPDATE `personal` SET `stars` = %s WHERE `user id` = %s """ %((ww[c.message.chat.id]['rating'] + rat[0][0])/ww[c.message.chat.id]['N'][0][0], i[0])
                        cursor.execute(qw)
                        db.commit()

                    if users[c.message.chat.id]['c.data'] == '5⭐️' + i[0]:
                        ww[c.message.chat.id]['rating'] = 5.0

                        qw = "SELECT distinct `rating` FROM `personal` WHERE `user id` = %s" %(i[0])
                        cursor.execute(qw)
                        rat = cursor.fetchall()

                        qw = """UPDATE `personal` SET `rating` = %d  WHERE `user id` = %s """ %(ww[c.message.chat.id]['rating'] + rat[0][0], i[0])
                        cursor.execute(qw)
                        db.commit()

                        qw = """UPDATE `personal` SET `N` = `N` + 1 WHERE `user id` = %s """ %(i[0])
                        cursor.execute(qw)
                        db.commit()
                        bot.send_message(c.message.chat.id, "Спасибо, учтено.")
                        ww[c.message.chat.id]['cou'] = 1

                        qw = "SELECT distinct `N` FROM `personal` WHERE `user id` = %s" %(i[0])
                        cursor.execute(qw)
                        ww[c.message.chat.id]['N'] = cursor.fetchall()

                        qw = """UPDATE `personal` SET `stars` = %s WHERE `user id` = %s """ %((ww[c.message.chat.id]['rating'] + rat[0][0])/ww[c.message.chat.id]['N'][0][0], i[0])
                        cursor.execute(qw)
                        db.commit()
                    ww[c.message.chat.id]['cou'] = 1
                else:
                    bot.send_message(c.message.chat.id, "Ваша оценка уже учтена!")


        if len(str(users[c.message.chat.id]['nickname'])) == 0:
            users[c.message.chat.id]['noname'] = 1
        else:
            users[c.message.chat.id]['noname'] = 0

        if 'buy_button' in users[c.message.chat.id]['c.data']: 
            ww[c.message.chat.id]['idx'] = users[c.message.chat.id]['c.data']
            ww[c.message.chat.id]['idx'] = ww[c.message.chat.id]['idx'].replace('buy_button', '')
            qw = "SELECT `balance` FROM `users` WHERE `user id` = '%s'" %(c.message.chat.id)
            cursor.execute(qw)
            ww[c.message.chat.id]['price0'] = cursor.fetchall()  
            ww[c.message.chat.id]['price1'] = ww[c.message.chat.id]['price0'][0][0]
            qw = "SELECT * FROM `users` WHERE `id` = '%d' and `subject` = '%s' and `class` = '%s'" %(int(ww[c.message.chat.id]['idx']), buy_users[c.message.chat.id]['buy_subject'], buy_users[c.message.chat.id]['buy_class']) 
            cursor.execute(qw)
            ww[c.message.chat.id]['result'] = cursor.fetchall()
            ww[c.message.chat.id]['result'].reverse()
            for ww[c.message.chat.id]['row'] in ww[c.message.chat.id]['result']:
                if int(ww[c.message.chat.id]['price1']) >= ww[c.message.chat.id]['row'][8]:
                    ww[c.message.chat.id]['delta'] = int(ww[c.message.chat.id]['price1']) - ww[c.message.chat.id]['row'][8]
                else:
                    ww[c.message.chat.id]['delta'] = 0
                num = len(ww[c.message.chat.id]['row'][6].split('\n'))

                if num%10 == 1 :
                    pic = 'картинку.'
                if num%10 in [2,3,4] :
                    pic = 'картинки.'
                if num%10 in [5,6,7,8,9,0] :
                    pic = 'картинок.'
                    
                qw = "SELECT `super` FROM `personal` WHERE `user id` = '%s'" %(c.message.chat.id)
                cursor.execute(qw)
                ww[c.message.chat.id]['result'] = cursor.fetchall()
                resin = ww[c.message.chat.id]['result']
                if int(ww[c.message.chat.id]['price1']) >= int(ww[c.message.chat.id]['row'][8]) or ww[c.message.chat.id]['result'][0][0] == 1:
                    qw = "SELECT `user id` FROM `users` WHERE `id` = '%d' and `subject` = '%s' and `class` = '%s'" %(int(ww[c.message.chat.id]['idx']), buy_users[c.message.chat.id]['buy_subject'], buy_users[c.message.chat.id]['buy_class']) 
                    cursor.execute(qw)
                    ww[c.message.chat.id]['result'] = cursor.fetchall()
                    ww[c.message.chat.id]['result'].reverse()
                    ww[c.message.chat.id]['mid'] = ww[c.message.chat.id]['result'][0][0]

                    qv = "SELECT `user id` FROM `users` WHERE `id` = '%d' and `subject` = '%s' and `class` = '%s'" %(int(ww[c.message.chat.id]['row'][0]), buy_users[c.message.chat.id]['buy_subject'], buy_users[c.message.chat.id]['buy_class']) 
                    cursor.execute(qw)
                    ww[c.message.chat.id]['result'] = cursor.fetchall()
                    ww[c.message.chat.id]['result'].reverse()
                    ww[c.message.chat.id]['mad'] = ww[c.message.chat.id]['result'][0][0]

                    pric = ww[c.message.chat.id]['row'][8]
                    qw = """UPDATE `users` SET `balance` = %d WHERE `user id` = %d """ %(ww[c.message.chat.id]['delta'], c.message.chat.id)
                    cursor.execute(qw)
                    db.commit()

                    if ww[c.message.chat.id]['row'][2] == "r":
                        users[c.message.chat.id]['subject_r'] = 'Русский'
                    if ww[c.message.chat.id]['row'][2] == "z":
                        users[c.message.chat.id]['subject_r'] = "Зарубежка"
                    if ww[c.message.chat.id]['row'][2] == "a":
                        users[c.message.chat.id]['subject_r'] = "Алгебра"
                    if ww[c.message.chat.id]['row'][2] == "g":
                        users[c.message.chat.id]['subject_r'] = "Геометрия"
                    if ww[c.message.chat.id]['row'][2] == "an":
                        users[c.message.chat.id]['subject_r'] = "Английский"
                    if ww[c.message.chat.id]['row'][2] == "f":
                        users[c.message.chat.id]['subject_r'] = "Физика"
                    if ww[c.message.chat.id]['row'][2] == "b":
                        users[c.message.chat.id]['subject_r'] = "Биология"
                    if ww[c.message.chat.id]['row'][2] == "y":
                        users[c.message.chat.id]['subject_r'] = "Укр.яз"   
                    if ww[c.message.chat.id]['row'][2] == "yk":
                        users[c.message.chat.id]['subject_r'] = "Укр.лит"  
                    if ww[c.message.chat.id]['row'][2] == "h":
                        users[c.message.chat.id]['subject_r'] = "Химия"
                    if ww[c.message.chat.id]['row'][2] == "ge":
                        users[c.message.chat.id]['subject_r'] = "География"
                    if ww[c.message.chat.id]['row'][2] == "v":
                        users[c.message.chat.id]['subject_r'] = "Всемирная история"
                    if ww[c.message.chat.id]['row'][2] == "i":
                        users[c.message.chat.id]['subject_r'] = "История Украины"
                    if ww[c.message.chat.id]['row'][2] == "fi":
                        users[c.message.chat.id]['subject_r'] = "Физкультура"
                    if ww[c.message.chat.id]['row'][2] == "in":
                        users[c.message.chat.id]['subject_r'] = "Информатика"
                    if ww[c.message.chat.id]['row'][2] == "o":
                        users[c.message.chat.id]['subject_r'] = "Основы здоровья"
                    if ww[c.message.chat.id]['row'][2] == "p":
                        users[c.message.chat.id]['subject_r'] = "Полезная инфа"

                    if ww[c.message.chat.id]['row'][3] == "1":
                        users[c.message.chat.id]['class_r'] = '7-Ф'
                    if ww[c.message.chat.id]['row'][3] == "2":
                        users[c.message.chat.id]['class_r'] = "7-М"
                    if ww[c.message.chat.id]['row'][3] == "3":
                        users[c.message.chat.id]['class_r'] = "7-ХБ"
                    if ww[c.message.chat.id]['row'][3] == "4":
                        users[c.message.chat.id]['class_r'] = "8-Ф"
                    if ww[c.message.chat.id]['row'][3] == "5":
                        users[c.message.chat.id]['class_r'] = "8-М"
                    if ww[c.message.chat.id]['row'][3] == "6":
                        users[c.message.chat.id]['class_r'] = "8-ХБ"
                    if ww[c.message.chat.id]['row'][3] == "7":
                        users[c.message.chat.id]['class_r'] = "9-Ф"
                    if ww[c.message.chat.id]['row'][3] == "8":
                        users[c.message.chat.id]['class_r'] = "9-М"   
                    if ww[c.message.chat.id]['row'][3] == "9":
                        users[c.message.chat.id]['class_r'] = "9-ХБ"  
                    if ww[c.message.chat.id]['row'][3] == "10":
                        users[c.message.chat.id]['class_r'] = "10-Ф"
                    if ww[c.message.chat.id]['row'][3] == "11":
                        users[c.message.chat.id]['class_r']= "10-М"
                    if ww[c.message.chat.id]['row'][3] == "12":
                        users[c.message.chat.id]['class_r'] = "10-ХБ"
                    if ww[c.message.chat.id]['row'][3] == "13":
                        users[c.message.chat.id]['class_r'] = "11-Ф"
                    if ww[c.message.chat.id]['row'][3] == "14":
                        users[c.message.chat.id]['class_r'] = "11-М"
                    if ww[c.message.chat.id]['row'][3] == "15":
                        users[c.message.chat.id]['class_r'] = "11-ХБ"

                    q = "SELECT distinct `nickname` FROM `users` WHERE `user id` = %s and `nickname` <> ''" %(ww[c.message.chat.id]['mad'])
                    cursor.execute(q)
                    ww[c.message.chat.id]['rabotay'] = cursor.fetchall()

                    if ww[c.message.chat.id]['row'][5] == '':
                        bot.send_message(c.message.chat.id, "Вы купили:" +   
                                     "\n\n🔑Цена:   " + str(ww[c.message.chat.id]['row'][8]) + '🍆' +
                                     "\n🔥Предмет:   " + users[c.message.chat.id]['subject_r'] + 
                                     "\n🔝Класс:   " +  users[c.message.chat.id]['class_r'] + 
                                     '\n📅Дата:  ' + ww[c.message.chat.id]['row'][4].strftime('%Y-%m-%d') + 
                                     '\n🕑Время:   ' + ww[c.message.chat.id]['row'][4].strftime('%H : %M') + 
                                     '\n+ ' + str(num) + ' ' + pic +
                                     '\nПродавец: ' + str(txt(ww[c.message.chat.id]['rabotay'])))
                        for ph in ww[c.message.chat.id]['row'][6].split('\n'):
                            bot.send_photo(c.message.chat.id, open(ph, 'rb'))
                        
                        
                        qw = "SELECT `super` FROM `personal` WHERE `user id` = '%s'" %(c.message.chat.id)
                        cursor.execute(qw)
                        ww[c.message.chat.id]['result'] = cursor.fetchall()
                        if ww[c.message.chat.id]['result'][0][0] == 0: 
                            qw = "SELECT distinct `balance` FROM `users` WHERE `user id` = %s" %(str(ww[c.message.chat.id]['result'][0][0])) 
                            cursor.execute(qw)
                            ww[c.message.chat.id]['result'] = cursor.fetchall()
                            if len(ww[c.message.chat.id]['result']) != 0:
                                ww[c.message.chat.id]['oldbal'] = ww[c.message.chat.id]['result'][0][0]
                            else:
                                ww[c.message.chat.id]['oldbal'] = 0
                            ww[c.message.chat.id]['new_balance'] = int(ww[c.message.chat.id]['oldbal']) + pric

                            qw = """UPDATE `users` SET `balance` = %s WHERE `user id` = %s """ %(str(ww[c.message.chat.id]['new_balance']), str(ww[c.message.chat.id]['mid']))   
                            cursor.execute(qw)
                            db.commit()
                            if str(c.message.chat.id) != ww[c.message.chat.id]['mid']:
                                bot.send_message(ww[c.message.chat.id]['mid'], "Пришел зароботок с продаж: " + str(pric) + "🍆")
                                if int(ww[c.message.chat.id]['row'][8]) >= 2:
                                    key = types.InlineKeyboardMarkup()
                                    button1 = types.InlineKeyboardButton(text="⭐️",callback_data = "1⭐️" + str(ww[c.message.chat.id]['mid']))
                                    button2 = types.InlineKeyboardButton(text="⭐️⭐️",callback_data = "2⭐️" + str(ww[c.message.chat.id]['mid']))
                                    button3 = types.InlineKeyboardButton(text="⭐️⭐️⭐️",callback_data = "3⭐️" + str(ww[c.message.chat.id]['mid']))
                                    button4 = types.InlineKeyboardButton(text="⭐️⭐️⭐️⭐️",callback_data = "4⭐️" + str(ww[c.message.chat.id]['mid']))
                                    button5 = types.InlineKeyboardButton(text="⭐️⭐️⭐️⭐️⭐️",callback_data = "5⭐️" + str(ww[c.message.chat.id]['mid']))
                                    key.add(button1, button2, button3)
                                    key.add(button4, button5)
                                    bot.send_message(c.message.chat.id, "На вашем счету " + str(ww[c.message.chat.id]['delta']) + '🍆' + "\n\nОцените пожалуйста товар:", reply_markup=key)
                                else:
                                    bot.send_message(c.message.chat.id, "На вашем счету " + str(ww[c.message.chat.id]['delta']) + '🍆')
                            else:
                                bot.send_message(c.message.chat.id, "Зачем покупать у себя же?")
                        else:
                            bot.send_message(c.message.chat.id, "Покупка успешно совершина!")
                        ww[c.message.chat.id]['cou'] = 0
                    else:
                        bot.send_message(c.message.chat.id, "Вы купили:" +
                                     "\n\n🔑Цена:   " + str(ww[c.message.chat.id]['row'][8]) + '🍆' +
                                     "\n🔥Предмет:   " + users[c.message.chat.id]['subject_r'] + 
                                     "\n🔝Класс:   " +  users[c.message.chat.id]['class_r'] + 
                                     '\n📅Дата:  ' + ww[c.message.chat.id]['row'][4].strftime('%Y-%m-%d') + 
                                     '\n🕑Время:   ' + ww[c.message.chat.id]['row'][4].strftime('%H : %M') + 
                                     '\n+ ' + str(num) + ' ' + pic + 
                                     '\nP.S. ' + txt(ww[c.message.chat.id]['row'][5]) +
                                     '\nПродавец: ' + str(txt(ww[c.message.chat.id]['rabotay'])))
                        for ph in ww[c.message.chat.id]['row'][6].split('\n'):
                            bot.send_photo(c.message.chat.id, open(ph, 'rb'))
                        qw = "SELECT `super` FROM `personal` WHERE `user id` = '%s'" %(c.message.chat.id)
                        cursor.execute(qw)
                        ww[c.message.chat.id]['result'] = cursor.fetchall()
                        if ww[c.message.chat.id]['result'][0][0] == 0: 
                            qw = "SELECT `balance` FROM `users` WHERE `user id` = %s" %(str(ww[c.message.chat.id]['result'][0][0])) 
                            cursor.execute(qw)
                            ww[c.message.chat.id]['result'] = cursor.fetchall()
                            if len(ww[c.message.chat.id]['result']) != 0:
                                ww[c.message.chat.id]['oldbal'] = ww[c.message.chat.id]['result'][0][0]
                            else:
                                ww[c.message.chat.id]['oldbal'] = 0
                            ww[c.message.chat.id]['new_balance'] = int(ww[c.message.chat.id]['oldbal']) + pric
                            qw = """UPDATE `users` SET `balance` = %s WHERE `user id` = %s """ %(str(ww[c.message.chat.id]['new_balance']), str(ww[c.message.chat.id]['mid']))   
                            cursor.execute(qw)
                            db.commit()
                            if str(c.message.chat.id) != ww[c.message.chat.id]['mid']:
                                bot.send_message(ww[c.message.chat.id]['mid'], "Пришел зароботок с продаж: " + str(pric) + "🍆")
                                if int(ww[c.message.chat.id]['row'][8]) >= 2:
                                    key = types.InlineKeyboardMarkup()
                                    button1 = types.InlineKeyboardButton(text="⭐️",callback_data = "1⭐️" + str(ww[c.message.chat.id]['mid']))
                                    button2 = types.InlineKeyboardButton(text="⭐️⭐️",callback_data = "2⭐️" + str(ww[c.message.chat.id]['mid']))
                                    button3 = types.InlineKeyboardButton(text="⭐️⭐️⭐️",callback_data = "3⭐️" + str(ww[c.message.chat.id]['mid']))
                                    button4 = types.InlineKeyboardButton(text="⭐️⭐️⭐️⭐️",callback_data = "4⭐️" + str(ww[c.message.chat.id]['mid']))
                                    button5 = types.InlineKeyboardButton(text="⭐️⭐️⭐️⭐️⭐️",callback_data = "5⭐️" + str(ww[c.message.chat.id]['mid']))
                                    key.add(button1, button2, button3)
                                    key.add(button4, button5)
                                    bot.send_message(c.message.chat.id, "На вашем счету " + str(ww[c.message.chat.id]['delta']) + '🍆' + "\n\nОцените пожалуйста товар:", reply_markup=key)
                                else:
                                    bot.send_message(c.message.chat.id, "На вашем счету " + str(ww[c.message.chat.id]['delta']) + '🍆')
                            else:
                                bot.send_message(c.message.chat.id, "Зачем покупать у себя же?")
                        else:
                            bot.send_message(c.message.chat.id, "Покупка успешно совершина!")
                        ww[c.message.chat.id]['cou'] = 0
                qw = "SELECT `super` FROM `personal` WHERE `user id` = '%s'" %(c.message.chat.id)
                cursor.execute(qw)
                ww[c.message.chat.id]['result'] = cursor.fetchall()
                if int(ww[c.message.chat.id]['price1']) < int(ww[c.message.chat.id]['row'][8]) and resin[0][0] == 0:
                    bot.send_message(c.message.chat.id, "У вас недостаточно средств для покупки этого Д.З.")
                    bot.send_message(c.message.chat.id, "На вашем счету " + str(ww[c.message.chat.id]['delta']) + '🍆' )

        
                    
        qw = "SELECT `nickname` FROM `personal`" 
        cursor.execute(qw)
        ww[c.message.chat.id]['result'] = cursor.fetchall()
        for i in ww[c.message.chat.id]['result']:
            if c.data == i[0] or c.data == '!' + i[0]:
                if c.data == i[0]:
                    key = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                    key.row("завершить чат")
                    bot.send_message(c.message.chat.id, "Чат с " + txt(i[0]) + ":" ,reply_markup=key)
                    qw = "SELECT `user id` FROM `personal` WHERE `nickname` = '%s'" %(i[0])
                    cursor.execute(qw)
                    ww[c.message.chat.id]['result'] = cursor.fetchall()
                    users[c.message.chat.id]['chat'] = int(ww[c.message.chat.id]['result'][0][0])
                    key = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                    key.row("завершить чат")
                    bot.send_message(users[c.message.chat.id]['chat'], "Чат с администратором:" ,reply_markup=key)
                    users[users[c.message.chat.id]['chat']]['chat'] = 653376416
                    break
                if c.data == '!' + i[0]:
                    bot.send_message(c.message.chat.id, 'Отлично, введите новый ник:')
                    count_er = 1
                    io = i[0]

        
        if users[c.message.chat.id]['c.data'] in [str(i) for i in range(16,31)]:
            if c.message.chat.id not in buy_users.keys():
                buy_users[c.message.chat.id] = {'buy_subject': '', 'buy_class': '', 'buy_data': '', 'buynum': '', 'buy_file': [], 'price': ''}
            if buy_users[c.message.chat.id]['buy_class'] not in [str(i) for i in range(16,31)]:
                key = types.InlineKeyboardMarkup()
                but_1 = types.InlineKeyboardButton(text="Русский",callback_data="r.")
                but_2 = types.InlineKeyboardButton(text="Зарубежку",callback_data="z.")
                but_3 = types.InlineKeyboardButton(text="Алгебру",callback_data="a.")
                but_4 = types.InlineKeyboardButton(text="Геометрию",callback_data="g.")
                but_5 = types.InlineKeyboardButton(text="Английский",callback_data="an.")
                but_6 = types.InlineKeyboardButton(text="Физику",callback_data="f.")
                but_7 = types.InlineKeyboardButton(text="Биологию",callback_data="b.")
                but_8 = types.InlineKeyboardButton(text="Укр.яз",callback_data="y.")
                but_9 = types.InlineKeyboardButton(text="Укр.лит",callback_data="yk.")
                but_10 = types.InlineKeyboardButton(text="Химию",callback_data="h.")
                but_11 = types.InlineKeyboardButton(text="Географию",callback_data="ge.")
                but_12 = types.InlineKeyboardButton(text="Всемирную историю",callback_data="v.")
                but_13 = types.InlineKeyboardButton(text="Историю Украины",callback_data="i.")
                but_14 = types.InlineKeyboardButton(text="Физкультуру",callback_data="fi.")
                but_15 = types.InlineKeyboardButton(text="Информатику",callback_data="in.")
                but_16 = types.InlineKeyboardButton(text="Основы здоровья",callback_data="o.")
                but_17 = types.InlineKeyboardButton(text="Полезную инфу",callback_data="p.")
                key.add(but_1, but_2, but_3, but_4, but_5, but_6, but_7, but_8, but_9, but_10, but_11, but_12, but_13, but_14, but_15, but_16, but_17)
                bot.send_message(c.message.chat.id, "Что купить?", reply_markup=key)  


                buy_users[c.message.chat.id]['buy_class'] = users[c.message.chat.id]['c.data']

        if users[c.message.chat.id]['c.data'] in ["r.", "z.", "a.", "g.", "an.", "f.", "b.", "y.", "yk.", "h.", "ge.", "v.", "i.", "fi.", "in.", "o.", "p."]:


            if users[c.message.chat.id]['c.data'] == "r.":
                sb = 'r'
            if users[c.message.chat.id]['c.data'] == "z.":
                sb = 'z'
            if users[c.message.chat.id]['c.data'] == "a.":
                sb = 'a'
            if users[c.message.chat.id]['c.data'] == "g.":
                sb = 'g'
            if users[c.message.chat.id]['c.data'] == "an.":
                sb = 'an'
            if users[c.message.chat.id]['c.data'] == "f.":
                sb = 'f'
            if users[c.message.chat.id]['c.data'] == "b.":
                sb = 'b'
            if users[c.message.chat.id]['c.data'] == "y.":
                sb = 'y'
            if users[c.message.chat.id]['c.data'] == "yk.":
                sb = 'yk'
            if users[c.message.chat.id]['c.data'] == "h.":
                sb = 'h'
            if users[c.message.chat.id]['c.data'] == "ge.":
                sb = 'ge'
            if users[c.message.chat.id]['c.data'] == "v.":
                sb = 'v'
            if users[c.message.chat.id]['c.data'] == "i.":
                sb = 'i'
            if users[c.message.chat.id]['c.data'] == "fi.":
                sb = 'fi'
            if users[c.message.chat.id]['c.data'] == "in.":
                sb = 'in'
            if users[c.message.chat.id]['c.data'] == "o.":
                sb = 'o'
            if users[c.message.chat.id]['c.data'] == "p.":
                sb = 'p'

            buy_users[c.message.chat.id]['buy_subject'] = sb

            key = types.InlineKeyboardMarkup()
            but_1 = types.InlineKeyboardButton(text="10 объявлений",callback_data="T")
            but_2 = types.InlineKeyboardButton(text="5 объявлений",callback_data="F")
            but_3 = types.InlineKeyboardButton(text="2 объявления",callback_data="W")
            key.add(but_1, but_2, but_3)
            bot.send_message(c.message.chat.id, "Показать последние:", reply_markup=key)

        if users[c.message.chat.id]['c.data'] in ['T','F','W']:
            buy_users[c.message.chat.id]['buynum'] = users[c.message.chat.id]['c.data']

        if users[c.message.chat.id]['c.data'] in [str(i) for i in range(1,16)] and counters[c.message.chat.id]['buy_data'] == 0:
            if c.message.chat.id not in users.keys():
                users[c.message.chat.id] = {'chat': 0, 'free': 0, 'ban': 0, 'subject_r': '', 'class_r': '','c.data': 0, 'nickname': '', 'nicou': 0, 'subject': '', 'class': '', 'date': '', 'note': '', 'file': [], 'price': 0, 'noname': ''}
            if users[c.message.chat.id]['class'] not in [str(i) for i in range(1,16)]:
                key = types.InlineKeyboardMarkup()
                but_1 = types.InlineKeyboardButton(text="Русский",callback_data="r")
                but_2 = types.InlineKeyboardButton(text="Зарубежку",callback_data="z")
                but_3 = types.InlineKeyboardButton(text="Алгебру",callback_data="a")
                but_4 = types.InlineKeyboardButton(text="Геометрию",callback_data="g")
                but_5 = types.InlineKeyboardButton(text="Английский",callback_data="an")
                but_6 = types.InlineKeyboardButton(text="Физику",callback_data="f")
                but_7 = types.InlineKeyboardButton(text="Биологию",callback_data="b")
                but_8 = types.InlineKeyboardButton(text="Укр.яз",callback_data="y")
                but_9 = types.InlineKeyboardButton(text="Укр.лит",callback_data="yk")
                but_10 = types.InlineKeyboardButton(text="Химию",callback_data="h")
                but_11 = types.InlineKeyboardButton(text="Географию",callback_data="ge")
                but_12 = types.InlineKeyboardButton(text="Всемирную историю",callback_data="v")
                but_13 = types.InlineKeyboardButton(text="Историю Украины",callback_data="i")
                but_14 = types.InlineKeyboardButton(text="Физкультуру",callback_data="fi")
                but_15 = types.InlineKeyboardButton(text="Информатику",callback_data="in")
                but_16 = types.InlineKeyboardButton(text="Основы здоровья",callback_data="o")
                but_17 = types.InlineKeyboardButton(text="Полезную инфу",callback_data="p")
                key.add(but_1, but_2, but_3, but_4, but_5, but_6, but_7, but_8, but_9, but_10, but_11, but_12, but_13, but_14, but_15, but_16, but_17)
                bot.send_message(c.message.chat.id, "Что продать?", reply_markup=key)   
                users[c.message.chat.id]['class'] = users[c.message.chat.id]['c.data']

                global ccllaass
                ccllaass = users[c.message.chat.id]['class']

        if users[c.message.chat.id]['c.data'] in ["r", "z", "a", "g", "an", "f", "b", "y", "yk", "h", "ge", "v", "i", "fi", "in", "o", "p"]:
            users[c.message.chat.id]['subject'] = users[c.message.chat.id]['c.data']
            bot.send_message(c.message.chat.id, 'Отлично! Пришлите фотографию:' )

        if buy_users[c.message.chat.id]['buynum'] in ['F','T','W']:

            counters[c.message.chat.id]['cou'] = 1
            if buy_users[c.message.chat.id]['buy_class'] == "16":
                buy_users[c.message.chat.id]['buy_class_r'] = '7-Ф'
            if buy_users[c.message.chat.id]['buy_class'] == "17":
                buy_users[c.message.chat.id]['buy_class_r'] = "7-М"
            if buy_users[c.message.chat.id]['buy_class'] == "18":
                buy_users[c.message.chat.id]['buy_class_r'] = "7-ХБ"
            if buy_users[c.message.chat.id]['buy_class'] == "19":
                buy_users[c.message.chat.id]['buy_class_r'] = "8-Ф"
            if buy_users[c.message.chat.id]['buy_class'] == "20":
                buy_users[c.message.chat.id]['buy_class_r'] = "8-М"
            if buy_users[c.message.chat.id]['buy_class'] == "21":
                buy_users[c.message.chat.id]['buy_class_r'] = "8-ХБ"
            if buy_users[c.message.chat.id]['buy_class'] == "22":
                buy_users[c.message.chat.id]['buy_class_r'] = "9-Ф"
            if buy_users[c.message.chat.id]['buy_class'] == "23":
                buy_users[c.message.chat.id]['buy_class_r'] = "9-М"   
            if buy_users[c.message.chat.id]['buy_class'] == "24":
                buy_users[c.message.chat.id]['buy_class_r'] = "9-ХБ"  
            if buy_users[c.message.chat.id]['buy_class'] == "25":
                buy_users[c.message.chat.id]['buy_class_r'] = "10-Ф"
            if buy_users[c.message.chat.id]['buy_class'] == "26":
                buy_users[c.message.chat.id]['buy_class_r'] = "10-М"
            if buy_users[c.message.chat.id]['buy_class'] == "27":
                buy_users[c.message.chat.id]['buy_class_r'] = "10-ХБ"
            if buy_users[c.message.chat.id]['buy_class'] == "28":
                buy_users[c.message.chat.id]['buy_class_r'] = "11-Ф"
            if buy_users[c.message.chat.id]['buy_class'] == "29":
                buy_users[c.message.chat.id]['buy_class_r'] = "11-М"
            if buy_users[c.message.chat.id]['buy_class'] == "30":
                buy_users[c.message.chat.id]['buy_class_r'] = "11-ХБ"

            if buy_users[c.message.chat.id]['buy_class'] == "16":
                buy_users[c.message.chat.id]['buy_class'] = '1'
            if buy_users[c.message.chat.id]['buy_class'] == "17":
                buy_users[c.message.chat.id]['buy_class'] = "2"
            if buy_users[c.message.chat.id]['buy_class'] == "18":
                buy_users[c.message.chat.id]['buy_class'] = "3"
            if buy_users[c.message.chat.id]['buy_class'] == "19":
                buy_users[c.message.chat.id]['buy_class'] = "4"
            if buy_users[c.message.chat.id]['buy_class'] == "20":
                buy_users[c.message.chat.id]['buy_class'] = "5"
            if buy_users[c.message.chat.id]['buy_class'] == "21":
                buy_users[c.message.chat.id]['buy_class'] = "6"
            if buy_users[c.message.chat.id]['buy_class'] == "22":
                buy_users[c.message.chat.id]['buy_class'] = "7"
            if buy_users[c.message.chat.id]['buy_class'] == "23":
                buy_users[c.message.chat.id]['buy_class'] = "8"   
            if buy_users[c.message.chat.id]['buy_class'] == "24":
                buy_users[c.message.chat.id]['buy_class'] = "9"  
            if buy_users[c.message.chat.id]['buy_class'] == "25":
                buy_users[c.message.chat.id]['buy_class'] = "10"
            if buy_users[c.message.chat.id]['buy_class'] == "26":
                buy_users[c.message.chat.id]['buy_class'] = "11"
            if buy_users[c.message.chat.id]['buy_class'] == "27":
                buy_users[c.message.chat.id]['buy_class'] = "12"
            if buy_users[c.message.chat.id]['buy_class'] == "28":
                buy_users[c.message.chat.id]['buy_class'] = "13"
            if buy_users[c.message.chat.id]['buy_class'] == "29":
                buy_users[c.message.chat.id]['buy_class'] = "14"
            if buy_users[c.message.chat.id]['buy_class'] == "30":
                buy_users[c.message.chat.id]['buy_class'] = "15"

            if buy_users[c.message.chat.id]['buynum'] ==  'T':
                qw = "SELECT * FROM `users` WHERE `subject` = '%s' and `class` = '%s' ORDER BY  `id` DESC LIMIT 10" %(buy_users[c.message.chat.id]['buy_subject'], buy_users[c.message.chat.id]['buy_class'])                     

                cursor.execute(qw)
                ww[c.message.chat.id]['result'] = cursor.fetchall()
                ww[c.message.chat.id]['result'].reverse()
                if not ww[c.message.chat.id]['result']:
                    counters[c.message.chat.id]['cou'] = 0           

            if buy_users[c.message.chat.id]['buynum'] ==  'F':
                qw = "SELECT * FROM `users` WHERE `subject` = '%s' and `class` = '%s' ORDER BY  `id` DESC LIMIT 5" %(buy_users[c.message.chat.id]['buy_subject'], buy_users[c.message.chat.id]['buy_class'])                     

                cursor.execute(qw)
                ww[c.message.chat.id]['result'] = cursor.fetchall() 
                ww[c.message.chat.id]['result'].reverse()
                if not ww[c.message.chat.id]['result']:
                    counters[c.message.chat.id]['cou'] = 0  

            if buy_users[c.message.chat.id]['buynum'] ==  'W':
                qw = "SELECT * FROM `users` WHERE `subject` = '%s' and `class` = '%s' ORDER BY  `id` DESC LIMIT 2" %(buy_users[c.message.chat.id]['buy_subject'], buy_users[c.message.chat.id]['buy_class'])                     
                cursor.execute(qw)
                ww[c.message.chat.id]['result'] = cursor.fetchall()
                ww[c.message.chat.id]['result'].reverse()
                if not ww[c.message.chat.id]['result']:
                    counters[c.message.chat.id]['cou'] = 0
            ww[c.message.chat.id]['row'] = ''
            for ww[c.message.chat.id]['row'] in ww[c.message.chat.id]['result']:

                qw = "SELECT `user id` FROM `users` WHERE `id` = '%d' and `subject` = '%s' and `class` = '%s'" %(int(ww[c.message.chat.id]['row'][0]), buy_users[c.message.chat.id]['buy_subject'], buy_users[c.message.chat.id]['buy_class']) 
                cursor.execute(qw)
                ww[c.message.chat.id]['result'] = cursor.fetchall()
                ww[c.message.chat.id]['result'].reverse()
                ww[c.message.chat.id]['mod'] = int(ww[c.message.chat.id]['result'][0][0])

                num = len(ww[c.message.chat.id]['row'][6].split('\n'))

                if num%10 == 1 :
                    pic = 'картинка.'
                if num%10 in [2,3,4] :
                    pic = 'картинки.'
                if num%10 in [5,6,7,8,9,0] :
                    pic = 'картинок.'

                counters[c.message.chat.id]['call'] = str(ww[c.message.chat.id]['row'][0])

                if ww[c.message.chat.id]['row'][2] == "r":
                    users[c.message.chat.id]['subject_r'] = 'Русский'
                if ww[c.message.chat.id]['row'][2] == "z":
                    users[c.message.chat.id]['subject_r'] = "Зарубежка"
                if ww[c.message.chat.id]['row'][2] == "a":
                    users[c.message.chat.id]['subject_r'] = "Алгебра"
                if ww[c.message.chat.id]['row'][2] == "g":
                    users[c.message.chat.id]['subject_r'] = "Геометрия"
                if ww[c.message.chat.id]['row'][2] == "an":
                    users[c.message.chat.id]['subject_r'] = "Английский"
                if ww[c.message.chat.id]['row'][2] == "f":
                    users[c.message.chat.id]['subject_r'] = "Физика"
                if ww[c.message.chat.id]['row'][2] == "b":
                    users[c.message.chat.id]['subject_r'] = "Биология"
                if ww[c.message.chat.id]['row'][2] == "y":
                    users[c.message.chat.id]['subject_r'] = "Укр.яз"   
                if ww[c.message.chat.id]['row'][2] == "yk":
                    users[c.message.chat.id]['subject_r'] = "Укр.лит"  
                if ww[c.message.chat.id]['row'][2] == "h":
                    users[c.message.chat.id]['subject_r'] = "Химия"
                if ww[c.message.chat.id]['row'][2] == "ge":
                    users[c.message.chat.id]['subject_r'] = "География"
                if ww[c.message.chat.id]['row'][2] == "v":
                    users[c.message.chat.id]['subject_r'] = "Всемирная история"
                if ww[c.message.chat.id]['row'][2] == "i":
                    users[c.message.chat.id]['subject_r'] = "История Украины"
                if ww[c.message.chat.id]['row'][2] == "fi":
                    users[c.message.chat.id]['subject_r'] = "Физкультура"
                if ww[c.message.chat.id]['row'][2] == "in":
                    users[c.message.chat.id]['subject_r'] = "Информатика"
                if ww[c.message.chat.id]['row'][2] == "o":
                    users[c.message.chat.id]['subject_r'] = "Основы здоровья"
                if ww[c.message.chat.id]['row'][2] == "p":
                    users[c.message.chat.id]['subject_r'] = "Полезная инфа"

                q = "SELECT distinct `nickname` FROM `users` WHERE `user id` = %s and `nickname` <> ''" %(ww[c.message.chat.id]['mod'])
                cursor.execute(q)
                ww[c.message.chat.id]['rabotay'] = cursor.fetchall()

                if ww[c.message.chat.id]['row'][5] == '':
                    counters[c.message.chat.id]['buy_data'] = 1
                    key = types.InlineKeyboardMarkup()
                    b_1 = types.InlineKeyboardButton(text="⬆️купить⬆️", callback_data = 'buy_button' + str(ww[c.message.chat.id]['row'][0]))
                    key.add(b_1)
                    bot.send_message(c.message.chat.id,"Продавец: " + txt(ww[c.message.chat.id]['rabotay']) +
                        "\n🔑Цена:   " + str(ww[c.message.chat.id]['row'][8]) + '🍆' + 
                        "\n🔥Предмет:   " + users[c.message.chat.id]['subject_r'] + 
                        "\n🔝Класс:   " +  buy_users[c.message.chat.id]['buy_class_r'] + 
                        '\n📅Дата:  ' + ww[c.message.chat.id]['row'][4].strftime('%Y-%m-%d') + 
                        '\n🕑Время:   ' + ww[c.message.chat.id]['row'][4].strftime('%H : %M') + 
                        '\n+ ' + str(num) + ' ' + pic, reply_markup=key)
                else:
                    counters[c.message.chat.id]['buy_data'] = 1

                    key = types.InlineKeyboardMarkup()
                    b_1 = types.InlineKeyboardButton(text="⬆️купить⬆️",callback_data = 'buy_button' + str(ww[c.message.chat.id]['row'][0]))
                    key.add(b_1)
                    bot.send_message(c.message.chat.id, "Продавец: " + txt(ww[c.message.chat.id]['rabotay']) +
                        "\n🔑Цена:   " + str(ww[c.message.chat.id]['row'][8]) + '🍆' + 
                        "\n🔥Предмет:   " + users[c.message.chat.id]['subject_r'] + 
                        "\n🔝Класс:   " +  buy_users[c.message.chat.id]['buy_class_r'] + 
                        '\n📅Дата:  ' + ww[c.message.chat.id]['row'][4].strftime('%Y-%m-%d') + 
                        '\n🕑Время:   ' + ww[c.message.chat.id]['row'][4].strftime('%H : %M') + 
                        '\n+ ' + str(num) + ' ' + pic + 
                        '\nP.S. ' + str(txt(str(ww[c.message.chat.id]['row'][5]))),
                        reply_markup=key)

            ww[c.message.chat.id]['row'] = ''
            buy_users[c.message.chat.id]['buynum'] = ''
            if counters[c.message.chat.id]['cou'] == 1:
                if users[c.message.chat.id]['noname'] == 1:
                    key = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                    key.row("продать", "купить")
                    key.row("пополнить счет", "регистрация", "баланс")
                    bot.send_message(c.message.chat.id, "⬆️Результат поиска⬆️",reply_markup=key) 
                if users[c.message.chat.id]['noname'] == 0:
                    key = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                    key.row("продать", "купить")
                    key.row("пополнить счет", "баланс")
                    bot.send_message(c.message.chat.id, "⬆️Результат поиска⬆️",reply_markup=key)
            if counters[c.message.chat.id]['cou'] == 0:
                if users[c.message.chat.id]['noname'] == 1:
                    key = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                    key.row("продать", "купить")
                    key.row("пополнить счет", "регистрация", "баланс")
                    bot.send_message(c.message.chat.id, "По вашему запросу ничего не найдено🙁",reply_markup=key) 
                if users[c.message.chat.id]['noname'] == 0:
                    key = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                    key.row("продать", "купить")
                    key.row("пополнить счет", "баланс")
                    bot.send_message(c.message.chat.id, "По вашему запросу ничего не найдено🙁",reply_markup=key)
            counters[c.message.chat.id]['cou'] = 0
    else:
        bot.send_photo(message.chat.id, open('D:\Дима\Програмирование\Python\BOT\Фото\Angrybot.jpg', 'rb'))
        bot.send_message(c.message.chat.id, 'Вы забанены! По всем вопросам —> @RL_support_Bot')

@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):


    if message.chat.id not in users.keys() or message.chat.id not in buy_users.keys() or message.chat.id not in ww.keys() or message.chat.id not in counters.keys():
        
        qw = "SELECT distinct `nickname` FROM `users` WHERE `user id` = %s and `nickname` <> ''" %(message.chat.id)
        cursor.execute(qw)
        result = cursor.fetchall()
        result = txt(result)
        
        if len(result) != 0:
            users[message.chat.id] = {'chat': 0, 'free': 0, 'ban': 0, 'subject_r': '','class_r':'', 'c.data': 0, 'nickname': result[0], 'nicou': 0, 'subject': '', 'class': '', 'date': '', 'note': '', 'file': [], 'price': 0, 'noname': ''}
            buy_users[message.chat.id] = {'buy_class_r': '', 'buy_subject': '', 'buy_class': '', 'buy_data': '', 'buynum': '', 'buy_file': []}
            counters[message.chat.id] = {'count_3': 0, 'cou': 0, 'count_2': 0, 'count': 0, 'call': '', 'ids': '', 'idz': '', 'csc': 0, 'bd': 0, 'buy_data': 0, 'uou': 0, 'uqu': 0, 'f': 0, 'zwz': 0, 'coc': 0, 'cec': 0,'cac': 0, 'czc': 0, 'cjc': 0}
            ww[message.chat.id] = {'result': '', 'row': '', 'b': 0, 'assessment': '', 'cou': 1, 'N': 0, 'rating': 0.0}
        else:
            users[message.chat.id] = {'chat': 0, 'free': 0, 'ban': 0, 'subject_r': '','class_r':'', 'c.data': 0, 'nickname': '', 'nicou': 0, 'subject': '', 'class': '', 'date': '', 'note': '', 'file': [], 'price': 0, 'noname': ''}
            buy_users[message.chat.id] = {'buy_class_r': '','buy_subject': '', 'buy_class': '', 'buy_data': '', 'buynum': '', 'buy_file': []}
            counters[message.chat.id] = {'count_3': 0, 'cou': 0, 'count_2': 0, 'count': 0, 'call': '', 'ids': '', 'idz': '', 'csc': 0, 'bd': 0, 'buy_data': 0, 'uou': 0, 'uqu': 0, 'f': 0, 'zwz': 0, 'coc': 0, 'cec': 0,'cac': 0, 'czc': 0, 'cjc': 0}
            ww[message.chat.id] = {'result': '', 'row': '', 'b': 0, 'assessment': '', 'cou': 1, 'N': 0, 'rating': 0.0}


    a = random.randint(0, 5)

    if message.chat.id not in users.keys():
        users[message.chat.id] = {'chat': 0, 'free': 0, 'ban': 0, 'subject': '', 'class': '', 'date': '', 'note': '', 'file': [], 'price': ''} 
        
    if users[message.chat.id]['class'] == '' and users[message.chat.id]['subject'] == '' and a == 0:
        bot.send_message(message.chat.id, "И что мне с этим делать? Нажми кнопку <продать> выбери все необходимое, а после шли фотки.")
    if users[message.chat.id]['class'] == '' and users[message.chat.id]['subject'] == '' and a == 1:
        bot.send_message(message.chat.id, "Прикольная картинка. Но что мне с ней делать? Нажми кнопку <продать> выбери все необходимое, а после шли фотки.")  
    if users[message.chat.id]['class'] == '' and users[message.chat.id]['subject'] == '' and a == 2:
        bot.send_message(message.chat.id, "😂👌 И что мне с этим делать? Нажми кнопку <продать> выбери все необходимое, а после шли фотки.")
    if users[message.chat.id]['class'] == '' and users[message.chat.id]['subject'] == '' and a == 3:
        bot.send_message(message.chat.id, "Это шедевр!!! Но что мне с этим делать? Нажми кнопку <продать> выбери все необходимое, а после шли фотки.")
    if users[message.chat.id]['class'] == '' and users[message.chat.id]['subject'] == '' and a == 4:
        bot.send_message(message.chat.id, "Это конечно красиво, но что мне с этим делать? Нажми кнопку <продать> выбери все необходимое, а после шли фотки.")  
    if users[message.chat.id]['class'] == '' and users[message.chat.id]['subject'] == '' and a == 5:
        bot.send_message(message.chat.id, "Так, хватит прикаловаться! Нажми кнопку <продать> выбери все необходимое, а после шли фотки.")
    
    if users[message.chat.id]['class'] != '' and users[message.chat.id]['subject'] != '':
        cur = datetime.datetime.now()
        a = datetime.timedelta(hours=6)
        cur += a
        file_name = "D://TEMP//ФОТОГРАФИИ Telegram BOT//" + cur.strftime('%Y-%m-%d-%H-%M-%S-%f') + '.jpg'
        try:
            file_info = bot.get_file(message.photo[len(message.photo)-1].file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            with open(file_name, 'wb') as new_file:
                new_file.write(downloaded_file)
            bot.reply_to(message,"Фото успешно добавлено!") 
        except Exception as e:
            bot.reply_to(message, e)

        users[message.chat.id]['date'] = cur
        users[message.chat.id]['file'].append(file_name)
        

        key = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        key.row('готово','добавить коментарий', 'отмена')
        bot.send_message(message.chat.id, "Если хотите, добавте еще фотографии.",reply_markup=key)

bot.polling(none_stop=True)

######################################################
