from fastapi import FastAPI, Path, HTTPException, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()
users = []
templates = Jinja2Templates(directory="templates")


class User(BaseModel):
    id: int = None
    username: str
    age: int = None


@app.get('/')
async def read_users(request: Request):
    return templates.TemplateResponse('users.html', {'request': request, 'users_list': users})


@app.get('/users/{user_id}')
async def get_user(request: Request, user_id: int):
    user = next((user for user in users if user.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return templates.TemplateResponse('users.html', {'request': request, 'user': user})


@app.post('/user/{username}/{age}')
async def create_users(username: str, age: int) -> User:
    user_id = 1 if not users else users[-1].id + 1
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put('/user/{user_id}/{username}/{age}')
async def update_users(user_id: int, username: str, age: int) -> User:
    user = next((user for user in users if user.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    user.username = username
    user.age = age
    return user


@app.delete('/user/{user_id}')
async def delete_users(user_id: int):
    user = next((user for user in users if user.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    users.remove(user)
    return user
