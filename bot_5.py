from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, \
    ReplyKeyboardMarkup, FSInputFile
from aiogram import F
from crud_functions import *

API_TOKEN = '7037185148:-pCoSM'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

button_calories = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button_formulas = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
inline_kb = InlineKeyboardMarkup(inline_keyboard=[[button_calories, button_formulas]], resize_keyboard=True)

button_info = KeyboardButton(text='Информация')
button_calculate = KeyboardButton(text='Рассчитать')
button_bay = KeyboardButton(text='Купить')
button_register = KeyboardButton(text='Регистрация')
kb = ReplyKeyboardMarkup(keyboard=[[button_info, button_calculate], [button_bay, button_register]],
                         resize_keyboard=True)

inline_buy_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Product1', callback_data='product_buying'),
     InlineKeyboardButton(text='Product2', callback_data='product_buying'),
     InlineKeyboardButton(text='Product3', callback_data='product_buying'),
     InlineKeyboardButton(text='Product4', callback_data='product_buying')]
])


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()


@dp.message(Command(commands=['start']))
async def start(message: Message):
    await message.answer("Привет! Я бот, помогающий твоему здоровью.", reply_markup=kb)


@dp.message(F.text == "Рассчитать")
async def main_menu(message: Message):
    await message.answer("Выберите опцию:", reply_markup=inline_kb)


@dp.callback_query(F.data == 'formulas')
async def get_formulas(call: CallbackQuery):
    formulas_text = "Для женщин: BMR = 10 * вес + 6.25 * рост - 5 * возраст - 161\n"
    await call.message.answer(formulas_text)


@dp.callback_query(F.data == 'calories')
async def set_age(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Введите свой возраст:")
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


@dp.message(F.text == "Купить")
async def get_buying_list(message: Message):
    products = get_all_products()

    for product in products:
        product_id, title, description, price = product
        file_path = f'photos/{product_id}.jpg'
        photo = FSInputFile(file_path)

        await message.answer_photo(photo=photo,
                                   caption=f"Название: {title} | Описание: {description} | Цена: {price} руб.")

    await message.answer("Выберите продукт для покупки:", reply_markup=inline_buy_kb)


@dp.callback_query(F.data == 'product_buying')
async def send_confirm_message(call: CallbackQuery):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()


@dp.message(F.text == "Регистрация")
async def sing_up(message: Message, state: FSMContext):
    await message.answer("Введите имя пользователя (только латинский алфавит):")
    await state.set_state(RegistrationState.username)


@dp.message(RegistrationState.username)
async def set_username(message: Message, state: FSMContext):
    username = message.text

    if is_included(username):
        await message.answer("Пользователь существует, введите другое имя:")
        return
    else:
        await state.update_data(username=username)
        await message.answer("Введите свой email:")
        await state.set_state(RegistrationState.email)


@dp.message(RegistrationState.email)
async def set_email(message: Message, state: FSMContext):
    email = message.text
    await state.update_data(email=email)
    await message.answer("Введите свой возраст:")
    await state.set_state(RegistrationState.age)


@dp.message(RegistrationState.age)
async def set_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)

    data = await state.get_data()
    username = data['username']
    email = data['email']
    age = data['age']

    add_user(username, email, int(age))

    await message.answer(f"Регистрация завершена! Пользователь {username} успешно добавлен.")
    await state.clear()


@dp.message(F.text)
async def handle_text(message: Message):
    await message.answer("Введите команду /start, чтобы начать общение.")


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    import asyncio

    asyncio.run(main())
