import random

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove
from keyboards.inline_keyboard import ikb1, ikb2, ikb3
from keyboards.simple_keyboard import kb
from config import API_TOKEN

# Создаем экземпляр бота, подключаясь к API
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Индикатор лайка. По умолчанию - нет лайка, т.е. False
flag = False

# Список команд
HELP = """
<b>/description</b> - <em> описание бота </em>
<b>/location</b> - <em> рандомная локация </em>
<b>/links</b> - <em> ссылки на поисковики </em>
<b>/vote</b> - <em> что-то </em>
"""

arr_photo = [
    'https://i.pinimg.com/originals/e3/41/40/e34140dc81a93041f8ae93e6b87b3c6c.jpg',
    'https://kot-pes.com/wp-content/uploads/2016/09/image2-6.jpeg',
    'https://s.mediasole.ru/cache/content/data/images/1294/1294292/chert-25111811570057_978.jpg',
    'https://tn.fishki.net/26/upload/post/2020/03/19/3260822/b75df20b18425efa4b880f2eb99953db.jpg',
    'https://wiki.mininuniver.ru/images/thumb/5/50/%D0%9A%D0%BE%D1%82..jpg/900px-%D0%9A%D0%BE%D1%82..jpg',
    'http://3.404content.com/1/A1/EB/1762484429274743997/fullsize.jpg',
]

photos = dict(zip(arr_photo, ['BiteCat', 'GrampyCat',
                              'ЪУЪ', 'Nope',
                              'Oh sh...', 'If monday had a face']))

random_photo = random.choice(list(photos.keys()))

# Функция сообщения при старте бота
async def on_startup(_):
    print('Бот запущен')


# Функция отправки рандомного фото
async def send_random(message: types.Message):
    global random_photo
    random_photo = random.choice(list(photos.keys()))
    await bot.send_photo(chat_id=message.chat.id,
                         photo=random_photo,
                         caption=photos[random_photo],
                         reply_markup=ikb3)


@dp.message_handler(Text(equals='Random photo'))
async def open_kb_photo(message: types.Message):
    await message.answer(text='Рандомное фото',
                         reply_markup=ReplyKeyboardRemove())
    await send_random(message)
    await message.delete()


@dp.message_handler(Text(equals='Главное меню'))
async def open_kb(message: types.Message):
    await message.answer(text='Добро пожаловать в главное меню',
                         reply_markup=kb)
    await message.delete()


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=HELP,
                           parse_mode='HTML')
    await message.delete()


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Уэлком в мой бот.',
                           parse_mode='HTML',
                           reply_markup=kb)
    await message.delete()


@dp.message_handler(commands=['description'])
async def description_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Этот бот создан для личного пользования\n'
                                'Гильмановым Альфредом Шамилевичем\n'
                                'для него же',
                           parse_mode='HTML')
    await message.delete()


@dp.message_handler(commands=['photo'])
async def send_photo(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo='https://krot.info/uploads/posts/2022-03/1646224946_39-krot-info-p-grustnii-kot-mem-smeshnie-foto-47.jpg')
    await message.delete()


@dp.message_handler(commands=['location'])
async def send_location(message: types.Message):
    await bot.send_location(chat_id=message.from_user.id,
                            latitude=random.uniform(55.45, 37.37),
                            longitude=random.uniform(55.45, 37.37))
    await message.delete()


@dp.message_handler(commands=['❤️'])
async def send_heart(message: types.Message):
    await bot.send_sticker(chat_id=message.from_user.id,
                           sticker='CAACAgIAAxkBAAEJ73Rkz4CdsDTa8_sFvqaL'
                                   't5xAlkFaYgACKwwAAiIwWEvIROJY0qdhFC8E')
    await message.delete()


@dp.message_handler(commands=['links'])
async def send_links(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Choose your searcher',
                           reply_markup=ikb1)
    await message.delete()


@dp.message_handler(commands=['vote'])
async def vote_command(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo='https://list-15.net/wp-content/uploads'
                               '/2023/02/8.jpg',
                         caption='Нравится?',
                         reply_markup=ikb2)
    await message.delete()


@dp.callback_query_handler()
async def callback_random_photo(callback: types.CallbackQuery):
    global random_photo
    global flag
    if callback.data == 'like':
        if not flag:
            await callback.answer(text='Вы поставили лайк!')
            flag = True
        else:
            await callback.answer(text='Вы уже лайкнули!')
    elif callback.data == 'dislike':
        if flag:
            await callback.answer(text='Вы поставили дислайк!')
            flag = False
        else:
            await callback.answer(text='Вы уже дислайкали!')
    elif callback.data == 'main':
        await callback.message.answer(text='Вы вернулись в гланое меню',
                                      reply_markup=kb)
    else:
        random_photo = random.choice(
            list(filter(lambda x: x != random_photo, list(photos.keys()))))
        await callback.message.edit_media(
            types.InputMedia(media=random_photo,
                             type='photo',
                             caption=photos[random_photo]),
            reply_markup=ikb3)
        await callback.answer()

if __name__ == "__main__":
    executor.start_polling(dp,
                           skip_updates=True,
                           on_startup=on_startup)
