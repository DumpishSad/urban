from fastapi import FastAPI


app = FastAPI()


@app.get('/')
async def welcome() -> str:
    return 'Главная страница'


@app.get('/user/admin')
async def welcome_admin() -> str:
    return 'Вы вошли как администратор'


@app.get('/user/{user_id}')
async def welcome_user_num(user_id: int) -> str:
    return f'Вы вышли как пользователь № {user_id}'


@app.get('/user/{first_name}/{age}')
async def user_info(first_name: str, age: int) -> str:
    return f'Информация о пользователе. Имя {first_name}, Возраст {age}.'