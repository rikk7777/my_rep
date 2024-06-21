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

# Создаем список списков с кнопками
keyboard: list[list[KeyboardButton]] = [
    [KeyboardButton(text=str(i)) for i in range(1, 4)],
    [KeyboardButton(text=str(i)) for i in range(4, 7)]
]

keyboard.append([KeyboardButton(text='7')])

# Создаем объект клавиатуры, добавляя в него кнопки
my_keyboard = ReplyKeyboardMarkup(
    keyboard=keyboard,
    resize_keyboard=True
)
# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Экспериментируем со специальными кнопками',
        reply_markup=my_keyboard
    )

if __name__ == '__main__':
    dp.run_polling(bot)