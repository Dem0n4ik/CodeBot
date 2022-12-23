import telebot
from telebot import types

import config

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Інша система числення")
    item2 = types.KeyboardButton("Коди")
    item3 = types.KeyboardButton("Шифри")
    markup.add(item1)
    markup.add(item2, item3)
    bot.send_message(message.chat.id, 'Привіт!👋 \nНатисни: \n'
                                      'Інша система числення '' - для кодування вашого числа у іншу систему числення\n' 
                                      'Коди - для кодування вашого числа у інші коди\n' 
                                      'Шифри - для шифрування вашого повідомлення', reply_markup=markup)


@bot.message_handler(content_types=["text"])
def check_callback_data(message):
    if message.text == 'Інша система числення':
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            types.InlineKeyboardButton('2', callback_data='code_2'),
            types.InlineKeyboardButton('3', callback_data='code_3'),
            types.InlineKeyboardButton('4', callback_data='code_4'),
            types.InlineKeyboardButton('5', callback_data='code_5'),
        )
        keyboard.row(
            types.InlineKeyboardButton('6', callback_data='code_6'),
            types.InlineKeyboardButton('7', callback_data='code_7'),
            types.InlineKeyboardButton('8', callback_data='code_8'),
            types.InlineKeyboardButton('9', callback_data='code_9')
        )
        keyboard.row(
            types.InlineKeyboardButton('11', callback_data='code_11'),
            types.InlineKeyboardButton('12', callback_data='code_12'),
            types.InlineKeyboardButton('13', callback_data='code_13'),
            types.InlineKeyboardButton('16', callback_data='code_16')
        )
        keyboard.row(
            types.InlineKeyboardButton('20', callback_data='code_20')
        )
        bot.send_message(message.chat.id, "Виберіть систему числення", reply_markup=keyboard)

    elif message.text == 'Коди':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.row(
            types.InlineKeyboardButton('Кореляційний', callback_data='code_k'),
            types.InlineKeyboardButton('Інверсний', callback_data='code_in')
        )
        keyboard.row(
            types.InlineKeyboardButton('Грея', callback_data='code_g'),
            types.InlineKeyboardButton('З повторенням', callback_data='code_zp')
        )
        keyboard.row(
            types.InlineKeyboardButton('З перевіркою на парність', callback_data='code_zpp')
        )
        bot.send_message(message.chat.id, "Виберіть код", reply_markup=keyboard)

    elif message.text == 'Шифри':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.row(
            types.InlineKeyboardButton('Цезаря', callback_data='cipher_c'),
            types.InlineKeyboardButton('Віженера', callback_data='cipher_v')
        )
        bot.send_message(message.chat.id, "Виберіть шифр", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda callback: callback.data)
def callback_query_but1(callback):
    if callback.data == 'code_2':
        dec_bin = bot.send_message(callback.message.chat.id, 'Введіть десяткове число:')
        bot.register_next_step_handler(dec_bin, binary)
    elif callback.data == 'code_3':
        dec_trp = bot.send_message(callback.message.chat.id, 'Введіть десяткове число:')
        bot.register_next_step_handler(dec_trp, triple)
    elif callback.data == 'code_4':
        dec_qdr = bot.send_message(callback.message.chat.id, 'Введіть десяткове число:')
        bot.register_next_step_handler(dec_qdr, quadruple)
    elif callback.data == 'code_5':
        dec_fv = bot.send_message(callback.message.chat.id, 'Введіть десяткове число:')
        bot.register_next_step_handler(dec_fv, five)
    elif callback.data == 'code_6':
        dec_sx = bot.send_message(callback.message.chat.id, 'Введіть десяткове число:')
        bot.register_next_step_handler(dec_sx, sixtn)
    elif callback.data == 'code_7':
        dec_svt = bot.send_message(callback.message.chat.id, 'Введіть десяткове число:')
        bot.register_next_step_handler(dec_svt, sevtn)
    elif callback.data == 'code_8':
        dec_oct = bot.send_message(callback.message.chat.id, 'Введіть десяткове число:')
        bot.register_next_step_handler(dec_oct, octal)
    elif callback.data == 'code_9':
        dec_nin = bot.send_message(callback.message.chat.id, 'Введіть десяткове число:')
        bot.register_next_step_handler(dec_nin, nintn)
    elif callback.data == 'code_9':
        dec_nin = bot.send_message(callback.message.chat.id, 'Введіть десяткове число:')
        bot.register_next_step_handler(dec_nin, nintn)
    elif callback.data == 'code_11':
        dec_eln = bot.send_message(callback.message.chat.id, 'Введіть десяткове число:')
        bot.register_next_step_handler(dec_eln, eleven)
    elif callback.data == 'code_12':
        dec_twl = bot.send_message(callback.message.chat.id, 'Введіть десяткове число:')
        bot.register_next_step_handler(dec_twl, twelve)
    elif callback.data == 'code_13':
        dec_trn = bot.send_message(callback.message.chat.id, 'Введіть десяткове число:')
        bot.register_next_step_handler(dec_trn, threetn)
    elif callback.data == 'code_16':
        dec_hex = bot.send_message(callback.message.chat.id, 'Введіть десяткове число:')
        bot.register_next_step_handler(dec_hex, hexadecimal)
    elif callback.data == 'code_20':
        dec_twn = bot.send_message(callback.message.chat.id, 'Введіть десяткове число:')
        bot.register_next_step_handler(dec_twn, twenty)

    elif callback.data == 'code_g':
        gra_comb = bot.send_message(callback.message.chat.id, 'Введіть десяткове число:')
        bot.register_next_step_handler(gra_comb, gray)
    elif callback.data == 'code_zpp':
        chec_comb = bot.send_message(callback.message.chat.id, 'Введіть десяткове число:')
        bot.register_next_step_handler(chec_comb, check_even_code)
    elif callback.data == 'code_in':
        inv_comb = bot.send_message(callback.message.chat.id, 'Введіть десяткове число:')
        bot.register_next_step_handler(inv_comb, inverse_code)
    elif callback.data == 'code_k':
        corl_comb = bot.send_message(callback.message.chat.id, 'Введіть десяткове число:')
        bot.register_next_step_handler(corl_comb, corelation_code)
    elif callback.data == 'code_zp':
        repit_comb = bot.send_message(callback.message.chat.id, 'Введіть десяткове число:')
        bot.register_next_step_handler(repit_comb, repetition_code)

    elif callback.data == 'cipher_c':
        caesar_key = bot.send_message(callback.message.chat.id, 'Введіть ключ (число) від 1 до 33:')
        bot.register_next_step_handler(caesar_key, cipher_caesar_key)
    elif callback.data == 'cipher_v':
        vijener_key = bot.send_message(callback.message.chat.id, 'Введіть ключ (слово):')
        bot.register_next_step_handler(vijener_key, cipher_vijener_key)


@bot.message_handler(content_types=["text"])
def binary(message):
    try:
        binar = message.text
        intgr = int(binar)
        con_bin = bin(intgr)
        bot.send_message(message.chat.id, f'Ваше двійкове число - {con_bin[2:]}')
    except Exception:
        b = bot.send_message(message.chat.id, 'Схоже ви ввели число не вірно, спробуйте ввести його ще раз:')
        bot.register_next_step_handler(b, binary)

def triple(message):
    try:
        digits_three = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        r = ""
        tripl = message.text
        intgr3 = int(tripl)
        while intgr3 > 0:
            k = intgr3 % 3
            r = digits_three[k] + r
            intgr3 = intgr3 // 3
        bot.send_message(message.chat.id, f'Ваше трійкове число - {r}')
    except Exception:
        t = bot.send_message(message.chat.id, 'Схоже ви ввели число не вірно, спробуйте ввести його ще раз:')
        bot.register_next_step_handler(t, triple)

def quadruple(message):
    try:
        digits_four = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        r = ""
        quadrup = message.text
        intgr4 = int(quadrup)
        while intgr4 > 0:
            k = intgr4 % 4
            r = digits_four[k] + r
            intgr4 = intgr4 // 4
        bot.send_message(message.chat.id, f'Ваше чотирьохрічне число - {r}')
    except Exception:
        t = bot.send_message(message.chat.id, 'Схоже ви ввели число не вірно, спробуйте ввести його ще раз:')
        bot.register_next_step_handler(t, quadruple)

def five(message):
    try:
        digits_five = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        r = ""
        fiv = message.text
        intgr5 = int(fiv)
        while intgr5 > 0:
            k = intgr5 % 5
            r = digits_five[k] + r
            intgr5 = intgr5 // 5
        bot.send_message(message.chat.id, f"Ваше п'ятирічне число - {r}")
    except Exception:
        t = bot.send_message(message.chat.id, 'Схоже ви ввели число не вірно, спробуйте ввести його ще раз:')
        bot.register_next_step_handler(t, five)

def sixtn(message):
    try:
        digits_six = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        r = ""
        sixt = message.text
        intgr6 = int(sixt)
        while intgr6 > 0:
            k = intgr6 % 6
            r = digits_six[k] + r
            intgr6 = intgr6 // 6
        bot.send_message(message.chat.id, f'Ваше шестирічне число - {r}')
    except Exception:
        t = bot.send_message(message.chat.id, 'Схоже ви ввели число не вірно, спробуйте ввести його ще раз:')
        bot.register_next_step_handler(t, sixtn)

def sevtn(message):
    try:
        digits_seven = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        r = ""
        sevt = message.text
        intgr7 = int(sevt)
        while intgr7 > 0:
            k = intgr7 % 7
            r = digits_seven[k] + r
            intgr7 = intgr7 // 7
        bot.send_message(message.chat.id, f'Ваше семирічне число - {r}')
    except Exception:
        t = bot.send_message(message.chat.id, 'Схоже ви ввели число не вірно, спробуйте ввести його ще раз:')
        bot.register_next_step_handler(t, sevtn)

def octal(message):
    try:
        octl = message.text
        intgr8 = int(octl)
        con_oct = oct(intgr8)
        bot.send_message(message.chat.id, f'Ваше вісімкове число - {con_oct[2:]}')
    except Exception:
        t = bot.send_message(message.chat.id, 'Схоже ви ввели число не вірно, спробуйте ввести його ще раз:')
        bot.register_next_step_handler(t, octal)

def nintn(message):
    try:
        digits_nine = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        r = ""
        ninet = message.text
        intgr9 = int(ninet)
        while intgr9 > 0:
            k = intgr9 % 9
            r = digits_nine[k] + r
            intgr9 = intgr9 // 9
        bot.send_message(message.chat.id, f"Ваше дев'ятирічне число - {r}")
    except Exception:
        t = bot.send_message(message.chat.id, 'Схоже ви ввели число не вірно, спробуйте ввести його ще раз:')
        bot.register_next_step_handler(t, nintn)

def eleven(message):
    try:
        digits_eleven = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        r = ""
        elvn = message.text
        intgr11 = int(elvn)
        while intgr11 > 0:
            k = intgr11 % 11
            r = digits_eleven[k] + r
            intgr11 = intgr11 // 11
        bot.send_message(message.chat.id, f"Ваше одинадцятирічне число - {r}")
    except Exception:
        t = bot.send_message(message.chat.id, 'Схоже ви ввели число не вірно, спробуйте ввести його ще раз:')
        bot.register_next_step_handler(t, eleven)

def twelve(message):
    try:
        digits_twelve = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        r = ""
        twlv = message.text
        intgr12 = int(twlv)
        while intgr12 > 0:
            k = intgr12 % 12
            r = digits_twelve[k] + r
            intgr12 = intgr12 // 12
        bot.send_message(message.chat.id, f"Ваше дванадцятирічне число - {r}")
    except Exception:
        t = bot.send_message(message.chat.id, 'Схоже ви ввели число не вірно, спробуйте ввести його ще раз:')
        bot.register_next_step_handler(t, twelve)

def threetn(message):
    try:
        digits_threetn = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        r = ""
        thrtn = message.text
        intgr13 = int(thrtn)
        while intgr13 > 0:
            k = intgr13 % 13
            r = digits_threetn[k] + r
            intgr13 = intgr13 // 13
        bot.send_message(message.chat.id, f"Ваше тринадцятирічне число - {r}")
    except Exception:
        t = bot.send_message(message.chat.id, 'Схоже ви ввели число не вірно, спробуйте ввести його ще раз:')
        bot.register_next_step_handler(t, twelve)

def hexadecimal(message):
    try:
        hexad = message.text
        intgr16 = int(hexad)
        con_hex = hex(intgr16)
        bot.send_message(message.chat.id, f'Ваше шістнадцяткове число - {con_hex[2:].upper()}')
    except Exception:
        t = bot.send_message(message.chat.id, 'Схоже ви ввели число не вірно, спробуйте ввести його ще раз:')
        bot.register_next_step_handler(t, hexadecimal)

def twenty(message):
    try:
        digits_twenty = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        r = ""
        twnt = message.text
        intgr20 = int(twnt)
        while intgr20 > 0:
            k = intgr20 % 20
            r = digits_twenty[k] + r
            intgr20 = intgr20 // 20
        bot.send_message(message.chat.id, f"Ваше двадцяткове число - {r}")
    except Exception:
        t = bot.send_message(message.chat.id, 'Схоже ви ввели число не вірно, спробуйте ввести його ще раз:')
        bot.register_next_step_handler(t, twenty)


def gray(message):
    try:
        gr_cod = message.text
        d_num = int(gr_cod)
        grey_code = (d_num ^ (d_num >> 1))
        b_num = bin(grey_code)
        bot.send_message(message.chat.id, f'Ваша комбінація для коду Ґрея - {b_num[2:]}')
    except Exception:
        sender = bot.send_message(message.chat.id, 'Схоже ви ввели число не вірно, спробуйте ввести його ще раз:')
        bot.register_next_step_handler(sender, gray)

def check_even_code(message):
    try:
        user_mesg = message.text
        binar_n = bin(int(user_mesg))
        str_binar_n = str(binar_n)
        count = 0
        for i in str_binar_n:
            if i == "1":
                count += 1
        if count % 2 == 0:
            bot.send_message(message.chat.id, f'Ваша комбінація для коду з перевіркою на парність - {binar_n[2:]}0')
        else:
            bot.send_message(message.chat.id, f'Ваша комбінація для коду з перевіркою на парність - {binar_n[2:]}1')
    except Exception:
        sender = bot.send_message(message.chat.id, 'Схоже ви ввели число не вірно, спробуйте ввести його ще раз:')
        bot.register_next_step_handler(sender, check_even_code)

def inverse_code(message):
    try:
        user_mesg = message.text
        binar_n = bin(int(user_mesg))
        str_binar_n = str(binar_n[2:])
        count = 0
        for i in str_binar_n:
            if i == '1':
                count += 1
        if count % 2 == 0:
            ch_inv = str_binar_n * 2
            bot.send_message(message.chat.id, f'Ваша комбінація для інверсного коду - {ch_inv}')
        else:
            ch_inv = str_binar_n + str_binar_n[::-1]
            bot.send_message(message.chat.id, f'Ваша комбінація для інверсного коду - {ch_inv}')
    except Exception:
        sender = bot.send_message(message.chat.id, 'Схоже ви ввели число не вірно, спробуйте ввести його ще раз:')
        bot.register_next_step_handler(sender, inverse_code)

def corelation_code(message):
    try:
        bot_mesg = ''
        user_mesg = message.text
        binar_num = bin(int(user_mesg))
        str_binar_num = str(binar_num[2:])
        for i in str_binar_num:
            if i == '0':
                bot_mesg += '01'
            elif i == '1':
                bot_mesg += '10'
        bot.send_message(message.chat.id, f'Ваша комбінація для кореляційного коду - {bot_mesg}')
    except Exception:
        sender = bot.send_message(message.chat.id, 'Схоже ви ввели число не вірно, спробуйте ввести його ще раз:')
        bot.register_next_step_handler(sender, inverse_code)

def repetition_code(message):
    try:
        user_mesg = message.text
        binar_n = bin(int(user_mesg))
        str_binar_n = str(binar_n[2:])
        bot.send_message(message.chat.id, f'Ваша комбінація для коду з повторенням - {str_binar_n * 2}')
    except Exception:
        sender = bot.send_message(message.chat.id, 'Схоже ви ввели число не вірно, спробуйте ввести його ще раз:')
        bot.register_next_step_handler(sender, inverse_code)


def cipher_caesar_key(message):
    try:
        global key
        key = message.text
        caesar_cipher = bot.send_message(message.chat.id, 'Введіть ваше повідомлення українською мовою:')
        bot.register_next_step_handler(caesar_cipher, cipher_caesar_coder)
    except Exception:
        sender = bot.send_message(message.chat.id, 'Схоже ви ввели число не вірно, спробуйте ввести його ще раз:')
        bot.register_next_step_handler(sender, cipher_caesar_key)

def cipher_caesar_coder(message):
    alphabet = 'абвгґдеєжзиіїйклмнопрстуфчцчшщьюя абвгґдеєжзиіїйклмнопрстуфчцчшщьюя '
    user_mesg_words = message.text
    encrypt = str(user_mesg_words)
    encrypt = encrypt.lower()
    encrypted = ''
    for letter in encrypt:
        position = alphabet.find(letter)
        new_position = position + int(key)
        if letter in alphabet:
            encrypted += alphabet[new_position]
        else:
            encrypted += letter
    bot.send_message(message.chat.id, f'Ваше повідомлення - {encrypted}')


def cipher_vijener_key(message):
    try:
        global key
        key = message.text
        vijener_cipher = bot.send_message(message.chat.id, 'Введіть ваше повідомлення українською мовою:')
        bot.register_next_step_handler(vijener_cipher, cipher_vijener_coder)
    except Exception:
        sender = bot.send_message(message.chat.id, 'Схоже ви ввели число не вірно, спробуйте ввести його ще раз:')
        bot.register_next_step_handler(sender, cipher_vijener_key)

def cipher_vijener_coder(message):
    alphabet = "абвгґдеєжзиіїйклмнопрстуфчцчшщьюя "

    letter_to_index = dict(zip(alphabet, range(len(alphabet))))
    index_to_letter = dict(zip(range(len(alphabet)), alphabet))

    encrypted = ""
    user_mesg_words = message.text
    split_message = [user_mesg_words[i: i + len(key)] for i in range(0, len(user_mesg_words), len(key))]

    for each_split in split_message:
        i = 0
        for letter in each_split:
            number = (letter_to_index[letter] + letter_to_index[key[i]]) % len(alphabet)
            encrypted += index_to_letter[number]
            i += 1

    bot.send_message(message.chat.id, f'Ваше повідомлення - {encrypted}')

bot.polling(none_stop=True)