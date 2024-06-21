from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import (KeyboardButton, Message, KeyboardButtonPollType, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
BOT_TOKEN = '7284383193:AAHf6TnCgB0gW4wGIDYn79Vi7Iv2ukwOor4'

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Инициализируем билдер
kb_builder = ReplyKeyboardBuilder()

# Создаем кнопки
contact_btn = KeyboardButton(
    text='Отправить телефон',
    request_contact=True
)
geo_btn = KeyboardButton(
    text='Отправить геолокацию',
    request_location=True
)
poll_btn = KeyboardButton(
    text='Создать опрос/викторину',
    request_poll=KeyboardButtonPollType()
)

# Добавляем кнопки в билдер
kb_builder.row(contact_btn, geo_btn, poll_btn, width=1)

# Создаем объект клавиатуры
keyboard: ReplyKeyboardMarkup = kb_builder.as_markup(
    resize_keyboard=True,
    one_time_keyboard=True
)


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Экспериментируем со специальными кнопками',
        reply_markup=keyboard
    )

# Этот хэндлер будет срабатывать на ответ "Собак 🦮" и удалять клавиатуру
@dp.message(F.text == 'Собак 🦮')
async def process_dog_answer(message: Message):
    await message.answer(
        text='Да, несомненно, кошки боятся собак. '
             'Но вы видели как они боятся огурцов?',
    )


# Этот хэндлер будет срабатывать на ответ "Огурцов 🥒" и удалять клавиатуру
@dp.message(F.text == 'Огурцов 🥒')
async def process_cucumber_answer(message: Message):
    await message.answer(
        text='Да, иногда кажется, что огурцов '
             'кошки боятся больше',
    )


if __name__ == '__main__':
    dp.run_polling(bot)