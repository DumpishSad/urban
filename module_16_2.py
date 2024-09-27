from typing import Annotated

from fastapi import FastAPI, Path

app = FastAPI()


@app.get('/')
async def welcome() -> str:
    return 'Главная страница'


@app.get('/user/admin')
async def welcome_admin() -> str:
    return 'Вы вошли как администратор'


@app.get('/user/{user_id}')
async def welcome_user_num(user_id: int = Path(gr=1,
                                               lr=100,
                                               description='Enter User ID',
                                               example=1)
                           ) -> str:
    return f'Вы вышли как пользователь № {user_id}'


@app.get('/user/{first_name}/{age}')
async def user_info(first_name: Annotated[str, Path(min_length=5,
                                                    max_length=20,
                                                    description='Enter username',
                                                    example='UrbanUser')],
                    age: int = Path(ge=18,
                                    le=120,
                                    description='Enter age',
                                    example='24')
                    ) -> str:
    return f'Информация о пользователе. Имя {first_name}, Возраст {age}.'
