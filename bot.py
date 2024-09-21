import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import F


bot = Bot(token=API_TOKEN)

dp = Dispatcher()


@dp.message(Command(commands=['start']))
async def start(message: Message):
    await message.answer("Привет! Я бот, помогающий твоему здоровью.")


@dp.message(F.text)
async def all_messages(message: Message):
    await message.answer("Введите команду /start, чтобы начать общение.")


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    import asyncio

    asyncio.run(main())
