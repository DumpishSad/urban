from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message, KeyboardButton
from aiogram import F
from aiogram.types import ReplyKeyboardMarkup


bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

button_calculate = KeyboardButton(text='Рассчитать')
button_info = KeyboardButton(text='Информация')
kb = ReplyKeyboardMarkup(
    keyboard=[[button_calculate], [button_info]],
    resize_keyboard=True
)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message(Command(commands=['start']))
async def start(message: Message):
    await message.answer("Привет! Я бот, помогающий твоему здоровью.", reply_markup=kb)


@dp.message(F.text == "Рассчитать")
async def set_age(message: Message, state: FSMContext):
    await message.answer("Введите свой возраст:")
    await state.set_state(UserState.age)


@dp.message(UserState.age)
async def set_growth(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост (в см):")
    await state.set_state(UserState.growth)


@dp.message(UserState.growth)
async def set_weight(message: Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес (в кг):")
    await state.set_state(UserState.weight)


@dp.message(UserState.weight)
async def send_calories(message: Message, state: FSMContext):
    await state.update_data(weight=message.text)

    data = await state.get_data()
    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])

    calories = 10 * weight + 6.25 * growth - 5 * age - 161

    await message.answer(f"Ваша норма калорий: {calories:.2f} ккал в день.")
    await state.clear()


@dp.message(F.text == "Информация")
async def send_info(message: Message):
    info_text = "Я могу помочь вам рассчитать вашу норму калорий."
    await message.answer(info_text, reply_markup=kb)


@dp.message(F.text)
async def handle_text(message: Message):
    await message.answer("Введите команду /start, чтобы начать общение.")


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    import asyncio

    asyncio.run(main())
