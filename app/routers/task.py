from fastapi import APIRouter, Depends, status, HTTPException
# Сессия БД
from sqlalchemy.orm import Session

from app.backend import db
# Функция подключения к БД
from app.backend.db_depends import get_db
# Аннотации, Модели БД и Pydantic.
from typing import Annotated

from app.modules.task import Task
from app.modules.user import User
from app.schemas import CreateUser, UpdateUser, CreateTask, UpdateTask
# Функции работы с записями.
from sqlalchemy import insert, select, update, delete
# Функция создания slug-строки
from slugify import slugify

router = APIRouter(prefix="/task", tags=["task"])


@router.get("/")
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    result = db.scalars(select(Task)).all()
    return result


@router.get("/task_id")
async def task_by_id(task_id: int, db: Annotated[Session, Depends(get_db)]):
    query = select(Task).where(Task.id == task_id)
    task = db.execute(query).scalars().first()
    if task is None:
        raise HTTPException(status_code=404, detail="User was not found")
    return task


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_task(task: CreateTask, user_id: int, db: Annotated[Session, Depends(get_db)]):
    user_query = select(User).where(User.id == user_id)
    existing_user = db.execute(user_query).scalars().first()

    if existing_user is None:
        raise HTTPException(status_code=404, detail="User was not found")

    db.execute(insert(Task).values(
        title=task.title,
        content=task.content,
        priority=task.priority,
        user_id=user_id
    ))

    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}


@router.put("/update/{task_id}", status_code=status.HTTP_200_OK)
async def update_task(task_id: int, task: UpdateTask, db: Annotated[Session, Depends(get_db)]):
    query = select(Task).where(Task.id == task_id)
    existing_task = db.execute(query).scalars().first()

    if existing_task is None:
        raise HTTPException(status_code=404, detail="Task was not found")

    db.execute(
        update(Task).where(Task.id == task_id).values(
            title=task.title,
            content=task.content,
            priority=task.priority,
            slug=slugify(task.title)
        )
    )
    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'Task update is successful!'}


@router.delete("/delete/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int, db: Annotated[Session, Depends(get_db)]):
    query = select(Task).where(Task.id == task_id)
    existing_task = db.execute(query).scalars().first()

    if existing_task is None:
        raise HTTPException(status_code=404, detail="User was not found")

    db.execute(delete(Task).where(Task.id == task_id))
    db.commit()
    return {'status_code': status.HTTP_204_NO_CONTENT, 'transaction': 'User deleted successfully!'}
