from pydantic import BaseModel
from typing import List, Dict
from fastapi import FastAPI, Path, HTTPException

app = FastAPI()
users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int = None


@app.get('/users')
async def get_dict() -> List[User]:
    return users


@app.post('/user/{username}/{age}')
async def create_users(username: str, age: int) -> User:
    user_id = 1 if not users else users[-1].id + 1
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put('/user/{user_id}/{username}/{age}')
async def update_users(user_id: int, username: str, age: int ) -> str:
    try:
        for user in users:
            if user.id == user_id:
                user.username = username
                user.age = age
                return user
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{user_id}')
async def delete_users(user_id: int):
    try:
        for i, user in enumerate(users):
            if user.id == user_id:
                return users.pop(i)
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")
