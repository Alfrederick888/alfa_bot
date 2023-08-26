from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Клавиатура (обычная)
kb = ReplyKeyboardMarkup(resize_keyboard=True)

# Создание кнопок обычной клавиатуры
button_help = KeyboardButton('/help')
button_desc = KeyboardButton('/description')
button_photo = KeyboardButton('/photo')
button_heart = KeyboardButton('/❤️')
button_loc = KeyboardButton('/location')
button_links = KeyboardButton('/links')
button_vote = KeyboardButton('/vote')
bp1 = KeyboardButton(text='Random photo')

# Добавление кнопок обычной клавиатуры
kb.add(button_help, button_desc,
       button_photo, button_heart,
       button_loc, button_links,
       button_vote, bp1)
