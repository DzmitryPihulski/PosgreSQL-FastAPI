from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from typing import List
from database import Session
import models

app = FastAPI()


class Item(BaseModel):  # serializer
    id: int
    name: str
    description: str
    user_id: int


class User(BaseModel):  # serializer
    id: int
    username: str
    email: str
    password: str


db = Session()


# GET METHODS
@app.get('/items', response_model=List[Item], status_code=200)
def get_all_items():
    items = db.query(models.Item).all()
    return items


@app.get('/users', response_model=List[User], status_code=200)
def get_all_users():
    users = db.query(models.User).all()
    return users


@app.get('/item/{item_id}', response_model=Item,
         status_code=status.HTTP_200_OK)
def get_an_item(item_id: int):
    item_to_get = db.query(models.Item).filter(models.Item.id == item_id).all()

    if item_to_get is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item Not Found")

    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    return item


@app.get('/user_items/{user_id}',
         response_model=List[Item],
         status_code=status.HTTP_200_OK)
def get_user_items(user_id: int):
    user_to_get = db.query(
        models.User).filter(
        models.User.id == user_id).first()

    if user_to_get is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User Not Found")

    items = db.query(models.Item).filter(models.Item.user_id == user_id).all()
    return items


# POST METHODS
@app.post('/adduser', status_code=status.HTTP_201_CREATED)
def create_a_user(user: User):
    new_user = db.query(models.User).filter(models.User.id == user.id).first()

    if new_user is not None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User exists")

    new_user = models.User(
        id=user.id,
        username=user.username,
        email=user.email,
        password=user.password
    )

    db.add(new_user)
    db.commit()

    return new_user


@app.post('/additem', response_model=Item,
          status_code=status.HTTP_201_CREATED)
def create_an_item(item: Item):
    user = db.query(models.User).filter(models.User.id == item.user_id).first()

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User Not Found")

    new_item = db.query(models.Item).filter(models.Item.id == item.id).first()

    if new_item is not None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item exists")

    new_item = models.Item(
        id=item.id,
        name=item.name,
        description=item.description,
        user_id=item.user_id,
    )

    db.add(new_item)
    db.commit()

    return new_item


# PUT METHODS
@app.put('/item/{item_id}', response_model=Item,
         status_code=status.HTTP_200_OK)
def update_an_item(item_id: int, item: Item):
    user = db.query(models.User).filter(models.User.id == item.user_id).first()

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User Not Found")
    item_to_update = db.query(
        models.Item).filter(
        models.Item.id == item_id).all()

    if item_to_update is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item Not Found")

    item_to_update = db.query(
        models.Item).filter(
        models.Item.id == item_id).first()
    item_to_update.name = item.name
    item_to_update.description = item.description
    item_to_update.user_id = item.user_id

    db.commit()

    return item_to_update


@app.put('/user/{user_id}', response_model=User,
         status_code=status.HTTP_200_OK)
def update_an_item(user_id: int, user: User):
    user_to_update = db.query(
        models.User).filter(
        models.User.id == user_id).first()

    if user_to_update is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User Not Found")

    user_to_update.id = user.id
    user_to_update.username = user.username
    user_to_update.email = user.email
    user_to_update.password = user.password

    db.commit()

    return user_to_update

# DELETE METHODS


@app.delete('/item/{item_id}')
def delete_item(item_id: int):
    item_to_delete = db.query(
        models.Item).filter(
        models.Item.id == item_id).first()

    if item_to_delete is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item Not Found")

    db.delete(item_to_delete)
    db.commit()

    return item_to_delete


@app.delete('/user/{user_id}')
def delete_user(user_id: int):
    user_to_delete = db.query(
        models.User).filter(
        models.User.id == user_id).first()

    if user_to_delete is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User Not Found")

    db.delete(user_to_delete)
    db.commit()

    return user_to_delete
