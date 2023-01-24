from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!"
                         f" Я являюсь ботом компании ООО ТехноСофт."
                         f" Чтобы написать обращение техподдержке наведитесь на меню,"
                         f" либо введите команды самостоятельно.")
