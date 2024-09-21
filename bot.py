import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import F

API_TOKEN = '7037185148:AAHBMpnPlA9psSGAnNJ3W0uwNSuX4-pCoSM'
bot = Bot(token=API_TOKEN)

dp = Dispatcher()


@dp.message(Command(commands=['start']))
async def start(message: Message):
    print('Привет! Я бот, помогающий твоему здоровью.')
    await message.answer("Привет! Я бот, помогающий твоему здоровью.")


@dp.message(F.text)
async def all_messages(message: Message):
    print('Введите команду /start, чтобы начать общение.')
    await message.answer("Введите команду /start, чтобы начать общение.")


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    import asyncio

    asyncio.run(main())
