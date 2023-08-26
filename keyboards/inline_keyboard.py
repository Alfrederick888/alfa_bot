from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Клавиатура инлайн
ikb1 = InlineKeyboardMarkup(row_width=2)
ikb2 = InlineKeyboardMarkup(row_width=2)
ikb3 = InlineKeyboardMarkup(row_width=2)

# Cоздание кнопок инлайн клавиатуры
ikb1_google = InlineKeyboardButton(text='Google',
                                   url='https://www.google.ru/')
ikb1_yandex = InlineKeyboardButton(text='Yandex',
                                   url='https://dzen.ru/?yredirect=true')
ikb2_like = InlineKeyboardButton(text='❤️',
                                 callback_data='like')
ikb2_dislike = InlineKeyboardButton(text='👎',
                                    callback_data='dislike')
ikb3_next = InlineKeyboardButton(text='Next photo',
                                 callback_data='next')
ikb3_main_menu = InlineKeyboardButton(text='Главное меню',
                                      callback_data='main')

# Добавление инлайн кнопок
ikb1.add(ikb1_google, ikb1_yandex)
ikb2.add(ikb2_like, ikb2_dislike)
ikb3.add(ikb3_next, ikb3_main_menu)
